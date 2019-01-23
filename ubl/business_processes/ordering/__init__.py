from abc import abstractmethod
from ubl.business_systems import BusinessService


class OrderingMixin:
    # ORDERING PROCESS
    __slots__ = ()

    @abstractmethod
    def place_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def reject_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def add_detail(self, *args, **kwargs):
        pass

    @abstractmethod
    def accept_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_response(self, *args, **kwargs):
        pass

    @abstractmethod
    def cancel_order(self, *args, **kwargs):
        pass

    @abstractmethod
    def change_order(self, *args, **kwargs):
        pass


class OrderingService(BusinessService, OrderingMixin):
    __slots__ = 'order', 'order_response_simple', 'order_response', \
                'order_change', 'order_cancellation'

    def __init__(self):
        self.order = None
        self.order_response_simple = None
        self.order_response = None
        self.order_change = None
        self.order_cancellation = None

    def receive_response(self, *args, **kwargs):
        super().receive_response(*args, **kwargs)

    def place_order(self, *args, **kwargs):
        super().place_order(*args, **kwargs)

    def accept_order(self, *args, **kwargs):
        super().accept_order(*args, **kwargs)

    def receive_order(self, *args, **kwargs):
        super().receive_order(*args, **kwargs)

    def change_order(self, *args, **kwargs):
        super().change_order(*args, **kwargs)

    def add_detail(self, *args, **kwargs):
        super().add_detail(*args, **kwargs)

    def cancel_order(self, *args, **kwargs):
        super().cancel_order(*args, **kwargs)

    def reject_order(self, *args, **kwargs):
        super().reject_order(*args, **kwargs)

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass
