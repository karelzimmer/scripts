# test met import + gebr v module datumfuncties

"""
import datumfn_jaar as df
import datumfn_jaar2 as df2
#import datumfn_jaar2 as df     #overschrijft vorige import
# -> fn's die niet in datumfuncties2 staan (bv toonVorigJaar()) kent ie niet meer
# hij gooit dus de 1e module datumfuncties uit het geheugen!

huidigJaar = 1993
print(df.__name__)
print('df.huidigJaar =', df.huidigJaar)
print('df._vorigJaar =', df._vorigJaar)    #met std import toont hij wel _namen, met from... niet
print('huidigJaar =', huidigJaar)

df.toonHuidigJaar()         #2016
df.huidigJaar = 2002
df.toonHuidigJaar()         #2002
df.toonVorigJaar()

df2.toonHuidigJaar()         #1961
df2.huidigJaar = 1951
df2.toonHuidigJaar()         #1951
"""

#from datumfn_jaar import huidigJaar, _vorigJaar        #werkt goed
from datumfn_jaar import *        #importeert niet _vorigJaar, vanwege de _ vooraan
from datumfn_jaar2 import *        #overschrijft de var's/fn's uit vorige import
print('huidigJaar =', huidigJaar)
#print('_vorigJaar =', _vorigJaar)           #werkt goed
toonHuidigJaar()            #NameError: name 'toonHuidigJaar' is not defined"""
toonHuidigJaar2()

toonVorigJaar()
tralala()
