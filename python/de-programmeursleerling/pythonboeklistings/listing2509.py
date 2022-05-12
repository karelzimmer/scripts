import re

pDatum = re.compile( 
    r"(?P<dag>\d{1,2})-(?P<maand>\d{1,2})-(?P<jaar>\d{4})" )
m = pDatum.search( "In antwoord op uw schrijven van 25-3-2015, \
heb ik besloten een zingend telegram op u af te sturen." )
if m:
    print( "dag is {}".format( m.group('dag') ) )
    print( "maand is {}".format( m.group('maand') ) )
    print( "jaar is {}".format( m.group('jaar') ) )