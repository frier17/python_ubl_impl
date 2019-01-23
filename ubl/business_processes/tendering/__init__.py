from abc import abstractmethod
from ubl.business_systems import BusinessService


class ContractPriorInformationMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_prior_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def publish_in_buyer_profile(self, *args, **kwargs):
        pass

    @abstractmethod
    def prepare_simplified_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def publish_simplified_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def publish_prior_information_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def validate_prior_information_notice(self, *args, **kwargs):
        pass


class ContractNotificationMixin:

    __slots__ = ()

    @abstractmethod
    def prepare_contract_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def publish_contract_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def validate_contract_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def publish_in_buyer_profile(self, *args, **kwargs):
        pass


class TenderInvitationMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_call_for_tenders(self, *args, **kwargs):
        pass

    @abstractmethod
    def submit_invitation_to_tender_(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_invitation_to_tender(self, *args, **kwargs):
        pass

    @abstractmethod
    def process_call_for_tender(self, *args, **kwargs):
        pass


class TenderQualificationInformationMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_qualification_document(self, *args, **kwargs):
        pass

    @abstractmethod
    def submit_qualification_document(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_result(self, *args, **kwargs):
        pass

    @abstractmethod
    def evaluate_qualification_document(self, *args, **kwargs):
        pass

    @abstractmethod
    def submit_qualification_result(self, *args, **kwargs):
        pass


class TenderSubmissionMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_tender_documents(self, *args, **kwargs):
        pass

    @abstractmethod
    def submit_tender_documents(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_receipt(self, *args, **kwargs):
        pass

    @abstractmethod
    def submit_tender_receipt(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_tender_documents(self, *args, **kwargs):
        pass


class TenderAwardPublicationMixin:
    __slots__ = ()

    @abstractmethod
    def prepare_contract_award_and_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def submit_contract_award_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def validate_contract_award_notice(self, *args, **kwargs):
        pass

    @abstractmethod
    def publish_contract_award_notice(self, *args, **kwargs):
        pass


class FinancialGuaranteeCertificateMixin:
    # GUARANTEE DEPOSIT
    __slots__ = ()

    @abstractmethod
    def get_guarantee_from_financial_institution(self, *args, **kwargs):
        pass

    @abstractmethod
    def submit_certificate(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_guarantee_certificate(self, *args, **kwargs):
        pass


class TenderService(BusinessService, ContractNotificationMixin,
                    ContractPriorInformationMixin,
                    FinancialGuaranteeCertificateMixin,
                    TenderAwardPublicationMixin, TenderInvitationMixin,
                    TenderQualificationInformationMixin):

    __slots__ = 'prior_information_notice', 'contract_notice', \
                'call_for_tenders', 'tender_qualification', \
                'tender_qualification_response', 'tender', 'tender_receipt', \
                'award_notification', 'unawarded_notification', \
                'contract_award_notice', 'guarantee_certificate'

    def __init__(self):
        self.prior_information_notice = None
        self.contract_notice = None
        self.call_for_tenders = None
        self.tender_qualification = None
        self.tender_qualification_response = None
        self.tender = None
        self.tender_receipt = None
        self.award_notification = None
        self.unawarded_notification = None
        self.contract_award_notice = None
        self.guarantee_certificate = None

    @classmethod
    def initialize(cls, prior_information_notice=None, contract_notice=None,
                   call_for_tenders=None, tender_qualification=None,
                   tender_qualification_response=None, tender=None,
                   tender_receipt=None, award_notification=None,
                   unawarded_notification=None, contract_award_notice=None,
                   guarantee_certificate=None):
        pass

    def submit_certificate(self, *args, **kwargs):
        super().submit_certificate(*args, **kwargs)

    def receive_guarantee_certificate(self, *args, **kwargs):
        super().receive_guarantee_certificate(*args, **kwargs)

    def get_guarantee_from_financial_institution(self, *args, **kwargs):
        super().get_guarantee_from_financial_institution(*args, **kwargs)

    def publish_prior_information_notice(self, *args, **kwargs):
        super().publish_prior_information_notice(*args, **kwargs)

    def validate_prior_information_notice(self, *args, **kwargs):
        super().validate_prior_information_notice(*args, **kwargs)

    def prepare_simplified_notice(self, *args, **kwargs):
        super().prepare_simplified_notice(*args, **kwargs)

    def publish_simplified_notice(self, *args, **kwargs):
        super().publish_simplified_notice(*args, **kwargs)

    def prepare_prior_notice(self, *args, **kwargs):
        super().prepare_prior_notice(*args, **kwargs)

    def publish_contract_award_notice(self, *args, **kwargs):
        super().publish_contract_award_notice(*args, **kwargs)

    def submit_contract_award_notice(self, *args, **kwargs):
        super().submit_contract_award_notice(*args, **kwargs)

    def prepare_contract_award_and_notice(self, *args, **kwargs):
        super().prepare_contract_award_and_notice(*args, **kwargs)

    def validate_contract_award_notice(self, *args, **kwargs):
        super().validate_contract_award_notice(*args, **kwargs)

    def submit_invitation_to_tender_(self, *args, **kwargs):
        super().submit_invitation_to_tender_(*args, **kwargs)

    def prepare_call_for_tenders(self, *args, **kwargs):
        super().prepare_call_for_tenders(*args, **kwargs)

    def process_call_for_tender(self, *args, **kwargs):
        super().process_call_for_tender(*args, **kwargs)

    def receive_invitation_to_tender(self, *args, **kwargs):
        super().receive_invitation_to_tender(*args, **kwargs)

    def submit_qualification_result(self, *args, **kwargs):
        super().submit_qualification_result(*args, **kwargs)

    def receive_result(self, *args, **kwargs):
        super().receive_result(*args, **kwargs)

    def evaluate_qualification_document(self, *args, **kwargs):
        super().evaluate_qualification_document(*args, **kwargs)

    def prepare_qualification_document(self, *args, **kwargs):
        super().prepare_qualification_document(*args, **kwargs)

    def submit_qualification_document(self, *args, **kwargs):
        super().submit_qualification_document(*args, **kwargs)

    def validate_contract_notice(self, *args, **kwargs):
        super().validate_contract_notice(*args, **kwargs)

    def prepare_contract_notice(self, *args, **kwargs):
        super().prepare_contract_notice(*args, **kwargs)

    def publish_contract_notice(self, *args, **kwargs):
        super().publish_contract_notice(*args, **kwargs)

    def publish_in_buyer_profile(self, *args, **kwargs):
        super().publish_in_buyer_profile(*args, **kwargs)
