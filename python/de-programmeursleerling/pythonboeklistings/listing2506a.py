import re

# List van strings die worden gebruikt voor testen.
slist = [ "aaabbb", "aaaaaa", "abbaba", "aaa", "bEver ottEr",
    "tango samba rumba", " hello world ", " Hello World " ]

# Reguliere expressies die moeten worden ingevuld.
relist = [
    r"^a*b*$",            # 1. Alleen a's gevolgd door alleen b's, inclusief ""
    r"^a*$",              # 2. Alleen a's, inclusief ""
    r"^[ab]*$",           # 3. Alleen a's en b's, willekeurige volgorde, incl. "" 
    r"^aaa$",             # 4. Precies drie a's
    r"^[^ab]*$",          # 5. Noch a's noch b's, maar "" is toegestaan
    r"^(aa)*$",           # 6. Een even aantal a's (en niks anders)
    r"^\s*\S+\s+\S+\s*$", # 7. Precies twee woorden, ongeacht spaties
    r"ba\b",              # 8. Bevat een woord dat op "ba" eindigt
    r"\b[A-Z]"            # 9. Bevat een woord dat begint met een hoofdletter
]

for s in slist:
    print( s, ':', sep='', end=' ' )
    for i in range( len( relist ) ):
        m = re.search( relist[i], s )
        if m:
            print( i+1, end=' ' )
    print()