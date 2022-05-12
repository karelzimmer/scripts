def toon_bord( b ):
    print( "  1 2 3" )
    for rij in range( 3 ):
        print( rij+1, end=" ")
        for kol in range( 3 ):
            print( b[rij][kol], end=" " )
        print()

bord = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
bord[1][1] = "X"
bord[0][2] = "O"
toon_bord( bord )