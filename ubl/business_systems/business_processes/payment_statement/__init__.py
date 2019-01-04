from abc import abstractmethod


class AccountStatementMixin:
    # PAYMENT: STATEMENT PROCESS
    __slots__ = ()

    @abstractmethod
    def receive_statement(self, *args, **kwargs):
        pass

    @abstractmethod
    def guarantee_statement(self, *args, **kwargs):
        pass