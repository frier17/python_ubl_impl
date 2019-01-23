import pytest
from ubl.business_document.components import DocumentRegistry
from ubl.business_processes import ProcessRegistry
from ubl.business_document.factory import BusinessDocumentFactory

from ubl.business_document.components.ccts import BusinessDocument

"""
Test the following features:
The test should cover following application features:
Generate UBL document or component as Python class
Provide means to index document or collection of documents
Provide a registry of documents mapped to their respective business
processes.
Describe data fields for a document with UBL designated annotations
Describe data fields for a component with UBL designated annotations
Parse python document to xml
Parse xml to python document
Generate pdf from the python document
Extend the behaviour and data attribute of component or document

test_business_document_factory
    Units: Base class - BusinessDocumentFactory
    .__init__
    -- Assert instances cannot be created
    -- Assert creating instances raise a RuntimeError
    Assert attributes _definition is set
    Assert attributes _fields is set
    Assert attributes _name is set
    Assert attributes _schema is set

    .generate_transaction_document(*args, **kwargs)
    Assert iterator of documents is returned by method
    Assert instances of documents are in default form

    .instance
    Assert .instance is either None or a default instance of UBL document

    .produce_documents(*args, **kwargs)
    Assert a default instance of UBL document
"""


def test_init():
    with pytest.raises(RuntimeError):
        a = BusinessDocumentFactory()
        business_doc = BusinessDocumentFactory.produce_document(
            DocumentRegistry.ATTACHED_DOCUMENT)
        print(business_doc)
        documents = BusinessDocumentFactory.generate_transaction_document(
            process=ProcessRegistry.TENDERING)
        assert a.instance is not None
        assert business_doc is not None
        assert isinstance(business_doc, BusinessDocument)
        assert documents is not None
        assert isinstance(documents[0], BusinessDocument)
