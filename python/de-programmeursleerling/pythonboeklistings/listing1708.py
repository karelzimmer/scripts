try:
    print( int( "GeenInteger" ) )
except ValueError as ex:
    print( ex.args )