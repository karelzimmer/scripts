from itertools import permutations

SIZE = 8 # Bord grootte

def toon_bord( kols ):
    for i in kols :
        for j in range( len( kols ) ):
            if i == j:
                print( 'K', end=" " )
            else:
                print( '-', end=" " )
        print()

def is_oplossing( kols ):
    for rij in range( len( kols ) ):
        kol = kols[rij]
        for i in range( rij+1, len( kols ) ):
            if i - rij == abs( kols[i] - kol ):
                return False
    return True
        
kols = list( range( SIZE ) )

for p in permutations( kols ):
    if is_oplossing( p ):
        toon_bord( p )
        break
else:
    print( "Geen oplossing gevonden" ) # Should not happen.