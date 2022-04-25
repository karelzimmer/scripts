# test met import + gebr v module datumfuncties

"""

import datumfuncties as df        #mag zonder alias
import datumfuncties2 as df2

#import datumfuncties2 as df     #overschrijft vorige import
# -> fn's die niet in datumfuncties2 staan (bv isLeapYear()) kent ie niet meer
# hij gooit dus de 1e module datumfuncties uit het geheugen!

#print(__name__)
#print(df.__name__)
print(df.monthName(4))
#print(datumfuncties.monthName(4))
#print(df2.__name__)
print(df2.monthName(4))

dag = 29
mnd = 2
jr = 2000
print(df.isValidDate(dag, mnd, jr))
#print(df2.isValidDate(dag, mnd, jr))        #error, zit niet in df2

"""

from datumfuncties import monthName, isValidDate
#from datumfuncties import *
#from datumfuncties2 import *        #overschrijft de overeenkomstige fn's uit vorige import
#from datumfuncties2 import monthName

dag = 29
mnd = 2
jr = 2000

print(isValidDate(dag, mnd, jr))
print(monthName(mnd))           #Feb; kiest monthName() uit 2e import
#printMonthName(mnd)             #feb; kiest altijd monthName() uit eigen module



