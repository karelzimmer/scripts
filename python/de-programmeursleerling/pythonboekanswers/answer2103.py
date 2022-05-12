KLEUR = ["Harten","Schoppen","Klaveren","Ruiten"]
RANG = ["2","3","4","5","6","7","8","9","10",
    "Boer","Vrouw","Heer","Aas"]

class Kaart:
    def __init__( self, kleur, rang ):
        self.kleur = kleur
        self.rang = rang
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

class Trekstapel:
    def __init__( self, stapel=[] ):
        self.stapel = stapel
    def __len__( self ):
        return len( self.stapel )
    def __getitem__( self, n ):
        return self.stapel[n]
    def voegtoe( self, c ):
        self.stapel.append( c )
    def trek( self ):
        if len( self ) <= 0:
            return None
        return self.stapel.pop(0)
    def __repr__( self ):
        sep = ""
        s = ""
        for c in self.stapel:
            s += sep + str( c )
            sep = ", "
        return s
    
ts1 = Trekstapel( [Kaart(3,0), Kaart(0,11), Kaart(2,5)] )
ts2 = Trekstapel( [Kaart(3,2), Kaart(3,1), Kaart(1,6)] )

i = 1
while len( ts1 ) > 0 and len( ts2 ) > 0:
    print( "Ronde", i )
    print( "Stapel1:", ts1 )
    print( "Stapel2:", ts2 )
    c1 = ts1.trek()
    c2 = ts2.trek()
    if c1 > c2:
        ts1.voegtoe( c1 )
        ts1.voegtoe( c2 )
    else:
        ts2.voegtoe( c2 )
        ts2.voegtoe( c1 )
    i += 1
        
print( "Het spel is uit" )
if len( ts1 ) > 0:
    print( "Stapel1:", ts1 )
    print( "De eerste stapel wint!" )
else:
    print( "Stapel2:", ts2 )
    print( "De tweede stapel wint!" )