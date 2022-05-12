from pcinput import getString
from random import randint

LEEG = "."
SCHIP = "X"
SCHEPEN = 3
BREEDTE = 4
HOOGTE = 3

def toonBord( b ):
    print( "  ", end="" )
    for kol in range( BREEDTE ):
        print( chr( ord("A")+kol ), end=" " )
    print()
    for rij in range( HOOGTE ):
        print( rij+1, end=" ")
        for kol in range( BREEDTE ):
            print( b[rij][kol], end=" " )
        print()

def plaatsSchepen( b ):
    for i in range( SCHEPEN ):
        while True:
            x = randint( 0, BREEDTE-1 )
            y = randint( 0, HOOGTE-1 )
            if b[y][x] == SCHIP:
                continue
            if x > 0 and b[y][x-1] == SCHIP:
                continue
            if x < BREEDTE-1 and b[y][x+1] == SCHIP:
                continue
            if y > 0 and b[y-1][x] == SCHIP:
                continue
            if y < HOOGTE-1 and b[y+1][x] == SCHIP:
                continue
            break
        b[y][x] = SCHIP
    
def neemDoel():
    while True:
        cel = getString( "Welke cel kies je? " ).upper()
        if len( cel ) != 2:
            print( "Geef een cel in als XY,",
                "met X een letter en Y een cijfer" )
            continue
        if cel[0] not in "ABCD":
            print( "De letter moet tussen A en",
                chr( ord("A")+BREEDTE-1 ), "liggen" )
            continue
        if cel[1] not in "123":
            print( "Cijfer moet tussen 1 en", HOOGTE, "liggen" )
            continue
        return ord(cel[0])-ord("A"), ord(cel[1])-ord("1")      
    
bord = []
for i in range( HOOGTE ):
    rij = BREEDTE * [LEEG]
    bord.append( rij )
plaatsSchepen( bord )
toonBord( bord )

raak = 0
zetten = 0
while raak < SCHEPEN:
    x, y = neemDoel()
    if bord[y][x] == SCHIP:
        print( "Raak!" )
        bord[y][x] = LEEG
        raak += 1
    else:
        print( "Mis!" )
    zetten += 1

print( "Je had", zetten, "zetten nodig om mij te verslaan." )