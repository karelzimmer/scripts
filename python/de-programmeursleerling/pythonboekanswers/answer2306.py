from itertools import combinations

testdict = {"a":1, "b":2, "c":3, "d":4 }
resultaat = [ {} ]

keylist = list( testdict.keys() )
for lengte in range( 1, len( testdict)+1 ):
    for item in combinations( keylist, lengte ):
        subdict = {}
        for key in item:
            subdict[key] = testdict[key]
        resultaat.append( subdict )

print( resultaat )