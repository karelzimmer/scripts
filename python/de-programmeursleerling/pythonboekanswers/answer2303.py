from itertools import permutations

woord = input( "Geef een woord: " )
seq = permutations( woord )
for item in seq:
    print( "".join( item ) )