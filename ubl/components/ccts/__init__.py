from datetime import datetime
from numbers import Real, Number
import math
from re import compile
from collections import namedtuple
from ubl.exceptions import ComponentValueError


class DocumentAnnotation:
    # Defines the lookup for various document annotations as specified by UBL
    # Entries in annotation can be filled from a annotation config parser
    __slots__ = ('unique_id', 'category_code', 'dictionary_entry_name',
                 'version_id', 'definition', 'representation_term_name',
                 'primitive_type', )

    def __init__(self, *, kwargs):
        self.unique_id = kwargs.get('unique_id', None)
        self.category_code = kwargs.get('category_code', None)
        self.dictionary_entry_name = kwargs.get('dictionary_entry_name', None)
        self.version_id = kwargs.get('version_id', None)
        self.definition = kwargs.get('definition', None)
        self.representation_term_name = \
            kwargs.get('representation_term_name', None)
        self.primitive_type = kwargs.get('primitive_type', None)


class DocumentFieldAnnotation:
    # list the meta data describing a given field
    # the annotation can be used to provide more information about a field
    # data
    # Defines the lookup for various fields' annotations as specified by UBL.
    # DocumentFieldAnnotation.get('Order','OrderDate', None_or_annotation)
    # This class serves as a wrapper to the config wrapper for field annotations
    pass


class DataType:
    __slots__ = '__desc__', '__meta__', 'value'
    
    def __init__(self, *args, **kwargs):
        super(DataType, self).__init__()

    def update(self, value):
        raise NotImplementedError

    @classmethod
    def mock(cls, *args, **kwargs):
        raise NotImplementedError


def _prepare_meta(*args, **kwargs):
    if isinstance(args[0], dict):
        meta = args[0]
        meta.update({x: str(y) for x, y in enumerate(kwargs) if x in meta})


class AssociatedBusinessEntity(DataType):
    __slots__ = 'associations'

    def __init__(self):
        self.associations = {}
        super(AssociatedBusinessEntity, self).__init__()

    def update(self, value):
        pass

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @staticmethod
    def associate(self, entity, **kwargs):
        # associate a given asbie with the target
        if entity not in self.associations:
            key = entity.__class__.__name__
            value = (entity, kwargs) if kwargs is not None else entity
            self.associations[key] = value


class AmountType(DataType, Real):
    # emulate a monetary value having magnitude and description e.g currency
    # all numeric operations are carried on the magnitude and the description
    # may be used to explain results or convert results to other monetary values

    __slots__ = '_amount', 'currency', 'currency_code',

    def __init__(self, amount, *, currency=None, currency_code=None,
                 version_id=None):
        self.__meta__ = dict.fromkeys(['version_id', ])
        try:
            self._amount = float(amount)
            code = currency_code
            if code:
                self.currency_code = code
            if isinstance(currency, str) and len(currency) > 0:
                self.currency = currency
            _prepare_meta(self.__meta__, version_id=version_id)
            self.__desc__ = DocumentAnnotation(kwargs={
                'unique_id': 'UNDT000001',
                'category_code': 'CCT',
                'dictionary_entry_name': 'Amount.Type',
                'version_id': '1.0',
                'definition': 'A number of monetary units specified in a '
                              'currency where the unit of the currency is '
                              'explicit or implied.',
                'representation_term_name': 'Amount',
                'primitive_type': 'float',
            })
            super(AmountType, self).__init__()
        except ComponentValueError:
            raise ComponentValueError('Invalid parameters provided for '
                                      'component type')

    @property
    def amount(self):
        amt = namedtuple(
            self.__class__.__name__,
            (
                'amount',
                'currency',
                'currency_code',
                'version_id',
                'annotations'
            )
        )
        return amt(
            amount=self._amount,
            currency=self.__meta__['currency'],
            currency_code=self.__meta__['currency_code'],
            version_id=self.__meta__['version_id'],
            annotations=self.__desc__
        )

    def update(self, value):
        # override a given amount only if currency, currency_code are identical
        if isinstance(value, float):
            self._amount = value
        elif isinstance(value, dict):
            amount = value.get('amount', 0.00)
            currency = value.get('currency', None)
            currency_code = value.get('currency_code', None)
            version_id = value.get('version_id', None)
            if all((
                        currency == self.__meta__['currency'],
                        currency_code == self.__meta__['currency_code'],
                        version_id == self.__meta__['version_id'],
                        isinstance(amount, float)
                    )):
                self._amount = amount
            else:
                # monetary objects are not equal
                money = AmountType.mock(amount, currency=currency,
                                        currency_code=currency_code,
                                        version_id=version_id)
                target = self.convert_currency(money)
                self._amount = target.amount
        elif isinstance(value, self):
            money = self.convert_currency(value)
            self._amount = money.amount
        else:
            return NotImplemented

    @classmethod
    def mock(cls, *args, **kwargs):
        # make default instance with no currency or code
        return cls(0.0, currency=kwargs.get('currency', None),
                   currency_code=kwargs.get('currency_code', None),
                   version_id=kwargs.get('version_id', None))

    def convert_currency(self, other):
        # convert other amount in different currencies to self if currencies
        # are different
        money = None
        if other.currency != self.currency:
            money = AmountType.currency_exchange(other, self.currency)
        return money

    @staticmethod
    def currency_exchange(self, amount, target=None):
        # compare from self currency to the target currency updating __meta__
        # to target (currency, currency_code, and version_id*)
        # This function will enable adding different currency types as they
        # will be internally converted if their currencies differ before +/- etc
        # Exchange rates retrieved from web services
        # If target is specified, then compares both self (method called from
        #  instance context) & amount to target
        # currency returning tuple of both conversions (self_conv, amount_conv)
        raise NotImplementedError

    def __le__(self, other):
        if isinstance(other, self):
            amt = self.convert_currency(other)
            amount = amt.get('amount', 0.0)
            return self._amount <= amount
        elif isinstance(other, (int, float)):
            return self._amount <= other
        else:
            return NotImplemented

    def __floor__(self):
        return math.floor(self._amount)

    def __rdivmod__(self, other):
        if isinstance(other, (int, float)):
            return super().__rdivmod__(other)
        elif isinstance(other, self):
            money = self.convert_currency(other)
            return super().__rdivmod__(money.get('amount', 0.0))

    def __divmod__(self, other):
        if isinstance(other, (int, float)):
            return super().__divmod__(other)
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return super().__divmod__(amt.get('amount', 0.0))

    def __round__(self, ndigits=None):
        return round(self._amount, ndigits)

    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return self._amount % other
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return self._amount % amt.get('amount', 0.0)
        else:
            return NotImplemented

    def __trunc__(self):
        return math.trunc(self._amount)

    def __lt__(self, other):
        if isinstance(other, self):
            amt = self.convert_currency(other)
            return self._amount < amt.get('amount', 0.0)
        elif isinstance(other, (int, float)):
            return self._amount < other
        else:
            return NotImplemented

    @property
    def real(self):
        return super().real()

    def conjugate(self):
        return super().conjugate()

    @property
    def imag(self):
        return super().imag()

    def __rfloordiv__(self, other):
        if isinstance(other, (int, float)):
            return other // self._amount
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return amt.get('amount', 0.0) // self._amount

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self._amount // other
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return self._amount // amt.get('amount', 0.0)

    def __rmod__(self, other):
        if isinstance(other, (int, float)):
            return other % self._amount
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return amt.get('amount', 0.0) % self._amount

    def __complex__(self):
        return super().__complex__()

    def __float__(self):
        # convert the AmountType to a float
        if not isinstance(self._amount, float):
            self._amount = 0.00
        return self._amount

    def __ceil__(self):
        math.ceil(self._amount)

    def __eq__(self, other):
        # monetary objects are equal if their currencies and amount are same
        if isinstance(other, self):
            return self.amount == other.amount
        return False

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return other - self._amount
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return amt.get('amount', 0.0) - self._amount

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self._amount - other
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return self._amount - amt.get('amount', 0.0)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self._amount + other
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return self._amount + amt.get('amount', 0.0)

    def __bool__(self):
        return self._amount != 0

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return other / self._amount
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return amt.get('amount', 0.0) / self._amount

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self._amount / other
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return self._amount / amt.get('amount', 0.0)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self._amount * other
        elif isinstance(other, self):
            amt = self.convert_currency(other)
            return self._amount * amt.get('amount', 0.0)
        else:
            return NotImplemented

    def __abs__(self):
        return abs(self._amount)

    def __pow__(self, exponent):
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return other * self._amount
        else:
            return NotImplemented

    def __neg__(self):
        return -1 * self._amount

    def __rpow__(self, base):
        return NotImplemented

    def __pos__(self):
        return self._amount

    def __radd__(self, other):
        if isinstance(other, self):
            amount = self.convert_currency(other)
            return amount.get('amount', 0.0) + self._amount
        elif isinstance(other, (int, float)):
            return other + self._amount


class BinaryObjectType(DataType):

    def __init__(self, source=None, encoding=None, errors=None):
        self.value = bytearray(source, encoding, errors)
        super(BinaryObjectType, self).__init__()

    def update(self, value):
        raise NotImplementedError

    @classmethod
    def mock(cls, *args, **kwargs):
        return bytearray()


class TextType(DataType):
    # define the attributes common to all text type for components
    __slots__ = '_pattern', 'max_length', 'value',

    def __init__(self, value, pattern=None, max_length=200, **kwargs):
        self._pattern = compile(pattern)
        if isinstance(value, str) and len(value) > 0:
            self.value = value if self._pattern.search(value) else None
        if max_length > 0 and self.value:
            if len(self.value) > max_length:
                raise ValueError('Max length exceeded')
        super(TextType, self).__init__()

    def is_valid(self):
        return self.value is not None

    def update(self, value):
        return NotImplemented

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls(*args, **kwargs)


class CodeType(TextType):
    __slots__ = 'code', '__meta__'

    def __init__(self, code, *, pattern=None, max_length=None, list_id=None,
                 list_agency_id=None, list_agency_name=None,
                 list_name=None, list_version_id=None, name=None,
                 language_id=None, list_uri=None, list_scheme_uri=None):
        self.__meta__ = dict.fromkeys(['list_id', 'list_agency_id',
                                       'list_agency_name', 'list_name',
                                       'list_version_id', 'name', 'language_id',
                                       'list_uri', 'list_scheme_uri'])
        _prepare_meta(self.__meta__, list_id=list_id,
                      list_agency_id=list_agency_id,
                      list_agency_name=list_agency_name, list_name=list_name,
                      list_version_id=list_version_id, name=name,
                      language_id=language_id, list_uri=list_uri,
                      list_scheme_uri=list_scheme_uri)
        if code:
            code = str(code).upper()
            super(CodeType, self).__init__(code, pattern=pattern,
                                           max_length=max_length,
                                           list_id=list_id,
                                           list_agency_id=list_agency_id,
                                           list_agency_name=list_agency_name,
                                           list_name=list_name,
                                           list_version_id=list_version_id,
                                           name=name,
                                           language_id=language_id,
                                           list_uri=list_uri,
                                           list_scheme_uri=list_scheme_uri,)


class NameType(TextType):

    def __init__(self, name, pattern=None, max_length=150):
        if isinstance(name, str) and len(name) > 150:
            raise ValueError('Name should not be longer than 150 characters')
        else:
            self.value = name
            super(NameType, self).__init__(self.value, pattern=pattern,
                                           max_length=max_length)


class DateTimeType(DataType):
    __slots__ = 'year', 'month', 'day', 'hour', 'minute', 'second', \
                'microsecond', 'tzinfo', 'fold', 'value'

    def __new__(cls, year, month, day, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *, fold=0):
        return datetime(DateTimeType, cls).__new__(
            year, month, day, hour=hour, minute=minute, second=second,
            microsecond=microsecond, tzinfo=tzinfo, fold=fold)

    def __init__(self, value, year=None, month=None, day=None,
                 hour=None, minute=None, second=None,
                 microsecond=None, tzinfo=None, fold=None):
        if isinstance(value, datetime):
            self.value = value
        else:
            self.value = datetime(year=year, month=month, day=day, hour=hour,
                                  minute=minute, second=second,
                                  microsecond=microsecond, tzinfo=tzinfo,
                                  fold=fold)
        super(DateTimeType, self).__init__()

    @classmethod
    def update(cls, value):
        if isinstance(value, datetime):
            cls.year = value.year
            cls.month = value.month
            cls.day = value.day
            cls.hour = value.hour
            cls.minute = value.minute
            cls.second = value.second
            cls.microsecond = value.microsecond
            cls.tzinfo = value.tzinfo
        else:
            return NotImplemented

    @classmethod
    def mock(cls, *args, **kwargs):
        if len(args) > 0:
            return args[0] if isinstance(args[0], datetime) else datetime.now()
        elif kwargs:
            return datetime(**kwargs)
        else:
            return datetime.now()


class IdentifierType(TextType):
    def __init__(self, value, *, pattern=None, max_length=100, scheme_id=None,
                 scheme_name=None, scheme_agency_id=None,
                 scheme_agency_name=None,
                 scheme_version_id=None, scheme_data_uri=None, scheme_uri=None):

        self.__meta__ = dict.fromkeys(['scheme_id', 'scheme_name',
                                       'scheme_agency_id',
                                       'scheme_agency_name',
                                       'scheme_version_id',
                                       'scheme_data_uri', 'scheme_uri', ])
        _prepare_meta(self.__meta__, scheme_id=scheme_id,
                      scheme_name=scheme_name,
                      scheme_agency_id=scheme_agency_id,
                      scheme_agency_name=scheme_agency_name,
                      scheme_version_id=scheme_version_id,
                      scheme_data_uri=scheme_data_uri,
                      scheme_uri=scheme_uri)
        super(IdentifierType, self).__init__(value, pattern=pattern,
                                             max_length=max_length)


class IndicatorType(DataType):

    __slots__ = ('_state', 'indicator_name')

    def __init__(self, indicator=None, state=False):
        self._state = state
        self.__meta__ = None
        self.__desc__ = None
        self.indicator_name = indicator
        super(IndicatorType, self).__init__()

    def update(self, value):
        self._state = bool(value)

    def __and__(self, other):
        """ Return self and other. """
        if isinstance(other, self):
            return self._state and other._state
        elif isinstance(other, bool):
            return self._state and other
        else:
            return self._state and bool(other)

    def __or__(self, other):
        """ Return self or other. """
        if isinstance(other, self):
            return self._state or other._state
        elif isinstance(other, bool):
            return self._state or other
        else:
            return self._state or bool(other)

    def __rand__(self, other):
        """ Return value and self = self and value """
        return self.__and__(other)

    def __ror__(self, other):
        """ Return value or self = self or value. """
        return self.__or__(other)

    def __rxor__(self, other):
        """ Return value^self. """
        if isinstance(other, self):
            return self._state ^ other._state
        elif isinstance(other, bool):
            return self._state ^ other
        else:
            return self._state ^ bool(other)

    def __xor__(self, other):
        """ Return self^value. """
        if isinstance(other, self):
            return other._state ^ self._state
        elif isinstance(other, bool):
            return other ^ self._state
        else:
            return bool(other) ^ self._state

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls(*args, **kwargs)


class NumericType(DataType, Number):

    __slots__ = '_value',

    def __init__(self, value, *, kwargs):
        try:
            self._value = float(value)
            self.__desc__ = kwargs.get('__desc__', None)
            super(NumericType, self).__init__()
        except ValueError:
            raise ValueError('Invalid parameter provided as number')

    def update(self, value):
        try:
            self._value = float(value)
        except ValueError:
            raise ValueError
        except Exception:
            raise Exception('Invalid numeric data provided')

    @property
    def value(self):
        return self._value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self._value + other
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self._value - other
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self._value * other
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self._value / other
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self._value // other
        else:
            return NotImplemented

    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return self._value % other
        else:
            return NotImplemented

    def __divmod__(self, other):
        if isinstance(other, (int, float)):
            return divmod(self._value, other)
        else:
            return NotImplemented

    def __pow__(self, other, modulo=None):
        if isinstance(other, (int, float)) and isinstance(modulo, (int, float)):
            return pow(self._value, other, modulo)
        elif isinstance(other, (int, float)) and modulo is None:
            return pow(self._value, other)
        else:
            return NotImplemented

    def __and__(self, other):
        if isinstance(other, (int, float, bool)):
            return self._value and other
        else:
            return NotImplemented

    def __or__(self, other):
        if isinstance(other, (int, float, bool)):
            return self._value or other
        else:
            return NotImplemented

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls(*args, **kwargs)


class MeasureType(NumericType):
    pass


class QuantityType(NumericType):
    pass


class BusinessDocument:

    __slots__ = '__desc__', 'xml_namespace', 'extension'

    def __init__(self):
        # Namespace can be defined by individual documents
        self.xml_namespace = None
        # @todo: define annotation lookups for document and field level
        self.__desc__ = None

    def __iter__(self):
        if self.__slots__ is not None:
            for field in self.__slots__:
                yield (field, getattr(self, field, None))
        else:
            for field in self.__dict__:
                yield (field, getattr(self, field, None))

    def __getitem__(self, item):
        if item not in self.__slots__ or item not in self.__dict__:
            raise IndexError('Index does not exist in Business Document')
        return getattr(self, item, None)

    def __setitem__(self, key, value):
        # @todo: add the lookup for the allowed values and datatype
        if key not in self.__slots__ or key not in self.__dict__:
            raise IndexError('Index does not exist in Business Document')
        setattr(self, key, value)

    def __delattr__(self, item):
        raise AttributeError('Attribute cannot be deleted in Business Document')

    def __getattribute__(self, name):
        return getattr(self, name, None)
