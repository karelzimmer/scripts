# testen met runtime exceptions/errors

import sys

def delen():
    print('We gaan delen')
    a = int(input('Geef getal 1: '))
    b = int(input('Geef getal 2: '))
    c = a / b
    print(c)
    print('klaar')

def delen_ex():
    print('We gaan delen, met exception handling')
    try:
        a = int(input('Geef getal 1: '))
        b = int(input('Geef getal 2: '))
        c = a / b
        print(c)
    except ValueError as ex:
        #print("Fout 0x23A2B8DD opgetreden. Neem contact op met de beheerder.")
        print(ex)
        #print(repr(ex))
        #print(ex.__cause__)         #None
        #print(ex.args)              #wordt tupel: (str(ex),)
        #print(ex.args[0])
        #print(ex.__context__)       #None
        #tb = sys.exc_info()[2]       #traceback
        #print("  fout op regel: %d" % tb.tb_lineno)
        #print("  in bestand: %s" % tb.tb_frame.f_code.co_filename)
        
    except ZeroDivisionError:
        print('Delen door 0 mag niet!')
    print('klaar')

def lijst():
    print('Een lijst')
    lst = [23, 2, 5, -11, 4]
    print(lst)
    print('len =', len(lst))
    idx = int(input('Geef indexnr van item: '))
    print(lst[idx])

def lijst_ex():
    print('Een lijst, met exception handling')
    lst = [23, 2, 5, -11, 4]
    print(lst)
    print('len =', len(lst))
    try:
        idx = int(input('Geef indexnr van item: '))
        print(lst[idx])
    except (ValueError,IndexError) as ex:
        print(ex)
        return
    else:
        print('  geen fout opgetreden')
    finally:
        print('  tenslotte')
    print('klaar')

def bereken(a,b, optor):
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
    a = 4
    b = 3
    try:
        c = bereken(a, b, "**")
        print("c =", c)
    except ValueError as ex:
        print(ex)
    print("Klaar.")


#--- script ---

#delen()
#delen_ex()
#lijst()
#lijst_ex()
test_bereken_ex()

