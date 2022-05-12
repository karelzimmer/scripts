from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
i = 1
while i <= 10:
    print( i, "*", num, "=", i*num )
    i += 1