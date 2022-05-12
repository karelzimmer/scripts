# generator functions; eigen variant van range

"""
yield expression: (yield "Kwik")     officieel
yield statement:  yield "Kwek"       mag vaak ook
fout: print(yield)                   eist yield expr
goed: print((yield))                 bevat (yield ..)


"""

import random


def namen_simpel():
    yield "Kwik"            #yield statement
    (yield "Kwek")          #yield expression
    yield "Kwak"
    return "Donald"         #wordt StopIteration: Donald
    # ex.args[0] == ex.value = "Donald"; alleen StopIteration heeft .value
    # als je geen return stmt hebt, maar wel te vaak next(gen) doet,
    # geeft hij een StopIteration met .value=None
    # print(ex) wordt dan: StopIteration, ipv StopIteration: Donald

def namen_print():
    print("  namen_print, start")
    yield "Kwik"            #yield statement
    print("  namen_print, na 1e yield")
    yield "Kwek"
    print("  namen_print, na 2e yield")
    yield "Kwak"
    print("  namen_print, na 3e yield")
    #return "Donald"         #wordt StopIteration: Donald

def getnaam():
    return "Kwak"
    #yield "Kwak"
    #return "K"             #deze en vlg altijd goed, want str is iterable
    #yield "K"               #ook met 1 of 0 letters ""
    #return 42
    #yield 42
    
def namen2():
    yield "Kwik"
    yield "Kwek"

    yield getnaam()
    # als: return "Kwak"/42 ->hier: yield "Kwak" of 42
    # als: yield "Kwak"/42  ->hier: yield <generator-obj getnaam>

    #yield from getnaam()
    # als: return "Kwak"    ->hier: yield "K", yield "w", enz
    # als: return 42        ->hier: TypeError, 'int' object is not iterable
    # als: yield "Kwak"/42  ->hier: yield "Kwak" of 42

    #val = yield from getnaam()
    #print("  namen2, val =",val)

    return "Donald"         #wordt StopIteration: Donald

def namen3(stop=10):
    lst = ["Anton", "Beatrix", "Dirk", "Elly", "Harald", "Iris", "Koos", "Marie", "Otto", "Ria"]
    for _ in range(stop):
        yield random.choice(lst)

# 2 eigen varianten van range()
def reeks1(maxwaarde):
    num = 0
    while num < maxwaarde:
        yield num
        num += 1

def reeks2(*args):
    stap = 1
    if len(args) == 0 or len(args) > 3:
        return None
    elif len(args) == 1:
        van = 0
        tot = args[0]
    elif len(args) == 2:
        van = args[0]
        tot = args[1]
    elif len(args) == 3:
        van = args[0]
        tot = args[1]
        if args[2] != 0:
            stap = args[2]
    
    num = van
    if stap > 0:
        while num < tot:
            yield num
            num += stap
    else:
        while num > tot:
            yield num
            num += stap

def reekstuple(maxval = 5):
    if maxval < 1 or maxval > 10:
        maxval = 5
    c = 0
    while c < maxval:
        yield chr(c+65), c      #tuple
        c += 1

# vlg komt oorspr uit de help, aangepast
def accumulate_return():
    print("  accumulate_return, start")
    tally = 0
    while True:
        val = yield     #yield bevat val uit acc.send(val), ret None
        print("  accumulate_return, while, val =", val)
        if val is None:
            print("  accumulate_return, voor return tally =", tally)
            return tally    #->normaal StopIteration, maar okee bij yield from
        tally += val

def accumulate_yield():
    print("  accumulate_yield, start")
    tally = 0
    while True:
        val = yield
        print("  accumulate_yield, while, val =", val)
        if val is None:
            print("  accumulate_yield, voor yield tally =", tally)
            yield tally
        else:
            tally += val

# vlg yield from stuurt alle acc.send(val)'s v hfdprog door naar accumulate,
# totdat die een return retval doet; dat gebeurt als hfdprog acc.send(None)
# doet [willekeurige marker, had ook acc.send("sommeer") kunnen zijn]
# ->die retval komt in tally, vandaar in globale list tallies
def gather_tallies(tallies):
    print("gather_tallies, start")
    #yield "**gather start**"
    while True:
        print("gather_tallies, begin while")
        tally = yield from accumulate_return()
        print("gather_tallies, na yield from, tally=", tally)
        tallies.append(tally)
        #yield tally       #alleen doen als ik in hfdprog next(acc) doe

# zonder yield from moet je zelf de .send(..) doorsturen; als hfdprog None
# meegeeft ->None naar accumulate ->return int ->komt in StopIteration error
# ->moet ik afvangen...
def gather_tallies_StopIteration(tallies):
    print("gather_tallies_StopIteration, start")
    while True:
        print("gather_tallies_StopIteration, begin while")
        accu = accumulate_return()
        next(accu)
        while True:
            try:
                val = yield
                accu.send(val)
            except StopIteration as ex:
                #tally = ex.args[0]      #->int, bevat retval uit accumulate
                tally = ex.value            #->int
                print("gather_tallies_StopIteration, in sub-while, tally=", tally)
                tallies.append(tally)
                #yield tally
                break

def gather_tallies2(tallies):
    print("gather_tallies2, start")
    while True:
        print("gather_tallies2, begin while")
        accu = accumulate_yield()
        next(accu)
        while True:
            val = yield
            accu.send(val)
            if val is None:
                next(accu)              #deze geeft None, weet niet waarom
                tally = next(accu)      #goed
                print("gather_tallies2, in sub-while, tally=", tally)
                tallies.append(tally)
                #yield tally
                break

def echo():
    print("  echo, start")              #wordt gedraaid na 1e next(gen)
    val = -1          #vereist bij: val = yield val, anders ref before assignment
    # next(gen) is equivalent aan gen.send(None)
    # de eerste next(gen) geeft deze -1 terug
    # hij begint met: (yield val) en blijft meteen daarna wachten, dus
    # midden in: val = (yield val) + 100
    # als daarna gen.send(1) komt, doet ie eerst: val = 1 + 100 = 101,
    # en daarna weer (yield val), dwz yield 101, en wacht dan weer
    # doet hfdprog echter next(gen) of gen.send(None),
    # dan krijg je: val = None + 100 ->TypeError

    #yield "**echo start**"
    while True:
        #print("  echo, while met yield expr:", (yield))      #goed
        # vor goed, maar eist (yield) ipv yield
        #print("  echo, while met yield expr:", (yield 101))   #goed

        print("  echo, while voor yield, val:", val)
        #val = yield val             #goed
        val = (yield val) + 100      #val wordt 100, 101, enz; dit ook teruggegeven
        # hij doet dus eerst: val = [in:yield] + 100
        # daarna: out:yield val [val bevat nu 101, 102, enz]
        # en wacht dan op volgende send(..) of next(gen)
        print("  echo, while na yield, val:", val)

def echo2():
    print("  echo2, start")              #wordt gedraaid na 1e next(gen)
    while True:
        #print("  echo, while met yield expr:", (yield))      #goed
        # vor goed, maar eist (yield) ipv yield
        #print("  echo, while met yield expr:", (yield 101))   #goed

        #val = yield             #doet: yield None  ->gen.send(i) ret None
        val = yield -1
        print("  echo2, na 1e yield, val:", val)
        if val is None:
            val = -2
        yield val + 100
        print("  echo2, na 2e yield, val:", val)
    

#--- script functies ---


def test_namen_simpel():
    for n in namen_simpel():
        print(n, end=' ')       #Kwik kwek Kwak
    print()
    print(namen_simpel)         #<function namen_simpel at 0x020414B0>
    print(namen_simpel())       #<generator object namen_simpel at 0x0203EDC8>
    print(*namen_simpel())             #Kwik kwek Kwak

def test_namen_print():
    gen = namen_print()
    for n in gen:
        print(n)       #Kwik kwek Kwak

    try:    
        next(gen)
    except StopIteration as ex:
        print(ex)
        print(ex.value)         #None of str Donald

def test_namen_next():
    gen = namen_simpel()
    #gen = namen_print()
    print(gen)                  #generator object

    print("test_namen_next, voor 1e next(gen)")
    print(next(gen))
    print("test_namen_next, voor 2e next(gen)")
    print(next(gen))
    print("test_namen_next, voor 3e next(gen)")
    print(next(gen))
    
    #print(next(gen))           #error: StopIteration of StopIteration: Donald

def test_generator_for():
    for n in namen2():
    #for n in namen3(5):         #max 5 namen
        print(n, type(n))
        #print(*n)

def test_list_iter():
    lst = [1,2,3,4,5]
    print(lst)                  #[1, 2, 3, 4, 5]
    print(*lst)                 #1 2 3 4 5
    for i in lst:
        print(i, end=' - ')
    print()
    #print(next(lst))           #TypeError: 'list' object is not an iterator

    it = iter(lst)
    print(it)                   #<list_iterator object at 0x02013DF0>
    print(next(it))             #1
    print(next(it))             #2
    print(next(it))

    it = reversed(lst)          #wordt iterator; sorted(lst) wordt list
    print(it)                   #<list_reverseiterator object at 0x02053DD0>
    print(next(it))             #5
    print(next(it))             #4
    print(next(it))
    
def test_reeks1():
    print(reeks1)               #<function reeks1 at 0x02A5BE40>
    print([reeks1(7)])          #[<generator object reeks1 at 0x02A5F630>]
    print([range(7)])           #[range(0, 7)]

    print(list(range(7)))       #[0, 1, 2, 3, 4, 5, 6]
    print(list(reeks1(8)))      #[0, 1, 2, 3, 4, 5, 6, 7]
    
    for i in reeks1(5):
        print(i, end=' ')       #0 1 2 3 4 
    print()
    print(*reeks1(6))

def test_reeks1_next():
    #r = iter(reeks1(3))
    r = reeks1(3)               #werkt ook zonder iter(), want yield geeft al iterable
    print("r:",r)
    print(next(r))
    print(next(r))
    print(next(r))
    #print(next(r))          #StopIteration error

    print(next(reeks1(6)))      #0
    print(next(reeks1(6)))      #0
    print(next(reeks1(6)))      #0

def test_reeks2():
    #lst = list(range(1, 8, 0))  #ValueError: range() arg 3 must not be zero
    #print(lst)

    for i in reeks2():
        print(i, end=' ')       #niets
    print()

    for i in reeks2(4):
        print(i, end=' ')       #0 1 2 3 
    print()

    for i in reeks2(1, 9):
        print(i, end=' ')       #1 2 3 4 5 6 7 8 
    print()

    for i in reeks2(1, 9, 2):
        print(i, end=' ')       #1 3 5 7 
    print()

    for i in reeks2(1, 9, -2):
        print(i, end=' ')       #niets
    print()

    for i in reeks2(9, 1, -2):
        print(i, end=' ')       #9 7 5 3 
    print()

    for i in reeks2(0.0, 5.0, 0.5):
        print(i, end=' ')       #0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5
    print()

def test_reekstuple():
    #for k,v in reekstuple(5):
    #    print(k,v)
    for t in reekstuple(5):
        print(t)

def test_accumulate_send():
    tallies = []
    #acc = gather_tallies(tallies)
    #acc = gather_tallies_StopIteration(tallies)
    acc = gather_tallies2(tallies)
    print(acc)      #<generator object gather_tallies at 0x01F420F0>

    print("test, voor 1e next(acc)")
    print(next(acc))               #moet om generator te starten,
    # anders TypeError: can't send non-None value to a just-started generator
    #acc.send(None)          #kan ook ipv next(acc)

    print("test, voor 1e lus acc.send(i)")
    for i in range(1,4):
        acc.send(i)         #->None
        #print(acc.send(i))
    print("test, doe acc.send(None)")
    acc.send(None)          #marker voor accumulate; of bv: send("sommeer") 
    #print("test, doe next(acc)")
    #print(next(acc))       #alleen doen als onderin while staat: yield tally
    print("test, tallies:", tallies)

    print("test, voor 2e lus acc.send(i)")
    for i in range(1,5):
        acc.send(i)
    print("test, doe acc.send(None)")
    acc.send(None)
    print("test, tallies:", tallies)

    print("test, voor 2 losse acc.send(..)")
    #acc.close()            #kan na deze geen acc.send(..) meer doen
    acc.send(15)
    acc.send(23)
    print("test, doe acc.send(None)")
    acc.send(None)
    print("test, tallies:", tallies)

def test_echo():
    print("test_echo, start")
    gen = echo()            #mkt generator-wrapper rond echo; echo wordt NIET gedraaid
    print("test_echo, voor next(gen)")
    print(next(gen))        #goed, draait echo() t/m eerste yield
    #gen.send(None)         #ook goed
    print("test_echo, na next(gen)")

    for i in range(1,5):
        #print("test_echo, i =", i, ", na gen.send(i) =", gen.send(i))
        print("test_echo, i =", i, ", na next(gen) =", next(gen))

def test_echo2():
    print("test_echo2, start")
    gen = echo2()
    print("test_echo2, voor next(gen)")
    print(next(gen))
    print("test_echo2, na next(gen)")

    for i in range(1,5):
        print("test_echo2, i =", i, ", na gen.send(i) =", gen.send(i))
        print("test_echo2, i =", i, ", na next(gen) =", next(gen))


#--- script ---

test_namen_simpel()
#test_namen_print()
#test_namen_next()
#test_generator_for()

#test_list_iter()

#test_reeks1()
#test_reeks1_next()
#test_reeks2()
#test_reekstuple()

#test_accumulate_send()
#test_echo()
#test_echo2()

