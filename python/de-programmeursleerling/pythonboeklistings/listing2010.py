from copy import copy

class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rechthoek:
    def __init__( self, punt, breedte, hoogte ):
        self.punt = copy( punt )
        self.breedte = breedte
        self.hoogte = hoogte
    def __repr__( self ):
        return "[{},b={},h={}]".format( self.punt, self.breedte, 
            self.hoogte )

p = Punt( 3.5, 5.0 )
r = Rechthoek( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )