num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def kleinste_van_twee( n1, n2 ):
    if n1 < n2:
        return n1
    return n2

def grootste_van_twee( n1, n2 ):
    if n1 > n2:
        return n1
    return n2

def kleinste( n1, n2, n3 ):
    return kleinste_van_twee( kleinste_van_twee( n1, n2 ), n3 )

def middelste( n1, n2, n3 ):
    return n1 # geef iets terug

def grootste( n1, n2, n3 ):
    return grootste_van_twee( grootste_van_twee( n1, n2 ), n3 )

print( "som van kleinste =", kleinste( num11, num12, num13 ) + 
    kleinste( num21, num22, num23 ) )
print( "som van middelste =", middelste( num11, num12, num13 ) + 
    middelste( num21, num22, num23 ) )
print( "som van grootste =", grootste( num11, num12, num13 ) + 
    grootste( num21, num22, num23 ) )