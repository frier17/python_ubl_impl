from abc import abstractmethod


class FreightBillingMixin:
    # FREIGHT BILLING PROCESS
    __slots__ = ()

    @abstractmethod
    def receive_freight_invoice(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_freight_invoice_to_cosignor(self, *args, **kwargs):
        pass