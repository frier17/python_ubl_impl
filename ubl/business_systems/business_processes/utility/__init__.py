from abc import abstractmethod


class UtilityMixin:
    # UTILITY BILLING PROCESS
    __slots__ = ()

    @abstractmethod
    def receive_utility_statement(self, *args, **kwargs):
        pass

    @abstractmethod
    def report_usage(self, *args, **kwargs):
        pass


class PaymentNotificationMixin:
    # PAYMENT NOTIFICATION PROCESS
    __slots__ = ()

    @abstractmethod
    def authorize_payment(self, *args, **kwargs):
        pass

    @abstractmethod
    def notify_of_payment(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def notify_payee(self, *args, **kwargs):
        pass
