import pytest
from ubl.business_processes.billing import BillingService
from ubl.business_processes.cataloguing import CatalogueService
from ubl.business_processes.forecasting import ForecastService
from ubl.business_processes.frieght import InitiateFreightService
from ubl.business_processes.fulfilment import FulfilmentService
from ubl.business_processes.inventory import InventoryService
from ubl.business_processes.ordering import OrderingService
from ubl.business_processes.quotation import QuotationService
from ubl.business_processes.tendering import TenderService
from ubl.business_systems import BusinessService


@pytest.mark.parametrize("service, expected", [
    (BillingService, True),
    (CatalogueService, True),
    (ForecastService, True),
    (InitiateFreightService, True),
    (FulfilmentService, True),
    (InventoryService, True),
    (OrderingService, True),
    (QuotationService, True),
    (TenderService, True),
])
def test_services(service, expected):
    assert issubclass(service, BusinessService) == expected

