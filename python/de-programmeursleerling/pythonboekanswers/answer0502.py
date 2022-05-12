from pcinput import getFloat
from math import sqrt

zijde1 = getFloat( "Geef de lengte van de eerste zijde: " )
zijde2 = getFloat( "Geef de lengte van de tweede zijde: " )
zijde3 = sqrt( zijde1 * zijde1 + zijde2 * zijde2 )
print( "De lengte van de diagonaal is {:.3f}.".format( zijde3 ) )
