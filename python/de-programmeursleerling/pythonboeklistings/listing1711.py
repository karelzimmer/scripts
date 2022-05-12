def getStringLenMax10( prompt ):
    s = input( prompt )
    if len( s ) > 10:
        raise ValueError( "Lengte groter dan 10", len( s ) )
    return s

print( getStringLenMax10( "Gebruik 10 tekens of minder: " ) )