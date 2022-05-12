from pcinput import getInteger
    
num = getInteger( "Geef een nummer: " )
totaal = 0
while num != 0:
    totaal += num
    num = getInteger( "Geef een nummer: " )
print( "Totaal is", totaal )