from abc import abstractmethod
from ubl.business_systems import BusinessService


class FreightMixin:
    __slots__ = ()

    @abstractmethod
    def receive_status_report(self, *args, **kwargs):
        pass

    @abstractmethod
    def request_transport_service(self, *args, **kwargs):
        pass

    @abstractmethod
    def report_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_transport_service_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def request_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_rejected_transport_execution_plan(self, *args, **kwargs):
        pass


class InitiateFreightMixing:
    __slots__ = ()

    @abstractmethod
    def request_logistic_service(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_bill_of_lading(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_waybill(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_bill_of_lading(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_waybill_to_cosignor(self, *args, **kwargs):
        pass

    @abstractmethod
    def transport_goods_to_delivery_party(self, *args, **kwargs):
        pass


class FreightStatusReportMixin:
    __slots__ = ()

    @abstractmethod
    def receive_status_request(self, *args, **kwargs):
        pass


class CertificateOfOriginProcessMixin:
    __slots__ = ()

    @abstractmethod
    def apply_for_certificate(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_response(self, *args, **kwargs):
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
        pass


class IntermodalFreightMixin:
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


class TransportExecutionPlanMixin:
    __slots__ = ()

    @abstractmethod
    def create_update_transport_execution_plan_request(self, *args, **kwargs):
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
    def reject_transport_excecution_plan(self, *args, **kwargs):
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


class GoodsItemItinerary:
    __slots__ = ()

    @abstractmethod
    def receive_goods_item_itinerary(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_goods_item_itinerary(self, *args, **kwargs):
        pass


class TransportProgressStatusMixin:
    __slots__ = ()

    @abstractmethod
    def request_transport_progess_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_transport_progress_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_transport_progress_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_transport_progress_status_request(self, *args, **kwargs):
        pass


class InitiateFreightService(BusinessService, CertificateOfOriginProcessMixin,
                             TransportProgressStatusMixin, FreightMixin,
                             InitiateFreightMixing, FreightStatusReportMixin,
                             GoodsItemItinerary, IntermodalFreightMixin,
                             TransportExecutionPlanMixin,
                             TransportServiceMixin):

    __slots__ = 'freight_invoice', 'forwarding_instruction', \
                'bill_of_lading', 'waybill', 'transportation_status', \
                'packing_list', 'transportation_status_request', \
                'certificate_of_origin', 'application_response', \
                'transport_service_description_request', \
                'transport_service_description', \
                'transport_execution_plan_request', \
                'transport_execution_plan', 'goods_item_itinerary', \
                'transport_progress_status', 'transport_progress_status_request'

    def __init__(self):
        pass

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass

    def receive_goods_item_itinerary(self, *args, **kwargs):
        super().receive_goods_item_itinerary(*args, **kwargs)

    def send_goods_item_itinerary(self, *args, **kwargs):
        super().send_goods_item_itinerary(*args, **kwargs)

    def receive_transport_progress_status_request(self, *args, **kwargs):
        super().receive_transport_progress_status_request(*args, **kwargs)

    def send_transport_progress_status(self, *args, **kwargs):
        super().send_transport_progress_status(*args, **kwargs)

    def receive_transport_progress_status(self, *args, **kwargs):
        super().receive_transport_progress_status(*args, **kwargs)

    def request_transport_progess_status(self, *args, **kwargs):
        super().request_transport_progess_status(*args, **kwargs)

    def receive_proposed_transport_execution_plan(self, *args, **kwargs):
        super().receive_proposed_transport_execution_plan(*args, **kwargs)

    def reject_transport_service_request(self, *args, **kwargs):
        super().reject_transport_service_request(*args, **kwargs)

    def reject_transport_excecution_plan(self, *args, **kwargs):
        super().reject_transport_excecution_plan(*args, **kwargs)

    def confirm_execution_plan(self, *args, **kwargs):
        super().confirm_execution_plan(*args, **kwargs)

    def evaluate_transport_execution_plan(self, *args, **kwargs):
        super().evaluate_transport_execution_plan(*args, **kwargs)

    def evaluate_transport_execution_plan_request(self, *args, **kwargs):
        super().evaluate_transport_execution_plan_request(*args, **kwargs)

    def create_update_transport_execution_plan_request(self, *args, **kwargs):
        super().create_update_transport_execution_plan_request(*args, **kwargs)

    def confirm_transport_service_request(self, *args, **kwargs):
        super().confirm_transport_service_request(*args, **kwargs)

    def receive_confirmed_transport_execution_plan(self, *args, **kwargs):
        super().receive_confirmed_transport_execution_plan(*args, **kwargs)

    def request_logistic_service(self, *args, **kwargs):
        super().request_logistic_service(*args, **kwargs)

    def receive_bill_of_lading(self, *args, **kwargs):
        super().receive_bill_of_lading(*args, **kwargs)

    def send_bill_of_lading(self, *args, **kwargs):
        super().send_bill_of_lading(*args, **kwargs)

    def transport_goods_to_delivery_party(self, *args, **kwargs):
        super().transport_goods_to_delivery_party(*args, **kwargs)

    def receive_waybill(self, *args, **kwargs):
        super().receive_waybill(*args, **kwargs)

    def send_waybill_to_cosignor(self, *args, **kwargs):
        super().send_waybill_to_cosignor(*args, **kwargs)

    def request_transport_service_description(self, *args, **kwargs):
        super().request_transport_service_description(*args, **kwargs)

    def receive_transport_service_description(self, *args, **kwargs):
        super().receive_transport_service_description(*args, **kwargs)

    def send_transport_service_description(self, *args, **kwargs):
        super().send_transport_service_description(*args, **kwargs)

    def receive_transport_service_description_request(self, *args, **kwargs):
        super().receive_transport_service_description_request(*args, **kwargs)

    def receive_status_report(self, *args, **kwargs):
        super().receive_status_report(*args, **kwargs)

    def request_transport_service(self, *args, **kwargs):
        super().request_transport_service(*args, **kwargs)

    def report_status(self, *args, **kwargs):
        super().report_status(*args, **kwargs)

    def receive_rejected_transport_execution_plan(self, *args, **kwargs):
        super().receive_rejected_transport_execution_plan(*args, **kwargs)

    def receive_transport_service_request(self, *args, **kwargs):
        super().receive_transport_service_request(*args, **kwargs)

    def request_status(self, *args, **kwargs):
        super().request_status(*args, **kwargs)

    def reject_certificate(self, *args, **kwargs):
        super().reject_certificate(*args, **kwargs)

    def apply_for_endorsement(self, *args, **kwargs):
        super().apply_for_endorsement(*args, **kwargs)

    def query_certificate(self, *args, **kwargs):
        super().query_certificate(*args, **kwargs)

    def endorse_certificate(self, *args, **kwargs):
        super().endorse_certificate(*args, **kwargs)

    def receive_certificate(self, *args, **kwargs):
        super().receive_certificate(*args, **kwargs)

    def apply_for_certificate(self, *args, **kwargs):
        super().apply_for_certificate(*args, **kwargs)

    def receive_response(self, *args, **kwargs):
        super().receive_response(*args, **kwargs)

    def send_certificate(self, *args, **kwargs):
        super().send_certificate(*args, **kwargs)

    def receive_status_request(self, *args, **kwargs):
        super().receive_status_request(*args, **kwargs)

    def finalize_transport_service(self, *args, **kwargs):
        super().finalize_transport_service(*args, **kwargs)

    def plan_transport_service(self, *args, **kwargs):
        super().plan_transport_service(*args, **kwargs)

    def perform__order_management(self, *args, **kwargs):
        super().perform__order_management(*args, **kwargs)

    def monitor_and_control_transport_services(self, *args, **kwargs):
        super().monitor_and_control_transport_services(*args, **kwargs)

    def perform_booking_management(self, *args, **kwargs):
        super().perform_booking_management(*args, **kwargs)

    def provide_transportation_network_information(self, *args, **kwargs):
        super().provide_transportation_network_information(*args, **kwargs)

    def perform_compliance_management(self, *args, **kwargs):
        super().perform_compliance_management(*args, **kwargs)

    def define_transport_demand(self, *args, **kwargs):
        super().define_transport_demand(*args, **kwargs)

    def announce_transport_service(self, *args, **kwargs):
        super().announce_transport_service(*args, **kwargs)

    def manage_completion(self, *args, **kwargs):
        super().manage_completion(*args, **kwargs)

    def execute_transport_services(self, *args, **kwargs):
        super().execute_transport_services(*args, **kwargs)



