class FilippineWoord:
    def __init__( self, woord, index, vraag ):
        self.woord = woord
        self.index = index
        self.vraag = vraag

class Filippine:
    def __init__( self, naam, woorden ):
        self.naam, self.woorden = naam, woorden
    def __len__( self ):
        return len( self.woorden )
    def __getitem__( self, n ):
        return self.woorden[n]
    def __setitem__( self, n, waarde ):
        self.woorden[n] = waarde
    def __delitem__( self, n ):
        del self.woorden[n]
    def toon( self ):
        print( self.naam )
        for i in range( len( self ) ):
            print( "{}. {}".format( i+1, self[i].vraag ), 
                end = "  " )
            for j in range( len( self[i].woord ) ):
                if j == self[i].index:
                    print( "* ", end="" )
                else:
                    print( "_ ", end="" )
            print()
    def oplossing( self ):
        s = ""
        for i in range( len( self ) ):
            s += self[i].woord[self[i].index]
        return s
    
puzzel = Filippine( 
    "De Monty Python en de Heilige Graal Filippine",
    [ FilippineWoord( "ANTHRAX", 5, 
          "Sir Galahad bestormde kasteel" ),
      FilippineWoord( "BORS", 2, "Een konijn doodde Sir" ),
      FilippineWoord( "TIM", 0, "De wijze tovenaar heet" ),
      FilippineWoord( "HERBERT", 0, 
          "De erfgenaam van het Moeras Kasteel is prins" ),
      FilippineWoord( "ZWALUW", 4, 
          "Een kokosnoot is te zwaar voor een Europese" ),
      FilippineWoord( "MINSTREELS", 5, 
          "De ridders aten Robins" ) ] )
          
puzzel.toon()