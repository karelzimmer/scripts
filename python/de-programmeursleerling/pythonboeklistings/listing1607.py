NAAM = "pc_writetest.tmp"

def tooninhoud( bestandsnaam ):
    fp = open( bestandsnaam )
    print( fp.read() )
    fp.close()

tooninhoud( NAAM )

fp = open( NAAM, "a" )
while True:
    tekst = input( "Geef een regel tekst: " )
    if tekst == "":
        break
    fp.write( tekst+"\n" )
fp.close()

tooninhoud( NAAM )