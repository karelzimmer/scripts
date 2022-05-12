import datumfuncties as df


def telop(a,b):
    return a + b


def bereken(a,b, optor):
    if optor == '+':
        return a + b
    elif optor == '-':
        return a - b
    elif optor == '*':
        return a * b
    elif optor == '/':
        return a / b
    else:
        return None
    

def fac(a):
    i = fac = 1
    while i <= a:
        fac = fac * i
        i = i + 1
    return fac


trekaf = lambda a, b : a -b
vermvuld = lambda a, b : a * b
deel = lambda a, b : a / b


def test_funcinfunc(a):

    inc = lambda a : a + 1
##    def inc(a):
##        return a + 1

    dec = lambda a : a - 1
##    def dec(a):
##        return a - 1

    while True:
        invoer = input("Geef een geheel getal, 'stop' om te stoppen: ")
        if invoer == 'stop':
            break
        getal = int(invoer)
        print("Invoer : ", invoer)
        print(f"inc({invoer}) : ", inc(getal))
        print(f"dec({invoer}) : ", dec(getal))


def test_datumfuncties():
    dag = 2
    maand = 5
    jaar = 2020
    if df.isGeldigeDatum(dag,maand,jaar):
        # Kan ook met f-string en {dag}, {maand}, {jaar}, etc.
        print("%d-%d-%d is een geldige datum" % (dag,maand,jaar))
    else:
        print("%d-%d-%d is een ongeldige datum" % (dag,maand,jaar))
        print(isGeldigeDatum(dag, maand, jaar))


def test_delen():

    a = int(input("Geef getal 1: "))
    b = int(input("Geef getal 2: "))
    c = a / b
    print(f"Getal 1 / 2 is {c}")
    print('klaar')


def test_delen_ex():

    try:
        a = int(input("Geef getal 1: "))
        b = int(input("Geef getal 2: "))
        c = a / b
    except ValueError as ex:
        print(ex)
    except ZeroDivisionError:
        print('Delen door 0 mag niet!')
    else:
        print(f"Getal 1 / 2 is {c}")
    print('klaar')


def bereken_ex(a,b, optor):
        if optor == '+':
            return a + b
        elif optor == '-':
            return a - b
        elif optor == '*':
            return a * b
        elif optor == '/':
            return a / b
        else:
            raise ValueError(f"Ongeldige operator '{optor}'")


def test_bereken_ex():
    try:
        #c = bereken_ex(5, 7, "*")
        #c = bereken_ex(5, 7, "^")
        c = bereken_ex(5, 0, "/")
        print("c =", c)
    except (ValueError,ZeroDivisionError) as ex:
        print(ex)

    print("Klaar.")

# --- script ---

##c = telop(5, 7)
##print(c)
##
##print(telop(5, 7))
##
##print(telop(2, 3*4))
##
##print(telop('boeken','bal'))
##
##print(telop(3, 'boeken'))
##TypeError: unsupported operand type(s) for +: 'int' and 'str'

##c = bereken(5,7,'*')
##c = bereken(5,0,'*')
##c = bereken(5,0,'/')
##print(c)

#print(fac(0))
##print(fac(1))
##print(fac(2))
##print(fac(3))
##print(fac(4))
##print(fac(5))
##print(fac(6))
##print(fac(7))
##print(fac(8))

##print(trekaf(13,5))
##print(vermvuld(13,5))
##print(deel(13,5))
##
##print(vermvuld('ojee',3))

#test_funcinfunc(5)

#test_datumfuncties()

#test_delen()

#test_delen_ex()

#print(bereken_ex(5,7, '*'))
#print(bereken_ex(2,5, '^'))

test_bereken_ex()
