# callable class en geneste fn's met closures

import functools as fun
import random

class BingoBox:
    """Class: haalt random waarde uit meegegeven items"""
    
    def __init__(self, items):
        self._items = list(items)       #items mag willek iterable zijn
        random.shuffle(self._items)

    def pick(self):
        return self._items.pop()        #laatste item

    def __call__(self):         #class als callable function
        return self.pick()

    def show_list(self):
        return self._items

def maak_bingo2(items):
    """Fn: haalt random waarde uit meegegeven items"""
    _items = list(items)
    random.shuffle(_items)

    def pick():
        return _items.pop()
    return pick

def maak_som(start = 0):
    tot = start           #closure, kan rechtstreeks met start (zie hieronder)

    def som(x):
        nonlocal tot        #Python3
        tot += x
        return tot
    return som

def maak_som2(start = 0):
    def som(x):
        nonlocal start
        start += x
        return start
    return som

def maak_verhoog(a):
    def verhoog(getal):
        return getal + a
    return verhoog


def memo(fn):                   #wordt decorator
    #print("dit is memo")       #wordt 1 keer gedraaid, bij @memo1-decl
    #return fn
    @fun.wraps(fn)              #handig voor __name__, __doc__
    def wrapper(*args):
        """fn wrapper"""
        print("--boodschap voor %s--" % args[0])
        return fn(*args)
    return wrapper

@memo                       #printGroet is niet langer de naam vd fn,
def printGroet(nm):         #maar de naam v wrapper rond fn
    """fn printGroet"""
    print('Hallo', nm)

def printGroet2(nm):
    """fn printGroet2"""
    print('Hoi', nm)

# zo werkt een decorator echt: 
printGroet2 = memo(printGroet2)     #dwz de wrapper krijgt de naam printGroet2


#--- script functies ---

def test_Bingo():
    print("bingo")
    bingo = BingoBox(range(3))      #3 items in lijst ->kan 3* .pick() doen
    #print(bingo)                    #<__main__.BingoBox object at 0x02D60DD0>
    #print(callable(BingoBox))       #True
    #print(callable(bingo))          #True

    print(bingo.show_list())
            
    print(bingo.pick())
    print(bingo())                  #doet __call__(); die doet .pick()
    print(bingo.__call__())
    # nu is de meegegeven lijst leeg ->vlg geeft error
    #print(bingo())                  #IndexError: pop from empty list
    
    print("\nbingo2")
    bingo2 = maak_bingo2([3,5,6,22,-2,9])
    #print(bingo2)               #<function maak_bingo2.<locals>.pick at 0x01FF7A98>
    #print(callable(bingo2))     #True
    for _ in range(3):
        print(bingo2())

def test_maak_som():
    print("maak_som")           #running sum vanaf opgegeven startwaarde
    totaal = maak_som(0)           #->fnptr naar som(); arg: startwaarde

    #print(totaal)               #<function maak_som.<locals>.som at 0x01FC7930>
    print(totaal(3))                #3
    print(totaal(5))                #8
    print(totaal(6))                #14
    print(totaal(7))                #21

    uitkomst = maak_som(0)(9)          #doet eerst maak_som(0)->som(), daarna som(9)
    print(uitkomst)                 #9
    # let op: de vorige tot van de eerste maak_som(0) is nog steeds bewaard!
    print(totaal(6))                #27

    print("\nmaak_som2")
    totaal2 = maak_som2(10)         #running sum vanaf 10
    print(totaal2(4))               #14
    print(totaal2(5))               #19
    print(maak_som2(100)(9))        #109
    print(totaal2(2))               #21

def test_maak_som_info():
    global totaal               #voor analyse in shell
    totaal = maak_som(0)
    print(totaal.__code__.co_stacksize)     #2
    print(totaal.__code__.co_nlocals)       #1 [=number of locals]
    print(totaal.__code__.co_varnames)      #('x',)
    print(totaal.__code__.co_freevars)      #('tot',)
    print(totaal.__code__.co_name)          #som
    #totaal.__code__.co_code            b'\x88\x00\x00|\x00\x007\x89\x00\x00\x88\x00\x00S'
    #dir(totaal.__code__) ->namen v alle __code__ props

def test_maak_verhoog():
    print("maak_verhoog")
    fn = maak_verhoog(2)        #verhoog arg met 2
    #print(fn)
    print(fn(5))                #7
    print(fn(0))                #2
    print(maak_verhoog(3)(5))   #8
    print(fn(4))                #6

def test_decorator():
    print("Test met printGroet:")
    printGroet('Marie')
    printGroet('Klaas')

    # vlg testen zonder en met @fun.wraps
    print(printGroet.__name__)    #zonder @fun.wraps: wrapper; met: printGroet
    print(printGroet.__doc__)     #zonder: 'fn wrapper'; met: 'fn printGroet'

    print("\nTest met printGroet2:")
    printGroet2("Willem")
    print(printGroet2.__name__)    #zonder @fun.wraps: wrapper; met: printGroet2
    print(printGroet2.__doc__)     #zonder: 'fn wrapper'; met: 'fn printGroet2'

def test_decorator_info():
    pass

#--- script ---

#test_Bingo()
#test_maak_som()
#test_maak_som_info()
#test_maak_verhoog()

test_decorator()

