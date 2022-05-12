fruitmand = {"appel":3,"banaan":5,"kers":50,"druif":0,"mango":2}

appel = fruitmand.get( "appel" )
if appel:
    print( "appel is in de mand" )
else:
    print( "geen appels in de mand")

aardbei = fruitmand.get( "aardbei" )
if aardbei:
    print( "aardbei is in de mand" )
else:
    print( "geen aardbei in de mand")

banaan = fruitmand.get( "banaan", 0 )
print( "aantal bananen in de mand:", banaan )

aardbei = fruitmand.get( "aardbei", 0 )
print( "aantal aarbeien in de mand:", aardbei )