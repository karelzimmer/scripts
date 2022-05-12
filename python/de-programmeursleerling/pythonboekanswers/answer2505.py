import re

zin = "Klant: \"Ik wens een klacht te deponeren! \
Hallo mevrouw!\"\n\
Winkelier: \"Hoe bedoelt u, mevrouw?\"\n\
Klant: \"Het spijt me, ik ben verkouden.\"\n"

pgesproken = re.compile( r"\"[^\"]*\"" )
gesprokenlist = pgesproken.findall( zin )
for tekst in gesprokenlist:
    print( tekst )