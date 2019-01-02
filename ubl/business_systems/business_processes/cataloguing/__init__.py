from collections import OrderedDict

from ubl.business_systems import business_service


class Catalogue(business_service, OrderedDict):
    """
    The process for creating new catalogue requires the cooperation of the following classes:
    Catalogue, CatalogueRequest, ApplicationRespons. instances of the catalogue like other BSO are not created
    directly but
    through factory class, CatalogueBuilder. Business services involving the catalogue are managed using
    CatalogueManagement and not directly by the catalogue. The catalogue instances are often passed to
    the CatalogueManagement methods to perform tasks.
    This pattern encourages BSO which are essentially datatypes to be managed by external classes and not accessed
    directly
    preventing unnecessary mutations or side effects. This will enable BSO to be treated as
    assets which are not self governing.

    test serve as optimized list of items and an adapter for business services applicable to items
    """

    def __init__(self, provider, *args, **kwargs):
        # the contract classification scheme has its own metadata
        # classification is passed as an object or dict with named attributes with corresponding value
        # receiver, classification = {}, validity_period can be accessed via kwargs or args.
        # self._items, self._item_classifications, self._referenced_contract,
        pass

    def replace_catalogue_item(self, old_item, new_item, authority_parties, actor, reason, *args, **kwargs):
        # the catalogue does not have an update method. Update to items is a replacement of the old with new item
        # replacement does not delete historical information of deleted items
        # prices may be updated independently of catalogue information
        pass

    def update_catalogue_item_price(self, item, old_price, new_price):
        # a convenience method which internally uses replace_catalogue_item to update the price of a given item
        # Prices may be updated independently of other Catalogue information.
        pass

    def send_catalogue(self, sender, receivers):
        # distribute the catalogue to a list of recipients from a specify sender
        # fxn should be in CatalogueManagement
        # Catalogue distribution may be Provider or Receiver Party initiated.
        pass

    def request_catalogue(self, catalogue, requester, items=None, section=None, flags=None):
        # This function enables users to request catalogue, section of a catalogue, or information on specific
        # items in the catalogue the flag attribute is used to further customize response
        # fxn in CatalogueManagement
        # If a Receiver initiates a request for a Catalogue, they may request an entire Catalogue or only
        # updates to either pricing or item specification details.
        pass

    def issue_catalogue(self, catalogue, provider):
        # issue a catalogue released as a new catalogue
        # Whether Receiver Party initiated or not, the decision to issue a new Catalogue or update an
        # existing one shall be at the discretion of the Provider Party.
        # If an updated Catalogue is issued, then an action code shall define the status of the items in the Catalogue.
        pass

    def initiate_catalogue(self, catalogue, requester):
        # enable receiver party initiate a request for an existing catalogue to be issued/re-issued.
        # the initiate_catalogue request is approved by the provider party using the issue_catalogue fxn
        pass
