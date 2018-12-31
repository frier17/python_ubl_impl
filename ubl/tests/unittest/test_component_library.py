from enum import IntFlag

import pytest

from ubl.components.ccts import CodeType, AmountType, \
    AssociatedBusinessEntity, DateTimeType, NumericType, TextType, \
    MeasureType, QuantityType, IdentifierType, IndicatorType, NameType
from ubl.components import ABIERegistry, BIERegistry, \
    BusinessDocumentRegistry, ProcessRegistry, Components, Documents, Schemas

"""
test_component_library
    Units: Base class - BIERegistry, ABIERegistry, BusinessDocumentRegistry
    -- Assert BIERegistry, ABIERegistry, BusinessDocumentRegistry are all types
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
    (BusinessDocumentRegistry, True),
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
    ('APPLICATION_RESPONSE', BusinessDocumentRegistry, True),
    ('BILL_OF_LADING', BusinessDocumentRegistry, True),
    ('CATALOGUE', BusinessDocumentRegistry, True),
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
    (Documents, BusinessDocumentRegistry.ORDER_CANCELLATION, True),
    (Documents, BusinessDocumentRegistry.CATALOGUE, True),
    (Documents, BusinessDocumentRegistry.CATALOGUE, True),
    (Schemas, BusinessDocumentRegistry.CATALOGUE, True),
    (Schemas, BusinessDocumentRegistry.CREDIT_NOTE, True),
    (Schemas, BusinessDocumentRegistry.DEBIT_NOTE, True),
    (Schemas, BusinessDocumentRegistry.ORDER, True),
])
def test_component_maps(component_map, attribute, expected):
    with pytest.raises(AttributeError):
        instance = component_map()
        assert component_map.get(attribute) == expected
        assert instance[attribute] == expected


@pytest.mark.parametrize("component_map, attribute, expected", [
    (Components, ABIERegistry.APPEAL_TERMS, iter([
            ('description', text),
            ('presentation_period', asbie),
            ('appeal_information_party', asbie),
            ('appeal_receiver_party', asbie),
            ('mediation_party', asbie),
        ])),
    (Components, ABIERegistry.BUDGET_ACCOUNT, iter([
            ('id', identifier),
            ('budget_year', numeric),
            ('required_classification_scheme', asbie),
        ])),
    (Documents, BusinessDocumentRegistry.APPLICATION_RESPONSE, iter([
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
        ])),
    (Documents, BusinessDocumentRegistry.ATTACHED_DOCUMENT, iter([
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
        ])),
    (Schemas, BusinessDocumentRegistry.ATTACHED_DOCUMENT,
     'http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html'
     '#T-APPLICATION-RESPONSE'),
    (Schemas, BusinessDocumentRegistry.ATTACHED_DOCUMENT,
     'http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html'
     '#T-ATTACHED-DOCUMENT'),
])
def test_business_maps(component_map, attribute, expected):
    with pytest.raises(IndexError):
        instance = component_map()
        assert component_map.get(attribute) == expected
        assert instance[attribute] == expected

    with pytest.raises(AttributeError):
        record = component_map.get(attribute)
        assert record == expected
