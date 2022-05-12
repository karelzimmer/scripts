from pcinput import getInteger
from sys import exit

while True:
    x = getInteger( "Geef nummer 1: " )
    if x == 0:
        break
    y = getInteger( "Geef nummer 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "De nummers moeten tussen 0 en 1000 liggen" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Fout: de nummers mogen geen delers zijn" )
        exit()
    print( "Vermenigvuldiging van", x, "met", y, "geeft", x * y )

print( "Tot ziens!" )