from abc import abstractmethod


class EstablishForecastMixin:
    # COLLABORATIVE PLANNING: FORECASTING & REPLENISHMENT: ESTABLISH RELATIONSHIP
    __slots__ = ()

    @abstractmethod
    def receive_exception_criteria(self, *args, **kwargs):
        pass

    @abstractmethod
    def revise_exception(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_revision(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_exception_criteria(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_exception(self, *args, **kwargs):
        pass

    @abstractmethod
    def review_and_resend_revision(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_revision(self, *args, **kwargs):
        pass

class JointBusinessPlanningMixin:
    # COLLABORATIVE: CREATE JOINT BUSINESS PLAN
    __slots__ = ()

    @abstractmethod
    def create_retail_event(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_retail_event(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_retail_event_revision(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_trade_location_profile(self, *args, **kwargs):
        pass

    @abstractmethod
    def revise_trade_location_profile(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_TILP_revision(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_TILP(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_TILP(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_TILP(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_retail_event(self, *args, **kwargs):
        pass

    @abstractmethod
    def revise_retail_event(self, *args, **kwargs):
        pass

class SalesForecastMixin:
    # COLLABORATIVE: CREATE SALES FORECAST
    __slots__ = ()

    @abstractmethod
    def create_product_activity(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_product_activity(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_product_activity(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_item_information_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_product_activity(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_sales_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_sales_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_sales_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def reuse_sales_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def revise_sales_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_sales_forecast_revision(self, *args, **kwargs):
        pass


class ExceptionHandlingMixin:
    # COLLABORATIVE:EXCEpassION HANDLING
    __slots__ = ()

    @abstractmethod
    def wait_for_sales_forecast_exception_notification(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_exception(self, *args, **kwargs):
        pass

    @abstractmethod
    def resolve_exception(self, *args, **kwargs):
        pass


class OrderForecastMixin:
    # COLLABORATIVE: CREATE ORDER FORECAST
    __slots__ = ()

    @abstractmethod
    def receive_retail_product_activity(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_order_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def receive_order_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def revise_order_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def send_order_forecast_revision(self, *args, **kwargs):
        pass


class ExceptionMonitorMixin:
    # COLLABORATIVE: EXCEpassION MONITOR DURING EXCEpassION
    __slots__ = ()

    @abstractmethod
    def ordering(self, *args, **kwargs):
        pass

    @abstractmethod
    def wait_for_exception_notification(self, *args, **kwargs):
        pass
