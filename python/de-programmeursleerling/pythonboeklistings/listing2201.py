class Persoon:
    def __init__( self, voornaam, achternaam, leeftijd ):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.leeftijd = leeftijd
    def __repr__( self ):
        return "{} {}".format( self.voornaam, self.achternaam )
    def minderjarig( self ):
        return self.leeftijd < 18

class Student( Persoon ):
    pass

albert = Student( "Albert", "Applebaum", 19 )
print( albert )
print( albert.minderjarig() )