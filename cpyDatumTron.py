import clr
clr.AddReference('PyInterface')
clr.AddReference('DatumTron.Datum.AbstractExt')
clr.AddReference('DatumTron.Datum.Abstract')
clr.AddReference('DatumTron.Datum.Atum')

from DatumTron.Datum.AbstractExt import *
from DatumTron.Datum.Abstract import *
from DatumTron.Datum.Atum import *

from PyInterface import Wrapper

import sys

main_module = sys.modules['__main__']


def Get(self, s):
    if s.__class__ == self.__class__:
        return Wrapper.get(self, s)
    if type(s) == type(lambda x:x):
        setattr(main_module, s.__name__, s)
        return Wrapper.get(self, s.__name__)
    return Wrapper.get(self, s)
    
def And(self, s):
    return Wrapper.andI(self, s)
    
def Of(k, *s):
    if len(s) > 1:
        t = k.of(s[0], None, s[1])
        if t is not None:
            return t
        return None
    elif 'tokatum' in dir(s[0]):
        t = k.of(s[0])
        if t is None:
            return None
        if t.asString in dir(main_module) and type(getattr(main_module, t.asString)) == type(lambda x:x):
            return getattr(main_module, t.asString)(s[0], k)
        return k.of(s[0])
    
    
def _is(self, s,check=True):
    return self.__getattribute__('is')(s,check=check)
    
katum.Get = Get
katum.And = And
katum._is = _is

Intersect = Wrapper.Intersect
Union = Wrapper.Union