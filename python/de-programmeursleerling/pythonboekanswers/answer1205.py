nummers = 101 * [True]
nummers[1] = False
for i in range( 1, len( nummers ) ):
    if not nummers[i]:
        continue
    print( i, end=" " )
    j = 2
    while j*i < len( nummers ):
        nummers[j*i] = False
        j += 1