# if- en while-statements

# voornaam en leeftijd
##voornaam = input('Uw voornaam: ')
##leeftijd = int(input('Uw leeftijd: '))
##print('%s is %d jaar oud.' % (voornaam, leeftijd))
##jaren = 67 - leeftijd
#print('Nog %d jaren werken tot het pensioen!' % jaren)
#print('%s, je moet nog %d jaren werken tot je pensioen!' % (voornaam,jaren))

##if jaren > 0:
##    print('Nog %d jaren werken tot het pensioen!' % jaren)
##
##else:
##    print('Ah, al %d jaren vrijheid!' % -jaren)
##    #print('Ah, al %d %s vrijheid!' % (-jaren, "jaar" if jaren == -1 else "jaren"))
##
##if leeftijd < 30:
##    print("jonkie")
##elif leeftijd < 50:
##    print("ervaren")
##elif leeftijd < 60:
##    print("uitstekend")
##else:
##    print("begint star te worden")

# voornaam en leeftijd, while-versie
##voornaam = input('Geef voornaam: ')
##while voornaam != "stop":
##    leeftijd = int(input('Geef leeftijd: '))
##    print('%s is %d jaar oud.' % (voornaam, leeftijd))
##    jaren = 67 - leeftijd
##    #print('Nog %d jaren werken tot het pensioen!' % jaren)
##    #print('%s, je moet nog %d jaren werken tot je pensioen!' % (voornaam,jaren))
##
##    if jaren > 0:
##        print('Nog %d jaren werken tot het pensioen!' % jaren)
##        if leeftijd < 30:
##            print("jonkie")
##        elif leeftijd < 50:
##            print("ervaren")
##        elif leeftijd < 60:
##            print("uitstekend")
##        else:
##            print("begint star te worden")
##    else:
##        print('Ah, al %d jaren vrijheid!' % -jaren)
##
##    voornaam = input('Geef voornaam: ')


# test op geldige datum
#let op: we werken niet in een function, dus kunnen we return niet gebruiken!

# 1904 is geldig schrikkeljaar, want 1904 % 4 == 0 en 1904 % 100 != 0
# 1900 is ongeldig, want 1900 % 4 == 0 (goed) en 1900 % 100 == 0 (fout)
# we vullen eerst de boolean variabele isSchrikkel en rekenen dan verder

##dag = 29
##maand = 2
##jaar = 2001

# manier 1:
##if jaar % 400 == 0:
##    isSchrikkel = True
##elif jaar % 100 == 0:
##    isSchrikkel = False
##elif jaar % 4 == 0:
##    isSchrikkel = True
##else:
##    isSchrikkel = False

# manier 2:
##isSchrikkel = jaar % 400 == 0 or (jaar % 4 == 0 and jaar % 100 != 0)
##
##if maand == 2:
##    maxDag = 29 if isSchrikkel else 28
##elif maand in (4,6,9,11):
##    maxDag = 30
##else:
##    maxDag = 31
##
##if dag >= 1 and dag <= maxDag and maand >= 1 and maand <= 12 and jaar >= 0:
##    print('%d-%d-%d is geldige datum' % (dag, maand, jaar))
##else:
##    print('%d-%d-%d is ongeldige datum' % (dag, maand, jaar))


# bmi
gewicht = float(input('Uw gewicht: '))
lengte = float(input('Uw lengte: '))
bmi = gewicht / (lengte*lengte)
print("bmi =", bmi)

#if bmi >= 28.0 and bmi <= 32.0:
if 28.0 <= bmi <= 32.0:
    print("werk aan de winkel")

print("bmi =", round(bmi,2))
print("bmi = %.2f" % (bmi))
