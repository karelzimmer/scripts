import re

zin = "Michael Jordan, Bill Gates, and de Dalai Lama besloten \
om samen een vliegtochtje te ondernemen, toen ze een hippie \
zagen op de landingsbaan."

pnaam = re.compile( r"\b([A-Z][a-z]*\s+[A-Z][a-z]*)\b" )
naamlist = pnaam.findall( zin )
for naam in naamlist:
    print( naam )