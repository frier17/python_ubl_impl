import pytest
from ubl.business_doc_template import BusinessDocumentFactory

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
"""


def test_init():
    with pytest.raises(RuntimeError):
        a = BusinessDocumentFactory()
        assert a.instance is None


def test_document_factory():
    order_docs = BusinessDocumentFactory.generate_transaction_document(
        process=ProcessRegistry.ORDERING)
    tender_docs = BusinessDocumentFactory.generate_transaction_document(
        process=ProcessRegistry.TENDERING)
    assert order_docs is not None
    assert tender_docs is not None
    # ensure each entry in list is a document type
    assert isinstance(order_docs[0], BusinessDocument)
    assert isinstance(tender_docs[0], BusinessDocument)
