fruitmand = {"appel":3,"banaan":5,"kers":50,"druif":0,"mango":2}
keylist = list( fruitmand.keys() )
keylist.sort()
for key in keylist:
    print( "{}:{}".format( key, fruitmand[key] ) )