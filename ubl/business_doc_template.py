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
from ubl.components.ccts.component_library import DocumentMap, Schemas

# @todo: do you export the various template or only the factory?

__all__ = (
    'ApplicationResponse',
    'AttachedDocument',
    'UnawardedNotification',
    'BillOfLading',
    'CallForTenders',
    'Catalogue',
    'CatalogueDeletion',
    'CatalogueItemSpecificationUpdate',
    'CataloguePricingUpdate',
    'CatalogueRequest',
    'CertificateOfOrigin',
    'ContractAwardNotice',
    'ContractNotice',
    'CreditNote',
    'DebitNote',
    'DespatchAdvice',
    'DocumentStatus',
    'DocumentStatusRequest',
    'ExceptionCriteria',
    'ExceptionNotification',
    'Forecast',
    'ForecastRevision',
    'ForwardingInstructions',
    'FreightInvoice',
    'FulfilmentCancellation',
    'GoodsItemItinerary',
    'GuaranteeCertificate',
    'InstructionForReturns',
    'InventoryReport',
    'Invoice',
    'ItemInformationRequest',
    'Order',
    'OrderCancellation',
    'OrderChange',
    'OrderResponse',
    'OrderResponseSimple',
    'PackingList',
    'PriorInformationNotice',
    'ProductActivity',
    'Quotation',
    'ReceiptAdvice',
    'Reminder',
    'RemittanceAdvice',
    'RequestForQuotation',
    'RetailEvent',
    'SelfBilledCreditNote',
    'SelfBilledInvoice',
    'Statement',
    'StockAvailabilityReport',
    'Tender',
    'TendererQualification',
    'TendererQualificationResponse',
    'TenderReceipt',
    'TradeItemLocationProfile',
    'TransportationStatus',
    'TransportationStatusRequest',
    'TransportExecutionPlan',
    'TransportExecutionPlanRequest',
    'TransportProgressStatus',
    'TransportProgressStatusRequest',
    'TransportServiceDescription',
    'TransportServiceDescriptionRequest',
    'UtilityStatement',
    'Waybill',
    'BusinessDocumentPrototype',
    'DocumentRevisions'
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


class BusinessDocument:

    __slots__ = ['__desc__', 'xml_namespace']

    def __init__(self):
        # Namespace can be defined by individual documents
        self.xml_namespace = None
        # @todo: define annotation lookups for document and field level
        self.__desc__ = None

    def __iter__(self):
        if self.__slots__ is not None:
            for field in self.__slots__:
                yield (field, getattr(self, field, None))
        else:
            for field in self.__dict__:
                yield (field, getattr(self, field, None))

    def __getitem__(self, item):
        if item not in self.__slots__ or item not in self.__dict__:
            raise IndexError('Index does not exist in Business Document')
        return getattr(self, item, None)

    def __setitem__(self, key, value):
        # @todo: add the lookup for the allowed values and datatype
        if key not in self.__slots__ or key not in self.__dict__:
            raise IndexError('Index does not exist in Business Document')
        setattr(self, key, value)

    def __delattr__(self, item):
        raise AttributeError('Attribute cannot be deleted in Business Document')

    def __getattribute__(self, name):
        return getattr(self, name, None)

    @staticmethod
    def initialize(cls):
        pass


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


class BusinessDocumentPrototype:
    """
    The document prototype used to produce the various types of documents
    defined in the UBL 2.1 implementation.
    This class has a factory method which generate the named document and
    returns a copy of it. To improve efficiency, an instance of each copy of
    document is bound to the class enabling caching of created document.
    Upon creating a new type of document, the instance is replaced. This is
    resource saving where a given type of document is created in a loop
    """
    __slots__ = ('instance', '_fields', '_definition', '_schema')

    def __init__(self):
        self.instance = None
        self._fields = None
        self._definition = None
        self._schema = None

    def __init_subclass__(self, *args, **kwargs):
        raise Exception('Document Factory not to be extended')

    @staticmethod
    def produce_document(self, document):
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
                self._name = document
                self._definition = bt.get_definition(document)
                self._fields = bt.document_fields(document)
                self._schema = bt.schema(document)
                instance = \
                    type(
                        self._name,
                        (BusinessDocument, object,),
                        {'__slots__': self._fields},
                    )
                # @todo: define the initialize method
                # initialize: get associations and set default values for fields
                prototype = instance().initialize()
                DocumentCache.save(self._name, prototype)
                return copy.deepcopy(DocumentCache.cached_instance(self._name))
