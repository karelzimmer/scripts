from math import sqrt

# Retourneert de afstand tussen twee punten in 2-dimensionale
# ruimte. The punten zijn de parameters van de functie.
# Ieder punt is een tuple met twee numerieke waardes.
def afstand( p1, p2 ):
    return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

punt1 = (1,2)
punt2 = (5,5)
print( "Afstand tussen", punt1, "en", punt2, "is", 
    afstand( punt1, punt2 ) )