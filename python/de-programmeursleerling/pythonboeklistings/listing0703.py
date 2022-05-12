from pcinput import getInteger
    
num = -1
totaal = 0
while num != 0:
    num = getInteger( "Geef een nummer: " )
    totaal += num
print( "Totaal is", totaal )