from ubl.business_systems import business_service


class Item(business_service):
    """
    Note the following about item as adopted from the UBL 2.1 Business Rules:
    An item may be a product (goods) or a service
    Items may have multiple classifications
    A contract may influence prices of items
    An item may be part of another item
    An item may have a price per unit and an order unit
    An item may reference pictures and documents
    An item may have a validity period
    An item may refer to other relevant or necessary items
    """

    def __init__(self, *args, **kwargs):
        self._identification = None
        self._price = None
        self._description = None
        self._measurement = None  # may require measurement of item as named tuple (length, breath, height)
        super(Item, self).__init__(*args, **kwargs)
