try:
    fp = open( "pc_rose.txt" )
    print( "Bestand geopend" )
    print( fp.read() )
finally:
    fp.close()
    print( "Bestand gesloten" )