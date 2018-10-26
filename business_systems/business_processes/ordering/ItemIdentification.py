

class ItemIdentification(object):
    """
    Defines various means of identifying a business item depicted as a valuable commodity
    """

    def __init__(self, *args, **kwargs):
        self._buyer_identification = None
        self._seller_identification = None
        self._manufacturer_identification = None
        self._catalogue_identification = None
        self._system_identification = None
        super(ItemIdentification, self).__init__()
