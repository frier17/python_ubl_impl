"""
Define test suites for the application.
The test should cover following application features:
Generate UBL document or component as Python class
Provide means to index document or collection of documents
Provide a registry of documents mapped to their respective business processes
Describe data fields for a document with UBL designated annotations
Describe data fields for a component with UBL designated annotations
Parse python document to xml
Parse xml to python document
Generate pdf from the python document
Extend the behaviour and data attribute of component or document

Tests will be executed via the following test files:
test_business_document_factory
test_transaction_registry
test_component_library
test_document_writer

test_transaction_registry
    Units: Base Class - ProcessRegistry, BusinessProcesses
    Assert the ProcessRegistry is an IntFlag enum type
    Assert the ProcessRegistry has UBL named processes
    Assert the BusinessProcesses .lookup returns a collection of UBL named
    document for a named process

test_component_library
    Units: Base class - BIERegistry, ABIERegistry, BusinessDocumentRegistry
    Assert BIERegistry, ABIERegistry, BusinessDocumentRegistry are all types
    of IntFlag enum
    Assert each registry has named UBL components (BIE, ASBIE)
    Assert Components obeys the mapping protocol with support for __get__,
    __contains__, __getattr__, __setitem__, __setattr__
    Assert Components __setitem__, __setattr__ both throw RuntimeError
    Assert Components lookup calls of UBL named components returns instances
    of the python object with fields set to their default values
    Assert Documents obeys the mapping protocol with support for __get__,
    __contain__, __getattr__, __setitem__, __setattr__
    Assert Documents __setitem__, __setattr__ both throw RuntimeError
    Assert Documents lookup calls of UBL named documents returns instances of
    the python object with fields set to their default values

test_document_writer
    Units: Base Class - DocumentWriter, formatter, parser
    Assert DocumentWriter cannot be instantiated but throws RuntimeError
    when __init__ is called
    Assert DocumentWriter.parse(*args, **kwargs) returns a given electronic
    document based on the type of format specified
    Assert the DocumentFormat is a type of Enum with aliases for approved or
    support electronic documents e.g PDF, DOCX, DOC
    Assert the formatter accept a UBL document and parses it to the target
    textual format using appropriate template with key word argument list
"""
