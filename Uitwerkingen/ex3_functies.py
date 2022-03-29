# Functies!

import datumfuncties as df
#from datumfuncties import isGeldigeDatum
import re

def telop(a,b):
    return a + b

def bereken(a,b, optor):
    if optor == "+":
        return a + b
    elif optor == "-":
        return a - b
    elif optor == "*":
        return a * b
    elif optor == "/":
        return a / b

def bereken2(a,b, optor):
    #ret = None              #zonder deze UnboundLocalError bij optor="^"
    if optor == "+":
        ret = a + b
    elif optor == "-":
        ret =  a - b
    elif optor == "*":
        ret =  a * b
    elif optor == "/":
        ret = a / b
    else:
        ret = None
    return ret

def fac(a):
    f = 1
    while a > 1:
        #print(f,a)
        f *= a          #f = f * a
        a -= 1
    return f

trekaf = lambda a,b : a - b
vermvuld = lambda a,b : a * b
deel = lambda a,b : a / b

def test_funcinfunc():
    def inc(getal):
        return getal + 1

    def dec(getal):
        return getal - 1

    antw = input("Geef geheel getal: ")
    while antw != "stop":
        if antw.isnumeric():
            a = int(antw)
            print(a, inc(a), dec(a))
        antw = input("Geef geheel getal: ")

def test_funcinfunc2(getal):
    def inc(g):
        return g + 1

    def dec(g):
        return g - 1

    print(getal, "->", inc(getal), dec(getal))
        
def test_datumfuncties():
    dag = 29
    maand = 2
    jaar = 2000
    if df.isGeldigeDatum(dag,maand,jaar):
        print("%d-%d-%d is een geldige datum" % (dag,maand,jaar))
    else:
        print("%d-%d-%d is een ongeldige datum" % (dag,maand,jaar))
    
def test_delen():
    print('We gaan delen')
    a = int(input('Geef getal 1: '))
    b = int(input('Geef getal 2: '))
    c = a / b
    print(c)
    print('klaar')

def test_delen_ex():
    print('We gaan delen, met exception handling')
    try:
        a = int(input('Geef getal 1: '))
        b = int(input('Geef getal 2: '))
        c = a / b
        print(c)
    except ValueError as ex:
        print(ex)
        #print(ex.args)             #wordt tupel
        #print(ex.args[0])
    except ZeroDivisionError:
        print('Delen door 0 mag niet!')
    print('klaar')


def bereken_ex(a,b, optor):
    if optor == "+":
        return a + b
    elif optor == "-":
        return a - b
    elif optor == "*":
        return a * b
    elif optor == "/":
        return a / b
    else:
        raise ValueError("Ongeldige operator: '%s'" % optor)

def test_bereken_ex():
    try:
        #c = bereken_ex(5, 7, "*")
        #c = bereken_ex(5, 7, "^")
        c = bereken_ex(5, 0, "/")
        print("c =", c)
    except (ValueError,ZeroDivisionError) as ex:
        print(ex)
    print("Klaar.")

def regex_pcode():
    pcode = "3022 BF"
    #pcode = "3022 BFF"
    #pcode = "3022BF"

    #pat = r"\d\d\d\d [A-Z][A-Z]"
    #pat = r"\d{4} [A-Z][A-Z]"
    pat = r"[1-9]\d{3} ?[A-Z][A-Z]"

    m = re.fullmatch(pat, pcode)
    #print(m)
    #print(m.group())
    if m:
        print(pcode, "is een geldige postcode")
    else:
        print(pcode, "is een ongeldige postcode")

def regex_datum():
    datum = "23/05/2019"
    #datum = "23/05-2019"
    #datum = "23/5/2019"

    pat = r"\d\d[-/]\d\d[-/]\d{4}"
    #pat = r"\d\d([-/])\d\d\1\d{4}"      #\1 is een back reference
    #pat = r"\d\d-\d\d-\d{4}|\d\d/\d\d/\d{4}"

    m = re.fullmatch(pat, datum)
    if m:
        print(datum, "is een geldige datum")
    else:
        print(datum, "is een ongeldige datum")

def regex_vervang():
    s = "O. wat. is. dit. leuk."
    t = re.sub(r"\.", "", s)
    
    #t = re.sub(r"\.", "", s) + "."     #slotpunt van s laten staan...
    #t = re.sub(r"\. ", " ", s)
    #t = re.sub(r"\.", "", s[:-1]) + s[-1]
    #t = re.sub(r"\.(?!$)", "", s)       #neg look ahead: vlg niet einde tekst
    print(t)

def interpoleer(getal, min1, max1, min2, max2):
    return min2 + (getal-min1) * ((max2-min2) / (max1-min1))

def fahrcels(a):
    return (a-32) * 5/9

def celsfahr(a):
    return a * 9/5 + 32

def maak_verhoog(a):
    def verhoog(getal):
        return getal + a
    return verhoog

def test_maak_verhoog():
    inc2 = maak_verhoog(2)
    print(inc2)
    print(inc2(5))
    print(inc2(0))
    print(maak_verhoog(3)(5))
    inc5 = maak_verhoog(5)
    print(inc5(3))
    print(inc5(10))

#--- script ---

#telop(5, 7)
c = telop(5, 7)
print(c)
#print(telop(2, 3*4))
#print(telop("boeken", "bal"))
#print(telop(3, "boeken"))
#print(telop(str(3), "boeken"))

#c = bereken(5,7, "+")
#c = bereken('appel','flap', "+")
#c = bereken(5,7, "-")
#c = bereken(3,2, "/")
#c = bereken(3,0, "/")
#c = bereken(3,4, "^")           #None
#c = bereken(78,3, "*")
#c = bereken("ai",5, "*")
#c = bereken(5,"ai", "*")

#c = bereken2(5,7, "*")          #-2
#c = bereken2(3,4, "^")          #soms UnboundLocalError: local variable 'ret' referenced before assignment
#print(c)

#print(fac(4))
#print(fac(8))
#print(fac(10))
#print(fac(14))
#print(fac(69))
#print(fac(0))

#print(trekaf(13,5))
#print(vermvuld(13,5))
#print(deel(13,5))
#print(vermvuld('ojee ',3))

#test_funcinfunc()
#print(inc(4))              #NameError: niet bekend buiten test_funcinfunc()
#test_funcinfunc2(25)

#test_datumfuncties()
#print(__name__)
#print(df.__name__)
#print(df.__doc__)
#print(df.isGeldigeDatum.__doc__)
#help(df)

#test_delen()
#test_delen_ex()
#test_bereken_ex()

#regex_pcode()
#regex_datum()
#regex_vervang()

#print(interpoleer(47, 32,212, 0,100))
#print(fahrcels(47))
#print(interpoleer(30, 0,100, 32,212))
#print(celsfahr(30))
#print(interpoleer(102, 0,255, 0,100))

#test_maak_verhoog()
