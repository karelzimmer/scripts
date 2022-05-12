import re

# List van strings die worden gebruikt voor testen.
slist = [ "aaabbb", "aaaaaa", "abbaba", "aaa", "bEver ottEr",
    "tango samba rumba", " hello world ", " Hello World " ]

# Reguliere expressies die moeten worden ingevuld.
relist = [
    r"",  # 1. Alleen a's gevolgd door alleen b's, inclusief ""
    r"",  # 2. Alleen a's, inclusief ""
    r"",  # 3. Alleen a's en b's, willekeurige volgorde, incl. "" 
    r"",  # 4. Precies drie a's
    r"",  # 5. Noch a's noch b's, maar "" is toegestaan
    r"",  # 6. Een even aantal a's (en niks anders)
    r"",  # 7. Precies twee woorden, ongeacht spaties
    r"",  # 8. Bevat een woord dat op "ba" eindigt
    r""   # 9. Bevat een woord dat begint met een hoofdletter
]

for s in slist:
    print( s, ':', sep='', end=' ' )
    for i in range( len( relist ) ):
        m = re.search( relist[i], s )
        if m:
            print( i+1, end=' ' )
    print()