from pcinput import getFloat

num1 = getFloat( "Geef nummer 1: " )
num2 = getFloat( "Geef nummer 2: " )
num3 = getFloat( "Geef nummer 3: " )

print( "De grootste is", max( num1, num2, num3 ) )
print( "De kleinste is", min( num1, num2, num3 ) )
print( "Het gemiddelde is", round( (num1 + num2 + num3)/3, 2 ) )
