from abc import abstractmethod
from ubl.business_systems import BusinessService


class InventoryMixin:
    __slots__ = ()

    @abstractmethod
    def send_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_despatch_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def despatch_item(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_despatch_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_products_database(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_item(self, *args, **kwargs):
        pass

    @abstractmethod
    def check_status_of_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_receipt_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_receipt_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def adjust_supply_status(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_order(self, *args, **kwargs):
        pass


class VendorManagedInventoryMixin:
    __slots__ = ()

    @abstractmethod
    def calculate_the_initial_delivery(self, *args, **kwargs):
        pass


class SalesInventoryMovementMixin:
    __slots__ = ()

    @abstractmethod
    def send_a_report_about_sales(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_a_report_about_movement_of_goods(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_a_report_about_sales(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_a_report_about_movement_of_goods(self, *args, **kwargs):
        pass


class InvoicingForVendorManagedInventory:
    __slots__ = ()

    @abstractmethod
    def raise_invoice(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_invoice(self, *args, **kwargs):
        pass


class InitiatedReturnByProducer:
    __slots__ = ()

    @abstractmethod
    def send_instruction_for_returns(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_the_advice(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_item(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_advice_to_notify_return(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_instruction_for_returns(self, *args, **kwargs):
        pass


class InitialStockingByRetailerMixin:
    __slots__ = ()

    @abstractmethod
    def despatch_order_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_order_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_order(self, *args, **kwargs):
        pass


class SynchronizingStockInformationMixin:
    __slots__ = ()

    @abstractmethod
    def synchronize_stock_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_information_about_stock(self, *args, **kwargs):
        pass


class CatalogueItemChangeMixin:
    __slots__ = ()

    @abstractmethod
    def inform_about_changes_inside_the_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_information(self, *args, **kwargs):
        pass


class PeriodicAvailabilityReport:
    __slots__ = ()

    @abstractmethod
    def send_stock_availability_report(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_stock_availability_report(self, *args, **kwargs):
        pass


class InventoryService(BusinessService, PeriodicAvailabilityReport,
                       CatalogueItemChangeMixin,
                       InitialStockingByRetailerMixin,
                       InitiatedReturnByProducer, InventoryMixin,
                       InvoicingForVendorManagedInventory,
                       SalesInventoryMovementMixin,
                       SynchronizingStockInformationMixin,
                       VendorManagedInventoryMixin):
    __slots__ = 'catalogue', 'despatch_advice', 'receipt_advice', \
                'product_activity', 'instruction_for_returns', 'order', \
                'invoice', 'inventory_report', 'stock_availability_report'

    def __init__(self):
        self.catalogue = None
        self.despatch_advice = None
        self.receipt_advice = None
        self.product_activity = None
        self.instruction_for_returns = None
        self.order = None
        self.invoice = None
        self.inventory_report = None
        self.stock_availability_report = None

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass

    def send_information_about_stock(self, *args, **kwargs):
        super().send_information_about_stock(*args, **kwargs)

    def synchronize_stock_information(self, *args, **kwargs):
        super().synchronize_stock_information(*args, **kwargs)

    def check_status_of_items(self, *args, **kwargs):
        super().check_status_of_items(*args, **kwargs)

    def receive_item(self, *args, **kwargs):
        super().receive_item(*args, **kwargs)

    def despatch_item(self, *args, **kwargs):
        super().despatch_item(*args, **kwargs)

    def receive_catalogue(self, *args, **kwargs):
        super().receive_catalogue(*args, **kwargs)

    def adjust_supply_status(self, *args, **kwargs):
        super().adjust_supply_status(*args, **kwargs)

    def send_despatch_advice(self, *args, **kwargs):
        super().send_despatch_advice(*args, **kwargs)

    def receive_receipt_advice(self, *args, **kwargs):
        super().receive_receipt_advice(*args, **kwargs)

    def receive_order(self, *args, **kwargs):
        super().receive_order(*args, **kwargs)

    def update_products_database(self, *args, **kwargs):
        super().update_products_database(*args, **kwargs)

    def receive_despatch_advice(self, *args, **kwargs):
        super().receive_despatch_advice(*args, **kwargs)

    def send_receipt_advice(self, *args, **kwargs):
        super().send_receipt_advice(*args, **kwargs)

    def send_catalogue(self, *args, **kwargs):
        super().send_catalogue(*args, **kwargs)

    def receive_a_report_about_movement_of_goods(self, *args, **kwargs):
        super().receive_a_report_about_movement_of_goods(*args, **kwargs)

    def send_a_report_about_sales(self, *args, **kwargs):
        super().send_a_report_about_sales(*args, **kwargs)

    def receive_a_report_about_sales(self, *args, **kwargs):
        super().receive_a_report_about_sales(*args, **kwargs)

    def send_a_report_about_movement_of_goods(self, *args, **kwargs):
        super().send_a_report_about_movement_of_goods(*args, **kwargs)

    def raise_invoice(self, *args, **kwargs):
        super().raise_invoice(*args, **kwargs)

    def receive_invoice(self, *args, **kwargs):
        super().receive_invoice(*args, **kwargs)

    def receive_information(self, *args, **kwargs):
        super().receive_information(*args, **kwargs)

    def inform_about_changes_inside_the_catalogue(self, *args, **kwargs):
        super().inform_about_changes_inside_the_catalogue(*args, **kwargs)

    def send_order(self, *args, **kwargs):
        super().send_order(*args, **kwargs)

    def despatch_order_items(self, *args, **kwargs):
        super().despatch_order_items(*args, **kwargs)

    def receive_order_items(self, *args, **kwargs):
        super().receive_order_items(*args, **kwargs)

    def calculate_the_initial_delivery(self, *args, **kwargs):
        super().calculate_the_initial_delivery(*args, **kwargs)

    def receive_the_advice(self, *args, **kwargs):
        super().receive_the_advice(*args, **kwargs)

    def receive_instruction_for_returns(self, *args, **kwargs):
        super().receive_instruction_for_returns(*args, **kwargs)

    def send_advice_to_notify_return(self, *args, **kwargs):
        super().send_advice_to_notify_return(*args, **kwargs)

    def send_instruction_for_returns(self, *args, **kwargs):
        super().send_instruction_for_returns(*args, **kwargs)

    def send_item(self, *args, **kwargs):
        super().send_item(*args, **kwargs)

    def send_stock_availability_report(self, *args, **kwargs):
        super().send_stock_availability_report(*args, **kwargs)

    def receive_stock_availability_report(self, *args, **kwargs):
        super().receive_stock_availability_report(*args, **kwargs)
