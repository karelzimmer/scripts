from pcinput import getLetter
from sys import exit

teller = 0
laagste = 0
hoogste = 1001
print( "Denk aan een getal tussen 1 en 1000." )

while True:
    poging = int( (laagste + hoogste) / 2 )
    teller += 1
    prompt = "Ik raad "+str( poging )+". Is jouw getal"+\
        " (L)ager of (H)oger, of is dit (C)orrect? "
    antwoord = getLetter( prompt )
    if antwoord == "C":
        break
    elif antwoord == "L":
        hoogste = poging
    elif antwoord =="H":
        laagste = poging
    else:
        print( "Antwoord H, L, of C." )
        continue
    if laagste >= hoogste-1:
        print( "Je moet een fout gemaakt hebben,", 
            "want je hebt gezegd dat het getal hoger is dan",
            laagste, "maar ook lager dan", hoogste )
        print( "Ik stop ermee" )
        exit()

if teller == 1:
    print( "In 1 keer geraden! Ik kan gedachten lezen!" )
else:
    print( "Ik moest", teller, "keer raden." )