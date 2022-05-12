from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
for i in range( 1, 11 ):
    print( i, "*", num, "=", i*num )