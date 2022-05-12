letters = "etaoinshrdlcum "
gecodeerd = b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'

# Toon de gecodeerde byte string ter controle.
print( gecodeerd, len( gecodeerd ) )

# Creeer een half-byte-list op basis van de byte string.
halfbytelist = []
for c in gecodeerd:
    halfbytelist.extend( [ int( c/16 ), c%16 ] )
if halfbytelist[-1] == 0:
    del halfbytelist[-1]
    
# Maak van de half-byte-string een string.
gedecodeerd = ""
while len( halfbytelist ) > 0:
    num = halfbytelist.pop(0)
    if num > 0:
        gedecodeerd += letters[num-1]
        continue
    num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
    gedecodeerd += chr( num )

# Toon de string, ter controle.
print( gedecodeerd, len( gedecodeerd ) )