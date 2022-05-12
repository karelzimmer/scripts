from random import randint

stok = []
for value in ("Aas", "2", "3", "4", "5", "6", "7", "8", 
    "10", "Boer", "Vrouw", "Heer"):
    for kleur in ("Harten", "Schoppen", "Klaveren", "Ruiten"):
        stok.append( kleur + ' ' + value )
        
for i in range( len( stok ) ):
    j = randint( i, len( stok )-1 )
    stok[i], stok[j] = stok[j], stok[i]
    
for kaart in stok:
    print( kaart )