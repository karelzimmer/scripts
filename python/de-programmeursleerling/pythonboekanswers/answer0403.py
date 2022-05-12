CENTEN_IN_DOLLAR = 100
CENTEN_IN_KWARTJE = 25
CENTEN_IN_DUBBELTJE = 10
CENTEN_IN_STUIVER = 5

bedrag = 1156
centen = bedrag

dollars = int( centen / CENTEN_IN_DOLLAR )
centen -= dollars * CENTEN_IN_DOLLAR
kwartjes = int( centen / CENTEN_IN_KWARTJE )
centen -= kwartjes * CENTEN_IN_KWARTJE
dubbeltjes = int( centen / CENTEN_IN_DUBBELTJE )
centen -= dubbeltjes * CENTEN_IN_DUBBELTJE
stuivers = int( centen / CENTEN_IN_STUIVER )
centen -= stuivers * CENTEN_IN_STUIVER
centen = int( centen )

print( bedrag / CENTEN_IN_DOLLAR, "bestaat uit:" )
print( "Dollars:", dollars )
print( "Kwartjes:", kwartjes )
print( "Dubbeltjes:", dubbeltjes )
print( "Stuivers:", stuivers )
print( "Centen:", centen )
