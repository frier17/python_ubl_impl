# Implement the BSO system
import types
import copy
from abc import ABC, abstractmethod
from weakref import WeakValueDictionary
from hashlib import sha512
from datetime import datetime
from ubl.utils import Singleton
from collections import namedtuple, Sequence, Iterable


class Payable(ABC):
    """
    The Payable interface defines a service which has monetary value.
    The services provided by this class will include:
    make payment
    acknowledge payment
    cancel payment
    receive payment
    """

    @abstractmethod
    def make_payment(self, payment, parties=None, documents=None,
                     protocol=None):
        """
        Attempt to make a payment using the specified parameters and protocol
        :param payment: the transactional or payment object.
        If a callable is passed, it should return a transaction object that
        can be paid for
        :param parties: the business entities involved in the transaction
        :param documents: the proof of business transaction as may be
        captured in a business document object, e.g an invoice
        :param protocol: the defined function or method by which the payment
        will be made. The protocol may, for example, make HTTP request to a
        payment gateway and return the result. If the protocol is not
        provided, then this method should be overridden in subclasses
        :return: True if the payment protocol was successful, else None
        """
        pass

    @abstractmethod
    def acknowledge_payment(self, payment, protocol=None):
        """
        Acknowledge a payment has been received and generate necessary
        business proof for that payment.
        :param payment: the transactional or payment object that was paid for
        :param protocol: Bespoke method to process acknowledgement of
        payment. If protocol is not provided then this method should be
        overridden in subclasses
        :return: business document as proof of payment
        """
        pass

    @property
    @abstractmethod
    def acknowledgement(self):
        """
        Returns a list of payment proofs for a recent transactional object
        :return: list of business documents as proof of payments
        """
        pass

    @abstractmethod
    def cancel(self, payment, protocol=None):
        """
        Attempts to cancel a payment or transactional object using the
        specified protocol
        :param payment: transactional or payment object
        :param protocol: the bespoke function for cancelling a payment. If
        none, then this method should be overridden in subclasses
        :return: True if successful or None otherwise.
        """
        pass

    @abstractmethod
    def receive(self, payment, protocol=None):
        """
        Attempts to receive a payment being offered by a buyer or entity.
        :param payment: transactional or payment object
        :param protocol: the bespoke function for receiving payment or None
        if method is overridden
        :return: True if successful, None otherwise.
        """
        pass


class BusinessOperations:

    @classmethod
    def assign_task(cls, assignment=None, documents=None, actions=None,
                    parties=None, conditions=None):
        """
        Assign a specified task to the named party(-ies)
        :param assignment: the named task or duty to assign
        :param documents: the required business document object
        :param actions: tuple of bespoke functions to perform assigning or
        called
        after assigning the named task
        :param parties: the assigner and assignee parties provided as tuples
        or dictionary
        :param conditions: list of boolean conditions or enumeration flags
        under which the task should be assigned
        :return: True if successful
        """
        pass

    @classmethod
    def award(cls, benefits=None, documents=None, actions=None, parties=None,
              conditions=None):
        """
        Attempts to assign benefit to selected party (-ies) based on the 
        operation of actions
        :param benefits: a mapping of the attribute name and value to be 
        updated in specified party, or a callable which performs the update 
        of the party attributes based on satisfied conditions
        :param documents: required business document instance by which 
        information for reward can be retrieved 
        :param actions: tuple of functions called to award a benefit or 
        after awarding a benefit
        :param parties: the specified benefactor(-s) and beneficiary(-ies)
        :param conditions: list of boolean conditions or enumeration flags
        under which the benefit should be awarded
        :return: True if successful and None otherwise.
        """
        pass

    @classmethod
    def create_document(cls, documents=None, actions=None, parties=None,
                        conditions=None):
        """
        Attempts to create a list of document by specified creator for 
        target recipients
        :param documents: the list of business documents to be generated 
        :param actions: tuple of function to call to create document and 
        function to call afterwards. Unused functions can be passed as None
        :param parties: the tuple of creator of the document and the 
        recipients. The document creator may be single entity or a group
        :param conditions: list of boolean conditions or enumeration flags
        under which the document should be created
        :return: list of document created or None if unsuccessful or an
        error occurred.
        """
        pass

    @classmethod
    def evaluate_document(cls, document=None, actions=None, parties=None,
                          conditions=None):
        """
        Attempts to evaluate a business document satisfies requirements for a
        business service
        :param document: business document object to evaluate
        :param actions: tuple of bespoke functions used to evaluate document or
        called after successfully evaluating document
        :param parties: various user parties involved with document. If not
        specified, the parties may be retrieved from the business document
        :param conditions: list of boolean conditions or enumeration flags
        under which the document should be evaluated
        :return: True if successful and None otherwise
        """
        pass

    @classmethod
    def prepare_task(cls, documents=None, actions=None, parties=None,
                     conditions=None):
        """
        # @todo: set needed document or business objects for a given task
        :param documents:
        :param actions:
        :param parties:
        :param conditions:
        :return:
        """
        pass

    @classmethod
    def perform_task(cls, task=None, documents=None, actions=None, parties=None,
                     conditions=None):
        """
        Attempt to execute a specific task using the defined functions
        :param task: The named task or service hash to be performed
        :param documents: tuple of documents needed to execute task
        :param actions: tuple of bespoke functions used to execute the task
        or called after executing task. The service can also be executed
        if the actions are not provided by accessing the registered function
        against the given task or hash stored in ServiceRegistry
        :param parties: listed user parties involved with performing task
        :param conditions: list of boolean conditions or enumeration flags
        under which the task should be performed
        :return:
        """
        pass

    @classmethod
    def publish(cls, document=None, actions=None, parties=None,
                conditions=None):
        """
        Broadcast the outcome of a given operation
        :param document: message, text, or document to be published
        :param actions: bespoke function for broadcasting
        :param parties: user parties involved, e.g publisher, recipients, author
        :param conditions: list of boolean conditions or enumeration flags
        under which the document should be published
        :return:
        """
        pass

    @classmethod
    def receive_document(cls, document=None, actions=None, parties=None,
                         conditions=None):
        """
        Attempts to receive or accept a document published or forwarded to
        given user or user group
        :param document: The business document to receive
        :param actions: tuple of bespoke functions to receive a document or
        called after receiving one. The later function should only be called
        if the former was successful
        :param parties: user parties involved in sending and receiving document
        :param conditions: list of boolean conditions or enumeration flags
        under which the document should be received
        :return: True if successful or None otherwise
        """
        pass

    @classmethod
    def request_document(cls, document=None, actions=None, parties=None,
                         conditions=None, flags=None):
        """
        Request a given document be sent to specified user or user parties
        :param document: document being requested for
        :param actions:
        :param parties: the user parties involved in the document request.
        Example, author, editors may be specified for approvals to send
        document to recipients
        :param conditions: list of boolean conditions, access control code, or
        enumeration flags under which the document should be assigned
        :param flags:
        :return: None
        """
        pass

    @classmethod
    def request_action(cls, task=None, documents=None, parties=None,
                       conditions=None, flags=None):
        """
        Request a given business action be performed by specified parties
        :param task: name of business action or service being requested
        :param documents: list of documents that may be needed for performing
        named task, if approved
        :param parties: user parties involved in the request and approval
        :param conditions: list of boolean conditions or enumeration flags
        under which the task should be performed
        :param flags: meta data for describing the task
        :return: None
        """
        pass

    @classmethod
    def terminate_task(cls, documents=None, actions=None, parties=None,
                       conditions=None, flags=None):
        """
        Attempts to terminate a running business service or operation
        :param documents: list of required document for termination of service
        :param actions: tuple of bespoke functions to call to terminate the
        service or called after terminating service
        :param parties: user parties involved in the request-approve-cancel
        cycle
        :param conditions: list of boolean conditions or enumeration flags
        under which the task should be terminated
        :param flags: mete data describing the task
        :return: True if the task was successfully terminated
        """
        pass


class BusinessService(ABC):

    @classmethod
    def initialize(cls, *args, **kwargs):
        # initialize class or instance variables in sub classes
        # initialize the associated _tasks and specify the business _process
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def request_action(cls, action=None, requester=None, performer=None,
                       action_params=None):
        """
        Provide means of running bespoke function related to a business
        activity. The function may generate an action request object which is
        saved to the ServiceRunner internal registry
        :param action: the function to execute which satisfies an activity
        :param requester: the entity requesting the action or source address
        :param performer: the entity performing the action or target address
        :param action_params: the parameters needed to fulfill the action.
        The parameters should be a tuple of two values: a list of positional
        arguments, and a dictionary of keyword arguments
        :return: action request object
        """
        # key responsibility is to create an entry in the ServiceRunner which
        # will be executed based on the implemented decision process.
        # NB: this function call does not run the action (callable) as provided
        #  to this function
        pass

    @classmethod
    @abstractmethod
    def reply_action(cls, action=None, reply=None):
        """
        Execute a bespoke function or a callable when the specified action has
        been performed and needs a response to the requester
        :param action: The action performed
        :param reply: text or bespoke function to call in response to the
        action that has been performed.
        If a callable is used, then it should return a business document or text
        :return: action response object
        """
        # execute the reply function and registering the business state with
        # ServiceRunner
        pass

    @classmethod
    @abstractmethod
    def perform_action(cls, action=None):
        """
        Execute a bespoke function or callable for satisfying the specified
        business action
        :param action: The bespoke function to execute to satisfy a business
        activity
        :return: True if action was executed successfully
        """
        # execute the requested action with provided parameters
        pass

    @classmethod
    @abstractmethod
    def action_outcome(cls, action=None, response=None, outcome=None):
        """
        Operation to perform after an action has been fully executed and its
        outcome received.
        :param action: the bespoke action (function executed by the user
        specified as performer in request_action method) performed
        :param response: the bespoke function to call in response
        to a completed action
        :param outcome: the returned outcome object upon completion of the
        performed action.
        If not specified, the outcome may be retrieved from the ServiceRunner
        registry by looking up the action entries.
        :return: None
        """
        # generate information needed to create business document as response
        # save list of possible outcomes (objects) associated with an action
        pass


class BusinessParty(ABC):
    # may be a buyer or seller and identified by BusinessPartyEnum
    """
    BusinessParty represents the various business system actors
    """
    _actor = None
    _user = None

    @property
    def party(self):
        return NotImplemented

    def cancel(self, *args, **kwargs):
        pass

    def confirm(self, *args, **kwargs):
        pass

    def initiate(self, *args, **kwargs):
        pass

    def enroll(self, *args, **kwargs):
        pass

    def resign(self, *args, **kwargs):
        pass

    def prepare(self, *args, **kwargs):
        pass

    def confirm_contradiction(self, *args, **kwargs):
        pass

    def terminate(self, *args, **kwargs):
        pass

    def interrupt(self, *args, **kwargs):
        pass

    def timeout(self, *args, **kwargs):
        pass


class BusinessAction:
    # record the effect of a given action. Action effect are set by
    # dedicated signal handlers
    action = None
    provisional_effect = None
    final_effect = None
    counter_effect = None

    def __init__(self):
        pass

    @classmethod
    def get(cls, effect=None):
        pass

    @classmethod
    def rollback(cls, action=None, process=None, previous_state=None):
        """
        This reverses the current state of the business service to specified
        previous state or most recent state (if previous_state is not
        provided). The service type is identified by the enum process
        The function executed is identified by the action parameter which is
        a function hash of the bespoke function to execute.
        The previous_state references a state key which can be used to
        retrieve all database records e.g key maps to SQL query or function
        that executes a query.
        """
        pass

    @classmethod
    def push_forward(cls, action=None, process=None, previous_state=None):
        pass


class BusinessTransaction(Payable):
    __slots__ = '_transaction', '_parties', '_documents', '_actions'

    def acknowledge_payment(self, payment, protocol=None):
        super().acknowledge_payment(payment, protocol)

    @property
    def acknowledgement(self):
        return super().acknowledgement

    def receive(self, payment, protocol=None):
        super().receive(payment, protocol)

    def make_payment(self, payment, parties=None, documents=None,
                     protocol=None):
        super().make_payment(payment, parties, documents, protocol)

    def cancel(self, payment, protocol=None):
        super().cancel(payment, protocol)

    class Context:
        # The Context class gives a base and broad definition of a business
        # transaction or a payment record
        __slots__ = 'timestamp', 'description', 'parties', 'uid', 'transaction'

        def __init__(self, timestamp=None, description=None, parties=None,
                     uid=None, transaction=None):
            self.timestamp = timestamp if \
                isinstance(timestamp, datetime.timestamp()) else None
            self.description = description if isinstance(description, str) \
                else None
            self.parties = parties if isinstance(parties, Iterable) else None
            self.uid = uid if isinstance(uid, str) else None
            self.transaction = transaction

        @classmethod
        def get(cls, item=None):
            if item in cls.__slots__:
                return getattr(cls, item)
            elif item in cls.transaction:
                return getattr(cls.transaction, item)


class ServiceRegistry(metaclass=Singleton):
    _history = WeakValueDictionary()
    _registry = WeakValueDictionary()

    class History(list):
        # subclass the list type to enable weakref of histories.
        pass

    @classmethod
    def register(cls, service, func, base=None, force=False):
        # take a given business process function and implement via given user
        #  function
        named_service = None
        if (not isinstance(func, types.MethodType)) and \
                (not isinstance(func, types.FunctionType)):
            raise RuntimeError('Expected a function or method. Got %s' %
                               type(func))
        if isinstance(service, types.MethodType) or \
                isinstance(service, types.FunctionType):
            named_service = service.__name__
        elif isinstance(service, str):
            named_service = service
        elif isinstance(service, Sequence):
            # validate if the service is of type Enum and BusinessProcessEnum
            if len(service) == 3 and all(service):
                named_service = '%s%d%d' % service
        service_hash = sha512(str.encode(named_service)).hexdigest()
        if service_hash in cls._registry and not force:
            return
        if hasattr(base, named_service):
            previous = getattr(base, named_service)
            history = cls._history.get(service_hash, cls.History())
            history.append((copy.copy(previous), datetime.utcnow()))
            cls._history.update({service_hash: history})
            setattr(base, named_service, func)
            cls._registry[service_hash] = (named_service, func)
        elif not (base and isinstance(service, Sequence)):
            # override the function in globals while keeping previous
            # Caution! Avoid using functions only class methods should be
            # used as updating globals may have side effects
            globals().update({named_service: func})
        elif isinstance(service, namedtuple) and not base:
            business_process = [x for x in service._fields if x ==
                                'process'].pop()
            if business_process:
                cls._registry[service_hash] = (named_service, func)

    @classmethod
    def history(cls, service_hash=None, service=None):
        # return a history of a given service hash or named function
        history = None
        if service_hash:
            history = [records for x, records in enumerate(cls._history)
                       if x == service_hash].pop()
        elif service and (isinstance(service, types.MethodType) or isinstance(
                service, types.FunctionType)):
            service_hash = sha512(str.encode(service.__name__)).hexdigest()
            history = [records for x, records in enumerate(cls._history)
                       if x == service_hash].pop()
        return history if history else cls._history

    @property
    def registry(self):
        return self._registry

    @registry.setter
    def registry(self, value):
        raise RuntimeError('Registry cannot be modified')

    @classmethod
    def get(cls, service_hash=None, service=None):
        # return the value of the service_hash or service if registered
        if isinstance(service_hash, str) and not service:
            cls._registry.get(service_hash, None)
        elif isinstance(service, types.MethodType) or \
                isinstance(service, types.FunctionType) and not service_hash:
            service_hash = sha512(str.encode(service.__name__)).hexdigest()
            return cls._registry.get(service_hash, None)
        elif isinstance(service_hash, str) and \
            (isinstance(service, types.MethodType) or
                isinstance(service, types.FunctionType)):
            cal_hash = sha512(service.__name__).hexdigest()
            if not cal_hash == service_hash:
                raise RuntimeError('The hash or checksum provided does not '
                                   'match the specified function')
            return cls._registry.get(service_hash, None)


class ServiceRunner(metaclass=Singleton):
    _action_requests = WeakValueDictionary()

    @classmethod
    def register(cls, action, params, requester, performer, conditions=None,
                 target=None):
        """
        Register a given action that will be executed when specified
        conditions are reached
        :param action: bespoke function to execute
        :param params: tuple of positional and keyword arguments needed by
        the action object
        :param requester: requesting entity or source address
        :param performer: performing entity or target address
        :param conditions: specified boolean conditions or flags for
        deciding if action will be performed or not
        :param target: target outcome if action was specified.
        The target may be provided as a means of asserting the action behaved
        as expected. An equality comparison is carried to assert the target
        :return: None
        """
        action_request = namedtuple('ActionRequest',
                                    (
                                        'action',
                                        'params',
                                        'requester',
                                        'performer',
                                        'conditions',
                                        'target',
                                    ))
        if isinstance(action, types.FunctionType) or isinstance(
                action, types.MethodType):
            action_hash = sha512(str.encode(action.__name__)).hexdigest()
            cls._action_requests[action_hash] = \
                action_request(action, params, requester, performer,
                               conditions, target)

    @classmethod
    def execute(cls, action):
        outcome = None
        execution = None
        target = None
        if isinstance(action, str):
            if action in cls._action_requests.keys():
                execution = cls._action_requests[action]
                if all(execution.conditions):
                    outcome = execution.action(*execution.params)
                    target = execution.target
        elif isinstance(action, types.FunctionType) or \
                isinstance(action, types.MethodType):
            action_hash = sha512(str.encode(action.__name__)).hexdigest()
            execution = cls._action_requests.get(action_hash, None)
            if execution:
                if all(execution.conditions):
                    outcome = execution.action(*execution.params)
                    target = execution.target
        if execution and (outcome == target):
            return outcome
        else:
            raise AssertionError('Target outcome not achieved upon execution '
                                 'of action %s' % action.__name__)
