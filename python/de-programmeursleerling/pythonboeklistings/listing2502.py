import re

mlist = re.finditer( r"a+", 
    "Kijk uit! Een gevaarlijk aardvarken is ontsnapt!" )
for m in mlist:
    print( "{} gevonden bij index {} tot index {}.".format( 
        m.group(), m.start(), m.end() ) )