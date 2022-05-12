from pcinput import getInteger

num = getInteger( "Geef een getal: " )
try:
    print( "3 gedeeld door {} is {}".format( num, 3/num ) )
except:
    print( "Je kunt niet delen door nul" )
print( "Tot ziens!" )