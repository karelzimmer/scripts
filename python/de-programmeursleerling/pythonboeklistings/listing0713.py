from pcinput import getInteger

x = getInteger( "Geef nummer 1: " )
y = getInteger( "Geef nummer 2: " )

while (x != 0) and (y != 0) and (x%y != 0) and (y%x != 0):
    if (x > 1000) or (y > 1000) or (x < 0) or (y < 0):
        print( "Nummers moeten tussen 0 en 1000 zijn" )
        x = getInteger( "Geef nummer 1: " )
        y = getInteger( "Geef nummer 2: " )
        continue
    print( x, "keer", y, "is", x * y )
    x = getInteger( "Geef nummer 1: " )
    y = getInteger( "Geef nummer 2: " )

if x == 0 or y == 0:
    print( "Klaar!" )
else:
    print( "Fout: de nummers mogen geen delers zijn" )