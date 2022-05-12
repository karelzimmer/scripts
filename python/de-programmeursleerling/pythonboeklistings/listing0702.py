from pcinput import getInteger

totaal = 0
teller = 0
while teller < 5:
    totaal += getInteger( "Geef een nummer: " )
    teller += 1

print( "Totaal is", totaal )