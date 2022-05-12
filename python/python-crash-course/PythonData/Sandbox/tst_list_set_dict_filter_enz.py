#oefeningen met range(), list, set, dict, lambda, enz
#timing kan je testen met import time, doe ik hier niet
#collections.namedtuple in filehandling.py


def toonTafelVan10():
    for i in range(1,11):
        print('%2d maal 10 is %3d' % (i, i*10))
    print()

def toonTafelVanX(getal):
    for i in range(1,11):
        print('%2d maal %d is %3d' % (i, getal, i*getal))
    print()

def toonTafelVanXDefault(getal=10):
    for i in range(1,11):
        print('%2d maal %d is %3d' % (i, getal, i*getal))
    print()

def test_range():
    print('ranges:')        #range(..) eist integers
    for a in range(5):      #let op: a wordt module variabele!
        #print(a)
        print(a, end=' ')
    print()
    #print(a)           #goed ->a heeft local scope; block scope bestaat niet

    for a in range(1,6):
        print(a, end=' ')
    print()

    for a in range(2,22,2):
        print(a, end=' ')
    print()

    for a in range(10,4,-1):    #10 9 8 7 6 5
        print(a, end=' ')
    print()

    #for a in range(2.5,11):    #TypeError: mag geen float zijn
    #    print(a, end=' ')

def test_range_continue_break():
    print('\nrange met continue:')
    for a in range(5):
        if a == 3:
            continue        #dwz sla 3 over
        print(a)
    print()

    print('range met break en else:')
    for b in range(15):
        if b == 7:         # b == 7
            break
        print(b)
    else:       #alleen doen als geen break
        print('  niet afgebroken; b=', b)
    print()


def test_list_for_basis():
    lst = [45, 55, 6, -2, 0, 9]
    print(lst)
    for a in lst:
        print(a)
        #print(a, end=' ')
    print()         #nieuwe regel
    
    lst = ["appel", "peer", "kiwi", "banaan"]
    for a in lst:
        print(a, end=' ')
    print()

    lst = [42, "Monty", True, 3.14]
    for a in lst:
        print(a, end=' ')
    print()

    lst = [42, "Monty", lambda x : x * x]
    for a in lst:
        print(a, end=' ')
    print()

    lst = [lambda x,y : x+y, lambda x,y : x-y, lambda x,y : x*y,
      lambda x,y : x/y]
    for a in lst:
        print(a(9,3), end=' ')
    print()

def test_list_loop():
    print('\nlist met for-loop:')
    fruit = ["peer", "citroen", "appel", "banaan", "sinaasappel", "kiwi"]
    for f in fruit:
        print(f)

    #vlg regel: enumerate(..) geeft tupels terug: (teller,item_uit_list)
    #i,f zijn samen tupel; mag dus: for (i,j) in ..., of: for i,j in ...
    print('\nenumerate(), 3 manieren:')
    for (i,f) in enumerate(fruit):
        print(i, f)
        #if f.startswith('c'): del fruit[i]      #goed
        # vor toont geen appel, want appel schuift naar voren,
        # wordt nwe item1 en die hebben we al gehad
    print()

    for i,f in enumerate(fruit, start=1):
        print(i, f)
    print()
    
    for t in enumerate(fruit, start=1):
        print(t)                        #hier rechtstreeks tupel afdrukken

    print('\ntellen met range():')
    for i in range(len(fruit)):
        print(i, fruit[i])

    print('\nachterstevoren met range():')
    for i in range(len(fruit)-1, -1, -1):
        print(i, fruit[i])

    print('\nachterstevoren met slice:')
    print(fruit[::-1])
    for f in fruit[::-1]:
        print(f)

    print('\nachterstevoren met reversed():')
    for f in reversed(fruit):           #iterable
        print(f)

    fruit.reverse()                     #wijz org list
    print(fruit)

def test_list_iterator():
    print('\nlist met iterator en next():')
    it = iter([5,6,7])
    print(it)               #<list_iterator object at 0x02004E30>
    #print(it[0])           #error
    print(next(it))         #zonder iter() werkt next() niet; wel bij yield
    print(next(it))
    print(next(it))
    #print(next(it))         #error: StopIteration, want geen items meer

    #for i in it: print(i)      #kan ook
    #na gebruik is een iterator 'op', kan niet worden hergebruikt
    #zie ook import itertools

def test_list_basis():
    print('\nlist met is en ==:')
    la = [1,2,3]
    lb = la
    lc = [1,2,3]
    print(la)
    print(lb)
    print(lc)
    print()
    
    # is -> identiteit; == -> equivalentie (gelijke waarden)
    print(la is lb)         #True
    print(la == lb)         #True
    print(la is lc)         #False
    print(la == lc)         #True
    print(id(la), id(lb), id(lc))

    #ld = list(la)           #kopie
    ld = la.copy()          #idem, vanaf 3.3
    #ld = la[:]              #idem, volledige slice
    print(ld)
    print(id(la), id(ld))

    print('\nna la[0] = 366:')
    la[0] = 366
    print(la[0])
    print(la[1])
    print(la[2])
    print(la)
    print(lb)
    print(lc)

    lb = la * 2
    lb[0] = 367
    print(id(la), id(lb))
    print(la)
    print(lb)

def test_list_append_enz():
    print('\nlist met append/insert enz:')
    la = [1,2,3]
    la.append(-100)
    la.insert(1, 444)
    la.append(444)
    print(la)
    la.remove(444)           #wis 1e item met waarde 444, retval None
    #la.remove(25)            #ValueError: list.remove(x): x not in list
    #la.discard(2)           #AttributeError: niet in list, wel in set
    print(la)
    del la[1]               #wis item[1]
    #del la[128]             #IndexError, idx bestaat niet
    print(la.pop())         #toon en wis laatste item, is: .pop(-1)
    print(la)

    la += [11,12,13]        #list toevoegen aan einde la
    la.extend([14,15])
    la += [-4]              #list v 1 item toevoegen aan la
    la.extend([-5])         #idem
    la[len(la):] = [-6,-7]  #list toevoegen aan "bereik" einde v la
    la[:0] = [-51,-52]      #list vooraan toevoegen, kan ook met la[0:0]
    print(la)
    #la[2] = [-201,-202,-203,-204]   #dit wordt een list binnen een list
    #la[2:] = [-201,-202,-203,-204]      #gooit rest v list la weg
    la[2:2] = [-201,-202,-203,-204]     #insert nwe list op pos 2
    #la += 777               #TypeError: 'int' object is not iterable
    print(la)

    print(la[-3:])          #vanaf item[-3] t/m laatste
    print(la[-3:-1])        #vanaf item[-3] tot laatste
    print(la[:-3])          #vanaf begin tot item[-3]

def test_list_unpack():
    print('\nlist uitpakken:')
    lst = [1,2,3,4,5]
    p,q,r,s,t = lst              #unpacking
    #p,q,r,s = lst                #ValueError: too many values to unpack
    #p,q,r,s,t,u = lst            #ValueError: not enough values to unpack
    print('lst uitpakken: p=%d, q=%d, r=%d, s=%d, t=%d' % (p,q,r,s,t))
    p,q,*r = lst
    print('lst uitpakken: p=%d, q=%d, r=%s' % (p,q,r))
    p,*q,r,s = lst
    print('lst uitpakken: p=%d, q=%s, r=%d, s=%d' % (p,q,r,s))

def test_list_min_max_enz():
    print('\nlist met min, max, sum:')
    lst = [12,2,73,41,5]
    #vlg regel re tupel aan li tupel toekennen
    som, mini, maxi = sum(lst), min(lst), max(lst)
    print(lst)
    print('som=%d, min=%d, max=%d' % (som, mini, maxi))

def test_list_slice():
    lst = [1,2,3,4,5,6,7,8]
    print(lst)
    print(lst[2:5])
    slc = slice(3,6)        #slice-obj
    #slc = [3:6]             #error, invalid syntax
    print(lst[slc])
    slc = slice(1,6,2)      #stap 2
    print(lst[slc])
    #print(lst[[4,1]])      #error; wel goed in numpy

def test_tupels():
    print('\ntupels:')
    ta = (11,12,13)         #tupel
    tb = ta
    #tc = tuple(ta)          #maakt GEEN kopie, anders dan bij list
    #tc = ta.copy()         #error, .copy() bestaat niet
    tc = ta[:]              #goed, maakt ook geen kopie
    td = ta[:2]             #goed, nwe tupel
    print(ta)
    print(tb)
    print(tc)
    print(td)
    print(ta is tb)         #True
    print(ta == tb)         #True
    print(ta is tc)         #True
    print(ta == tc)         #True
    print(id(ta), id(tb), id(tc), id(td))

    te = 21,22,23           #ook een tupel
    print(te)
    tf = (31)               #geen tupel
    print(tf)
    tg = 41,                #wel een tupel, mag met: (41,) of: 41,
    print(tg)
    print(ta[0])
    #ta[0] = 511           #TypeError: kan tupel niet wijzigen
    for a in ta:
        print(a, end=' ')
    print()

def test_list_sort_search():
    import bisect           #binary search ->insertion point new value
    
    print('\nlist sorteren en afdrukken:')
    fruit = ["peer", "citroen", "appel", "banaan", "sinaasappel", "kiwi"]
    print(fruit)
    print(sorted(fruit))        #sorted(..) mkt een gesorteerde kopie

    zuivel = ('melk', 'boter', 'yoghurt', 'kwark')
    print(zuivel)
    print(sorted(zuivel))

    #fruit2 = fruit.copy()   #shallow copy, vanaf 3.3
    fruit2 = list(fruit)     #idem, ook oude versies
    fruit2.sort()
    print(fruit)
    print(fruit2)
    print('"braam" insert pos bisect_left: %d' % bisect.bisect_left(fruit2,"braam"))
    print('"braam" insert pos bisect_right: %d' % bisect.bisect_right(fruit2,"braam"))
    print('"banaan" insert pos bisect_left: %d' % bisect.bisect_left(fruit2,"banaan"))
    print('"banaan" insert pos bisect_right: %d' % bisect.bisect_right(fruit2,"banaan"))

    #zk = "kiwi"
    zk = "braam"
    idx = bisect.bisect_left(fruit2,zk)
    if idx < len(fruit2) and fruit2[idx] == zk:
        print('"%s" staat op pos %d'% (zk,idx))
    else:
        print('"%s" niet gevonden' % zk)

def test_list_comprehensionexpr_map_filter():
    lst = [4,2,3,8,1,7,5,6]

    print('\ncomprehension expr vs map(lambda, lst):')
    # bij test met timeit is compreh expr 2* zo snel
    lst2 = [x*x for x in lst]       #in range(1,6)
    print(lst2)
    lst2 = list(map(lambda x: x*x, lst))        #map() geeft iterable object, loopt items in lst langs + past fn toe + retouneert item na fn
    # niet [map(..)], want dan krijg je een list met 1 elem, nl iterable
    print(lst2)
    lst2 = [(x,x*x) for x in lst]           #wordt list van tupels, () moeten
    print(lst2)
    print(lst2[0])
    print(lst2[0][1])
   
    print('\ncompr expr + if vs filter(lambda, lst):')
    lst2 = [x for x in lst if x & 1 == 1]     #oneven: x % 2 != 0 of x & 1 == 1
    # if even snel als filter(); geen else, filtert in, dwz geef items die gelden
    print(lst2)
    lst2 = [x if x % 2 != 0 else None for x in lst]
    # vor: .. if .. else .. is deel van output v compr expr; else verplicht
    print(lst2)
    lst2 = list(filter(lambda x: x % 2 != 0, lst))     #filter() geeft oneven getallen
    # vor: lambda is predicate, dwz fn die bool retourneert: True->infilteren
    print(lst2)
    lst2 = [x for x in filter(lambda x: x % 2 != 0, lst)]	#idem, mengvorm
    print(lst2)

    print('\ncompr expr + if vs map(lambda, filter(lambda, lst)):')
    lst2 = [x*x for x in lst if x&1==1]     #oneven
    print(lst2)
    lst2 = list(map(lambda x: x*x, filter(lambda x: x&1==1, lst)))
    print(lst2)

    print('\nfilter() als generator:')
    for x in filter(lambda x: x % 2 == 0, lst):
        print(x, end=' ')
    print()
    
    print('\nflatten een list v lists (of matrix):')
    #lst2 = [item for lst in [['a'],['b'],['c']] for item in lst]
    lst2 = sum([['a'],['b'],['c']],[])		#concat lists -> eist [] als startwaarde ipv default 0
    print(lst2)
    #print(lst)             #oorspr lst onveranderd

def test_generatorexpr():
    f1 = (x*x for x in range(2,5))
    print(f1)               #<generator object>
    f1, f2, f3 = (x*x for x in range(2,5))
    print(f1, f2, f3)       #4 9 16

def test_zip():
    # zip() rijgt elementsgewijs twee of meer lists aan elkaar
    print('\nzip(lst1,lst2), geeft iterable met tuples')
    for x in zip(['Jan', 'Marie', 'Geesje', 'Frits'], [25,22,31,45]):
        print(x)  #wordt: ('Jan',25) ('Marie',22) enz
    for x in zip(['Jan', 'Marie', 'Geesje', 'Frits'], [25,22,31,45], ['a','b','c','d']):
        print(x)  #wordt: ('Jan',25, 'a') ('Marie',22,'b') enz
    # vlg geen error, toont alleen Jan en Marie
    for x in zip(['Jan', 'Marie', 'Geesje', 'Frits'], [25,22,31,45], ['a','b']):
        print(x)

    #lst = [zip(['Jan', 'Marie'], [25,22])]     #fout, lst met 1 zip-obj
    #lst = [*zip(['Jan', 'Marie'], [25,22])]     #cp error
    #lst = *zip(['Jan', 'Marie'], [25,22])      #cp error

    lst = [a for a in zip(['Jan', 'Marie'], [25,22])]   #[('Jan', 25), ('Marie', 22)]
    #lst = [(b,a) for a,b in zip(['Jan', 'Marie'], [25,22])]
    print(lst)

    print(*zip(['Ans', 'Wil'], [45,46]))    #('Ans', 45) ('Wil', 46)

    lst = [11,12,13,14,15]
    #res = [lst[i] for i in range(2)]        #[11, 12]
    #res = [lst[i:] for i in range(2)]       #[[11, 12, 13, 14, 15], [12, 13, 14, 15]]
    res = (lst[i:] for i in range(2))       #gen-obj, eist ook zip(*res)
    print(res)
    for x in zip(*res):         #* om hfd-lst/gen-obj te splitsen in z'n 2 sublists
        print(x)
  

def test_set():
    print('\nset:')
    #set heeft geen volgorde/index, wel unieke items
    vz = {1,2,2,3,3,3,4,5,6,7,7,-1}            #bij getallen toevallig wel volgorde
    print('len(vz)=%d, vz=%s' % (len(vz),vz))
    #print(vz[0])        #TypeError: 'set' object does not support indexing

    lst = ['appel', 'appel', 'appel', 'banaan']
    print(lst)
    vz = set(lst)
    print(vz)

    vz = {'appel','peer','banaan','abrikoos','meloen','kiwi','peer'}
    #iedere keer dat je prog draait, kan de volgorde anders zijn
    print(vz)
    vz.remove('banaan')
    #vz.remove('aardbei')        #KeyError: 'aardbei', want bestaat niet
    vz.discard('aardbei')        #geen error; .discard() alleen bij set, niet list/dict
    print("pop:", vz.pop())
    print(vz)

def test_dict():
    #LET OP: Python 3.5 ->dict geen invoervolgorde (idem set)
    #Python 3.6 ->nwe implementatie dict; nu WEL invoervolgorde...
    #Python 3.7 ->dict voortaan officieel ordered
    #keys uniek; indien string dan hfdlet gevoelig
    print('\ndict:')
    d = {'Jan': 25, 'Marie': 22, 'Geesje': 31, 'Frits': 45}     #namen + leeftijden
    #d = dict(Jan=25, Marie=22, Geesje=31, Frits=45)         #let op: keys ZONDER kwoots!
    #d = dict(zip(['Jan', 'Marie', 'Geesje', 'Frits'], [25,22,31,45]))   #zip() combineert 2 lists tot tupel-iterable

    #vlg ValueError, want krijgt tupels v 3 items
    #d = dict(zip(['Jan2', 'Marie2', 'Geesje2', 'Frits2'], [25,22,31,45], ['a','b','c','d']))

    print(type(d))      #Python 3.4: <class 'dict'>
    print(d)            #Python 3.5: keys niet op volgorde

    d['Wim'] = 58       #voeg item toe; geen .add()/.put()/.append()/.set()
    d['Frits'] += 1
    #d['Anneke'] += 1    #KeyError, want Anneke bestaat niet
    if 'Anneke' in d:
        d['Anneke'] += 1
    else:
        d['Anneke'] = 18                #goed
    d['Els'] = d.get('Els', 17) + 1     #goed, mkt + verhoogt 'Els'
    d['Jan'] = d.get('Jan', 17) + 1     #goed, verhoogt bestaande 'Jan'

    print(d)

    print(d['Marie'])
    #print(d['Joop'])                    #KeyError: 'Joop', Joop bestaat niet
    print(d.get('Joop'))                #wordt None, geen error
    print(d.get('Joop', 101))           #->101, Joop bestaat niet
    print(d.setdefault('Ben', 20))      #->d['Ben'] als bestaat, anders d['Ben']=20 ->20
    print(d.setdefault('Marie', 5))     #->d['Marie'] ->22; zet niks

    #d.remove('Marie')       #error, kent geen .remove()
    #d.discard('Marie')      #error, kent geen .discard()
    #del d['Koos']           #KeyError: 'Koos'
    del d['Marie']           #wel goed

    #print("pop:", d.pop())             #TypeError, d.pop(..) eist key, [default]
    print("popitem:", d.popitem())      #wist + ret (key,value); 3.7: laatste, 3.4: willek
    print("pop:", d.pop('Frits'))       # 45
    #print("pop:", d.pop('Joop'))       #KeyError: 'Joop'
    print("pop:", d.pop('Joop', 101))   # 101
    print(d)

def test_dict_loop():
    print('\ndict, loop:')
    d = {'Jan': 25, 'Marie': 22, 'Geesje': 31, 'Frits': 45}     #namen + leeftijden

    totleeftijd = 0
    for k,v in d.items():
        totleeftijd += v
        print('key = %s, val = %d' % (k,v))
    print('\ntot leeftijd = %d\n' % totleeftijd)

    totleeftijd = 0
    for k in d:                     #hetzelfde als: for k in d.keys()
        totleeftijd += d[k]
        print('key = %s, val = %d' % (k,d[k]))
    print('\ntot leeftijd = %d\n' % totleeftijd)

    #for k in d:                             #idem bij d.keys()
    #    if k.startswith('M'): del d[k]      #RuntimeError, dict gewijz tijdens iter
    print(d)

def test_dict_comprehensionexpr():
    print('\ndict, comprehension expression:')
    #ord(c) geeft getal in ascii-tabel, hex(..) maakt string: '0x6f'
    d = {c: hex(ord(c)) for c in 'boekdrukkunst'}    #wordt key:value; 3.7: volgorde, 3.4: niet
    #d = {c.upper(): hex(ord(c.upper())) for c in 'boekdrukkunst'}      #toont hfdlett
    print(d)
    print(sorted(d))        #geeft lst met de keys, gesorteerd
    print(sorted('boekdrukkunst'))


def test_list_shallowdeepcopy():
    import copy
    
    m1 = [[1,2], [3,4]]
    m2 = m1.copy()          #m2 bevat ptrs naar de twee org rijen
    #m3 = copy.copy(m1)     #idem
    m3 = copy.deepcopy(m1)
    print(m1)
    print(m2)
    print(m1 is m2)         #False
    print(m1 == m2)         #True
    print(id(m1), id(m2), id(m3))
    print(id(m1[0]), id(m2[0]), id(m3[0]))     #m1[0] en m2[0] zelfde id, m3[0] niet

    print('\nm1[0] wijzigen:')
    m1[0][0] = 99
    m1[0].append(5)
    print(m1)               #[[99, 2, 5], [3, 4]]
    print(m2)               #[[99, 2, 5], [3, 4]]
    print(m3)               #[[1, 2], [3, 4]]  vanwege deepcopy
    m1[0] = [-1,-2]
    print(m1)               #[[-1, -2], [3, 4]]
    print(m2)               #[[99, 2, 5], [3, 4]]
    print(m3)               #[[1, 2], [3, 4]]

    print('\nondiepe herhaling:')
    m1 = [[1,2,3]] * 3      #geeft list met 3 ptrs naar dezelfde rij
    print(m1)
    m1[0][0] = -1
    print(m1)               #[[-1, 2, 3], [-1, 2, 3], [-1, 2, 3]]
    del m1[0][2]
    print(m1)               #[[-1, 2], [-1, 2], [-1, 2]]
    

def test_matrix():
    import operator
    
    m = [
        [4,3,6,5],
        [1,1,2,2]
    ]
    print(m)
    print("len(m)   :", len(m))           #2 
    print("len(m[0]):", len(m[0]))        #4
    #print(m[0][0], m[0][1], m[1][0], m[1][1])

    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
    print()
    print("i=%d, j=%d" % (i,j))     #i, j zijn hier nog bekend, geen block scope
    
    for rij in m:
        for item in rij:
            print(item, end=' ')
    print()

    # vlg geen NameError omdat rij al bekend is van vorige lus
    #lst = [item for item in rij for rij in m]       #wel foute uitkomst...
    #lst = [item for item in row for row in m]       #NameError: 'row' not defined
    #lst = [type(x) for x in m]                      #[<class 'list'>, <class 'list'>]
    lst = [item for rij in m for item in rij]       #goed
    print(lst)

    #dot prod v 2 vectoren:
    a = m[0]
    b = m[1]
    it = map(operator.mul, a, b)         #wordt iterator (map-obj)
    # je kan it maar 1* draaien, geen reset [iter kopie: itertools.tee()]
    # ->hetzij items tonen, hetzij sum, hetzij list(map(..)) doen
    #for x in it: print(x, end=' ')
    print(sum(it))
    #c = a @ b                  #error, unsupported for list; goed in pandas
    # @ bestaat vanaf 3.5; maar list ondersteunt onderliggende __matmul__() niet

def test_matrixmul():
    m1 = [
      [1, 2],
      [3, 4]
    ]
    m2 = [
      [5, 3, 2],
      [2, 7, 1]
    ]
    m3 = matrixmul(m1, m2)
    print(m3)
    
def matrixmul(m1, m2):
    R1 = len(m1)
    K1 = len(m1[0])
    K2 = len(m2[0])

    #doelmatrix krijgt aant rijen v m1 en aant kols van m2
    #eist: kols m1 == rijen m2

    if K1 != len(m2):
        raise ValueError("Ongeldig aantal rijen/kolommen")
    
    m3 = []
    for i in range(R1):
        m3.append([0]*K2)
    # vor niet eerst [0]*K2 apart maken en dan telkens toevoegen aan m3,
    # want dan wordt iedere rij in m3 een ptr naar hetzelfde rij-object
    # kan wel met rij = [0]*K2; m3.append(rij.copy()) of .append(rij[:])

    for rij1 in range(R1):
        for kol2 in range(K2):
            # per elem in m3 vlg dotproduct kol*rij draaien:
            for kol1 in range(K1):
                m3[rij1][kol2] += m1[rij1][kol1] * m2[kol1][kol2]
    return m3

calcdict = {"+": lambda x,y: x+y, "-": lambda x,y: x-y,
    "*": lambda x,y: x*y, "/": lambda x,y: x/y}

def bereken_dict(a,b, optor):
    # dict als jump table
    return calcdict[optor](a,b)


#--- script ---

#toonTafelVan10()
#toonTafelVanX(8)
#toonTafelVanX()         #error, argument verplicht
#toonTafelVanXDefault(12)
#toonTafelVanXDefault()      #goed, default arg
#toonTafelVanXDefault(int(input('Geef getal: ')))

#test_range()
#test_range_continue_break()

#test_list_for_basis()
#test_list_loop()
#test_list_iterator()
#test_list_basis()
#test_list_append_enz()
#test_list_unpack()
#test_list_min_max_enz()
#test_list_slice()

#test_tupels()

#test_list_sort_search()
#test_list_comprehensionexpr_map_filter()
#test_generatorexpr()

#test_zip()
#test_set()
test_dict()
#test_dict_loop()
#test_dict_comprehensionexpr()

#test_list_shallowdeepcopy()
#test_matrix()
#test_matrixmul()

#print(bereken_dict(13,8,'+'))

