from enum import IntFlag
from collections import OrderedDict, Iterable
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


class business_action:
    """
    Define the base class callable for performing business actions. These
    callable can also serve as decorators.
    Each business_action takes a service charge object (cost) as a parameter
    """
    # @todo: initialize all business actions with a cost component
    def __init__(self, documents=None, tasks=None, parties=None,
                 conditions=None, flags=None):
        self.outcome = None  # defines outcome of the task
        self.status = None  # defines status of the task
        self.phase = None  # defines phase the task is in
        self.rank = None  # defines the rank of the task in the task queue
        if isinstance(documents, Iterable) and len(documents) == 2:
            self.source, self.target = documents
        else:
            raise RuntimeError('Expected parameter to be iterable with two '
                               'elements: source document, target document')
        if isinstance(tasks, Iterable) and len(tasks) == 2:
            self.task, self.parent = tasks
        else:
            raise RuntimeError('Expected parameter to be iterable with two '
                               'elements: task, parent task')
        if isinstance(parties, Iterable) and len(parties) == 2:
            self.buyer, self.seller = parties
        else:
            raise RuntimeError('Expected parameter to be iterable with two '
                               'elements: buyer, seller')
        if isinstance(conditions, Iterable):
            self.conditions = conditions
        else:
            raise RuntimeError('Expected parameter to be iterable')
        if isinstance(flags, Iterable):
            self.flags = flags
        else:
            raise RuntimeError('Expected parameter to be iterable')


class assign_task(business_action):
    def __init__(self, *args, **kwargs):
        super(assign_task, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class award(business_action):
    def __init__(self, *args, **kwargs):
        super(award, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class create_document(business_action):
    def __init__(self, *args, **kwargs):
        super(create_document, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class evaluate_document(business_action):
    def __init__(self, *args, **kwargs):
        super(evaluate_document, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass

class prepare_task(business_action):
    def __init__(self, *args, **kwargs):
        super(prepare_task, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class perform_task(business_action):
    def __init__(self, *args, **kwargs):
        super(perform_task, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass

class publish_document(business_action):
    def __init__(self, *args, **kwargs):
        super(publish_document, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class receive_document(business_action):
    def __init__(self, *args, **kwargs):
        super(receive_document, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class request_document(business_action):
    def __init__(self, *args, **kwargs):
        super(request_document, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class request_action(business_action):
    def __init__(self, *args, **kwargs):
        super(request_action, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class validate_task(business_action):
    def __init__(self, *args, **kwargs):
        super(validate_task, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class conditional_decision(business_action):
    def __init__(self, *args, **kwargs):
        super(conditional_decision, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass


class terminate_task(business_action):
    def __init__(self, *args, **kwargs):
        super(terminate_task, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        pass