from random import randint

TESTS = 10000
succes = 0
for i in range( TESTS ):
    for j in range( 5 ):
        if randint( 1, 6 ) != 6:
            break
    else:
        succes += 1
print( "Waarschijnlijkheid van vijf zessen is", succes / TESTS )