# define the various CCTS data types for UBL components
from datetime import datetime
from numbers import Real, Number
import math
from re import search, compile
from collections import namedtuple


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
    __slots__ = '__desc__', '__meta__'

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
        pass

    def update(self, value):
        pass

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @staticmethod
    def associate(self, entity, **kwargs):
        # associate a given asbie with the target
        if isinstance(entity, self):
            # create association
            if entity not in self.associations:
                key = entity.__class__.__name__
                value = (entity, dict(kwargs)) if kwargs is not None else entity
                self.associations[key] = value


class AmountType(DataType, Real):
    # emulate a monetary value having magnitude and description e.g currency
    # all numeric operations are carried on the magnitude and the description
    # may be used to explain results or convert results to other monetary values

    __slots__ = ('_amount',)

    def __init__(self, amount, *, currency, currency_code, version_id):
        self.__meta__ = {}
        try:
            self._amount = float(amount)
            _prepare_meta(self.__meta__, currency=currency,
                          currency_code=currency_code,
                          version_id=version_id)
            self.__desc__ = DocumentAnnotation(kwargs={
                'unique_id': 'UNDT000001',
                'category_code': 'CCT',
                'dictionary_entry_name': 'Amount. Type',
                'version_id': '1.0',
                'definition': 'A number of monetary units specified in a '
                              'currency where the unit of the currency is '
                              'explicit or implied.',
                'representation_term_name': 'Amount',
                'primitive_type': 'float',
            })
        except TypeError:
            raise TypeError('Invalid amount provided')

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

    @property
    def currency(self):
        return self.__meta__.get('currency', None)

    def get(self, name, default=0.0):
        name = str(name).lower()
        if name == 'amount':
            return self._amount if self._amount > 0 else default
        if name == 'currency' or name == 'currency_code' or name == \
                'version_id':
            return self.__meta__.get(name, default)
        else:
            raise KeyError('Invalid key provided')

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
                money = AmountType(amount, currency=currency,
                                   currency_code=currency_code,
                                   version_id=version_id)
                target = self.convert_currency(money)
                self._amount = target.get('amount')
        elif isinstance(value, self):
            money = self.convert_currency(value)
            self._amount = money.get('amount')
        else:
            return NotImplemented

    @classmethod
    def mock(cls, *args, **kwargs):
        # make default instance with no currency or code
        return cls(0.0, currency='', currency_code='', version_id='')

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


class BinaryObjectType(DataType, bytearray):

    def update(self, value):
        pass

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls(*args, **kwargs)


class TextType(DataType, str):
    # define the attributes common to all text type for components
    __slots__ = '_pattern', 'max_length'

    def __init__(self, pattern=None, max_length=200):
        if compile(pattern):
            self._pattern = pattern
        if max_length > 0:
            if len(self) <= max_length:
                raise ValueError('Max length exceeded')
        super(TextType, self).__init__()

    def is_valid(self):
        # return true if the regex pattern is matched by self
        if self._pattern:
            return search(self._pattern, self)

    def update(self, value):
        pass

    @classmethod
    def mock(cls, *args, **kwargs):
        return cls(*args, **kwargs)


class CodeType(TextType):
    __slots__ = 'code'

    def __init__(self, code, *, list_id, list_agency_id, list_agency_name,
                 list_name, list_version_id, name, language_id, list_uri,
                 list_scheme_uri):
        self.__meta__ = {}
        if code:
            self.code = str(code).upper()
            _prepare_meta(self.__meta__, list_id=list_id,
                          list_agency_id=list_agency_id,
                          list_agency_name=list_agency_name,
                          list_name=list_name,
                          list_version_id=list_version_id, name=name,
                          language_id=language_id, list_uri=list_uri,
                          list_scheme_uri=list_scheme_uri, )
        super(CodeType, self).__init__()

    def update(self, value):
        return NotImplemented


class NameType(TextType):
    __slots__ = '_name'

    def __init__(self, name):
        if len(name) > 150:
            raise RuntimeError('Name should not be longer than 150 characters')
        else:
            self._name = name
            super(NameType, self).__init__(max_length=150)


class DateTimeType(DataType, datetime):

    def __new__(cls, year, month, day, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *, fold=0):
        return super(DateTimeType, cls).__new__(
            year, month, day, hour=hour, minute=minute, second=second,
            microsecond=microsecond, tzinfo=tzinfo, fold=fold)

    @classmethod
    def update(cls, value):
        if isinstance(value, datetime):
            cls._year = value.year
            cls._month = value.month
            cls._day = value.day
            cls._hour = value.hour
            cls._minute = value.minute
            cls._second = value.second
            cls._microsecond = value.microsecond
            cls._tzinfo = value.tzinfo
        else:
            return NotImplemented

    @classmethod
    def mock(cls, *args, **kwargs):
        if args is not None or kwargs is not None:
            return cls(*args, **kwargs)
        else:
            return datetime.now()


class IdentifierType(TextType):
    __slots__ = ('_identifier', 'scheme_id', 'scheme_name', 'scheme_agency_id',
                 'scheme_agency_name', 'scheme_version_id',
                 'scheme_data_uri', 'scheme_uri', )

    def __init__(self, *, scheme_id, scheme_name, scheme_agency_id,
                 scheme_agency_name, scheme_version_id, scheme_data_uri,
                 scheme_uri):
        self.__meta__ = {}
        _prepare_meta(self.__meta__, scheme_id=scheme_id,
                      scheme_name=scheme_name,
                      scheme_agency_id=scheme_agency_id,
                      scheme_agency_name=scheme_agency_name,
                      scheme_version_id=scheme_version_id,
                      scheme_data_uri=scheme_data_uri,
                      scheme_uri=scheme_uri)
        self.__desc__ = None
        super(IdentifierType, self).__init__()


class IndicatorType(DataType):

    __slots__ = ('_state', 'indicator_name')

    def __init__(self, indicator=None, state=False):
        self._state = state
        self.__meta__ = None
        self.__desc__ = None
        self.indicator_name = indicator

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

    __slots__ = '_value'

    def __init__(self, value, *, kwargs):
        try:
            self._value = float(value)
            self.__meta__ = kwargs.get('__meta__', {})
            self.__desc__ = kwargs.get('__desc__', None)
        except TypeError:
            raise TypeError('Invalid type provided as number')

    def update(self, value):
        try:
            self._value = float(value)
        except ValueError:
            raise ValueError

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
