import clr

clr.AddReference('PyInterface')
clr.AddReference('DatumTron.Datum.AbstractExt')
clr.AddReference('DatumTron.Datum.Abstract')
clr.AddReference('DatumTron.Datum.Atum')

from DatumTron.Datum.AbstractExt import *
from DatumTron.Datum.Abstract import *
from DatumTron.Datum.Atum import *

from PyInterface import Wrapper, ExtensionMethods


import sys

main_module = sys.modules['__main__']

    
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
        

Intersect = Wrapper.Intersect
Union = Wrapper.Union
