from itertools import combinations

numlist = [ 3, 8, -1, 4, -5, 6 ]
oplossing = []

for i in range( 1, len( numlist )+1 ):
    seq = combinations( numlist, i )
    for item in seq:
        if sum( item ) == 0:
            oplossing = item
            break
    if len( oplossing ) > 0:
        break
        
if len( oplossing ) <= 0:
    print( "Er is geen subset die optelt tot nul" )
else:
    for i in range( len( oplossing ) ):
        if oplossing[i] < 0 or i == 0:
            print( oplossing[i], end="" )
        else:
            print( "+{}".format( oplossing[i] ), end="" )
    print( "=0" )