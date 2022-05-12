class Zin:
    def __init__( self, words ):
        self.words = words
    def __repr__( self ):
        return " ".join( self.words )

s = Zin( [ "Er", "is", "slechts", "een", "ding", "ter", 
"wereld", "erger" "dan", "beroddeld", "worden", "en", 
"dat", "is", "niet", "beroddeld", "worden" ] )
print( s )
print( len( s ) )
print( s[7] )
s[7] = "prettiger"
print( "beroddeld" in s )