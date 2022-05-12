class Rechthoek:
    def __init__( self, x, y, b, h ):
        self.x, self.y, self.b, self.h = x, y, b, h
    def __repr__( self ):
        return "[({},{}),b={},h={}]".format( self.x, self.y, 
          self.b, self.h )
    def oppervlakte( self ):
        return self.b * self.h
    def omtrek( self ):
        return 2*(self.b + self.h)

class Vierkant( Rechthoek ):
    def __init__( self, x, y, b ):
        super().__init__( x, y, b, b )
        
s = Vierkant( 1, 1, 4 )
print( s, s.oppervlakte(), s.omtrek() )