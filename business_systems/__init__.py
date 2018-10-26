class BusinessTaskMixin(ABC):
    # Define the methods handling the base behaviour of the business task object
    # Methods will include operations for task's condition, process, phase, status, & documents
    pass


class TaskRegistry:
    _business_tasks = None

    def __init__(self):
        _tasks = [
            'prepare_information_notice',

        ]


class BusinessTask (BusinessTaskMixin):
    # define various task actions as methods
    _business_service
    _associated_documents
    _status
    _phase
    _name
    _actor  # tuple of actor type and id
    _func

    def __init__(self):
        pass


class TaskStatus(IntEnum):
    pass


class TaskCondition(Flag):
    pass


class TaskState:
    # Save the state of the business service or process after executing a task
    pass


class TaskQueue(OrderedDict):
    # Save the business task or functions for a given process or entire
    # business processes
    pass


