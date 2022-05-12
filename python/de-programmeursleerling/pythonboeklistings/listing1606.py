fp = open( "pc_writetest.tmp", "w" )
while True:
    tekst = input( "Geef een regel tekst: " )
    if tekst == "":
        break
    fp.write( tekst )
fp.close()

fp = open( "pc_writetest.tmp" )
buffer = fp.read()
fp.close()

print( buffer )