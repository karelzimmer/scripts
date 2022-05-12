# Berekent de faculteit van de paremeter n, een integer.
# Retourneert de uitkomst als integer.
def faculteit( n ):
    waarde = 1
    for i in range( 2, n+1 ):
        waarde *= i
    return waarde

# Berekent n boven k; n en k zijn integer parameters;
# Retourneert n boven k als integer (want dat is het altijd). 
def binomiaalcoefficient( n, k ):
    if k > n:
        return 0
    return int( faculteit( n ) / 
        (faculteit( k )*faculteit( n - k )) )

def main():
    print( faculteit( 5 ) )
    print( binomiaalcoefficient( 8, 3 ) )
    
if __name__ == '__main__':
    main()