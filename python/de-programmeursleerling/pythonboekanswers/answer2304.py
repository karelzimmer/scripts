from itertools import permutations

woord = input( "Geef een woord: " )
seq = permutations( woord )
for item in set( seq ):
    print( "".join( item ) )