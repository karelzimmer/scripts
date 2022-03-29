# Mijn eerste Python programma!
print("Ah! Het werkt!")
a = 5
b = 7
c = a + b

print(a,'+',b,'=',c)

print(str(a) + '+' + str(b) + '=' + str(c))

print("%d + %d = %d" % (a,b,c))

print("{0} + {1} = {2}".format(a,b,c))
print("{1} + {0} = {2}".format(a,b,c))
print("{derde} is de som van {eerste} en {tweede}".format(eerste=a,tweede=b,derde=c))

print(f"{a} + {b} = {c}")

a = input('Geef getal 1: ')
b = input('Geef getal 2: ')
c = a + b
print(f"{a} + {b} = {c}")

a = input('Geef getal 1: ')
b = input('Geef getal 2: ')
c = int(a) + int(b)
print(f"{a} + {b} = {c}")
