from math import pi

class Vorm:
    def oppervlakte( self ):
        return NotImplemented
    def omtrek( self ):
        return NotImplemented

class Cirkel( Vorm ):
    def __init__( self, x, y, s ):
        self.x, self.y, self.s = x, y, s
    def __repr__( self ):
        return "[({},{}),r={}]".format( self.x, self.y, self.s )
    def oppervlakte( self ):
        return pi * self.s * self.s
    def omtrek( self ):
        return 2 * pi * self.s
    
class Rechthoek( Vorm ):
    def __init__( self, x, y, b, h ):
        self.x, self.y, self.b, self.h = x, y, b, h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y, 
            self.b, self.h )
    def oppervlakte( self ):
        return self.b * self.h
    def omtrek( self ):
        return 2*(self.b + self.h)

class Vierkant( Rechthoek ):
    def __init__( self, x, y, b ):
        super().__init__( x, y, b, b )
        
v = Vierkant( 1, 1, 4 )
print( v, v.oppervlakte(), v.omtrek() )
c = Cirkel( 1, 1, 4 )
print( c, c.oppervlakte(), c.omtrek() )