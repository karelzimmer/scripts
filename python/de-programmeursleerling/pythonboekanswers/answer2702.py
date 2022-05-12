from collections import Counter
from pcinput import getInteger
from statistics import mean, median
from sys import exit

numlist = []
while True:
    num = getInteger( "Geef een getal: " )
    if num == 0:
        break
    numlist.append( num )

if len( numlist ) <= 0:
    print( "Geen getallen ingegeven" )
    exit()
    
print( "Gemiddelde:", mean( numlist ) )
print( "Mediaan:", median( numlist ) )

clist = Counter( numlist ).most_common()
if clist[0][1] <= 1:
    print( "Er is geen modus" )
else:
    mlist = [str( x[0] ) for x in clist if x[1] == clist[0][1] ]
    s = ", ".join( mlist )
    print( "Modus:", s )