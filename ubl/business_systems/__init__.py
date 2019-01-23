# Implement the BSO system

from abc import ABC


class Payable(ABC):
    pass


class Service(ABC):

    # define the various user parties
    buyer_parties = None
    seller_parties = None
    publishers = None
    activity = None


class BusinessService(Service, Payable):

    def __new__(cls, *args, **kwargs):
        # creating new object of the Business service should be through
        # factory methods
        pass

    def __init_subclass__(self, *args, **kwargs):
        # prevent the initialization or subclassing of BSO objects as BSOs will
        # be created only through factories
        pass

    @classmethod
    def initialize(cls, *args, **kwargs):
        # initialize class or instance variables in sub classes
        raise NotImplementedError


class BusinessParty(ABC):
    pass


class Buyer(BusinessParty):
    pass


class Seller(BusinessParty):
    pass


class Supplier(BusinessParty):
    """
    A supplier may not necessarily be the manufacturer or final seller of
    goods and items. Supplier may be middleman, however, for simplicity,
    this implementation defines a supplier as the source or manufacturer who
    may also be a seller. Seller may not be Supplier but Supplier can both
    sell and supply goods and services.
    """
    pass


class Transaction:
    pass
