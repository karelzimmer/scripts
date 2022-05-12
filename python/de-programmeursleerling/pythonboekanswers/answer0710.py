from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
if num < 2:
    print( num, "is niet priem" )
else:
    i = 2
    while i*i <= num:
        if num%i == 0:
            print( num, "is niet priem" )
            break
        i += 1
    else:
        print( num, "is priem" )