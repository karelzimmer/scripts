# Mijn eerste Python programma!


print("Ah! Het werkt!")
a = 5
b = 7
c = a + b
print(c)
print(a,'+',b,'=',c)

# volgende werkt niet: je kunt geen ints bij strings optellen
#print(a + '+' + b + '=' + c)
print(str(a) + '+' + str(b) + '=' + str(c))     #werkt, maar omslachtig
print("%d + %d = %d" % (a,b,c))

print("{0} + {1} = {2}".format(a,b,c))
print("{} + {} = {}".format(a,b,c))
print("{1} + {0} = {2}".format(a,b,c))
print("{derde} is de som van {eerste} en {tweede}".format(eerste=a,tweede=b,derde=c))

#met f-strings (Python 3.6)
print(f"{a} + {b} = {c}")
print(f"{b} - {a} = {b-a}")

a = input('Geef getal 1: ')
b = input('Geef getal 2: ')
c = a + b
print(c)

a = int(input('Geef getal 1: '))
b = int(input('Geef getal 2: '))
c = a + b
#print(c)
print("De uitkomst is:", c)
#print("De uitkomst is: %02X" % c)


