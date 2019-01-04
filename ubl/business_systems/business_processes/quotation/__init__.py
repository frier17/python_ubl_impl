from abc import abstractmethod


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