import re

zin = "William Randolph Hearst trachtte alle exemplaren van \
Orson Welles' meesterwerk 'Citizen Kane', te vernietigen, omdat \
hij het bezwaarlijk vond dat de protagonist een nauwelijks-\
verhulde karikatuur van hemzelf was. Ik vraag me af of William \
Henry Gates De Derde hetzelfde zou doen."

pnaam = re.compile( r"\b([A-Z][a-z]*(\s+[A-Z][a-z]*)+)\b" )
naamlist = pnaam.finditer( zin )
for naam in naamlist:
    print( naam.group(1) )