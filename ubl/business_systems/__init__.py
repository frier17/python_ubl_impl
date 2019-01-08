from abc import ABC, abstractmethod


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
