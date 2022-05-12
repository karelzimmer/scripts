import re

zin = "De prijs voor een 2-kamer appartement op  Manhattan \
start bij 1 miljoen dollars, en kan oplopen tot het tienvoudige \
op 42nd Street."

pwoord = re.compile( r"[A-Za-z]+" )
woordlist = pwoord.findall( zin )
for woord in woordlist:
    print( woord )