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


class ContractNoticeManagement:
    """
    Manage the life cycle and services of a contract notice in the contract tender process
    """
    def prepare_notice(self, contracting_authority, contracting_parties, publishers, suppliers, *args, **kwargs):
        pass

    def publish_notice(self, tender, notice, *args, **kwargs):
        # contracting_authority, contracting_parties, publishers, suppliers can be accessed via the tender
        # while the TenderManagement can publish tender notice, a generic NoticeManagement can be used for publishing
        # @todo: refactor publishing of notices (tender, awards, billing etc.) into NoticeManagement
        pass

    def public_notice_to_supplier(self, tender, notice, supplier, *args, **kwargs):
        # contracting_authority, publishers accessed via tender or notice
        pass

    @staticmethod
    def validate_contract_notice(self, tender, contracting_authority, publishers, suppliers, notice, notice_flag=None):
        # verifies if the given tender has notice appropriate for contracting authority, publishers, suppliers
        # validates prior notice or simplified notice
        pass



