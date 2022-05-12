##voornaam = input('Wat is uw voornaam: ')
##leeftijd = int(input("Wat is uw leeftijd: "))
##                 
##print(f"Uw voornaam is {voornaam}.")
##print(f"Uw leeftijd is {leeftijd}.")
##
##nogwerken = 67 - leeftijd
##print(f"Nog {nogwerken} jaren werken tot het pensioen!")
##

##if leeftijd >= 67:
##    print(f"Ah, al {abs(nogwerken)} jaren vrijheid!")
##

####Druk bij een leeftijd onder de 30 af: "jonkie", tussen 30 en 50: "ervaren",
####tussen 50 en 60: "uitstekend" en boven de 60: "begint star te worden".
##if leeftijd < 30:
##    print('jonkie')
##elif 30 < leeftijd < 50:
##    print('ervaren')
##elif 50 < leeftijd < 60:
##    print('uitstekend')
##else:
##    print("begint star te worden")

while True:
    voornaam = input("Wat is uw voornaam (typ 'stop' om te stoppen): ")
    if voornaam == 'stop':
        break
    leeftijd = int(input("Wat is uw leeftijd: "))
                 
    print(f"Uw voornaam is {voornaam}.")
    print(f"Uw leeftijd is {leeftijd}.")

    nogwerken = 67 - leeftijd
    print(f"Nog {nogwerken} jaren werken tot het pensioen!")

    if leeftijd >= 67:
        print(f"Ah, al {abs(nogwerken)} jaren vrijheid!")

    ##Druk bij een leeftijd onder de 30 af: "jonkie", tussen 30 en 50: "ervaren",
    ##tussen 50 en 60: "uitstekend" en boven de 60: "begint star te worden".
    if leeftijd < 30:
        print('jonkie')
    elif leeftijd < 50:
        print('ervaren')
    elif leeftijd < 60:
        print('uitstekend')
    else:
        print("begint star te worden")


isSchrikkel = jaar % 400 == 0 or (jaar % 4 == 0 and jaar % 100 != 0)

if maand == 2:
    maxDag = 29 if isSchrikkel else 28
elif maand in (4,6,9,11):
    maxDag = 30
else:
    maxDag = 31

if dag >= 1 and dag <= maxDag and maand >= 1 and maand <= 12 and jaar >= 0:
    print('%d-%d-%d is geldige datum' % (dag, maand, jaar))
else:
    print('%d-%d-%d is ongeldige datum' % (dag, maand, jaar))
