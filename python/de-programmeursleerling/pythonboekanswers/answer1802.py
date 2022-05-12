letters = "etaoinshrdlcum "
ongecodeerd = "Hello, world!"

# Toon de string zonder codering, ter controle
print( ongecodeerd, len( ongecodeerd ) )

# Creeer een half-byte-list als basis voor codering
halfbytelist = []
for c in ongecodeerd:
    if c in letters:
        halfbytelist.append( letters.index( c )+1 )
    else:
        byte = ord( c )
        halfbytelist.extend( [0, int( byte/16 ), byte%16 ] )
if len( halfbytelist )%2 != 0:
    halfbytelist.append( 0 )

# Maak van de half-byte-list een bytelist.
bytelist = []
for i in range( 0, len( halfbytelist ), 2 ):
    bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )

# Maak van de bytelist een bytestring en toon die ter controle. 
gecodeerd = bytes( bytelist )
print( gecodeerd, len( gecodeerd ) )