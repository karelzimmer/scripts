NAAM = "pc_binarytest.tmp"

fp = open( NAAM, encoding="latin-1" )
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer )
fp.close()