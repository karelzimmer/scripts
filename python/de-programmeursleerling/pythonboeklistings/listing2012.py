class Punt:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

totaalx = 0
totaaly = 0 

for i in range( 1000 ):
    for j in range( 1000 ):
        p = Punt( i, j )
        totaalx += p.x
        totaaly += p.y
        
print( "De totalen van x en y zijn", totaalx, "en", totaaly )