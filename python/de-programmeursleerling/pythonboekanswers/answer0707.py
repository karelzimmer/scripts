from random import random

DARTS = 100000
raak = 0
for i in range( DARTS ):
    x = random()
    y = random()
    if x*x + y*y < 1:
        raak += 1

print( "Een redelijke benadering van pi is", 4 * raak / DARTS )