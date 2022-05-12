COOPERATIE = 'C'
DEFECTIE = 'D'
RONDES = 100

class Strategie:
    def __init__( self, name="" ):
        self.name = name
        self.score = 0
    def keuze( self ):
        # Moet COOPERATIE of DEFECTIE retourneren
        return NotImplemented
    def laatstezet( self, mijnzet, opponentzet ):
        # Krijgt de laatste zet die gemaakt is, na keuze()
        pass
    def plusscore( self, n ):
        self.score += n

strategie1 = Strategie()
strategie2 = Strategie()

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

print( "Eind score", strategie1.name, "is", strategie1.score )
print( "Eind score", strategie2.name, "is", strategie2.score )