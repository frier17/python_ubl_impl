from abc import abstractmethod


class ReplenishmentMixin:
    '''
    VENDOR MANAGED INVENTORY:PERMANENT REPLENISHMENT
    VENDOR MANAGED INVENTORY:INVOICING FOR VENDOR MANAGED INVENTORY
    VENDOR MANAGED INVENTORY:RETURNS INITIATED BY THE PRODUCER
    '''
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

class InitialStockingtMixin:
    '''
    VENDOR MANAGED INVENTORY:PRICE ADJUSTMENTS
    VENDOR MANAGED INVENTORY:INITIAL STOCKING OF THE AREA BY RETAILER
    '''

    @abstractmethod
    def despatch_order_items(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_order(self, *args, **kwargs):
        pass


class SynchronizeStockMixin:
    # VENDOR MANAGED INVENTORY:SYNCHRONIZING STOCK INFORMATION

    @abstractmethod
    def synchronize_stock_information(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_information_about_stock(self, *args, **kwargs):
        pass


class InitialStockingMixin:
    # VENDOR MANAGED INVENTORY:INITIAL STOCKING OF THE AREA BY PRODUCER
    __slots__ = ()

    @abstractmethod
    def calculate_the_initial_delivery(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def despatch_item(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_products_database(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_item(self, *args, **kwargs):
        pass


class SalesInventoryMixin:
    # VENDOR MANAGED INVENTORY:REPORT OF SALES AND INVENTORY MOVEMENT
    __slots__ = ()

    @abstractmethod
    def report_sales(self, *args, **kwargs):
        pass

    @abstractmethod
    def report_movement_of_goods(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_sales_report(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_goods_movement_report(self, *args, **kwargs):
        pass


class InventoryItemChangeMixin:
    # VENDOR MANAGED INVENTORY:CHANGES TO THE ITEM CATALOGUE
    __slots__ = ()

    @abstractmethod
    def inform_about_changes_inside_the_catalogue(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_information(self, *args, **kwargs):
        pass


class PeriodicAvailabilityReportMixin:
    # VMI:PERIODIC TRANSFER ARTICLE AVAILABILITY INFORMATION
    __slots__ = ()

    @abstractmethod
    def send_stock_availability_report(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_stock_availability_report(self, *args, **kwargs):
        pass