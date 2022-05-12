from datetime import datetime

numlist = []
for i in range( 10000 ):
    numlist.append( i )

start = datetime.now()
teller = 0
for i in range( 10000, 20000 ):
    if i in numlist:
        teller += 1
eind = datetime.now()

print( "{}.{} seconden om {} nummers te vinden".format( 
    (eind-start).seconds, (eind-start).microseconds, teller ) )