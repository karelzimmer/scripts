from random import randint
from pcinput import getInteger

antwoord = randint( 1, 1000 )
teller = 0
while True:
    poging = getInteger( "Raad een getal: " )
    if poging < 1 or poging > 1000:
        print( "Je moet een getal tussen de 1 en 1000 noemen" )
        continue
    teller += 1
    if poging < antwoord:
        print( "Hoger" )
    elif poging > antwoord:
        print( "Lager" )
    else:
        print( "Je hebt het geraden!" )
        break
        
if teller == 1:
    print( "Je hoefde maar 1 keer te raden. Geluksvogel." )
else:
    print( "Je moest", teller, "keer raden." )