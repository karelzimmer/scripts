try:
    fp = open( "GeenBestand" )
    fp.close()
except IOError as ex:
    print( ex.args )