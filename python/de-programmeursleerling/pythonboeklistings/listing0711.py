for i in range( 3 ):
    print( "De buitenste loop begint met i =", i )
    for j in range( 3 ):
        print( "    De binnenste loop begint met j =", j )
        print( "    (i,j) = ({},{})".format( i, j ) )
        print( "    De binnenste loop eindigt met j =", j )
    print( "De buitenste loop eindigt met i =", i )