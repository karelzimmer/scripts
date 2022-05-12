class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

puntlist = []

for i in range( 100 ):
    for j in range( 100 ):
        p = Punt( i, j )
        puntlist.append( p )
        
print( "Er zijn", len( puntlist ), "punten in de list" )