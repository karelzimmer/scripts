from pcinput import getFloat
from math import sqrt

# Deze functie lost een kwadratische vergelijking op.
# De parameters zijn numerieke waardes voor A, B, and C in de 
# vergelijking Ax**2 + Bx + C = 0. Het retourneert drie waardes.
# De eerste is een integer 0, 1, of 2, die aangeeft hoeveel 
# oplossingen er zijn. Daarna volgen de oplossingen.
# Zonder oplossingen zijn beide 0. 1 oplossing wordt geretourneerd
# als de eerste van de twee, en de tweede is 0.
def wortelformule( a, b, c ):
    if a == 0:
        if b == 0:
            return 0, 0, 0
        return 1, -c/b, 0
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0, 0, 0
    elif discriminant == 0:
        return 1, -b/(2*a), 0
    else:
        return 2, (-b+sqrt(discriminant))/(2*a), \
            (-b-sqrt(discriminant))/(2*a)
    
num, opl1, opl2 = wortelformule( getFloat( "A: " ), 
    getFloat( "B: " ), getFloat( "C: " ) )
if num == 0:
    print( "Er zijn geen oplossingen" )
elif num == 1:
    print( "Er is 1 oplossing, namelijk", opl1 )
else:
    print( "Er zijn 2 oplossingen, namelijk:", opl1, "en", opl2 )