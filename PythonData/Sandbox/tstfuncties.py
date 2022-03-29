# eenvoudige functies

def doeniks():
    pass            #zonder pass error: expected indented block

tekst = 'Ojee, ojee'

def toonTekst():
    tekst = 'aha aha'
    print(tekst)
    #print(locals())

#toonTekst()        #error
#tekst = 'Ojee, ojee, hadsiekiedee'

def toonTekst2(tekst):
    print(tekst)
    #print(locals())        #arg wordt loc var
    #return None
    #return 42
    #return len(tekst)

def toon_namen(n1='Jan', n2='Piet', n3='Geesje'):
    print(n1, n2, n3)

def toon_namen2(n1, n2, n3):
    print(n1, n2, n3)

def telop(a, b):
    return a + b

tel2 = telop            #adres van fn telop in fnptr tel2 zetten

trekaf = lambda x,y : x - y     #hij doet: return x-y; NIET zelf intypen: return x-y

multi = lambda x,y :\
    x * y                   # na de \ hierboven mag ook geen commentaar staan!
#body mag maar 1 regel zijn, dus \ voor vervolgregel verplicht

def funcinfunc(a):
    def kwadraat(x):
        return x * x
    def wortel(x):
        return x ** 0.5

    k = kwadraat(a)
    w = wortel(a)
    print(k, w)

def funcinfunc2(a):
    kwadraat = lambda x : x * x
    wortel = lambda x : x ** 0.5

    k = kwadraat(a)
    w = wortel(a)
    print(k, w)


#let op: achter *arg mag nog een ander arg, MITS je dat met naam aanroept!
def som(*getallen):
    totaal = 0
    #totaal = ""
    #print("in som(): aantal getallen = %d" % len(getallen))
    #print("in som(): getallen[1] = %d" % getallen[1])
    for a in getallen:
        totaal += a
    return totaal

#list v functies:
fn = [lambda x,y : x+y, lambda x,y : x-y, lambda x,y : x*y,
      lambda x,y : x/y]


#--- script ---

#print('hallo', end=' ')
#print('Marie!')

#doeniks()               #deze doet niks
#print(doeniks())        #geeft None

#toonTekst()             #gaat goed
#print(tekst)

#toonTekst2('hallo')
#toonTekst2()
#toonTekst2(None)
#toonTekst2("")
#print(toonTekst2('hallo'))

#toon_namen()
#print('telop:', telop(True, True))

#toon_namen('Klaas')
#toon_namen('Klaas',,'Ursula')       #invalid syntax
#toon_namen('Klaas',pass,'Ursula')       #invalid syntax
#toon_namen('Klaas',None,'Ursula')
#toon_namen('Klaas',n3='Ursula')       #goed
#toon_namen(n1='Klaas',n3='Ursula')
#toon_namen('Klaas',n1='Ursula')     #TypeError: multiple values for n1
#toon_namen(n3='Ursula', n1='Klaas')
#toon_namen('Klaas',n3='Ursula','Frits') #invalid syntax: pos arg follows keyword
#toon_namen('Klaas',n2='Ursula','Frits')  #invalid syntax

#toon_namen2()
#toon_namen2('Klaas')
#toon_namen2('Klaas','Frans','Hubert')
#Hubert = 'Joop'
#Hubert = telop
#Hubert = telop(5,6.3)
#toon_namen2('Klaas','Frans',Hubert)

#print('\ntelop() + fn ptrs:')
#telop(5, 6.2)
#a = telop(5, 6.2)
#print(a)
#print('telop:', telop(5, 6.2))
#print('telop:', telop(5, float("33.95")))
#print('telop:', telop(int(input("geef getal 1: ")), int(input("geef getal 2: "))))
#print('telop:', telop("Hallo ", "Marie!"))
#print('telop:', telop(True, True))
#print('telop:', telop(True, False))

#print('tel2:', tel2(5, 6.1))
#print('tel2:', tel2)

#print('trekaf:', trekaf(5, 6.2))           #rare benadering
#print('trekaf:', trekaf(6.2, 5))           #rare benadering
#print('trekaf:', trekaf)
#print('multi:', multi(5, 6.2))
#print('deel:', (lambda x,y : x / y)(7, 5))  #goed
#print('mod :', (lambda a,b : a % b)(7, 5))

#print('functie lambda:', lambda x,y : x / y)
#print('functie lambda:', lambda x,y : x / y)    #wordt zelfde adres als vor
#print('functie lambda:', lambda a,b : a / b)    #idem
#print('functie lambda:', lambda a,b : a % b)
#print('functie telop:', telop)

#funcinfunc(4)
#funcinfunc(7.3)
#funcinfunc2(7.3)

#print('\nsom(..):')
uitk = som(2,13,5)           #goed
#uitk = som(2, 13, 5, -4, 67, 112, 51)
#uitk = som(2,13,5, -4, 67, 'ready', 51)        #TypeError
#uitk = som('appel', 'taart', 'en')      #kan wel, maar hier fout vanwege totaal=0 in fn
#uitk = som(2)
#uitk = som()            #goed, want hij maakt zelf lege lijst ->1 arg
#uitk = som((2,3,5))        #TypeError: unsupported for += : 'int' and 'tuple'
#uitk = som([1,2,4])         #TypeError: unsupported for += : 'int' and 'tuple'
#uitk = som(*[1,2,4])        #goed, want * ontbindt de list in factoren
#uitk = som(*(1,2,34))       #goed
print("som:", uitk)
#print(som(1,2,3,4,5))

#print('\nlist v fn ptrs:')
#print(fn[0](4,7))
#print(fn[1](4,7))
#print(fn[2](4,7))
#print(fn[3](4,7))

"""
print("\nMetadata:")
print("\ntoonTafelVanXDefault():")
print(toonTafelVanXDefault.__defaults__)        # (10,)
print(toonTafelVanXDefault.__code__)        # <code object ...>
print(toonTafelVanXDefault.__code__.co_argcount)
print(toonTafelVanXDefault.__code__.co_varnames)
print(toonTafelVanXDefault.__code__.co_code)    #b'x2\x00t\x00\x00d\x01\x00d enz

import inspect
print(inspect.getargspec(toonTafelVanXDefault))
print(inspect.signature(toonTafelVanXDefault))

print("\ntot():")
print(tot.__doc__)
tot.extrainfo = "Dit is een waardeloos voorbeeld!"
print(tot.extrainfo)
print(dir(tot))

print("\nsom():")
print(som.__doc__)

print("\ntelop() enz:")
print(telop.__qualname__)       #module.fnnaam
print(telop.__name__)           #fnnaam
print(multi.__qualname__)

print(tel2.__qualname__)        # telop, want niet gedecl in aparte module
print(tel2.__name__)            # telop

#print(locals())                #geeft dict v alle items+values in module
#print(dir())                   #geeft alleen namen van items
"""

