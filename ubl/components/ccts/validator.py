import heapq
import ast
from collections import defaultdict
from enum import IntFlag, unique


class NoneDataIndexes(IntFlag):
    NONE_DATA = 0


class NotImplementedDataIndexes(IntFlag):
    NOT_IMPLEMENTED_DATA = 1


@unique
class IntDataIndexes(IntFlag):
    INT_DATA = 2
    ABOVE_ALLOWED_MIN = 3
    BELOW_ALLOWED_MAX = 4
    ABOVE_INT_MIN = 2
    BELOW_INT_MAX = 3


@unique
class BoolDataIndexes(IntFlag):
    BOOL_DATA = 0
    TRUE = 1
    FALSE = 2


@unique
class FloatDataIndexes(IntFlag):
    FLOAT_DATA = 0
    ABOVE_ALLOWED_MIN = 4
    BELOW_ALLOWED_MAX = 5
    ABOVE_FLOAT_MIN = 2
    BELOW_FLOAT_MAX = 3


@unique
class DateTimeDataIndexes(IntFlag):
    DATETIME_DATA = 0
    NULL = 1
    ABOVE_ALLOWED_MIN = 3
    BELOW_ALLOWED_MAX = 4
    BEFORE_DATETIME = 2
    AFTER_DATETIME = 3


@unique
class StrDataIndexes(IntFlag):
    STRING_DATA = 0
    EMPTY = 1
    ABOVE_ALLOWED_MIN = 2
    BELOW_ALLOWED_MAX = 3
    EQUAL_TARGET = 4


class CCTSCategoryCode(IntFlag):
    pass


class DocumentFieldDict(dict):
    # defines the lookup table for the document fields.
    # Each field has a given data type it accepts
    _fields = ()
    _values = ()
    _type_match = {}

    def __init__(self, *args, **kwargs):
        super(DocumentFieldDict, self).__init__(*args, **kwargs)
        allowed_datatype = defaultdict()
        heapq.heapify(allowed_datatype)
        self._type_match = {
            'string': 1,
            'int': 2
        }
        self.value_map = [0, 0, 0, 0]

    def __getitem__(self, item):
        # retrieve value for the given item matching a key
        result = ast.literal_eval(item)
        data_type = type(result)
        index = self._type_match.get(data_type.__class__.__name__, None)
        v = self.value_map
        v[index] = 1

    def __setitem__(self, key, value):
        # set the value for the given key matching a named field
        pass


def data_checker(*args, **kwargs):
    # define means of validating various datatypes
    truth_table = []

    def _int_check(int_data, *, allowed_min, allowed_max, int_min, int_max):
        nonlocal truth_table
        data_type, value = int_data
        if data_type == 'int':
            a = 1 if value < allowed_min else 0
            b = 1 if value > allowed_max else 0
            c = 1 if value > int_min else 0,
            d = 1 if value > int_max else 0,
            truth_table[IntDataIndexes.INT_DATA] = (a, b, c, d)
        return all(truth_table[IntDataIndexes.INT_DATA])

    def _float_check(float_data, *, allowed_min, allowed_max, float_min,
                     float_max):
        nonlocal truth_table
        data_type, value = float_data
        if data_type == 'float':
            a = 1 if value < allowed_min else 0
            b = 1 if value > allowed_max else 0
            c = 1 if value > float_min else 0,
            d = 1 if value > float_max else 0,
            truth_table[FloatDataIndexes.FLOAT_DATA] = (a, b, c, d)
        return all(truth_table[FloatDataIndexes.FLOAT_DATA])

    def _bool_check(bool_data):
        nonlocal truth_table
        data_type, value = bool_data
        if data_type == 'bool':
            a = 1 if value is True else 0
            b = 1 if value is False else 0
            truth_table[BoolDataIndexes.BOOL_DATA] = (a, b, None, None)
        return any(truth_table[FloatDataIndexes.FLOAT_DATA])

    def _datetime_check(*args):
        nonlocal truth_table
        pass

    def _str_check(*args):
        nonlocal truth_table
        pass

    try:
        dt = ast.literal_eval(args[0])
        dd = type(dt)
        data = dd.__class__.__name__, dt
        return _bool_check(data) or \
            _int_check(data) or \
            _float_check(data) or \
            _datetime_check(data) or \
            _str_check(data)

    except SyntaxError:
        raise SyntaxError('Invalid string argument being parsed')

    except TypeError:
        raise TypeError('Invalid datatype being assigned')
