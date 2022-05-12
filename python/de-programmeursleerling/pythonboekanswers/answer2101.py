KLEUR = ["Harten","Schoppen","Klaveren","Ruiten"]
RANG = ["2","3","4","5","6","7","8","9","10",
    "Boer","Vrouw","Heer","Aas"]

class Kaart:
    def __init__( self, kleur, rang ):
        self.kleur = kleur # index in KLEUR list
        self.rang = rang # index in RANG list
    def __repr__( self ):
        return "({},{})".format( self.kleur, self.rang )
    def __str__( self ):
        return "{} {}".format(KLEUR[self.kleur],RANG[self.rang])
    def __eq__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang == c.rang
        return NotImplemented
    def __gt__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang > c.rang
        return NotImplemented
    def __ge__( self, c ):
        if isinstance( c, Kaart ):
            return self.rang >= c.rang
        return NotImplemented
    
k5 = Kaart( 2, 3 )
r5 = Kaart( 3, 3 )
sh = Kaart( 1, 11 )
print( "{}, {}, {}".format( k5, r5, sh ) )
print( k5 == r5 )
print( k5 == sh )
print( k5 > sh )
print( k5 >= sh )
print( k5 < sh )
print( k5 <= sh )