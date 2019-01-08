from abc import abstractmethod
from collections import OrderedDict

from ubl.business_processes import BusinessService


class Catalogue(OrderedDict):
    """
    The process for creating new catalogue requires the cooperation of the
    following classes:
    Catalogue, CatalogueRequest, ApplicationRespons. instances of the
    catalogue like other BSO are not created
    directly but through factory class, CatalogueBuilder. Business services
    involving the catalogue are managed using CatalogueManagement and not
    directly by the catalogue. The catalogue instances are often passed to
    the CatalogueManagement methods to perform tasks.
    This pattern encourages BSO which are essentially datatypes to be managed
    by external classes and not accessed directly preventing unnecessary
    mutations or side effects. This will enable BSO to be treated as
    assets which are not self governing.

    test serve as optimized list of items and an adapter for business
    services applicable to items
    """

    def __init__(self, provider, *args, **kwargs):
        # the contract classification scheme has its own metadata
        # classification is passed as an object or dict with named attributes
        #  with corresponding value
        # receiver, classification = {}, validity_period can be accessed via
        # kwargs or args.
        # self._items, self._item_classifications, self._referenced_contract,
        super(Catalogue, self).__init__(*args, **kwargs)


class CatalogueMixin:
    __slots__ = ()

    def replace_catalogue_item(self, old_item, new_item, authority_parties,
                               actor, reason, *args, **kwargs):
        # the catalogue does not have an update method. Update to items is a
        # replacement of the old with new item
        # replacement does not delete historical information of deleted items
        # prices may be updated independently of catalogue information
        pass

    def update_catalogue_item_price(self, item, old_price, new_price):
        # a convenience method which internally uses replace_catalogue_item
        # to update the price of a given item
        # Prices may be updated independently of other Catalogue information.
        pass

    def send_catalogue(self, sender, receivers):
        # distribute the catalogue to a list of recipients from a specify sender
        # fxn should be in CatalogueManagement
        # Catalogue distribution may be Provider or Receiver Party initiated.
        pass

    def request_catalogue(self, catalogue, requester, items=None, section=None,
                          flags=None):
        # This function enables users to request catalogue, section of a
        # catalogue, or information on specific
        # items in the catalogue the flag attribute is used to further
        # customize response
        # fxn in CatalogueManagement
        # If a Receiver initiates a request for a Catalogue, they may request
        #  an entire Catalogue or only
        # updates to either pricing or item specification details.
        pass

    def issue_catalogue(self, catalogue, provider):
        # issue a catalogue released as a new catalogue
        # Whether Receiver Party initiated or not, the decision to issue a
        # new Catalogue or update an
        # existing one shall be at the discretion of the Provider Party.
        # If an updated Catalogue is issued, then an action code shall define
        #  the status of the items in the Catalogue.
        pass

    def initiate_catalogue(self, catalogue, requester):
        # enable receiver party initiate a request for an existing catalogue
        # to be issued/re-issued.
        # the initiate_catalogue request is approved by the provider party
        # using the issue_catalogue fxn
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
    def send_rejection(self, *args, **kwargs):
        pass

    @abstractmethod
    def prepare_catalogue_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_acceptance_response(self, *args, **kwargs):
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
    def acknowledge_acceptance(self, *args, **kwargs):
        pass

    @abstractmethod
    def accept_catalogue(self, *args, **kwargs):
        pass


class CatalogueUpdateMixin:
    __slots__ = ()

    @abstractmethod
    def request_catalogue_update(self, *args, **kwargs):
        pass

    @abstractmethod
    def prepare_catalogue_item_update_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def distribute_item_notifications(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_item_update(self, *args, **kwargs):
        pass

    @abstractmethod
    def activate_changes(self, *args, **kwargs):
        pass

    @abstractmethod
    def apply_changes(self, *args, **kwargs):
        pass


class CataloguePricingMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_catalogue_pricing_update_information(self, *args, **kwargs):
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
    # PUNCHOUT SOURCING PROCESS
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


class CatalogueService(BusinessService, CatalogueDeleteMixin, CatalogueMixin,
                       CataloguePricingMixin, CatalogueProcessMixin,
                       CatalogueUpdateMixin, PunchoutSourcingMixin):

    __slots__ = 'catalogue_request', 'application_response', 'catalogue', \
                'catalogue_item_specification_update', \
                'catalogue_pricing_update', 'catalogue_deletion', 'quotation'

    def __init__(self):
        self.catalogue = None
        self.catalogue_deletion = None
        self.application_response = None
        self.catalogue_request = None
        self.catalogue_item_specification_update = None
        self.quotation = None
        self.catalogue_pricing_update = None

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass

    def notify_of_catalogue_deletion(self, *args, **kwargs):
        super().notify_of_catalogue_deletion(*args, **kwargs)

    def acknowledge_cancellation(self, *args, **kwargs):
        super().acknowledge_cancellation(*args, **kwargs)

    def delete_catalogue(self, *args, **kwargs):
        super().delete_catalogue(*args, **kwargs)

    def cancel_catalogue(self, *args, **kwargs):
        super().cancel_catalogue(*args, **kwargs)

    def identify_catalogue(self, *args, **kwargs):
        super().identify_catalogue(*args, **kwargs)

    def prepare_catalogue_pricing_update_information(self, *args, **kwargs):
        super().prepare_catalogue_pricing_update_information(*args, **kwargs)

    def distribute_pricing_modifications(self, *args, **kwargs):
        super().distribute_pricing_modifications(*args, **kwargs)

    def receive_pricing_update(self, *args, **kwargs):
        super().receive_pricing_update(*args, **kwargs)

    def send_shopping_basket(self, *args, **kwargs):
        super().send_shopping_basket(*args, **kwargs)

    def build_shopping_basket(self, *args, **kwargs):
        super().build_shopping_basket(*args, **kwargs)

    def receive_quotation(self, *args, **kwargs):
        super().receive_quotation(*args, **kwargs)

    def initiate_a_punchout_session(self, *args, **kwargs):
        super().initiate_a_punchout_session(*args, **kwargs)

    def update_catalogue_item_price(self, item, old_price, new_price):
        super().update_catalogue_item_price(item, old_price, new_price)

    def request_catalogue(self, catalogue, requester, items=None, section=None,
                          flags=None):
        super().request_catalogue(catalogue, requester, items, section, flags)

    def initiate_catalogue(self, catalogue, requester):
        super().initiate_catalogue(catalogue, requester)

    def replace_catalogue_item(self, old_item, new_item, authority_parties,
                               actor, reason, *args, **kwargs):
        super().replace_catalogue_item(old_item, new_item, authority_parties,
                                       actor, reason, *args, **kwargs)

    def issue_catalogue(self, catalogue, provider):
        super().issue_catalogue(catalogue, provider)

    def send_catalogue(self, sender, receivers):
        super().send_catalogue(sender, receivers)

    def receive_item_update(self, *args, **kwargs):
        super().receive_item_update(*args, **kwargs)

    def request_catalogue_update(self, *args, **kwargs):
        super().request_catalogue_update(*args, **kwargs)

    def apply_changes(self, *args, **kwargs):
        super().apply_changes(*args, **kwargs)

    def activate_changes(self, *args, **kwargs):
        super().activate_changes(*args, **kwargs)

    def distribute_item_notifications(self, *args, **kwargs):
        super().distribute_item_notifications(*args, **kwargs)

    def prepare_catalogue_item_update_information(self, *args, **kwargs):
        super().prepare_catalogue_item_update_information(*args, **kwargs)

    def prepare_catalogue_information(self, *args, **kwargs):
        super().prepare_catalogue_information(*args, **kwargs)

    def distribute_catalogue(self, *args, **kwargs):
        super().distribute_catalogue(*args, **kwargs)

    def acknowledge_acceptance(self, *args, **kwargs):
        super().acknowledge_acceptance(*args, **kwargs)

    def respond_to_request(self, *args, **kwargs):
        super().respond_to_request(*args, **kwargs)

    def send_rejection(self, *args, **kwargs):
        super().send_rejection(*args, **kwargs)

    def accept_catalogue(self, *args, **kwargs):
        super().accept_catalogue(*args, **kwargs)

    def produce_catalogue(self, *args, **kwargs):
        super().produce_catalogue(*args, **kwargs)

    def receive_catalogue(self, *args, **kwargs):
        super().receive_catalogue(*args, **kwargs)

    def send_acceptance_response(self, *args, **kwargs):
        super().send_acceptance_response(*args, **kwargs)