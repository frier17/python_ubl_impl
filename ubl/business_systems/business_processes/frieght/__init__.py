from abc import abstractmethod


class FreightProcessMixin:
    # FREIGHT MANAGEMENT:INITIATE FREIGHT PROCESS
    __slots__ = ()

    @abstractmethod
    def request_logistic_service(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_bill_of_landing(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_waybill(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_status_report(self, *args, **kwargs):
        pass

    @abstractmethod
    def request_transport_service(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_bill_of_landing(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_waybill_to_cosignor(self, *args, **kwargs):
        pass

    @abstractmethod
    def report_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_transport_service_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def transport_goods_items_to_delivery_party(self, *args, **kwargs):
        pass

class FreightStatusReportMixin:
    # FREIGHT MANAGEMENT:FREIGHT STATUS REPORTING PROCESS
    __slots__ = ()

    @abstractmethod
    def request_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_status_request(self, *args, **kwargs):
        pass


class CertificateOfGoodsMixin:
    # FREIGHT MANAGEMENT:CERTIFICATION OF ORIGIN OF GOODS PROCESS
    __slots__ = ()

    @abstractmethod
    def apply_for_certificate(self, *args, **kwargs):
        pass

    @abstractmethod
    def apply_for_endorsement(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_certificate(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_certificate(self, *args, **kwargs):
        pass

    @abstractmethod
    def reject_certificate(self, *args, **kwargs):
        pass

    @abstractmethod
    def query_certificate(self, *args, **kwargs):
        pass

    @abstractmethod
    def endorse_certificate(self, *args, **kwargs):
        # may entail signing certificate with a digital hash
        pass

    @abstractmethod
    def validate_certificate(self, *args, **kwargs):
        # bespoke method to confirm the validity of a certificate using
        # digital signature
        pass


class IntermodalFreightProcessMixin:
    # FREIGHT MANAGEMENT:INTERMODAL FREIGHT MANAGEMENT PROCESS
    __slots__ = ()

    @abstractmethod
    def define_transport_demand(self, *args, **kwargs):
        pass

    @abstractmethod
    def perform_booking_management(self, *args, **kwargs):
        pass

    @abstractmethod
    def perform__order_management(self, *args, **kwargs):
        pass

    @abstractmethod
    def announce_transport_service(self, *args, **kwargs):
        pass

    @abstractmethod
    def plan_transport_service(self, *args, **kwargs):
        pass

    @abstractmethod
    def monitor_and_control_transport_services(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute_transport_services(self, *args, **kwargs):
        pass

    @abstractmethod
    def perform_compliance_management(self, *args, **kwargs):
        pass

    @abstractmethod
    def provide_transportation_network_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def finalize_transport_service(self, *args, **kwargs):
        pass

    @abstractmethod
    def manage_completion(self, *args, **kwargs):
        pass


class TransportServiceMixin:
    # FREIGHT MANAGEMENT:TRANSPORT SERVICE DESCRIPTION
    __slots__ = ()

    @abstractmethod
    def request_transport_service_description(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_transport_service_description(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_transport_service_description(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_transport_service_description_request(self, *args, **kwargs):
        pass


class TransportExecutionMixin:
    # FREIGHT MANAGEMENT:TRANSPORT EXECUTION PLAN
    __slots__ = ()

    @abstractmethod
    def create_update_transport_execution_plan_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_rejected_transport_execution_plan(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_proposed_transport_execution_plan(self, *args, **kwargs):
        pass

    @abstractmethod
    def evaluate_transport_execution_plan(self, *args, **kwargs):
        pass

    @abstractmethod
    def confirm_execution_plan(self, *args, **kwargs):
        pass

    @abstractmethod
    def reject_transport_execution_plan(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_confirmed_transport_execution_plan(self, *args, **kwargs):
        pass

    @abstractmethod
    def reject_transport_service_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def confirm_transport_service_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def evaluate_transport_execution_plan_request(self, *args, **kwargs):
        pass


class GoodsItineraryMixin:
    # FREIGHT MANAGEMENT:GOODS ITEM ITINERY
    __slots__ = ()

    @abstractmethod
    def receive_goods_item_itinerary(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_goods_item_itinerary(self, *args, **kwargs):
        pass


class TransportProgressMixin:
    # FREIGHT MANAGEMENT:TRANSPORT PROGRESS STATUS
    __slots__ = ()

    @abstractmethod
    def request_progress_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_progress_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_progress_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_progress_status_request(self, *args, **kwargs):
        pass
