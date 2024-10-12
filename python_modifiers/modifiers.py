import inspect
from functools import wraps
from .exceptions.exceptions import ModifierOutsideOfClassException, PrivateFunctionException, ProtectedFunctionException
from ._messages import LEVEL_EXCEPTION

def public(func):
    """ Decorator for public function """
    return func

def __has_self_param(func):
    """
    Checks for 'self' param in function

    Args:
        func (function): function

    Raises:
        ModifierOutsideOfClassException: if `self` not found
    """
    # Checking for self param
    sigs = inspect.signature(func)
    isClassFunc = 'self' in sigs.parameters  # Update this line
    
    if not isClassFunc:
        raise ModifierOutsideOfClassException("Modifiers can only be used inside a class!")

def private(func):
    """ Decorator for private function """
    __has_self_param(func)
    
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        caller_frame = inspect.stack()[1]
        caller_self = caller_frame.frame.f_locals.get('self', None)

        if caller_self is None or not isinstance(caller_self, self.__class__):
            raise PrivateFunctionException(LEVEL_EXCEPTION)
        
        return func(self, *args, **kwargs)

    return wrapper

def protected(func):
    """ Decorator for protected function """
    __has_self_param()
    
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        caller_frame = inspect.stack()[1]
        caller_self = caller_frame.frame.f_locals.get('self', None)

        if caller_self is None or not isinstance(caller_self, (self.__class__, *self.__class__.__subclasses__)):
            raise ProtectedFunctionException(LEVEL_EXCEPTION)

        return func(self, *args, **kwargs)

    return wrapper

