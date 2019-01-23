"""
The functions module defines all registered functions for the various
business applications. These functions are defined to take arbitrary set of
positional and keyword arguments. The goal of these functions will include
but not limited to:
1. Set the state of defined business processes
2. Send or broadcast signals to dedicated signal handlers
3. Validate the input parameters to various tasks ensuring target function
receives appropriate parameters

These functions will not create and modify business documents for various
processes as target functions registered for each process will do this tasks as
applicable

The process covered will include:
1. Tendering
2. Catalogue
3.Quotation
4. Ordering
5. Fulfilment
6. Billing
7. Freight Billing
8. Utility Billing
9. Payment Notification
10. Collaborative Planning, Forecasting, and Replenishment
11. Vendor Managed Inventory
12. International Freight Management
13. Intermodal Freight Management
14. Freight Status Reporting
15. Certification of Origin of Goods
"""

from collections import Iterable
from ubl.business_systems import BusinessService


def pre_process(documents: tuple=None, tasks: tuple=None,
                parties: tuple=None, conditions: list=None, flags: list=None):
    # function takes a business process flag to determine what docs to create
    if isinstance(documents, Iterable) and len(documents) == 2:
        source, target = documents
    else:
        raise RuntimeError('Expected parameter to be iterable with two '
                           'elements: source document, target document')
    if isinstance(tasks, Iterable) and len(tasks) == 2:
        task, parent = tasks
    else:
        raise RuntimeError('Expected parameter to be iterable with two '
                           'elements: task, parent task')
    if isinstance(parties, Iterable) and len(parties) == 2:
        buyer, seller = parties
    else:
        raise RuntimeError('Expected parameter to be iterable with two '
                           'elements: buyer, seller')
    if not isinstance(conditions, Iterable):
        raise RuntimeError('Expected parameter to be iterable')
    if isinstance(flags, Iterable):
        # create multiple documents for each business process
        pass
    elif isinstance(flags, BusinessProcess):
        # create documents for the given process
        pass
    outcome = None  # defines outcome of the task
    status = None  # defines status of the task
    phase = None  # defines phase the task is in
    rank = None  # defines the rank of the task in the task queue
    service_cost = None # Each business_action takes a service charge object
    # (cost) as a parameter


def post_process():
    # set the state, create document etc.
    pass



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