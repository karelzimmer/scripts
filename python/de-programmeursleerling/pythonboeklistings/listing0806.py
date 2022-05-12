from math import sqrt
from pcinput import getInteger

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
    return sqrt( a*a + b*b )

num1 = getInteger( "Geef zijde 1: " )
num2 = getInteger( "Geef zijde 2: " )
num3 = pythagoras( num1, num2 )
if num3 < 0:
    print( "De getallen kunnen niet worden gebruikt." )
else:
    print( "De lengte van de diagonaal is", num3 )