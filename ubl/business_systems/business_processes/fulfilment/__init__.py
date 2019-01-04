from abc import abstractmethod


class FulfilmentMixin:
    __slots__ = ()


class FulfilmentDescriptor:
    __slots__ = 'fulfilment'

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class Fulfilment(FulfilmentMixin):
    class Consignor(FulfilmentDescriptor):
        pass

    class Consignee(FulfilmentDescriptor):
        pass

    class Shipper(FulfilmentDescriptor):
        pass

    class Recipient(FulfilmentDescriptor):
        pass

    class Supplier(FulfilmentDescriptor):
        pass

    class Buyer(FulfilmentDescriptor):
        pass

    class Forwarder(FulfilmentDescriptor):
        pass

    class FreightAgents(FulfilmentDescriptor):
        pass

    class Consignments(FulfilmentDescriptor):
        pass

    consignors = Consignor()
    consignees = Consignee()
    shipper = Shipper()
    recipient = Recipient()
    supplier = Supplier()
    buyer = Buyer()
    freight_forwarder = Forwarder()
    freight_agents = FreightAgents()
    consignments = Consignments()

    def __init__(self, *args, **kwargs):
        pass


class SimpleFulfilment(Fulfilment):
    pass


class ConsolidatedFulfilment(Fulfilment):
    pass


class IntermediaryFulfilment(Fulfilment):
    pass


class DispatchAdviceMixin:
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
    def cancel_dispatch(self, *args, **kwargs):
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
    def send_dispatch_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_dispatch_advice(self, *args, **kwargs):
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
