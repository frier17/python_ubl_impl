from enum import IntFlag

import pytest
from ubl.business_document.components import ABIERegistry, BIERegistry, \
    DocumentRegistry, ComponentRegistry, Components, \
    Documents, Schemas
from ubl.business_processes import ProcessRegistry
from ubl.business_document.components.ccts import CodeType, AmountType, \
    AssociatedBusinessEntity, DateTimeType, NumericType, TextType, \
    MeasureType, QuantityType, IdentifierType, IndicatorType, NameType

"""
test_component_library
    Units: Base class - BIERegistry, ABIERegistry, DocumentRegistry
    -- Assert BIERegistry, ABIERegistry, DocumentRegistry are all types
    of IntFlag enum
    -- Assert each registry has named UBL components (BIE, ASBIE)
    -- Assert Components obeys the mapping protocol with support for __get__,
    __contains__, __getattr__, __setitem__, __setattr__
    -- Assert Components __setitem__, __setattr__ both throw RuntimeError
    -- Assert Components lookup calls of UBL named components returns instances
    of the python object with fields set to their default values
    -- Assert Documents obeys the mapping protocol with support for __get__,
    __contain__, __getattr__, __setitem__, __setattr__
    -- Assert Documents __setitem__, __setattr__ both throw RuntimeError
    -- Assert Documents lookup calls of UBL named documents returns instances of
    the python object with fields set to their default values
"""


@pytest.mark.parametrize("registry, expected", [
    (ABIERegistry, True),
    (BIERegistry, True),
    (DocumentRegistry, True),
    (ProcessRegistry, True)
])
def abie_registry_test(registry, expected):
    assert isinstance(registry, IntFlag) is expected


# define parameters for searching registries' aliases match UBL names
@pytest.mark.parametrize("alias, registry, expected", [
    ('ACCEPTED_INDICATOR', BIERegistry, True),
    ('AMOUNT', BIERegistry, True),
    ('LANGUAGE_ID', BIERegistry, True),
    ('ACCESSORY_RELATED_ITEM', ABIERegistry, True),
    ('ACTIVITY_PERIOD', ABIERegistry, True),
    ('ALLOWED_SUBCONTRACT_TERMS', ABIERegistry, True),
    ('APPLICATION_RESPONSE', DocumentRegistry, True),
    ('BILL_OF_LADING', DocumentRegistry, True),
    ('CATALOGUE', DocumentRegistry, True),
])
def bie_registry_test(alias, registry, expected):
    assert alias in registry.__members__ is expected


@pytest.mark.parametrize("component_map, attribute, expected", [
    (Components, '__getitem__', True),
    (Components, '__setitem__', True),
    (Components, '__getattr__', True),
    (Components, '__setattr__', True),
    (Components, '__contains__', True),
    (Documents, '__getitem__', True),
    (Documents, '__setitem__', True),
    (Documents, '__getattr__', True),
    (Documents, '__setattr__', True),
    (Documents, '__contains__', True),
    (Schemas, '__getitem__', True),
    (Schemas, '__setitem__', True),
    (Schemas, '__getattr__', True),
    (Schemas, '__setattr__', True),
    (Schemas, '__contains__', True),
])
def test_component_maps(component_map, attribute, expected):
    # Assert Components obeys the mapping protocol with support for __get__,
    # __contains__, __getattr__, __setitem__, __setattr__
    with pytest.raises(AttributeError):
        instance = component_map()
        assert hasattr(instance, attribute) is expected
    with pytest.raises(RuntimeError):
        instance[attribute] = None
        setattr(instance, attribute, None)


code = CodeType.mock('SAMPLE', pattern=r'/(\w+)/', max_length=5)
asbie = AssociatedBusinessEntity.mock()
measure = MeasureType.mock(0.0, kwargs={})
quantity = QuantityType.mock(0, kwargs={})
datetime_ = DateTimeType.mock()
numeric = NumericType.mock(0.0, kwargs={})
text = TextType.mock('Sample', pattern=r'\w+', max_length=100)
identifier = IdentifierType.mock('sample', pattern=r'/w+/')
indicator = IndicatorType.mock()
name = NameType.mock('Sample Name', pattern=r'\w+', max_length=20)
amount = AmountType.mock(0.0, currency='NAIRA', currency_code='NGN',
                         version_id='2.1')


@pytest.mark.parametrize("component_map, attribute, expected", [
    (Components, ABIERegistry.BILLING_REFERENCE, True),
    (Components, ABIERegistry.ACCOUNTING_CONTACT, True),
    (Components, ABIERegistry.ACTIVITY_DATA_LINE, True),
    (Documents, DocumentRegistry.ORDER_CANCELLATION, True),
    (Documents, DocumentRegistry.CATALOGUE, True),
    (Documents, DocumentRegistry.CATALOGUE, True),
    (Schemas, DocumentRegistry.CATALOGUE, True),
    (Schemas, DocumentRegistry.CREDIT_NOTE, True),
    (Schemas, DocumentRegistry.DEBIT_NOTE, True),
    (Schemas, DocumentRegistry.ORDER, True),
])
def test_component_maps(component_map, attribute, expected):
    instance = component_map()
    assert component_map.get(attribute) and True is expected
    assert instance[attribute] and True is expected


@pytest.mark.parametrize("component_map, attribute, expected", [
    (Components, ComponentRegistry.ACTIVITY_DATA_LINE, [
        ('id', identifier),
        ('supply_chain_activity_type_code', code),
        ('buyer_customer_party', asbie),
        ('seller_supplier_party', asbie),
        ('activity_period', asbie),
        ('activity_origin_location', asbie),
        ('activity_final_location', asbie),
        ('sales_item', asbie),
    ]),
    (Components, ComponentRegistry.ALLOWANCE_CHARGE, [
        ('id', identifier),
        ('charge_indicator', indicator),
        ('allowance_charge_reason_code', code),
        ('allowance_charge_reason', text),
        ('multiplier_factor', numeric),
        ('prepaid_indicator', indicator),
        ('sequence', numeric),
        ('amount', amount),
        ('base_amount', amount),
        ('accounting_cost_code', code),
        ('accounting_cost', text),
        ('per_unit_amount', amount),
        ('tax_category', asbie),
        ('tax_total', asbie),
        ('payment_means', asbie),
    ]),
    (Documents, DocumentRegistry.APPLICATION_RESPONSE, [
            ('ubl_version_id', identifier),
            ('customization_id', identifier),
            ('profile_id', identifier),
            ('profile_execution_id', identifier),
            ('id', identifier),
            ('uuid', identifier),
            ('issue_date', datetime_),
            ('issue_time', datetime_),
            ('response_date', datetime_),
            ('response_time', datetime_),
            ('note', text),
            ('version_id', identifier),
            ('signature', asbie),
            ('sender_party', asbie),
            ('receiver_party', asbie),
            ('document_response', asbie),
        ]),
    (Documents, DocumentRegistry.ATTACHED_DOCUMENT, [
            ('ubl_version_id', identifier),
            ('customization_id', identifier),
            ('profile_id', identifier),
            ('profile_execution_id', identifier),
            ('id', identifier),
            ('uuid', identifier),
            ('issue_date', datetime_),
            ('issue_time', datetime_),
            ('note', text),
            ('document_type_code', code),
            ('document_type', text),
            ('parent_document_id', identifier),
            ('parent_document_type_code', code),
            ('parent_document_version_id', identifier),
            ('signature', asbie),
            ('sender_party', asbie),
            ('receiver_party', asbie),
            ('attachment', asbie),
            ('parent_document_line_reference', asbie),
        ]),
])
def test_business_maps(component_map, attribute, expected):
    # compare set of retrieved values
    instance = component_map()
    instance_fields = ((x, y.__class__) for x, y in instance[attribute])
    expected_fields = ((x, y.__class__) for x, y in expected)
    assert set(instance_fields) == set(expected_fields)


@pytest.mark.parametrize("schemas, attribute, expected", [
    (Schemas, DocumentRegistry.ATTACHED_DOCUMENT,
     'http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html#T-ATTACHED-DOCUMENT'),
    (Schemas, DocumentRegistry.AWARDED_NOTIFICATION,
     'http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html#T-AWARDED-NOTIFICATION'),
])
def test_schema_maps(schemas, attribute, expected):
    component_url = schemas.get(attribute)
    assert component_url == expected
