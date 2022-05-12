import re

pDatum = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
m = pDatum.search( "In antwoord op uw schrijven van 25-3-2015, \
heb ik besloten een huurmoordenaar op u af te sturen." )
if m:
    print( "Datum: {}; dag: {}; maand: {}; jaar: {}".format( 
            m.group(0), m.group(1), m.group(2), m.group(3) ) )