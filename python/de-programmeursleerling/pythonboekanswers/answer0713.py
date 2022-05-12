from random import randint

POGINGEN = 10000
DOBBELSTENEN = 5

succes = 0

for i in range( POGINGEN ):
    laatste = 0
    for j in range( DOBBELSTENEN ):
        waarde = randint( 1, 6 )
        if waarde < laatste:
            break
        laatste = waarde
    else:
        succes += 1
        
print( "De waarschijnlijkheid van een oplopende serie van vijf",
    "dobbelsteen worpen is {:.3f}".format( succes/POGINGEN ) )