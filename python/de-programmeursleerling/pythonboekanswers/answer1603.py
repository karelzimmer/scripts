from os.path import join
from os import getcwd

def verwijderklinkers( regel ):
    nieuweregel = ""
    for c in regel:
        if c not in "aeiouAEIOU":
            nieuweregel += c
    return nieuweregel

inputnaam = join( getcwd(), "pc_woodchuck.txt" )
outputnaam = join( getcwd(), "pc_woodchuck.tmp" )

fpi = open( inputnaam )
fpo = open( outputnaam, "w" )

telread = 0
telwrite = 0

while True:
    regel = fpi.readline()
    if regel == "":
        break
    telread += len( regel )
    regel = verwijderklinkers( regel )
    fpo.write( regel )
    telwrite += len( regel )

fpo.close()
fpi.close()

print( "Gelezen:", telread )
print( "Geschreven:", telwrite )