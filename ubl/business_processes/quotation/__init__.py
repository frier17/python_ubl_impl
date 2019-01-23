from abc import abstractmethod
from ubl.business_systems import BusinessService


class QuotationMixin:
    # QUOTATION PROCESS
    __slots__ = ()

    @abstractmethod
    def send_request_for_quotation(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_request_for_quotation(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_quotation(self, *args, **kwargs):
        pass


class QuotationService(BusinessService, QuotationMixin):

    __slots__ = 'request_quotation', 'quotation'

    def __init__(self):
        pass

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass

    def receive_request_for_quotation(self, *args, **kwargs):
        super().receive_request_for_quotation(*args, **kwargs)

    def send_request_for_quotation(self, *args, **kwargs):
        super().send_request_for_quotation(*args, **kwargs)

    def send_quotation(self, *args, **kwargs):
        super().send_quotation(*args, **kwargs)