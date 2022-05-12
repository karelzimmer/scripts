from math import sqrt

class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def afstand_tot_oorsprong( self ):
        return sqrt( self.x*self.x + self.y*self.y )

p = Punt( 3.5, 5.0 )
print( p.afstand_tot_oorsprong() )