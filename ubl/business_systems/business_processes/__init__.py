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

from abc import ABC, abstractmethod


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

    def __init__(self):
        pass

    def __init_subclass__(self, *args, **kwargs):
        # prevent the initialization or subclassing of BSO objects as BSOs will
        # be created only through factories
        pass

    @classmethod
    def initialize(cls, *args, **kwargs):
        raise NotImplementedError


class Transaction:
    pass


class BillingMixin:
    """
    Define the common behaviours of all billing services: self billling,
    billing with credit note, billing with debit note etc. as defined in the
    UBL 2.1 specification

    receive invoice
    send account response
    receive credit note
    receive account response
    raise credit note
    raise invoice

    """
    __slots__ = ()


class CatalogueMixin:
    __slots__ = ()


class CertificateOfGoodsMixin:
    __slots__ = ()


class ForecastingMixin:
    __slots__ = ()


class InternationalFreightMixin:
    def __init__(self):
        super().__init__()


class IntermodalFreightMixin:
    __slots__ = ()


class FreightBillingMixin:
    __slots__ = ()


class FulfilmentMixin:
    __slots__ = ()


class InventoryMixin:
    __slots__ = ()


class OrderingMixin:
    __slots__ = ()


class PaymentNotificationMixin:
    __slots__ = ()


class PaymentMixin:
    __slots__ = ()


class InventoryPlanningMixin:
    __slots__ = ()


class InventoryReplenishmentMixin:
    __slots__ = ()


class TenderingMixin:
    __slots__ = ()

    def prepare_prior_notice(self, *, document, callbacks, flags, conditions):
        # fallback on Service.prepare_documents(**kwargs)
        pass

    def publish_documents(self, *, buyers, flags, conditions):
        # fallback on the Service.publish(**kwargs) to execute
        # called for publish tender and publish prior information
        # publish in buyer, publish contract etc. base on flags & conditions
        pass

    def prepare_notices(self, *, document, callbacks, flags, conditions):
        pass

    def validate_documents(self, *, document, callbacks, flags, conditions):
        # validate contract notice doc.
        # fallback on Service.validate_document(**kwargs)
        pass

    def receive_tenders(self, *, document, callbacks, flags, conditions):
        # fallback on Service.receive_document(**kwargs)
        pass

    def call_for_tender(self, *, document, callbacks, flags, conditions):
        # fallback on Service.request_document(**kwargs)
        pass

    def prepare_tender(self, *, document, callbacks, flags, conditions):
        # fallback on Service.prepare_document(**kwargs)
        pass

    def receive_tender_invitation(self, *, document, callbacks, flags,
                                  conditions):
        # fallback on Service.receive_document(**kwargs)
        pass

    def request_invitation_response(self, *, document, callbacks, flags,
                                    conditions):
        # fallback on Service.request_action and Service.request_document
        pass

    def prepare_qualification_document(self, *, document, callbacks, flags,
                                       conditions):
        # fallback on Service.prepare_document(**kwargs)
        pass

    def submit_document(self, *, document, callbacks, flags, conditions):
        # fallback on Service.submit_document
        pass


class UtilityBillingMixin:
    __slots__ = ()


class QuotationMixin:
    __slots__ = ()
