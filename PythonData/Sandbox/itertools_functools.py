# itertools, functools, operator

"""
decorators: closure_decorator.py
@property:  bankaccount_techno.py

@fun.lru_cache(maxsize=128, typed=False)
@fun.total_ordering
  vor boven class def met __eq__() en bv __lt__() ->hij mkt andere cmp fn's
@fun.singledispatch(default)
  vor overloads voor 1e arg
@fun.wraps(fn)          in decorator
"""

import operator
import itertools as itt
import functools as fun

def itt_dotproduct_tee():
    #dot prod v 2 vectoren:
    a = [4,3,6,5]
    b = [1,1,2,2]

    print(a)
    print(b)
    dotprod = sum(map(operator.mul, a, b))
    print('dotprod:', dotprod, '\n')

    c = list(map(operator.mul, a, b))
    for x in c: print(x, end=' ')
    print('\nsum:', sum(c), '\n')         #idem, dotprod

    it = map(operator.mul, a, b)         #wordt iterator (map-obj)
    # je kan iter maar 1* draaien, geen reset
    # ->hetzij items tonen, hetzij sum, hetzij list(map(..)) doen
    # tee() mkt gekoppelde iters; de 1e haalt waarde op, de 2e gebr kopie vd waarde
    # efficienter om gewoon list(..) te gebr
    it1, it2 = itt.tee(it)           #n=2; mag org iterator niet hergebruiken
    #print(it1)                      #itertools._tee object
    for x in it1: print(x, end=' ')
    print('\nsum:', sum(it2))

    
def itt_count_enz():
    # vlg eindeloze counters
    print('count():')
    it = itt.count(10)         #start,step; telt oneindig door
    print(next(it))            #10
    print(next(it))            #11
    print(next(it))            #12
    it = itt.count(100, 5)
    for i in itt.takewhile(lambda x : x <= 120, it):
        print(i, end=' ')

    print('\n\ncycle():')
    it = itt.cycle('abc')
    #it = itt.cycle((5,8,2,1))
    for i in range(6):
        print(next(it), end=' ')     #a b c a b c

    print('\n\nrepeat():')
    it = itt.repeat(6, 3)        #herhaal de 6 3 keer; bij geen aantal ->oneindig
    for i in it: print(i, end=' ')      #6 6 6
    print()

    org = ['a','b','c','d','e']
    lst = [x+'1' for x in org]
    print(lst)
    # vlg zeer ingewikkeld:
    lst = list(map(lambda a,b: a+b, org, itt.repeat('1')))
    print(lst)          #['a1', 'b1', 'c1', 'd1', 'e1']

    print('\naccumulate():')
    lst = [1,2,3,4,5,6]
    for i in itt.accumulate(lst):      #dflt operator.add, eist 2 args
    #for i in itt.accumulate(lst, operator.mul):
        print(i, end=' ')       #1 3 6 10 15 21

    print('\n\nchain():')
    for i in itt.chain([9,8,7], range(5)):      #keten v iterables
        print(i, end=' ')       #9 8 7 0 1 2 3 4

    print('\n\ncompress():')
    # item uit 1e tonen als corresp item uit 2e True is
    for i in itt.compress('abcde',[1,0,1,1,0]):
    #for i in itt.compress(range(5),[1,0,1,1,0]):
        print(i, end=' ')           #a c d

    print('\n\nislice():')
    print(type(org[0:2]))       #list
    print(org[0:2])
    for i in itt.islice(org, 0,2):      #,step; iter; args niet < 0
        print(i, end=' ')
    print()

def itt_filter_enz():
    lst = [1,4,6,4,1,3,8]

    print('\ndropwhile():')
    it = itt.dropwhile(lambda x : x < 5, lst)
    for i in it: print(i, end=' ')  #zolang i<5 ->overslaan, daarna alles tonen

    print('\n\ntakewhile():')
    it = itt.takewhile(lambda x : x < 5, lst)
    for i in it: print(i, end=' ')  #zolang i<5 ->tonen, rest overslaan

    print('\n\nfilterfalse():')
    it = itt.filterfalse(lambda x : x < 5, lst)     #omgekeerd filter
    for i in it: print(i, end=' ')  #als i<5 ->overslaan

    print('\n\ngroupby():')
    # vlg hoeft niet gesorteerd (wel beter), doet groep per aansluitend blok
    # ik sorteer op 1e letter ->blok 2 a's, 1 d, 1 a, 2 b's, enz
    org = ['appel','aardbei','kers','aardappel','druif','banaan','boter','kiwi','peer','pruim']
    print(org)
    # vlg geeft iterator v tupels (key,subiterator)
    for key,it in itt.groupby(org, lambda x : x[0]):      #sortkey, x->str
        print('\n', key, end=': ')
        for i in it: print(i, end=' ')

    print('\n\nstarmap():')
    lst = list(map(lambda a,b : a ** b, [2,3,10],[5,2,2]))
    print(lst)
    lst = list(itt.starmap(pow, [(2,5),(3,2),(10,2)]))  #of: operator.pow
    print(lst)              #doet 2**5, 3**2, 10**2

    print('\n\nziplongest():')
    it = zip([2,3,10,8,8],[5,2,2])         #doet kortste
    for i in it: print(i, end=', ')
    print()
    it = itt.zip_longest([2,3,10,8,8],[5,2,2], fillvalue=-1)   #vult kortste aan
    for i in it: print(i, end=', ')
    print()    

def itt_combinations():
    print('product():')
    lst = [i+j for i in 'ABCD' for j in 'xy']   #of: [(i,j) for...]
    print(lst)
    lst = list(itt.product('ABCD','xy'))        #cart prod met tupels
    print(lst)          #[('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), enz]
    it = itt.product(range(2), repeat=3)        #repeat=2|3; combineer 0,1 met 0,1, met 0,1 enz
    for i in it: print(i, end=' ')

    print('\n\nproduct(), permutations(), combinations()')
    # vlg wel dubbele ('A','A') enz; wel ('B','A') naast ('A','B') enz
    print(list(itt.product('ABCD', repeat=2)))
    # vlg geen dubbele ('A','A'); wel ('B','A') naast ('A','B')
    print('\n', list(itt.permutations('ABCD', r=2)))      #of: r=2

    # vlg wel dubbelen; geen ('B','A') naast ('A','B')
    print('\n', list(itt.combinations_with_replacement('ABCD', 2)))
    # vlg geen dubbelen; geen ('B','A') naast ('A','B')
    print('\n', list(itt.combinations('ABCD', 2)))
    
#---

def fun_reduce():
    print("reduce():")
    lst = [2,3,10,8,8]
    print(lst)
    print(sum(lst))         #31
    x = fun.reduce(operator.add, lst)       #,initializer
    print("sum:", x)                #31
    x = fun.reduce(operator.mul, lst)       #,initializer
    print("mul:", x)                #31

def fun_partial():
    print("partial():")
    fn = lambda x,y : x - y
    #dec = fun.partial(fn, 1)        #1e arg wordt 1
    dec = fun.partial(fn, y=1)      #2e arg wordt 1
    # nwmethod = fun.partialmethod(method, arg1)
    a = 5
    print(fn(a,1))          #std 4, want 5 - 1
    print(dec(a))           #std -4, want 1 - 5

    print(dec)
    print()
    print(dec.func, dec.args, dec.keywords, sep='\n')
    print()
    
    binint = fun.partial(int, base=2)
    print(binint.args, binint.keywords)   #() {'base': 2}
    print(binint('01001001'))               #73

def fun_cache_fib():
    from time import perf_counter as timer
    
    M = 26
    # met M=26 ->0.81 zonder cache
    # 0.00017 met cache maxsize=4, 0.00015 met maxsize=None
    t = timer()
    x = [fib(n) for n in range(M+1)]
    t = timer() - t
    print("tijd:", t)
    print(x)

    print(fib.cache_info())     #CacheInfo(hits=50, misses=27, maxsize=4, currsize=4)
    #fib.cache_clear()

# vlg maxsize=4 bijna even snel als =None; =0 ->trager dan zonder decorator!
# Python 3.8 heeft ook @fun.cache zonder args
@fun.lru_cache(maxsize=4)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def fun_overloads():
    #print(trekaf.registry)            #->dict met key=class, value=fn-obj
    #print(trekaf.dispatch(int))       #->de fn(arg->object) variant

    #x = trekaf(7, 5)
    #x = trekaf(7, 5.2)
    #x = trekaf(True, False)           #1

    x = trekaf([1,2,3,4,5],[2,3,6])
    #x = trekaf((1,2,3,4,5),(2,3,6))
    #x = trekaf([1,2,3],(2,))            #goed, list-tuple
    #x = trekaf([1,2,3],2)            #TypeError. int not iterable

    #x = trekaf('appeltaart', 'taart')
    #x = trekaf('taart', 'taart')
    #x = trekaf('taartina Mina', 'taart')
    #x = trekaf('taartina Mina', 'taart', False)
    print(x, type(x))

@fun.singledispatch         #registreer trekaf() voor 1e arg v type object
def trekaf(a, b):           #fn voor alle types, behalve specifiek geregistreerde
    return a - b

@trekaf.register(list)      #kijkt alleen naar type 1e arg
@trekaf.register(tuple)     #mag meerdere register-decl
def _(a, b):
    return list(set(a)-set(b))      #volgorde willek vanwege set()

@trekaf.register(str)       #we hopen maar dat 2e arg ook str is...
def _(a, b, end=True):      #willek fnnaam, maar NIET trekaf
    if not end:
        return a.replace(b,'')
    else:
        if a.endswith(b):
            return a[0:a.rfind(b)]
        else:
            return a


#---script ---

#itt_dotproduct_tee()
#itt_count_enz()
#itt_filter_enz()
#itt_combinations()

#fun_reduce()
fun_partial()
#fun_cache_fib()
#fun_overloads()

