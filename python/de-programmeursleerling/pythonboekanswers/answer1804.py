from pcinput import getString, getLetter
from os.path import exists, getsize

LETTERS = b"etaoinshrdlcum "

# Comprimeer byte string ongecodeerd, retourneer gecomprimeerd
def comprimeer( ongecodeerd ):
    halfbytelist = []
    for c in ongecodeerd:
        if c in LETTERS:
            halfbytelist.append( LETTERS.index( c )+1 )
        else:
            halfbytelist.extend( [0, int( c/16 ), c%16 ] )
    if len( halfbytelist )%2 != 0:
        halfbytelist.append( 0 )
    bytelist = []
    for i in range( 0, len( halfbytelist ), 2 ):
        bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )
    return bytes( bytelist )

# Decomprimeer byte string gecodeerd, retourneer gedecomprimeerd
def decomprimeer( gecodeerd ):
    halfbytelist = []
    for c in gecodeerd:
        halfbytelist.extend( [ int( c/16 ), c%16 ] )
    if halfbytelist[-1] == 0:
        del halfbytelist[-1]
    bytelist = []
    while len( halfbytelist ) > 0:
        num = halfbytelist.pop(0)
        if num > 0:
            bytelist.append( LETTERS[num-1] )
            continue
        num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
        bytelist.append( num )
    return bytes( bytelist )

# Vraag om input bestand en lees de inhoud
while True:
    filein = getString( "Geef input bestand: " )
    if not exists( filein ):
        print( filein, "bestaat niet" )
        continue
    try:
        fp = open( filein, "rb" )
        buffer = fp.read()
        fp.close()
    except IOError as ex:
        print( filein, "kan niet verwerkt worden, kies andere" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break
    
# Vraag om output bestand en creeer het
while True:
    fileout = getString( "Geef output bestand: " )
    if exists( fileout ):
        print( fileout, "bestaat al" )
        continue
    try:
        fp = open( fileout, "wb" )
    except IOError as ex:
        print( fileout, "kan niet aangemaakt worden,",
            "kies een andere naam" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break

# Vraag of de gebruiker wil comprimeren of decomprimeren.
while True:
    dc = getLetter( "Wil je (C)omprimeren of (D)ecomprimeren? " )
    if dc != 'C' and dc != 'D':
        print( "Kies C of D" )
        continue
    break
    
# Comprimeer of decomprimeer de buffer.
if dc == 'C':
    buffer = comprimeer( buffer )
else:
    buffer = decomprimeer( buffer )
    
# Sla de verwerkte buffer op in het output bestand.
try:
    fp.write( buffer )
    fp.close()
except IOError as ex:
    print( "Het schrijven lukte niet" )
    print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))

# Rapporteer de groottes van input en output.
print( getsize( filein ), "bytes gelezen" )
print( getsize( fileout ), "bytes geschreven" )