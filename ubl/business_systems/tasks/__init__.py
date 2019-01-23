from enum import IntFlag
from collections import OrderedDict
from abc import ABC
from weakref import WeakValueDictionary, WeakKeyDictionary


class BusinessTaskMixin(ABC):
    # Define the methods handling the base behaviour of the business task object
    # Methods will include operations for task's condition, process, phase,
    # status, & documents
    pass


class TaskRegistry:
    _business_tasks = None
    _tasks = iter([
        'prepare_information_notice',
    ])

    def __init__(self):
        pass


class BusinessTask (BusinessTaskMixin):
    """
    define various task actions as methods
    _business_service
    _associated_documents
    _status
    _phase
    _name
    _actor  # tuple of actor type and id
    _func
    """
    def __init__(self):
        pass


class Status(IntFlag):
    # Define the general status flags and methods for status business_management
    pass


class TaskStatus(Status):
    pass


class TaskCondition(IntFlag):
    pass


class TaskState:
    # Save the state of the business service or process after executing a task
    pass


class TaskQueue(OrderedDict):
    # Save the business task or functions for a given process or entire
    # business processes. Use the weakref to manage tasks garbage collection
    cache = WeakKeyDictionary
    task_state_cache = WeakValueDictionary


