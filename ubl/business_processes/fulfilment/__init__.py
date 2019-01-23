from abc import abstractmethod
from ubl.business_systems import BusinessService


class FulfilmentDescriptor:
    __slots__ = 'fulfilment'

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class Fulfilment:
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


class FulfilmentMixin:
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
    def receive_fulfillment_cancellation(self, *args, **kwargs):
        pass

    @abstractmethod
    def check_status_of_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_order_items(self, *args, **kwargs):
        pass


class DespatchAdviceMixin:
    __slots__ = ()

    @abstractmethod
    def accept_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def cancel_despatch(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_despatch_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_despatch_advice(self, *args, **kwargs):
        pass


class ReceiptAdviceMixin:
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

    @abstractmethod
    def cancel_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def change_order(self, *args, **kwargs):
        pass


class FulfilmentService(BusinessService, DespatchAdviceMixin,
                        ReceiptAdviceMixin):
    __slots__ = 'despatch_advice', 'fulfillment_cancellation', 'receipt_advice'

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass

    def send_order_cancellation(self, *args, **kwargs):
        super().send_order_cancellation(*args, **kwargs)

    def cancel_receipt_notification(self, *args, **kwargs):
        super().cancel_receipt_notification(*args, **kwargs)

    def change_order(self, *args, **kwargs):
        super().change_order(*args, **kwargs)

    def adjust_order(self, *args, **kwargs):
        super().adjust_order(*args, **kwargs)

    def advise_buyer_of_status(self, *args, **kwargs):
        super().advise_buyer_of_status(*args, **kwargs)

    def cancel_order(self, *args, **kwargs):
        super().cancel_order(*args, **kwargs)

    def cancel_despatch(self, *args, **kwargs):
        super().cancel_despatch(*args, **kwargs)

    def send_despatch_advice(self, *args, **kwargs):
        super().send_despatch_advice(*args, **kwargs)

    def accept_order(self, *args, **kwargs):
        super().accept_order(*args, **kwargs)

    def receive_despatch_advice(self, *args, **kwargs):
        super().receive_despatch_advice(*args, **kwargs)