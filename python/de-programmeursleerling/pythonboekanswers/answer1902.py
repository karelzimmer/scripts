def setBit( opslag, index, value ):
    masker = 1<<index
    if value:
        opslag |= masker
    else:
        opslag &= ~masker
    return opslag

# getBit() retourneert 0 als de bit behorende bij de index op 1
# staat, en anders retourneert het iets anders. Omdat alleen 0 
# als False wordt beschouwd, kun je deze functie gebruiken om de
# waarde van een bit te testen.
def getBit( opslag, index ):
    masker = 1<<index
    return opslag & masker

def toonBits( opslag ):
    for i in range( 8 ):
        index = 7 - i
        if getBit( opslag, index ):
            print( "1", end="" )
        else:
            print( "0", end="" )
    print()
    
opslag = 0
opslag = setBit( opslag, 0, True )
opslag = setBit( opslag, 1, True )
opslag = setBit( opslag, 2, False )
opslag = setBit( opslag, 3, True )
opslag = setBit( opslag, 4, False )
opslag = setBit( opslag, 5, True )
toonBits( opslag )

opslag = setBit( opslag, 1, False )
toonBits( opslag )