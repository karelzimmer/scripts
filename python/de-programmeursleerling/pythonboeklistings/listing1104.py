from math import sqrt

# afstand tussen twee punten in N-dimensionale ruimte.
# De punten hebben dezelfde dimensie, ze zijn allebei tuples
# met numerieke waardes, met dezelfde lengte.
def afstand( p1, p2 ):
    totaal = 0
    for i in range( len( p1 ) ):
        totaal += (p1[i] - p2[i])**2
    return sqrt( totaal )

# 1-dimensionale ruimte
punt1 = (1,)
punt2 = (5,)
print( "1D: afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )

# 2-dimensionale ruimte
punt1 = (1,2)
punt2 = (5,5)
print( "2D: afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )

# 3-dimensionale ruimte
punt1 = (1,2,4)
punt2 = (5,5,8)
print( "3D: afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )