from collections import Counter

data = [ "appel", "banaan", "appel", "banaan", "appel", "kers" ]
c = Counter( data )
print( c )
print( c.most_common( 1 ) )

data2 = [ "mango", "kers", "kers", "kers", "kers" ]
c.update( data2 )
print( c )
print( c.most_common() )