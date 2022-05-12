from math import sqrt

def afstand( x1, y1, x2, y2 ):

    def pythagoras_binnen( a, b ):
        if a <= 0 or b <= 0:
            return -1
        return sqrt( a*a + b*b )

    return pythagoras_binnen( abs( x1 - x2 ), abs( y1 - y2 ) )

print( afstand( 1, 1, 4, 5 ) )
# print( pythagoras_binnen( 3, 4 ) )