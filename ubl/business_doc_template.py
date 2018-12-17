"""
The template module provides means for generating various business
documents. The Business Documents are based on the Universal Business
Language (UBL) XML schema definitions.
See: http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html

The python implementation closely follows the the xml
class definition. It does not however, follow a one-to-one conversion of xml
schema to python classes. A lose mapping which allows for flexibility and
extension of the python implementation was adopted to enable developers use
the UBL standard across various scenarios without rigid boundaries.
This means, the python implementation is designed to allow for developers to
have wrapper classes which performs as Business Document (BusinessDocument) or
can be parsed into a printable documents. Achieving this is done by defining
the various Business Information Elements (BIE) as specified in UBL 2.1

Collection of classes in this module will include:
* BusinessDocumentTemplate
Utility classes private to this module will be used to generate various
types of Business documents such as Order, Invoice etc. dynamically from
specifying the named document type.

"""
from ubl.utils import Singleton
from collections import OrderedDict
from datetime import datetime
from hashlib import sha512
import copy
from weakref import WeakValueDictionary
from ubl.components.ccts import BusinessDocument
from ubl.components.ccts.component_library import DocumentMap, Schemas, \
    TransactionDocumentMap as Tm

# @todo: do you export the various template or only the factory?

__all__ = (
    'BusinessDocumentFactory',
    'BusinessDocumentTemplate',
    'DocumentRevisions',
)


class BusinessDocumentTemplate(metaclass=Singleton):
    """
    Generate the various business components dynamically.
    This class serves as a factory for generating business components.
    Each component type is generated from a registry of defined UBL base
    components e.g BIE
    """
    __slots__ = ()

    @classmethod
    def get_definition(cls, document):
        return DocumentMap.document_definition(name=document)

    @classmethod
    def document_fields(cls, document):
        definition = DocumentMap.document_definition(name=document)
        if definition:
            return definition.keys()

    @classmethod
    def schema(cls, document):
        return Schemas.document_schema(name=document)

    @property
    def document_schemas(self):
        return Schemas.schemas

    @property
    def document_registry(self):
        return DocumentMap.registry


class DocumentRevisions:
    """
    Keeps instances of Business documents generated during the life cycle of
    an operation or business service.
    Each record is a signed timestamp and retrievable from internal list
    """
    _cache = OrderedDict()

    def __init__(self):
        raise RuntimeError('Instantiating this class is not allowed')

    @classmethod
    def revisions(cls):
        return cls._cache.items()

    @classmethod
    def set_revision(cls, key, value):
        stamped_key = sha512(datetime.utcnow() + key).hexdigest()
        cls._cache[stamped_key] = value


class DocumentCache:

    _cache = WeakValueDictionary()

    def __init__(self):
        raise RuntimeError('Instantiating this class is not allowed')

    @classmethod
    def save(cls, key, value):
        if key not in cls._cache:
            cls._cache[key] = value

    @classmethod
    def cached_instance(cls, key):
        return cls._cache.get(key, None)


class BusinessDocumentFactory:
    """
    The document prototype used to produce the various types of documents
    defined in the UBL 2.1 implementation.
    This class has a factory method which generate the named document and
    returns a copy of it. To improve efficiency, an instance of each copy of
    document is bound to the class enabling caching of created document.
    Upon creating a new type of document, the instance is replaced. This is
    resource saving where a given type of document is created in a loop
    """
    __slots__ = ('instance', '_fields', '_definition', '_schema', '_name')

    def __init__(self):
        self.instance = None
        self._fields = None
        self._definition = None
        self._schema = None

    def __init_subclass__(self, *args, **kwargs):
        raise Exception('Document Factory not to be extended')

    @classmethod
    def produce_document(cls, document):
        # if the document is not in document lists, exit
        # if the document is in list, then check if it's instance
        # else create instance and return a copy
        if not isinstance(document, str):
            document = str(document)
        if document not in BusinessDocumentTemplate.document_registry:
            # @todo: define business logic error for wrong document type
            raise TypeError('Unrecognised document type specified')
        else:
            bt = BusinessDocumentTemplate()
            if not DocumentCache.cached_instance(document):
                cls._name = document
                cls._definition = bt.get_definition(document)
                cls._fields = bt.document_fields(document)
                cls._schema = bt.schema(document)
                instance = \
                    type(
                        cls._name,
                        (BusinessDocument, object,),
                        {'__slots__': cls._fields},
                    )
                # @todo: define the initialize method
                # initialize: get associations and set default values for fields
                prototype = instance().initialize()
                DocumentCache.save(cls._name, prototype)
                return copy.deepcopy(DocumentCache.cached_instance(cls._name))

    @classmethod
    def generate_transaction_document(cls, documents=None, process=None):
        # generate set of documents for the given process
        return map(cls.produce_document, Tm.document_process_lookup(process,
                                                                    documents))
