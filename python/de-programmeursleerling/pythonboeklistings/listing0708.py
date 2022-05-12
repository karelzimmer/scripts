i = 1
while i <= 1000000:
    num1 = int( "1" + str( i ) )
    num2 = int( str( i ) + "1" )
    if num2 == 3 * num1:
        print( num2, "is drie keer", num1 )
        break
    i += 1
else:
    print( "Geen antwoord gevonden" )