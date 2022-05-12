from random import random

COOPERATIE = 'C'
DEFECTIE = 'D'
RONDES = 100

class Strategie:
    def __init__( self, naam="" ):
        self.naam = naam
        self.score = 0
    def keuze( self ):
        # Moet COOPERATIE of DEFECTIE retourneren
        return NotImplemented
    def laatstezet( self, mijnzet, tegenstanderzet ):
        # Krijgt de laatste zet die gedaan is, na keuze()
        pass
    def plusscore( self, n ):
        self.score += n
        
class AltijdD( Strategie ):
    def keuze( self ):
        return DEFECTIE
        
class Random( Strategie ):
    def keuze( self ):
        if random() >= 0.5:
            return COOPERATIE
        return DEFECTIE

class GeheugenStrategie( Strategie ):
    def __init__( self, naam="" ):
        super().__init__( naam )
        self.historie = []
    def laatstezet( self, mijnzet, tegenstanderzet ):
        self.historie.append( (mijnzet, tegenstanderzet) )
        
class OogOmOog( GeheugenStrategie ):
    def keuze( self ):
        if len( self.historie ) < 1:
            return COOPERATIE
        return self.historie[-1][1]

class OogOmTweeOgen( GeheugenStrategie ):
    def keuze( self ):
        if len( self.historie ) < 2:
            return COOPERATIE
        if self.historie[-1][1] == DEFECTIE and \
            self.historie[-2][1] == DEFECTIE:
            return DEFECTIE
        return COOPERATIE

class Meerderheid( GeheugenStrategie ):
    def keuze( self ):
        telD = 0
        for i in range( len( self.historie ) ):
            if self.historie[i][1] == DEFECTIE:
                telD += 1
        if telD > len( self.historie ) / 2:
            return DEFECTIE
        return COOPERATIE
            
strategie1 = AltijdD( "Altijd Defectie" )
strategie2 = Meerderheid( "Meerderheid" )

for i in range( RONDES ):
    c1 = strategie1.keuze()
    c2 = strategie2.keuze()
    if c1 == c2:
        strategie1.plusscore( 3 if c1 == COOPERATIE else 1 )
        strategie2.plusscore( 3 if c2 == COOPERATIE else 1 )
    else:
        strategie1.plusscore( 0 if c1 == COOPERATIE else 6 )
        strategie2.plusscore( 0 if c2 == COOPERATIE else 6 )
    strategie1.laatstezet( c1, c2 )
    strategie2.laatstezet( c2, c1 )
        
print( "Score van", strategie1.naam, "is", strategie1.score )
print( "Score van", strategie2.naam, "is", strategie2.score )