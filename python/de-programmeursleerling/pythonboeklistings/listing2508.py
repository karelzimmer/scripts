import re

pDatum = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
datumlist = pDatum.findall( "In antwoord op uw schrijven van \
25-3-2015, heb ik op 27-3-2015 besloten u verder te negeren." )
for datum in datumlist:
    print( datum )