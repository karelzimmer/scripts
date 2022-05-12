fp = open( "pc_binarytest.tmp", "rb" )
print( "1. Huidige positie van de pointer is", fp.tell() )
fp.seek( 50 )
print( "2. Huidige positie van de pointer is", fp.tell() )
buffer = fp.read( 23 )
print( "3. Huidige positie van de pointer is", fp.tell() )
fp.close()

print( buffer )
s = ""
for c in buffer:
    s += chr( c-128 )
print( "De geheime boodschap is:", s )