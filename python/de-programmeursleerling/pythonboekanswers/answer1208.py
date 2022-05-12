# Recursieve functie die bepaalt of intlist (integer-list) een 
# subset heeft die optelt tot totaal. Het retourneert de 
# subset, of een lege list als er geen subset is die werkt.
def subset_telt_op_tot( intlist, totaal ):
    for num in intlist:
        if num == totaal:
            return [num]
        nlist = intlist[:]
        nlist.remove( num )
        retlist = subset_telt_op_tot( nlist, totaal-num )
        if len( retlist ) > 0:
            retlist.insert( 0, num )
            return( retlist )
    return []

numlist = [ 3, 8, -1, 4, -5, 6 ]
oplossing = subset_telt_op_tot( numlist, 0 )
if len( oplossing ) <= 0:
    print( "Geen subset telt op tot nul" )
else:
    for i in range( len( oplossing ) ):
        if oplossing[i] < 0 or i == 0:
            print( oplossing[i], end="" )
        else:
            print( "+{}".format( oplossing[i] ), end="" )
    print( "=0" )