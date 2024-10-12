""" This is the main project file which contains private, protected, and public modifiers """
import inspect
from functools import wraps
from .exceptions.exceptions import PrivateFunctionException, ProtectedFunctionException
from ._messages import LEVEL_EXCEPTION

def public(func):
    """ This modifier makes function available for everyone """
    return func

def private(func):
    """ Makes function private, callable only within the class """
    @wraps(func)
    def private_function_wrapper(self, *args, **kwargs):
        current_file = inspect.getfile(func)
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        caller_self = caller_frame.frame.f_locals.get('self', None)

        # Check if the caller is from the same class
        if current_file != caller_file or (caller_self and not isinstance(caller_self, self.__class__)):
            raise PrivateFunctionException(LEVEL_EXCEPTION)
        
        return func(self, *args, **kwargs)
    return private_function_wrapper

def protected(func):
    """ Makes function protected, callable within the class or subclasses """
    @wraps(func)
    def protected_function_wrapper(self, *args, **kwargs):
        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame, 2)[1].frame
        caller_self = caller_frame.f_locals.get('self', None)

        # Check if the caller is from the same class or a subclass
        if caller_self is None or (caller_self.__class__ != self.__class__ and not isinstance(caller_self, type(self))):
            raise ProtectedFunctionException(LEVEL_EXCEPTION)

        return func(self, *args, **kwargs)
    return protected_function_wrapper
