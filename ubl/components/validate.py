import re
from enum import IntFlag, unique, auto
from datetime import datetime, timedelta

__all__ = 'validate'


class DataTypeIndexes(IntFlag):
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    STR = auto()
    DATETIME = auto()
    ASBIE = auto()
    BINARY = auto()
    NONE = auto()
    NOT_IMPLEMENTED = auto()


class NoneDataIndexes(IntFlag):
    IS_NONE = 0


class NotImplementedDataIndexes(IntFlag):
    NOT_IMPLEMENTED_DATA = 1


@unique
class IntDataIndexes(IntFlag):
    ABOVE_ALLOWED_MIN = 3
    BELOW_ALLOWED_MAX = 4
    ABOVE_INT_MIN = 2
    BELOW_INT_MAX = 3


@unique
class BoolDataIndexes(IntFlag):
    TRUE = 1
    FALSE = 2


@unique
class FloatDataIndexes(IntFlag):
    ABOVE_ALLOWED_MIN = 4
    BELOW_ALLOWED_MAX = 5
    ABOVE_FLOAT_MIN = 2
    BELOW_FLOAT_MAX = 3


@unique
class DateTimeDataIndexes(IntFlag):
    AFTER_LATEST = 1
    BEFORE_EARLIEST = 2
    BELOW_ALLOWED_MAX = 3
    BEFORE_DATETIME = 4
    AFTER_DATETIME = 5
    WITHIN_START_DURATION = 6
    WITHIN_END_DURATION = 7


@unique
class StrDataIndexes(IntFlag):
    EMPTY_STR = 1
    ABOVE_ALLOWED_MIN = 2
    BELOW_ALLOWED_MAX = 3
    EQUAL_TARGET = 4
    MATCHED_PATTERN = 5


@unique
class AsbieDataIndexes(IntFlag):
    TARGET_COMPONENT = 1
    FULL_ASSOCIATION = 2
    PARTIAL_ASSOCIATION = 3
    NO_ASSOCIATION = 4


@unique
class BinaryObjectIndexes(IntFlag):
    IS_BYTE_ARRAY = 1
    IS_EMPTY_BYTES = 2
    IS_TARGET_BYTES = 3


class CCTSCategoryCode(IntFlag):
    pass


def validate(data, *, asbie_associations, asbie_component, binary_object_target,
             datetime_after, datetime_before, datetime_earliest,
             datetime_latest, datetime_within_end_duration,
             datetime_within_start_duration, float_allowed_max,
             float_allowed_min, float_max, float_min, int_allowed_max,
             int_allowed_min, int_max, int_min, str_max_length, str_min_length,
             str_pattern, str_target):
    # define means of validating various data types and base components
    truth_table = []
    data = ()

    def _int_check(*, allowed_min, allowed_max, sys_min, sys_max):
        nonlocal truth_table
        nonlocal data
        check = all(x for x in [isinstance(data, int), isinstance(
            allowed_max, int), isinstance(allowed_min, int), isinstance(
            int_min, int), isinstance(int_max, int)])
        if check:
            a = 1 if data >= allowed_min else 0
            b = 1 if data <= allowed_max else 0
            c = 1 if data > sys_min else 0,
            d = 1 if data < sys_max else 0,
            truth_table[DataTypeIndexes.INT] = dict(zip(
                (IntDataIndexes.ABOVE_ALLOWED_MIN,
                 IntDataIndexes.BELOW_ALLOWED_MAX,
                 IntDataIndexes.ABOVE_INT_MIN,
                 IntDataIndexes.BELOW_INT_MAX,),
                (a, b, c, d)
            ))
        return all(truth_table[DataTypeIndexes.INT].values())

    def _float_check(*, allowed_min, allowed_max, sys_min, sys_max):
        nonlocal truth_table
        nonlocal data
        check = all(x for x in [isinstance(allowed_max, float), isinstance(
            allowed_min, float)])
        if check:
            a = 1 if data >= allowed_min else 0
            b = 1 if data <= allowed_max else 0
            c = 1 if data != sys_min else 0,
            d = 1 if data != sys_max else 0,
            truth_table[DataTypeIndexes.FLOAT] = dict(zip(
                (FloatDataIndexes.ABOVE_ALLOWED_MIN,
                 FloatDataIndexes.BELOW_ALLOWED_MAX,
                 FloatDataIndexes.ABOVE_FLOAT_MIN,
                 FloatDataIndexes.BELOW_FLOAT_MAX,),
                (a, b, c, d)
            ))
        return all(truth_table[DataTypeIndexes.FLOAT].values())

    def _bool_check():
        nonlocal truth_table
        nonlocal data
        if isinstance(data, bool):
            a = 1 if data is True else 0
            b = 1 if data is False else 0
            truth_table[DataTypeIndexes.BOOL] = dict(zip(
                (BoolDataIndexes.TRUE, BoolDataIndexes.FALSE),
                (a, b, None, None)
            ))
        return any(truth_table[DataTypeIndexes.BOOL].values())

    def _str_check(*, allowed_min, allowed_max, target, pattern):
        # validate if the data is string type and if the specification is
        # reached or satisfied
        nonlocal truth_table, data
        check = any(x for x in [isinstance(data, str), len(data) <=
                                allowed_max, len(data) >= allowed_min,
                                data == target, data is None, ])
        if check:
            a = 1 if len(data) <= allowed_max else 0
            b = 1 if len(data) >= allowed_min else 0
            c = 1 if data == target else 0
            d = 1 if re.search(pattern, data) is not None else 0
            f = 1 if data is None else 0
            truth_table[DataTypeIndexes.STR] = dict(zip(
                (StrDataIndexes.BELOW_ALLOWED_MAX,
                 StrDataIndexes.ABOVE_ALLOWED_MIN,
                 StrDataIndexes.EQUAL_TARGET, StrDataIndexes.MATCHED_PATTERN,
                 StrDataIndexes.EMPTY),
                (a, b, c, d, f)
            ))
        return any(truth_table[DataTypeIndexes.STR].values())

    def _asbie_check(*, component, associations):
        # evaluate if the data has listed associations or elements of
        # associations.
        # association must be dict of class_name: (data_type, **kwargs)
        nonlocal truth_table
        nonlocal data
        check = any(x for x in [isinstance(data, component),
                                data.associations == associations])
        if check:
            a = 1 if isinstance(data, component) else 0
            b = 1 if data.associations == associations else 0
            c = 1 if not b and any(x for x in data.associations if
                                   x in associations) else 0
            truth_table[DataTypeIndexes.ASBIE] = dict(zip(
                (AsbieDataIndexes.TARGET_COMPONENT,
                 AsbieDataIndexes.FULL_ASSOCIATION,
                 AsbieDataIndexes.PARTIAL_ASSOCIATION,),
                (a, b, c)
            ))
        return any(truth_table[DataTypeIndexes.ASBIE].values())

    def _binary_object_check(*, target):
        nonlocal truth_table, data
        check = any(x for x in [isinstance(data, bytearray), isinstance(
            target, bytearray), data is not None])
        if check:
            a = 1 if isinstance(data, bytearray) else 0
            b = 1 if isinstance(data, bytearray) and data is None else 0
            c = 1 if data == target else 0
            truth_table[DataTypeIndexes.BINARY] = dict(zip(
                (BinaryObjectIndexes.IS_BYTE_ARRAY,
                 BinaryObjectIndexes.IS_EMPTY_BYTES,
                 BinaryObjectIndexes.IS_TARGET_BYTES),
                (a, b, c)
            ))
        return any(truth_table[DataTypeIndexes.BINARY].values())

    def _datetime_check(*, start, end, start_duration, end_duration, before,
                        after):
        nonlocal truth_table, data
        check = any(x for x in [isinstance(data, datetime),
                                isinstance(start, datetime),
                                isinstance(end, datetime),
                                isinstance(start_duration, timedelta),
                                isinstance(end_duration, timedelta),
                                isinstance(before, datetime),
                                isinstance(after, datetime)])
        if check:
            a = 1 if isinstance(data, datetime) else 0
            b = 1 if data <= start else 0
            c = 1 if data >= end else 0
            d = 1 if data - start == start_duration else 0
            e = 1 if end - data == end_duration else 0
            f = 1 if data < before else 0
            g = 1 if data > after else 0
            truth_table[DataTypeIndexes.DATETIME] = dict(zip(
                (DateTimeDataIndexes.IS_DATETIME,
                 DateTimeDataIndexes.BEFORE_EARLIEST,
                 DateTimeDataIndexes.AFTER_LASTEST,
                 DateTimeDataIndexes.WITHIN_START_DURATION,
                 DateTimeDataIndexes.WITHIN_END_DURATION,
                 DateTimeDataIndexes.BEFORE_DATETIME,
                 DateTimeDataIndexes.AFTER_DATETIME,),
                (a, b, c, d, e, f, g)
            ))

    try:
        return _str_check(allowed_min=str_min_length,
                          allowed_max=str_max_length, pattern=str_pattern,
                          target=str_target) or \
               _asbie_check(component=asbie_component,
                            associations=asbie_associations) or \
               _float_check(allowed_min=float_allowed_min,
                            allowed_max=float_allowed_max, sys_min=float_min,
                            sys_max=float_max) or \
               _int_check(allowed_min=int_allowed_min,
                          allowed_max=int_allowed_max, sys_min=int_min,
                          sys_max=int_max) or \
               _datetime_check(start=datetime_earliest, end=datetime_latest,
                               start_duration=datetime_within_start_duration,
                               end_duration=datetime_within_end_duration,
                               before=datetime_before, after=datetime_after) \
               or _bool_check() or \
               _binary_object_check(target=binary_object_target)

    except SyntaxError:
        raise SyntaxError('Invalid string argument being parsed')

    except TypeError:
        raise TypeError('Invalid data type being assigned')
    except ValueError:
        raise ValueError('Invalid parameters provided as data')
