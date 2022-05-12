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
        self.breedte = abs( breedte )
        self.hoogte = abs( hoogte )
        if self.breedte == 0:
            self.breedte = 1
        if self.hoogte == 0:
            self.hoogte = 1
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.punt, 
            self.breedte, self.hoogte )
    def oppervlakte( self ):
        return self.breedte * self.hoogte
    def omtrek( self ):
        return 2*(self.breedte + self.hoogte)
    def rechtsonder( self ):
        return Punt( self.punt.x + self.breedte, 
            self.punt.y + self.hoogte )
    def overlap( self, r ):
        r1, r2 = self, r
        if self.punt.x > r.punt.x or \
            (self.punt.x == r.punt.x and \
            self.punt.y > r.punt.y):
            r1, r2 = r, self
        if r1.rechtsonder().x <= r2.punt.x or \
            r1.rechtsonder().y <= r2.punt.y:
            return None
        return Rechthoek( r2.punt, 
            min( r1.rechtsonder().x - r2.punt.x, r2.breedte ), 
            min( r1.rechtsonder().y - r2.punt.y, r2.hoogte ) )
    
r1 = Rechthoek( Punt( 1, 1 ), 8, 5 )
r2 = Rechthoek( Punt( 2, 3 ), 9, 2 )

print( r1.oppervlakte() )
print( r1.omtrek() )
print( r1.rechtsonder() )
r = r1.overlap( r2 )
if r:
    print( r )
else:
    print( "De rechthoeken overlappen niet" )