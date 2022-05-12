from pcinput import getFloat
from math import sqrt

a = getFloat( "A: " )
b = getFloat( "B: " )
c = getFloat( "C: " )

if a == 0:
    if b == 0:
        print( "Deze vergelijking heeft geen onbekende!" )
    else:
        print( "Er is 1 oplossing, namelijk", -c/b )
else:
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print( "Er zijn geen oplossingen" )
    elif discriminant == 0:
        print( "Er is 1 oplossing, namelijk", -b/(2*a) )
    else:
        print( "Er zijn 2 oplossingen, namelijk",  
                (-b+sqrt(discriminant))/(2*a), "en", 
                (-b-sqrt(discriminant))/(2*a) )