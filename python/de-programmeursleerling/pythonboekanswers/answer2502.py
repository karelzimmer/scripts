import re

zin = "De diender arresteerde de doerak op de Dam."

pde = re.compile( r"\bde\b", re.I )
delist = pde.findall( zin )
print( len( delist ) )