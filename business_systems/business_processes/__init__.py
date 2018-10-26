"""
Business process package defines routine services provided by a business.
The listed processes are used to manage the activities associated with a
given business service.
The design implemented of all processes are derived from the definition of
business service by Aniefiok Friday.
Every business service consists of activities performed at a cost and
requires a feedback (proof of transaction) to participants or parties involved

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
"""

from abc import ABC, abstractmethod
from functools import partial


class Service(ABC):

    # define the various user parties
    buyer_parties = None
    seller_parties = None
    publishers = None

    @abstractmethod
    def create_document(self, *, document_type, flags, conditions):
        pass

    @abstractmethod
    def perform_task(self, *, document, callbacks, flags, conditions):
        """
        The base operation of a business activity
        :param document: A business document provided to commerce an
        activity
        :param callbacks:
        :param conditions:
        :param flags: phase or process can be captured in flags
        """
        target_document = None
        next_task = None
        # yield or return. If function is a coroutine use @prime_coroutine
        # the return value could be used to set state.
        # next task can be set in the TaskSequenceQueue or returned

    @abstractmethod
    def publish(self, *, document, flags, conditions):
        # the flags can be used to determine how the tender will be published
        # E.g publish tender in buyer's profile
        # publish can be composed function taking other callbacks to run
        pass

    @abstractmethod
    def evaluate_document(self, *, document, flags, conditions):
        pass

    @abstractmethod
    def request_document(self, *, document, flags, conditions):
        pass

    @abstractmethod
    def receive_document(self, *, document, callbacks, flags, conditions):
        # callbacks can be document validators
        pass

    @abstractmethod
    def request_action(self, *, task, flags, conditions):
        pass

    @abstractmethod
    def respond_action(self, *, task, flags, conditions):
        pass

    @abstractmethod
    def terminate_task(self, *, document, callbacks, flags, conditions):
        # document parameter can be initial state before terminating
        pass

    @abstractmethod
    def validate_document(self, *, document, callbacks, flags, conditions):
        pass

    @abstractmethod
    def submit_document(self, *, document, callbacks, flags, conditions):
        pass


class BusinessService(Service):
    # @todo: define methods common to all processes/services
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        pass

    def __init_subclass__(self, *args, **kwargs):
        # prevent the initialization or subclassing of BSO objects as BSOs will
        # be created only through factories
        pass

    def perform_task(
            self,
            source_document=None,
            parent_task=None,
            conditions=None,
            flags=None
    ):
        pass


class BillingServiceMixin:
    # @todo: define methods only accessible in Billing service
    __slots__ = ()


class CatalogueServiceMixin:
    __slots__ = ()


class CertificateOfGoodsServiceMixin:
    __slots__ = ()


class ForecastingServiceMixin:
    __slots__ = ()


class InternationalFreightServiceMixin:
    def __init__(self):
        super().__init__()


class IntermodalFreightServiceMixin:
    __slots__ = ()


class FreightBillingServiceMixin:
    __slots__ = ()


class FulfilmentServiceMixin:
    __slots__ = ()


class InventoryMixin:
    __slots__ = ()


class OrderingServiceMixin:
    __slots__ = ()


class PaymentNotificationServiceMixin:
    __slots__ = ()


class PaymentServiceMixin:
    __slots__ = ()


class InventoryPlanningServiceMixin:
    __slots__ = ()


class InventoryReplenishmentServiceMixin:
    __slots__ = ()


class TenderingServiceMixin:
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


class UtilityBillingServiceMixin:
    __slots__ = ()


class QuotationServiceMixin:
    __slots__ = ()
