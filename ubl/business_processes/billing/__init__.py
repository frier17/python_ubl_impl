from abc import abstractmethod

from ubl.business_processes import BusinessService


class CreditNoteBillingMixin:
    # BILLING WITH CREDIT NOTE PROCESS
    __slots__ = ()

    @abstractmethod
    def receive_invoice(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_account_response(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_credit_note(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_account_response(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_credit_note(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_invoice(self, *args, **kwargs):
        pass


class DebitNoteBillingMixin:
    # BILLING WITH DEBIT NOTE PROCESS
    __slots__ = ()

    @abstractmethod
    def raise_debit_note(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_debit_note(self, *args, **kwargs):
        pass


class SelfCreditNoteBillingMixin:
    # SELF BILLING WITH CREDIT NOTE PROCESS
    __slots__ = ()

    @abstractmethod
    def raise_self_billed_invoice(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_self_billed_invoice(self, *args, **kwargs):
        pass


class SelfDebitNoteBillingMixin:
    # SELF BILLING WITH SELF BILLED CREDIT NOTE PROCESS
    __slots__ = ()

    @abstractmethod
    def raise_self_billed_credit_note(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_self_billed_credit_note(self, *args, **kwargs):
        pass


class PaymentReminderMixin:
    # REMINDER FOR PAYMENT PROCESS
    __slots__ = ()

    @abstractmethod
    def receive_reminder(self, *args, **kwargs):
        pass

    @abstractmethod
    def request_payment_of_account(self, *args, **kwargs):
        pass


class BillingService(BusinessService, CreditNoteBillingMixin,
                     DebitNoteBillingMixin, PaymentReminderMixin,
                     SelfCreditNoteBillingMixin, SelfDebitNoteBillingMixin):

    __slots__ = 'invoice', 'credit_note', 'application_response', \
                'debit_note', 'self_billed_invoice', 'payment_reminder'

    def __init__(self):
        self.invoice = None
        self.credit_note = None
        self.application_response = None
        self.debit_note = None
        self.self_billed_invoice = None
        self.payment_reminder = None

    @classmethod
    def initialize(cls):
        pass

    def receive_invoice(self, *args, **kwargs):
        super().receive_invoice(*args, **kwargs)

    def send_account_response(self, *args, **kwargs):
        super().send_account_response(*args, **kwargs)

    def receive_account_response(self, *args, **kwargs):
        super().receive_account_response(*args, **kwargs)

    def raise_invoice(self, *args, **kwargs):
        super().raise_invoice(*args, **kwargs)

    def receive_credit_note(self, *args, **kwargs):
        super().receive_credit_note(*args, **kwargs)

    def raise_credit_note(self, *args, **kwargs):
        super().raise_credit_note(*args, **kwargs)

    def receive_debit_note(self, *args, **kwargs):
        super().receive_debit_note(*args, **kwargs)

    def raise_debit_note(self, *args, **kwargs):
        super().raise_debit_note(*args, **kwargs)

    def receive_self_billed_invoice(self, *args, **kwargs):
        super().receive_self_billed_invoice(*args, **kwargs)

    def raise_self_billed_invoice(self, *args, **kwargs):
        super().raise_self_billed_invoice(*args, **kwargs)

    def request_payment_of_account(self, *args, **kwargs):
        super().request_payment_of_account(*args, **kwargs)

    def receive_reminder(self, *args, **kwargs):
        super().receive_reminder(*args, **kwargs)

    def receive_self_billed_credit_note(self, *args, **kwargs):
        super().receive_self_billed_credit_note(*args, **kwargs)

    def raise_self_billed_credit_note(self, *args, **kwargs):
        super().raise_self_billed_credit_note(*args, **kwargs)
