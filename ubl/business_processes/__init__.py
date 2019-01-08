"""
Business process package defines routine services provided by a business.
The listed processes are used to manage the activities associated with a
given business service.
The design implemented of all processes are derived from the definition of
business service by Aniefiok Friday:
"Every business service consists of activities performed at a cost and
requires a feedback (proof of transaction) to participants or parties involved"

Implement the business processes such as procurement, call to tender etc.
defined in the UBL 2.1
Section 2.3, “Tendering”
Section 2.4, “Catalogue”
Section 2.5, “Quotation”
Section 2.6, “Ordering”
Section 2.7, “Fulfilment”
Section 2.8, “Billing”
Section 2.9, “Freight Billing”
Section 2.10, “Utility Billing”
Section 2.11, “Payment Notification”
Section 2.13, “Collaborative Planning, Forecasting, and Replenishment”
Section 2.14, “Vendor Managed Inventory”
Section 2.15, “International Freight Management”
Section 2.18, “Intermodal Freight Management”
Section 2.16, “Freight Status Reporting”
Section 2.17, “Certification of Origin of Goods”
adopted from http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html
The named business operations are provided as corresponding service module
mixins. These mixins would define the features available in defined services.

Mixins to include:
1	TenderingMixin
2	CatalogueMixin
3	QuotationMixin
4	OrderingMixin
5	FulfilmentMixin
6	BillingMixin
7	FreightBillingMixin
8	UtilityBillingMixin
9	PaymentNotificationMixin
10	CollaborativePlanningForecastingandReplenishmentMixin
11	VendorManagedInventoryMixin
12	InternationalFreightManagementMixin
13	IntermodalFreightManagementMixin
14	FreightStatusReportingMixin
15	CertificationofOriginofGoodsMixin

"""

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
