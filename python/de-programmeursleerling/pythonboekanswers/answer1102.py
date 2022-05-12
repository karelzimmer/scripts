def maal_complex( c1, c2 ):
    return (c1[0]*c2[0] - c2[1]*c1[1], c1[0]*c2[1] + c1[1]*c2[0])

def toon_complex( c ):
    return "({},{}i)".format( c[0], c[1] )

num1 = (2,1)
num2 = (0,2)
print( toon_complex( num1 ), "*", toon_complex( num2 ), "=",
     toon_complex( maal_complex( num1, num2 ) ) )