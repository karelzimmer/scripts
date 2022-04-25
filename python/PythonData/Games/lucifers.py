#Een variant van het lucifer-spel
#(met Computer-speler, naam begint met "Computer")

"""
6 stapeltjes lucifers, met grootte 1 t/m 6.
Spelers moeten om en om een of meer lucifers weghalen, maar
slechts van 1 stapel tegelijk.
Wie de laatste lucifer weghaalt, heeft gewonnen.

https://nl.wikipedia.org/wiki/Nim_(spel)
In de gewone versie wint de speler die het laatste voorwerp wegneemt.
In de zg misère-versie van het spel verliest die speler. Deze versie,
de meest gebruikelijke, zit in de film L'Année dernière à Marienbad
(1961) van Alain Resnais. Sindsdien wordt het spel in het Frans
jeu de Marienbad genoemd.

In de misère-versie is de winnende strategie dezelfde als bij het
normale spel, behalve wanneer er (aan het einde van het spel) door
de zet alleen nog maar stapels van 1 voorwerp zouden overblijven.
De winnende zet is dan zo dat er daarna een oneven aantal stapels van
1 voorwerp overblijft (bij het gewone spel een even aantal).

"""

import random
import time

lucifers = [1, 2, 3, 4, 5, 6]
#lucifers = [1, 2, 3, 0, 0, 0]
spelers = ["dummie"]
huidige = 0

def init():
    global huidige
    
    nm = input("Geef naam speler 1: ")
    spelers.append(nm)
    nm = input("Geef naam speler 2: ")
    spelers.append(nm)
    
    #huidige = random.randint(1,10) % 2 + 1
    huidige = random.randint(1,2)           #1 t/m 2
    print("%s mag beginnen!" % spelers[huidige])

def toon_lucifers():
    #print(lucifers)
    print("1:%s  2:%s  3:%s  4:%s  5:%s  6:%s" % ('I'*lucifers[0], 'I'*lucifers[1],
        'I'*lucifers[2], 'I'*lucifers[3], 'I'*lucifers[4], 'I'*lucifers[5]))

def speler_zet():
    while True:
        st = int(input("  Welke stapel [1-6; 0 is stoppen]: "))
        if st == 0:
            return True
        if st < 1 or st > 6:
            continue
        st -= 1                     #index van 1-6 naar 0-5
        #print(st, lucifers[st])
        if lucifers[st]:
            break
    luc = int(input("  Hoeveel lucifers weghalen [1-%d]: " % lucifers[st]))
    if luc < 1:
        luc = 1
    elif luc > lucifers[st]:
        luc = lucifers[st]
    lucifers[st] -= luc
    return False

def computer_zet():
    crc = 0
    print("  Even denken...")
    time.sleep(1.2)
    for i in lucifers:
        crc ^= i
    if crc:                     #computer kan winnen
        for st, i in enumerate(lucifers):
            a = i ^ crc
            if a < i:
                i = lucifers[st] - a
                lucifers[st] = a
                break
    else:                       #computer staat op verlies
        st = lucifers.index(max(lucifers))
        #i = 1                   #1 weghalen v grootste stapel
        i = random.randint(1, lucifers[st])
        lucifers[st] -= i
    print("  Stapel: %d" % (st + 1))
    time.sleep(1.0)
    print("  Haal weg: %d" % i)
    return False

def doe_zet():
    print("\nSpeler %s:" % spelers[huidige])
    toon_lucifers()
    if spelers[huidige].lower().startswith("computer"):
        return computer_zet()
    else:
        return speler_zet()

def swap_spelers():
    global huidige

    if huidige == 1:
        huidige = 2
    else:
        huidige = 1
    
def spel_lus():
    while sum(lucifers):
        if doe_zet():        #True ->stoppen ->je verliest
            break
        swap_spelers()

    swap_spelers()
    print("\nSpeler %s heeft gewonnen!" % spelers[huidige])

#--- script ---

init()
#print(lucifers)
#print(spelers)

spel_lus()

print("Klaar.")
