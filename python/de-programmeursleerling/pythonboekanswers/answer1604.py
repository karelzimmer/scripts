from os.path import join
from os import getcwd

LEN = 3

def schoon( s ):
    nieuws = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            nieuws += c
        else:
            nieuws += " "
    return nieuws

lijst = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
setlist = []

for naam in lijst:
    bestandnaam = join( getcwd(), naam )
    woordset = set()
    setlist.append( woordset )
    fp = open( bestandnaam )
    while True:
        regel = fp.readline()
        if regel == "":
            break
        woordlist = schoon( regel ).split()
        for woord in woordlist:
            if len( woord ) >= LEN:
                woordset.add( woord )
    fp.close()

combinatie = setlist[0].copy()
i = 1
while i < len( setlist ):
    combinatie = combinatie & setlist[i]
    i += 1

for woord in combinatie:
    print( woord )