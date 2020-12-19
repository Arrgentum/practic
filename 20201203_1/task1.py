import sys
from types import FunctionType


def decorator(function):
    def newfunction(self, *args, **kwargs):
        print(function.__name__ + ":", "(", args,")" ,"(", kwargs, ")")
        return function(self, *args, **kwargs)
    return newfunction

class dump(type):
    def __init__(self, *ap, **an):
        for attr, obj in vars(self).items():
            if isinstance(obj, FunctionType):
            	setattr(self, attr, decorator(obj))
        super().__init__(*ap, **an)

exec(sys.stdin.read())
