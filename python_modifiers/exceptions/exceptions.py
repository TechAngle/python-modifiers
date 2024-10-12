class PrivateFunctionException(BaseException):
    """ Private function exception """
    pass
        
class ProtectedFunctionException(Exception):
    """ Protected function exception """
    pass

class ModifierOutsideOfClassException(Exception):
    """ If modifier was used outside class """
    pass