from abc import abstractmethod

from ubl.business_processes import BusinessService


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


class ForecastService(BusinessService, EstablishForecastMixin,
                      ExceptionHandlingMixin, ExceptionMonitorMixin,
                      JointBusinessPlanningMixin, OrderForecastMixin,
                      SalesForecastMixin):
    __slots__ = 'retail_event', 'retail_event_revision', \
                'retail_event_response', 'TILP', 'exception_criteria', \
                'exception_criteria_revision', \
                'TILP_response', 'TILP_revision', 'item_information_request', \
                'product_activity', 'sales_forecast', 'forecast_revision', \
                'forecast_response', 'exception_notification'

    def __init__(self):
        self.retail_event = None
        self.retail_event_response = None
        self.retail_event_revision = None
        self.TILP = None
        self.exception_criteria = None
        self.exception_criteria_revision = None
        self.TILP_response = None
        self.TILP_revision = None
        self.item_information_request = None
        self.product_activity = None
        self.sales_forecast = None
        self.forecast_revision = None
        self.forecast_response = None
        self.exception_notification = None

    @classmethod
    def initialize(cls, *args, **kwargs):
        pass

    def send_exception(self, *args, **kwargs):
        super().send_exception(*args, **kwargs)

    def wait_for_sales_forecast_exception_notification(self, *args, **kwargs):
        super().wait_for_sales_forecast_exception_notification(*args, **kwargs)

    def resolve_exception(self, *args, **kwargs):
        super().resolve_exception(*args, **kwargs)

    def ordering(self, *args, **kwargs):
        super().ordering(*args, **kwargs)

    def wait_for_exception_notification(self, *args, **kwargs):
        super().wait_for_exception_notification(*args, **kwargs)

    def send_order_forecast_revision(self, *args, **kwargs):
        super().send_order_forecast_revision(*args, **kwargs)

    def receive_order_forecast(self, *args, **kwargs):
        super().receive_order_forecast(*args, **kwargs)

    def revise_order_forecast(self, *args, **kwargs):
        super().revise_order_forecast(*args, **kwargs)

    def send_order_forecast(self, *args, **kwargs):
        super().send_order_forecast(*args, **kwargs)

    def receive_retail_product_activity(self, *args, **kwargs):
        super().receive_retail_product_activity(*args, **kwargs)

    def receive_revision(self, *args, **kwargs):
        super().receive_revision(*args, **kwargs)

    def review_and_resend_revision(self, *args, **kwargs):
        super().review_and_resend_revision(*args, **kwargs)

    def receive_exception(self, *args, **kwargs):
        super().receive_exception(*args, **kwargs)

    def send_exception_criteria(self, *args, **kwargs):
        super().send_exception_criteria(*args, **kwargs)

    def revise_exception(self, *args, **kwargs):
        super().revise_exception(*args, **kwargs)

    def send_revision(self, *args, **kwargs):
        super().send_revision(*args, **kwargs)

    def receive_exception_criteria(self, *args, **kwargs):
        super().receive_exception_criteria(*args, **kwargs)

    def create_sales_forecast(self, *args, **kwargs):
        super().create_sales_forecast(*args, **kwargs)

    def receive_sales_forecast_revision(self, *args, **kwargs):
        super().receive_sales_forecast_revision(*args, **kwargs)

    def send_sales_forecast(self, *args, **kwargs):
        super().send_sales_forecast(*args, **kwargs)

    def receive_product_activity(self, *args, **kwargs):
        super().receive_product_activity(*args, **kwargs)

    def create_product_activity(self, *args, **kwargs):
        super().create_product_activity(*args, **kwargs)

    def send_product_activity(self, *args, **kwargs):
        super().send_product_activity(*args, **kwargs)

    def create_item_information_request(self, *args, **kwargs):
        super().create_item_information_request(*args, **kwargs)

    def reuse_sales_forecast(self, *args, **kwargs):
        super().reuse_sales_forecast(*args, **kwargs)

    def receive_sales_forecast(self, *args, **kwargs):
        super().receive_sales_forecast(*args, **kwargs)

    def revise_sales_forecast(self, *args, **kwargs):
        super().revise_sales_forecast(*args, **kwargs)

    def receive_retail_event(self, *args, **kwargs):
        super().receive_retail_event(*args, **kwargs)

    def send_TILP_revision(self, *args, **kwargs):
        super().send_TILP_revision(*args, **kwargs)

    def receive_TILP(self, *args, **kwargs):
        super().receive_TILP(*args, **kwargs)

    def revise_trade_location_profile(self, *args, **kwargs):
        super().revise_trade_location_profile(*args, **kwargs)

    def send_retail_event(self, *args, **kwargs):
        super().send_retail_event(*args, **kwargs)

    def receive_retail_event_revision(self, *args, **kwargs):
        super().receive_retail_event_revision(*args, **kwargs)

    def send_TILP(self, *args, **kwargs):
        super().send_TILP(*args, **kwargs)

    def receive_trade_location_profile(self, *args, **kwargs):
        super().receive_trade_location_profile(*args, **kwargs)

    def revise_retail_event(self, *args, **kwargs):
        super().revise_retail_event(*args, **kwargs)

    def create_TILP(self, *args, **kwargs):
        super().create_TILP(*args, **kwargs)

    def create_retail_event(self, *args, **kwargs):
        super().create_retail_event(*args, **kwargs)
