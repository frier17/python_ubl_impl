from abc import abstractmethod


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