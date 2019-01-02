"""
Define the list of business exceptions or logical errors in the business
process and generation of documents
BusinessDocumentTypeError
MalformedDocumentError
UnknownDocumentError
ComponentValueError
DocumentValueError
DocumentAssociationError
"""


class DocumentAssociationError(Exception):
    pass


class DocumentTypeError(TypeError):
    pass


class MalformedDocumentError(Exception):
    pass


class UnknownDocumentError(IndexError):
    pass


class ComponentValueError(ValueError):
    pass


class DocumentValueError(ValueError):
    pass



