from os.path import join
from os import getcwd

lijst = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
letterlist = [ len( lijst )*[0] for i in range( 26 ) ]
totaallist = len( lijst ) * [0]

# Verwerk de invoerlijst regel voor regel, maak kleine letters 
# en tel de letters in letterlist, en houd totaaltellingen 
# bij in totaallist.
aantal = 0
for naam in lijst:
    bestandnaam = join( getcwd(), naam )
    fp = open( bestandnaam )
    while True:
        regel = fp.readline()
        if regel == "":
            break
        regel = regel.lower()
        for c in regel:
            if c >= 'a' and c <= 'z':
                totaallist[aantal] += 1
                letterlist[ord(c)-ord("a")][aantal] += 1
    fp.close()
    aantal += 1

# Schrijf tellingen in CSV formaat.
uitvoerbestand = join( getcwd(), "pc_writetest.csv" )
fp = open( uitvoerbestand, "w" )
for i in range( len( letterlist ) ):
    s = "\"{}\"".format( chr( ord("a")+i ) )
    for j in range( len( lijst ) ):
        s += ",{:.5f}".format( letterlist[i][j]/totaallist[j] )
    fp.write( s+"\n" )
fp.close()

# Laat de inhoud van de CSV zien ter controle.
fp = open( uitvoerbestand )
print( fp.read() )
fp.close()