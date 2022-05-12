MAXNUM = 100
nummers = list( range(2,MAXNUM+1) )
i = 0
while i < len( nummers ):
    j = i+1
    while j < len( nummers ):
        if nummers[j]%nummers[i]:
            j += 1
        else:
            nummers.pop(j)
    i += 1
for i in nummers:
    print( i, end=" " )
