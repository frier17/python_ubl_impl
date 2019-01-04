from abc import abstractmethod


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