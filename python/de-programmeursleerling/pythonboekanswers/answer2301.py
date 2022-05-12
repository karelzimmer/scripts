from pcinput import getInteger

class NietDeelbaarDoor:
    def __init__( self ):
        self.seq = list( range( 1, 101 ) )
    def __iter__( self ):
        return self
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()
    def verwerk( self, num ):
        i = len( self.seq )-1
        while i >= 0:
            if self.seq[i]%num == 0:
                del self.seq[i]
            i -= 1
    def __len__( self ):
        return len( self.seq )

ndd = NietDeelbaarDoor()
while True:
    num = getInteger( "Geef een getal: " )
    if num < 0:
        print( "Negatieve getallen worden overgeslagen" )
        continue
    if num == 0:
        break
    ndd.verwerk( num )

if len( ndd ) <= 0:
    print( "Er zijn geen getallen meer" )
else:
    for num in ndd:
        print( num, end=" " )