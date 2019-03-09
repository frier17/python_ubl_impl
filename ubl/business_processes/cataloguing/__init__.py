from abc import abstractmethod
from ubl.business_systems import BusinessService


class CatalogueMixin:
    """
    Defines the various methods common to all catalogue services. Each
    service type may be identified by the keyword argument service=None,
    by default.
    """
    __slots__ = ()

    @abstractmethod
    def send_rejection(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_acceptance_response(self, *args, **kwargs):
        pass

    @abstractmethod
    def acknowledge_acceptance(self, *args, **kwargs):
        pass

    @abstractmethod
    def request_catalogue_update(self, *args, **kwargs):
        pass

    @abstractmethod
    def activate_changes(self, *args, **kwargs):
        pass

    @abstractmethod
    def apply_changes(self, *args, **kwargs):
        pass


class CatalogueProcessMixin:
    # manage creation of catalogue
    __slots__ = ()

    @abstractmethod
    def request_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def respond_to_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def prepare_catalogue_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def produce_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def distribute_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def accept_catalogue(self, *args, **kwargs):
        pass


class CatalogueUpdateMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_item_update_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def distribute_item_notifications(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_item_update(self, *args, **kwargs):
        pass


class CataloguePriceUpdateMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_pricing_update_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def distribute_pricing_modifications(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_pricing_update(self, *args, **kwargs):
        pass


class CatalogueDeleteMixin:
    __slots__ = ()

    @abstractmethod
    def identify_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def notify_of_catalogue_deletion(self, *args, **kwargs):
        pass

    @abstractmethod
    def cancel_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def acknowledge_cancellation(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_catalogue(self, *args, **kwargs):
        pass


class PunchoutSourcingMixin:
    __slots__ = ()

    @abstractmethod
    def initiate_a_punchout_session(self, *args, **kwargs):
        pass

    @abstractmethod
    def build_shopping_basket(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_shopping_basket(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_quotation(self, *args, **kwargs):
        pass


class CatalogueService(BusinessService, CatalogueDeleteMixin,
                       CataloguePriceUpdateMixin, CatalogueProcessMixin,
                       CatalogueUpdateMixin, PunchoutSourcingMixin):

    __slots__ = 'catalogue_request', 'application_response', 'catalogue', \
                'catalogue_item_specification_update', \
                'catalogue_pricing_update', 'catalogue_deletion', 'quotation'

    def __init__(self):
        raise RuntimeError('Class %s should not be initialize' %
                           self.__class__.__name__)

    @classmethod
    def initialize(cls, *args, **kwargs):
        cls.catalogue = None
        cls.catalogue_deletion = None
        cls.application_response = None
        cls.catalogue_request = None
        cls.catalogue_item_specification_update = None
        cls.quotation = None
        cls.catalogue_pricing_update = None

    def initiate_a_punchout_session(self, *args, **kwargs):
        super().initiate_a_punchout_session(*args, **kwargs)

    def send_shopping_basket(self, *args, **kwargs):
        super().send_shopping_basket(*args, **kwargs)

    def build_shopping_basket(self, *args, **kwargs):
        super().build_shopping_basket(*args, **kwargs)

    def receive_quotation(self, *args, **kwargs):
        super().receive_quotation(*args, **kwargs)

    def acknowledge_cancellation(self, *args, **kwargs):
        super().acknowledge_cancellation(*args, **kwargs)

    def cancel_catalogue(self, *args, **kwargs):
        super().cancel_catalogue(*args, **kwargs)

    def delete_catalogue(self, *args, **kwargs):
        super().delete_catalogue(*args, **kwargs)

    def notify_of_catalogue_deletion(self, *args, **kwargs):
        super().notify_of_catalogue_deletion(*args, **kwargs)

    def identify_catalogue(self, *args, **kwargs):
        super().identify_catalogue(*args, **kwargs)

    def receive_pricing_update(self, *args, **kwargs):
        super().receive_pricing_update(*args, **kwargs)

    def distribute_pricing_modifications(self, *args, **kwargs):
        super().distribute_pricing_modifications(*args, **kwargs)

    def prepare_pricing_update_information(self, *args, **kwargs):
        super().prepare_pricing_update_information(*args, **kwargs)

    def prepare_item_update_information(self, *args, **kwargs):
        super().prepare_item_update_information(*args, **kwargs)

    def distribute_item_notifications(self, *args, **kwargs):
        super().distribute_item_notifications(*args, **kwargs)

    def receive_item_update(self, *args, **kwargs):
        super().receive_item_update(*args, **kwargs)

    def prepare_catalogue_information(self, *args, **kwargs):
        super().prepare_catalogue_information(*args, **kwargs)

    def respond_to_request(self, *args, **kwargs):
        super().respond_to_request(*args, **kwargs)

    def accept_catalogue(self, *args, **kwargs):
        super().accept_catalogue(*args, **kwargs)

    def produce_catalogue(self, *args, **kwargs):
        super().produce_catalogue(*args, **kwargs)

    def distribute_catalogue(self, *args, **kwargs):
        super().distribute_catalogue(*args, **kwargs)

    def request_catalogue(self, *args, **kwargs):
        super().request_catalogue(*args, **kwargs)

    def receive_catalogue(self, *args, **kwargs):
        super().receive_catalogue(*args, **kwargs)
