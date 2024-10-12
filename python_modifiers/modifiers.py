import inspect
from functools import wraps
from .exceptions.exceptions import PrivateFunctionException, ProtectedFunctionException
from ._messages import LEVEL_EXCEPTION

def public(func):
    """ Decorator for public function """
    return func

def private(func):
    """ Decorator for private function """
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
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        caller_frame = inspect.stack()[1]
        caller_self = caller_frame.frame.f_locals.get('self', None)

        if caller_self is None or not isinstance(caller_self, (self.__class__, *self.__class__.__subclasses__)):
            raise ProtectedFunctionException(LEVEL_EXCEPTION)

        return func(self, *args, **kwargs)

    return wrapper

