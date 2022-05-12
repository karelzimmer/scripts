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
    def __init__( self, voornaam, achternaam, 
        leeftijd, programma ):
        super().__init__( voornaam, achternaam, leeftijd )
        self.cursussen = []
        self.programma = programma
    def minderjarig( self ):
        return self.leeftijd < 21
    def inschrijven( self, cursus ):
        self.cursussen.append( cursus )

albert = Student( "Albert", "Applebaum", 19, "CSAI" )
print( albert )
print( albert.minderjarig() )
print( albert.programma )
albert.inschrijven( "Toepassingen van rationaliteit" )
albert.inschrijven( "Verweer tegen de zwarte kunsten" )
print( albert.cursussen )