#serializing met pickle en shelve
#PickleError <-PicklingError,UnpicklingError

#shelve is een persistent dict. Gebr mini db dbm.dumb of geinstall gnu dbm
#(dbm = database manager)
#dbm.dumb mkt xyz.dat + xyz.dir (+ xyz.bak, backup v .dir)
#dbm eist key=str, val=str; shelve eist key=str, val=pickled obj

#json kan alleen lists en dicts enz serializeren, geen eigen obj

import pickle, pickletools
import shelve
import json

class Doos:
    """Doos met std serializing"""
    
    def __init__(self, l,b,h):
        self.l = l
        self.b = b
        self.h = h
        self.kleur = 'bruin'
        self.beschrijving = '(geen)'

    def volume(self):
        return self.l * self.b * self.h

    def oppervlak(self):
        return 2 * (self.l*self.h + self.b*self.h + self.l*self.b)


class Emmer:
    """Emmer met custom serializing"""

    def __init__(self, diam, hg, kleur='grijs'):
        self.diam = diam
        self.hg = hg
        self.kleur = kleur

    def __getstate__(self):
        #bij serializeren
        import os, time
        state = self.__dict__.copy()
        del state['kleur']
        state['user'] = os.getlogin()   #of: getpass.getuser() [kijkt in env]
        state['tijd'] = time.ctime()
        return state

    def __setstate__(self, state):
        #bij deserializeren; hij draait __new__() ipv __init__()
        print('  Emmer deserializeren\n  geserialiseerd op %s door %s'
              % (state['tijd'], state['user']))
        state.pop('user')       #of: del state['user']
        state.pop('tijd')
        state['kleur'] = '(onbekend)'
        self.__dict__.update(state)

    def volume(self):
        import math
        return self.hg * self.diam * self.diam * math.pi * 0.25
    

def toonPickleFile(fnaam, aantal=1):        #aantal apart geser items
    with open(fnaam, 'rb') as fh:
        for i in range(aantal):
            pickletools.dis(fh)
    
def toonDoos(d):
    if d == None:
        print('geen doos gevonden')
        return
    print('Doos: %d, %d, %d -> vol=%d, %s, %s' % (d.l, d.b, d.h, d.volume(),
          d.kleur, d.beschrijving))

def toonEmmer(e):
    if e is None:               #kan ook ipv ==
        print('geen emmer gevonden')
        return
    print('Emmer: %d, %d -> vol=%d, kleur=%s' % (e.diam, e.hg, e.volume(),
          e.kleur))

def serializeerDoos():
    d1 = Doos(12, 7, 9)
    d1.beschrijving = 'oude elpees'
    toonDoos(d1)
    d2 = Doos(6, 7, 8)
    d2.beschrijving = 'oude videos'
    d2.kleur = 'wit'
    toonDoos(d2)

    fh = open('doos.pickle', 'wb')
    pickle.dump(d1, fh)
    pickle.dump(d2, fh)
    fh.close()
    print('serializeren naar doos.pickle')

def deserializeerDoos():
    fh = open('doos.pickle', 'rb')
    d1 = pickle.load(fh)
    d2 = pickle.load(fh)
    fh.close()

    toonDoos(d1)
    toonDoos(d2)

def serializeerDoosList():
    lst = []
    d = Doos(5,6,7)
    d.beschrijving = 'oude elpees'
    lst.append(d)
    d = Doos(4,8,8)
    d.beschrijving = 'oude videos'
    d.kleur = 'wit'
    lst.append(d)
    d = Doos(6,6,6)
    d.beschrijving = 'oude mensen'
    d.kleur = 'zwart'
    lst.append(d)
    d = Doos(12,8,6)
    d.beschrijving = 'oude boeken'
    d.kleur = 'blauw'
    lst.append(d)
    for d in lst:
        toonDoos(d)

    #b = pickle.dumps(lst)           #geeft bytes string ipv naar file
    #print(b)
    #return

    fh = open('dooslist.pickle', 'wb')
    pic = pickle.Pickler(fh)        #kan ook
    pic.dump(lst)
    fh.close()
    print('serializeren naar dooslist.pickle')

def deserializeerDoosList():
    #lst = pickle.loads(b)           #leest bytes array ipv file
    
    fh = open('dooslist.pickle', 'rb')
    pic = pickle.Unpickler(fh)        #kan ook
    lst = pic.load()
    fh.close()
    print(type(lst).__name__)       # list

    for d in lst:
        toonDoos(d)

def serializeerEmmerListCustom():
    lst = [Emmer(4,10), Emmer(6,8,'blauw'), Emmer(8,5,'zwart')]
    for e in lst:
        toonEmmer(e)
    
    fh = open('emmerlist.pickle', 'wb')
    pickle.dump(lst, fh)
    fh.close()
    print('serializeren naar emmerlist.pickle')

def deserializeerEmmerListCustom():
    fh = open('emmerlist.pickle', 'rb')
    lst = pickle.load(fh)
    fh.close()

    for e in lst:
        toonEmmer(e)


def serializeerDoosShelve():
    #dozen opslaan in persistent dict
    d1 = Doos(12, 7, 9)
    d1.beschrijving = 'oude elpees'
    toonDoos(d1)
    d2 = Doos(6, 7, 8)
    d2.beschrijving = 'oude videos'
    d2.kleur = 'wit'
    toonDoos(d2)

    sh = shelve.open('dozen')       # r/w; mkt dozen.dat + dozen.dir
    sh['doos1'] = d1
    sh['doos2'] = d2
    #als je d1/d2 wijzigt, dan opnieuw opslaan in db
    sh.close()
    print('opgeslagen via shelve naar dozen')

def deserializeerDoosShelve():
    sh = shelve.open('dozen')
    d2 = sh['doos2']
    d1 = sh['doos1']
    sh.close()

    toonDoos(d1)
    toonDoos(d2)

def serializeerDoosJson():
    #json kan alleen lists en dicts enz serializeren, geen eigen obj
    #.dump() ->naar file; .dumps() ->naar string
    #.load() ->uit file; .loads() ->uit string
    d1 = Doos(12, 7, 9)
    d1.beschrijving = 'oude elpees'
    toonDoos(d1)

    fh = open('doos.json', 'w')         #moet textmode
    #vlg okee met .__dict__, maar prb met geneste obj
    json.dump(d1.__dict__, fh, indent=2)
    #2 keer .dump() gaat goed, maar .load() niet: ValueError: extra data
    #json.dump(d2.__dict__, fh,indent=2)
    fh.close()
    print('serializeren naar doos.json')

def deserializeerDoosJson():
    fh = open('doos.json', 'r')
    dic1 = json.load(fh)
    fh.close()

    d1 = Doos(1,1,1)
    #d1 = Doos.__new__() werkt niet, want eist dezelfde args als __init__()
    d1.__dict__.update(dic1)
    toonDoos(d1)

def serializeerDoosJson_str():
    d1 = Doos(12, 7, 9)
    d1.beschrijving = 'oude videos'
    toonDoos(d1)
    #s = json.dumps(d1)              #TypeError, not JSON serializable
    s = json.dumps(d1.__dict__)     #goed
    #s = json.dumps(vars(d1))
    #s = json.dumps(vars(d1), indent=2)
    #s = json.dumps(vars(d1), sort_keys=True, indent=2)
    print(s)


#--- script ---

#print(pickle.HIGHEST_PROTOCOL)           # 4
#print(pickle.DEFAULT_PROTOCOL)           # 3
#toonPickleFile('doos.pickle', 2)         # aantal items
#toonPickleFile('dooslist.pickle')        # default 1 item
#toonPickleFile('emmerlist.pickle')

#serializeerDoos()
#deserializeerDoos()
#serializeerDoosList()
#deserializeerDoosList()

#serializeerEmmerListCustom()
#deserializeerEmmerListCustom()

#serializeerDoosShelve()
#deserializeerDoosShelve()

#serializeerDoosJson()
#deserializeerDoosJson()
serializeerDoosJson_str()
