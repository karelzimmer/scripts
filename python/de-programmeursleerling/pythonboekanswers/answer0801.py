from pcinput import getInteger

# tafel krijgt een integer als parameter. Het drukt de 
# tafel van vermenigvuldiging voor deze integer af.
def tafel( n ):
    i = 1
    while i <= 10:
        print( i, "*", n, "=", i*n )
        i += 1

num = getInteger( "Geef een getal: " )
tafel( num )