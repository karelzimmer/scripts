KLEUR = ["Harten","Schoppen","Klaveren","Ruiten"]
RANG = ["2","3","4","5","6","7","8","9","10",
    "Boer","Vrouw","Heer","Aas"]

class Kaart:
    def __init__( self, kleur, rang ):
        self.kleur = kleur
        self.rang = rang
    def __str__( self ):
        return "{} {}".format(KLEUR[self.kleur],RANG[self.rang])

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
    
ts1 = Trekstapel( [Kaart(0,1),Kaart(0,5),Kaart(2,4),Kaart(1,12)])
print( ts1 )
print( ts1[1] )
ts1.voegtoe( Kaart(3,12) )
print( ts1 )
print( ts1.trek() )
print( ts1 )