from abc import abstractmethod

from ubl.business_processes import BusinessService


class UtilityMixin:
    # UTILITY BILLING PROCESS
    __slots__ = ()

    @abstractmethod
    def receive_utility_statement(self, *args, **kwargs):
        pass

    @abstractmethod
    def report_usage(self, *args, **kwargs):
        pass


class UtilityService(BusinessService, UtilityMixin):

    __slots__ = 'application_response', 'utility_statement', 'invoice'

    def __init__(self):
        self.application_response = None
        self.utility_statement = None
        self.invoice = None

    @classmethod
    def initialize(cls, application_response=None, utility_statement=None,
                   invoice=None):
        """
        self.application_response = application_response if isinstance(
            application_response, BusinessDocument) else None
        self.utility_statement = utility_statement if isinstance(
            utility_statement, BusinessDocument) else None
        self.invoice = invoice if isinstance(invoice, BusinessDocument) else \
            None
        :return:
        """
        pass

    def report_usage(self, *args, **kwargs):
        super().report_usage(*args, **kwargs)

    def receive_utility_statement(self, *args, **kwargs):
        super().receive_utility_statement(*args, **kwargs)


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


class AccountStatementMixin:
    # PAYMENT: STATEMENT PROCESS
    __slots__ = ()

    @abstractmethod
    def receive_statement(self, *args, **kwargs):
        pass

    @abstractmethod
    def guarantee_statement(self, *args, **kwargs):
        pass


class PaymentService(BusinessService, PaymentNotificationMixin,
                     AccountStatementMixin):
    __slots__ = 'remittance_advice', 'statement'

    def __init__(self):
        self.remittance_advice = None
        self.statement = None

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass

    def notify_of_payment(self, *args, **kwargs):
        super().notify_of_payment(*args, **kwargs)

    def receive_advice(self, *args, **kwargs):
        super().receive_advice(*args, **kwargs)

    def authorize_payment(self, *args, **kwargs):
        super().authorize_payment(*args, **kwargs)

    def notify_payee(self, *args, **kwargs):
        super().notify_payee(*args, **kwargs)

    def receive_statement(self, *args, **kwargs):
        super().receive_statement(*args, **kwargs)

    def guarantee_statement(self, *args, **kwargs):
        super().guarantee_statement(*args, **kwargs)
        