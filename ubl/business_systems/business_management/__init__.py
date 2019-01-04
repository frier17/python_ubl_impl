"""
The business service management classes monitors the execution of a
business process
"""


class TenderManagement:
    """
    Manage the life cycle of a tender or call for tender.
    By adopting a business_management class, various operations by the tendering process will not need to call different tender
    objects directly
    """

    def __init__(self):
        pass

    def evaluate_tender(self, tender, contracting_party, *args, **kwargs):
        pass

    def award_tender(self, tender, contracting_party, *args, **kwargs):
        pass

    def post_awarding_service(self, tender, contracting_party, *args, **kwargs):
        # called only for tenders that have been awarded
        pass

    def receive_tender_document(self, tender, supplier, business_document, *args, **kwargs):
        pass

    def accept_tender(self, tender, contracting_authority, publisher, others=None, *args, **kwargs):
        # accept a submitted tender if business rules are satisfactory
        pass

    def register_for_tender(self, tender, supplier, *args, **kwargs):
        pass

    def submit_tender(self, tender, supplier, *args, **kwargs):
        pass

    def create_tender(self, tender, supplier, *args, **kwargs):
        pass

    def submit_qualification(self, tender, business_document, supplier, *args, **kwargs):
        pass

    def receive_tender_document(self, tender, *args, **kwargs):
        # this method is to loop through submitted document (mapped against supplier for a given tender)
        # and retrieve docs. for review
        # Document may be electronic or attached. Electronic document as specified by UBL is preferred
        pass

    def issue_tender_receipt(self, tender, *args, **kwargs):
        # send business doc or proof of receiving and processing response to call to tender from suppliers.
        pass

    def award_tender(self, tender, suppliers, *args, **kwargs):
        # award tender to the list of successful suppliers (not general supplier's list) which must exist in the tender
        # suppliers list
        pass

    def publish_tender_award(self, tender, notification, notification_flag, *args, **kwargs):
        # publish notification of tender award to list of suppliers both successful and failed applications by default
        # the notification_flag can be used to override the default behavior of what notice to
        # publish and which group of recipient to receive. E.g
        # E.g: send award_notification to successful, send failed_notification to unsuccessful;
        # send only award_notification to successful; send only failed_notification to unsuccessful
        pass

    def submit_guarantee_certificate(self, tender, certificate):
        # This feature will allow successful suppliers to send proof of their banker's deposit or financial support
        # The certificate could be a letter from the bank or other institution guaranteeing
        # the deposit to execute contract
        pass
