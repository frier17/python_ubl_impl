from abc import abstractmethod
"""
ContractAuthority
ContractNoticeManagement
FinancialGurantyCertificate
Tender
TendererQualification
TendererQualificationResponse
TenderManagement
TenderReceipt
"""


class ContractingInformationMixin:
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


class ContractingInformationNoticeMixin:

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
