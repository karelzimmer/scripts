from pcinput import getInteger

LEEG = "-"
SPELERX = "X"
SPELERO = "O"
MAXZET = 9

def toon_bord( b ):
    print( "  1 2 3" )
    for rij in range( 3 ):
        print( rij+1, end=" ")
        for kol in range( 3 ):
            print( b[rij][kol], end=" " )
        print()

def opponent( p ):
    if p == SPELERX:
        return SPELERO
    return SPELERX
        
def neemRowKolom( speler, wat ):
    while True:
        num = getInteger( "Speler "+speler+", welke "+wat+
            " kies je? " )
        if num < 1 or num > 3:
            print( "Geef 1, 2, of 3" )
            continue
        return num
    
def winnaar( b ):
    for rij in range( 3 ):
        if b[rij][0] != LEEG and b[rij][0] == b[rij][1] \
            and b[rij][0] == b[rij][2]:
            return True
    for kol in range( 3 ):
        if b[0][kol] != LEEG and b[0][kol] == b[1][kol] \
            and b[0][kol] == b[2][kol]:
            return True
    if b[1][1] != LEEG:
        if b[1][1] == b[0][0] and b[1][1] == b[2][2]:
            return True
        if b[1][1] == b[0][2] and b[1][1] == b[2][0]:
            return True
    return False

bord = [[LEEG,LEEG,LEEG],[LEEG,LEEG,LEEG],[LEEG,LEEG,LEEG]]
speler = SPELERX

toon_bord( bord )
zet = 0
while True:
    rij = neemRowKolom( speler, "rij" )
    kol = neemRowKolom( speler, "kolom" )
    if bord[rij-1][kol-1] != LEEG:
        print( "Rij", rij, "en kolom", kol, "is niet leeg" )
        continue
    bord[rij-1][kol-1] = speler
    toon_bord( bord )
    if winnaar( bord ):
        print( "Speler", speler, "wint!" )
        break
    zet += 1
    if zet == MAXZET:
        print( "Het is gelijkspel." )
        break
    speler = opponent( speler )