appel = "appel"
banaan = "banaan"
kers = "kers"
doerian = "doerian"

def printfruit_1():
    print( appel, banaan )

def printfruit_2( appel ):
    banaan = kers
    print( appel, banaan )

def printfruit_3( appel, banaan ):
    kers = "mango"
    banaan = kers
    print( appel, banaan )

printfruit_1()
printfruit_2( kers )
printfruit_3( kers, doerian )

print( "appel =", appel )
print( "banaan =", banaan )
print( "kers =", kers )
print( "doerian =", doerian )