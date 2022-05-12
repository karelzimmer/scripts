import errno

try:
    fp = open( "GeenBestand" )
    fp.close()
except IOError as ex:
    if ex.args[0] == errno.ENOENT:
        print( "Bestand niet gevonden!" )
    else:
        print( ex.args[0], ex.args[1] )