from random import random, randint, seed

seed()
print( "Een toevalsgetal tussen 1 en 10 is", randint( 1, 10 ) )
print( "Een ander is", randint( 1, 10 ) )
seed( 0 )
print( "3 toevalsgetallen zijn:", random(), random(), random() )
seed( 0 )
print( "Dezelfde 3 zijn:", random(), random(), random() )