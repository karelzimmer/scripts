from pcinput import getInteger
from sys import exit

num = getInteger( "Geef een positief geheel getal: " )
if num < 0:
    print( "Je had een positief geheel getal moeten geven!" )
    exit()

print( "Ik handel je getal", num, "af" )
print( "Nog meer code" )
print( "Honderden regels code" )