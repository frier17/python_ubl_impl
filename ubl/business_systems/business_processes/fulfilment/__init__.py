from abc import abstractmethod


class DespatchAdviceMixin:
    # FULFILLMENT WITH DESPATCH ADVICE PROCESS
    __slots__ = ()

    @abstractmethod
    def accept_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_receipt_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_receipt_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def adjust_supply_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def cancel_despatch(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_fulfillment_cancellation(self, *args, **kwargs):
        pass

    @abstractmethod
    def check_status_of_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_order_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_despatch_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_despatch_advice(self, *args, **kwargs):
        pass

class ReceiptAdviceMixin:
    # FULFILLMENT WITH RECEIPT ADVICE PROCESS
    __slots__ = ()

    @abstractmethod
    def adjust_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_order_cancellation(self, *args, **kwargs):
        pass

    @abstractmethod
    def advise_buyer_of_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def cancel_receipt_notification(self, *args, **kwargs):
        pass
