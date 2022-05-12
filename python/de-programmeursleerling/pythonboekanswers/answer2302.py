def faculteit():
    totaal = 1
    for i in range( 1, 11 ):
        totaal *= i
        yield totaal
        
fseq = faculteit()
for n in fseq:
    print( n, end=" " )