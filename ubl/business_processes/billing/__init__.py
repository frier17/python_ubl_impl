from abc import abstractmethod
from ubl.business_processes import BusinessService


class BillingMixin:
    __slots__ = ()

    @abstractmethod
    def send_account_response(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_account_response(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_invoice(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_invoice(self, *args, **kwargs):
        pass


class CreditNoteBillingMixin:
    """
    The credit note billing is a subset of the billing service in which a
    buyer's account may be credited by a given sum to compensate for damage
    goods, overly invoiced item, wrongly applied discount etc. This service
    mixin provides the necessary business activities for billing using a
    credit note.

    See more information at:
    http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html#S-BILLING
    """
    __slots__ = ()

    @abstractmethod
    def receive_credit_note(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_credit_note(self, *args, **kwargs):
        pass


class DebitNoteBillingMixin:
    """
    The debit note billing is a subset of the billing service in which a
    buyer is informed of amount due a seller for ordered item, despatch
    advice, or receipt advice. This service mixin provides the necessary
    business activities for billing using a debit note.

    See more information at:
    http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html#S-BILLING
    """
    __slots__ = ()

    @abstractmethod
    def raise_debit_note(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_debit_note(self, *args, **kwargs):
        pass


class SelfCreditNoteBillingMixin:
    """
    The Self Billing with Self Billed Credit Note process is a subset of the
    traditional billing services. In this scenario, the customer raises an
    invoice on behalf of a supplier. Both supplier and customer are
    responsible for providing taxation information
    """
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
    """
    A payment reminder is service notifies the customer of accounts due to be
    paid.
    """
    __slots__ = ()

    @abstractmethod
    def receive_reminder(self, *args, **kwargs):
        pass

    @abstractmethod
    def request_payment_of_account(self, *args, **kwargs):
        pass


class BillingService(BusinessService, BillingMixin, CreditNoteBillingMixin,
                     DebitNoteBillingMixin, PaymentReminderMixin,
                     SelfCreditNoteBillingMixin, SelfDebitNoteBillingMixin):
    """
    In the Billing process, a request is made for payment for goods or
    services that have been ordered, received, or consumed. In practice,
    there are several ways in which goods or services may be billed.
    Document types in these processes are Invoice, Credit Note, Debit Note,
    and Application Response.
    """

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
