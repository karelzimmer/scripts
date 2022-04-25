# werken met array en collections

"""
array efficienter dan list; je moet type bij creatie opgeven
vlg codes ook bij struct.pack() 
c=char(1); b=byte(1), h=short(2), i=int(4), l=long(4), q=longlong(8)
B-Q unsigned versie; f=float(4), d=double(8), 'u'=unicodechar(2)

module queue heeft Queue (fifo), LifoQueue, PriorityQueue (vanaf laagste)
met sync methods speciaal voor multithreading; .put(), .get()
"""

from array import array         #, typecodes
import collections as col

#print(typecodes)          #'bBuhHiIlLqQfd' (str)

def test_array():
    # doet op win little endian; niet instelbaar
    arr = array('H', [12, 65534, 3, 2])     # 'H' = unsigned short
    print(arr)
    print(type(arr))            #<class 'array.array'>
    print(arr.typecode)         #H
    print(arr.tobytes())        #b'\x0c\x00\xfe\xff\x03\x00\x02\x00'
    print('arr.itemsize=', arr.itemsize)    # 2
    print('len=', len(arr))
    print(arr.buffer_info())    #(28342416, 4) ->(adres,len)

    print('\nWijzigen:')
    a = arr[1]                  #a ->int
    print(a)
    arr[1] = 19
    print(arr[:2])              #array('H', [12, 65533])
    arr[:2] = array('H',[31,32])    #kan niet direct met list, eist zelfde type

    arr.frombytes(b'a\0b\0')    #append, goed, wordt shorts: 97, 98; \0 = 0-byte
    print(arr)
    del arr[-2:]
    print(arr)

    arr.append(0)
    arr.insert(0, 8)
    arr.fromlist([51,52])           #append list
    arr.extend([21,22,23])          #append iterable

    for x in arr: print(x, end=' ')
    print()

    print(arr.index(3))
    #print(arr.index(999))      #ValueError, zit niet in arr

    print(arr.count(3))         #hoe vaak komt 3 voor
    print(arr.count(17))        #hoe vaak komt 17 voor

    print(arr.pop())            #verwijder en retourneer laatste [= .pop(-1)]
    print(arr.pop(0))
    #arr.remove(501)            #ValueError, want 501 zit niet in arr

    print(arr.tolist())
    arr.reverse()
    print(arr)
    arr.byteswap()
    print(arr)

def test_deque():
    # deque geoptim voor toev/wissen voor- en achteraan
    # bij maxlen boekenplank-model: toev aan ene kant ->weg aan andere kant 
    deq = col.deque([0,2,4,6,8,10])       #,maxlen
    print(deq)
    deq.append(11)
    deq.extend([12,13])
    deq.appendleft(-1)
    deq.extendleft([-2,-3])
    #deq.insert(2,3)            #error
    print(deq)
    print(deq.pop())
    print(deq.popleft())
    deq.remove(4)               #wis getal 4
    del deq[2]
    print(deq)
    print(deq[0])
    #print(deq[1:3])            #error, kent geen slices
    deq.rotate(2)               #-2 = twee naar kinks
    print(deq)
    print()

    deq = col.deque('abcde', 4)
    print(deq)                  #deque(['b', 'c', 'd', 'e'], maxlen=4)
    deq.append('f')
    deq.append('g')
    print(deq)
    

def test_namedtuple():
    # vlg geeft verwarring tup vs Point
    tup = col.namedtuple('Point', 'x y')    #'x y'; 'x, y'; ['x','y']
    print(tup)              #<class '__main__.Point'>
    #print(tup._source)      #class Point(tuple) met daarin enorme class-def
    pt = tup(3,4)           #Point(x=3, y=4)
    print(pt)
    #pt = Point(5,5)         #NameError, Point not defined
    del tup

    # vlg beter
    Point = col.namedtuple('Point', 'x y')
    pt = Point(5,7)         #pos of named arg, dus ook: Point(x=5,y=7)
    print(pt)
    print(pt.x, pt.y)
    #print(pt['x'], pt['y'])    #TypeError, must be integers (indices)
    print(pt[0], pt[1])         #goed
    for a in pt: print(a, end=' ')      #goed
    print()
    a,b = pt                    #unpack
    print(a,b)

    pt2 = Point._make((3,4))    #iterable ipv losse args
    print(pt2)
    d2 = pt2._asdict()          #col.OrderedDict
    print(d2)
    pt3 = pt2._replace(x=9)
    print(pt3)
    d4 = dict(x=7, y=8)               #d4={'x':7, 'y':8}
    print(d4)
    pt4 = Point(**d4)           #goed, moet dict uitpakken

    print(Point._fields)        #('x', 'y'), kan ook met pt._fields
    Color = col.namedtuple('Color', 'r g b')
    Pixel = col.namedtuple('Pixel', Point._fields + Color._fields)
    Point3D = col.namedtuple('Point3D', Point._fields + ('z',))

    px = Pixel(25,50, 10,10,255)
    print(px)                   #Pixel(x=25, y=50, r=10, g=10, b=255)
    pt = Point3D(3,3,6)
    print(pt)
    
def test_OrderedDict():
    # vanaf Python 3.6 is dict ook ordered, vanaf 3.7 officieel
    # ->OrderedDict niet meer zo relevant
    # tot aan 3.7 zijn de kw NIET ordered ->volgorde kan anders zijn
    # dan hieronder!
    #d = col.OrderedDict(jan=26, piet=32, klaas=47, frits=18, geesje=19)
    # vlg wel geordend, want list:
    d = col.OrderedDict([('jan',26),('piet',32),('klaas',47),('frits',18),('geesje',19)])
    print(d)
    for k,v in d.items(): print(k,':',v)
    d['marie'] = 25
    print(d)
    print(d.popitem())          #last=True (dflt), False->first
    d.move_to_end('jan')        #last=True (dflt), False->move to first
    print(d)

def test_defaultdict():
    # mk een dict met voor iedere nwe key een default value (0, leeg) v opgeg type
    d = col.defaultdict(list)       #hier per nwe key een nwe lege list
    
    lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    for k, v in lst:
        d[k].append(v)
    d['green'].append(88)       #gebr wel lege [] voor 'green'
    d['green'].append(99)
    d['purple'] = [21,22,23]    #mkt zelf lege list [], die ik niet gebr
    print(d.items())

    # vlg met gewone dict
    d2= {}
    for k, v in lst:
        d2.setdefault(k, []).append(v)   #.setdefault() doet een get
    print(d2.items())

    counters = col.defaultdict(int)		#hier per nwe key een int=0
    counters['ams'] = 5         #mkt zelf int 0, die ik niet gebr
    counters['rt'] += 1         #gebr wel int 0 voor 'rt', en tel door
    counters['rt'] += 1
    print(counters.items())
    
def test_Counter():
    counters = col.Counter()
    lst = ['appel','peer','banaan','peer','kiwi','appel','appel','aardbei','appel']
    for a in lst:
        counters[a] += 1
    counters['aardbei'] += 1
    counters['sinaasappel'] += 1
    counters['banaan'] += 1
    print(counters)         #officieel ongeordend, maar hij doet freq hoog->laag
    print(counters.items())	#ongeordende list v tupels: dict_items([('can', 7), ('in', 6), ...]
    print(counters.most_common(3))  #ordered list v (item,freq), meest->minst, niet ex equo (ties)

    for a in counters.elements():
        print(a, end=' ')       #4 keer een appel enz, maar niet meest->minst
    print('\n')

    counters = col.Counter('appelflappenbakgerei en andere keukenspullen')
    # vor wordt gezien als list v letters
    print(counters)
    print(counters.keys())          #unordered
    print(counters.items())         #unordered (item,freq)
    print(counters.most_common())   #ordered (item,freq)

    print()
    c = col.Counter(['a','b','d','a','c','a','d','d','b','a'])
    print('c:', c)
    d = col.Counter(a=1, b=2, c=2, d=1)     #of: ({'a':1,'b':2, 'c':2, 'd':1})
    print('d:', d)
    c.subtract(d)           #d mag iterable of map zijn
    print('c:', c)
    d['e'] += 1
    print('d:', d)
    c.update(d)             #merge, dwz tel counters op + voeg toe
    print('c:', c)
    print(d - c)            #->'c':1, trek counters v elk af, toon resterende positieve

def test_ChainMap():
    # heeft intern list v maps, zkn vlnr, update/del alleen in 1e map
    d = {'a':5, 'b':27, 'c':9}
    e = dict(m=11, n=12, c=13)
    f = {'x':-1, 'y':-2}
    g = {'E':21, 'F':22}
    cm = col.ChainMap(d,e)
    print(cm)
    cm = cm.new_child(f)    #nwe chain met f vooraan, dus: f, d, e
    print(cm.maps)          #->list v dicts
    cm.maps.append(g)
    print(cm)
    print(cm['c'])          #vindt de 1e 'c' -> in d
    cm['c'] = -9            #let op: voegt 'c' toe aan f
    cm['x'] = -11
    #del cm['b']            #error, update/del alleen in 1e map
    del cm['y']             #goed, want dict f vooraan
    print(cm)
    dm = cm.parents         #nwe chain vanaf 2e map, dus d, e, g
    print(dm)


#--- script ---

#test_array()
#test_deque()
#test_namedtuple()
#test_OrderedDict()
#test_defaultdict()
#test_Counter()
test_ChainMap()

