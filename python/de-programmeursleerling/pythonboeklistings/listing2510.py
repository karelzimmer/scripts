import re

m = re.search( r"(\S).*\1", "Monty Python's Flying Circus" )
if m:
    print( "{} komt twee keer voor in de string".format( 
        m.group(1) ) )
else:
    print( "Geen match gevonden." )