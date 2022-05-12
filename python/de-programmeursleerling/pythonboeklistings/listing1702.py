from pcinput import getInteger

num = getInteger( "Geen een getal: " )
try:
    print( "3 gedeeld door {} is {}".format( num, 3/num ) )
    print( "3 gedeeld door {}-3 is {}".format( num, 3/(num-3) ) )
except:
    print( "Je kunt niet delen door nul" )
print( "Tot ziens!" )