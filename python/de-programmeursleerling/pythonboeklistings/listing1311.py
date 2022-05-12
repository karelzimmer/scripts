from datetime import datetime

numdict = {}
for i in range( 10000 ):
    numdict[i] = 1

start = datetime.now()
teller = 0
for i in range( 10000, 20000 ):
    if i in numdict:
        teller += 1
eind = datetime.now()

print( "{}.{} seconden om {} nummers te vinden".format( 
    (eind-start).seconds, (eind-start).microseconds, teller ) )