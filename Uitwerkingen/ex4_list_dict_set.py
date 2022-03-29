#oefeningen met list etc

import re

def tafel10():
    for i in range(1,11):
        print('%2d maal 10 is %3d' % (i,i*10))

def telop(*getallen):
    print(getallen)        #tupel
    totaal = 0
    for g in getallen:
        totaal += g
    return totaal

def test_naam():
    naam = 'Pieter-Jan van den Hoogenbandt'
    print(naam, len(naam))
    print(naam[0:len(naam):2])          #of willek lang getal, bv 40
    print(naam[:len(naam):2])           #idem
    print(naam[::2])                    #idem

    print('Alle letters afdrukken:')
    for c in naam:
        print('%c: %d' % (c,ord(c)))
    print('Oneven letters afdrukken:')
    for c in naam[0:len(naam):2]:              #of: naam[::2]
        print('%c: %d' % (c,ord(c)), end=', ')
    print()

def test_naam2():
    naam = 'Pieter-Jan van den Hoogenbandt'
    print(naam, len(naam))
    for n in range(len(naam)):
        if n % 2 == 0:
            print(naam[n], end='')
    print()

def test_getallen():
    lst = [1,2,3,4,5]
    print(lst)
    mini = min(lst)
    maxi = max(lst)
    som = sum(lst)
    print('min=%d, max=%d, som=%d' % (mini,maxi,som))

def test_comprehension():
    lst = [3, 5, 8, -4, 2]
    #lst2 = [x*x for x in lst]
    lst2 = [x*x for x in lst if x > 0]
    print(lst2)

    lst3 = list(map(lambda x: x*x*x, lst))
    print(lst3)

    lst4 = list(filter(lambda x: x>0, lst))
    print(lst4)

    lst5 = list(map(lambda x: round(x**0.5,2), filter(lambda x: x>0,lst)))
    print(lst5)

#de module statistics (vanaf 3.4) bevat mean(), median(), median_low(), median_high)
#median_grouped(), mode(), pstdev(), pvariance(), stdev(), variance()
#kun je ook gebruiken
def statistiek():
    lst = []
    idx = 1
    som2 = 0            #voor variantie

    while idx <= 6:
        invoer = input('Geef getal %d ("stop" om te stoppen): ' % idx)
        if invoer == 'stop':
            break
        if not invoer.isdigit():
            #.isdigit(), .isdecimal(), isnumeric() werken NIET met neg getallen
            #en floats;
            # invoer.lstrip('-').isdigit()
            # invoer.lstrip('-').replace('.','',1).isdigit() -> 1 '.' vervangen
            print('foute invoer')
        else:
            a = int(invoer)
            lst.append(a)
            som2 += a*a             #voor variantie
            idx += 1

    if not lst:
        print('geen invoer')
        return
    
    print(lst)
    som = sum(lst)
    cnt = len(lst)
    print('min=%d, max=%d, som=%d, aantal=%d'
          % (min(lst),max(lst), som, cnt))
    gem = som / cnt
    print('gem=%f' % gem)

    #populatievariantie: sigma^2 = 1/n * SOM(x-m)^2 = 1/n * SOM(x^2) - m^2
    #steekproefvariantie: sigma^2 = 1/(n-1) * SOM(x-m)^2 = 1/(n-1) * SOM(x^2) - n/(n-1) * m^2
    var = som2 / cnt - gem * gem;
    print('var=%.2f; stdev=%.2f' % (var, var**0.5))

def autos():
    d = {'volvo': 32000, 'mercedes': 128500, 'lada': 6329, 'renault': 16750}
    print(d)
    som = 0
    #for key in d:
    #    print('Een %s kost %d' % (key, d[key]))
    #    som += d[key]
    for key,value in d.items():
        #print('Een %s kost %s' % (key, value))
        print('Een %s kost %s' % (key.capitalize(), value))
        #if type(value) == tuple:        #if isinstance(value, tuple):
        #    print(value[1])
        som += value
    print('Gemiddelde prijs van de autos: %.2f' % (som/len(d)))
    print(d['mercedes'])
    #print(d.get('mercedes'))

def fruit():
    f1 = {'peer', 'banaan', 'appel', 'citroen', 'kiwi'}
    print(f1)
    f2 = {'framboos', 'aardbei', 'peer'}
    print(f2)

    fx = f1 | f2         #of: f1.union(f2)
    print(fx)
    fx = f1 & f2         #of: f1.intersection(f2)
    print(fx)
    fx = f1 - f2         #of: f1.difference(f2)
    print(fx)
    fx = f2 - f1
    print(fx)

    f1.add('meloen')
    f1.add('banaan')
    f1.add('bonono')
    #f1 |= {'meloen', 'banaan', 'bonono'}    #of: f1.update(..)
    print(f1)
    print(len(f1))
    print(sorted(f1))       #wordt een list!


def matrix():
    m1 = [
      [1, 2],
      [3, 4]
    ]
    m2 = [
      [5, 3],
      [2, 7]
    ]
    m3 = [
      [0, 0],
      [0, 0]
    ]

    for i in range(2):
        for j in range(2):
            m3[i][j] = m1[i][j] + m2[i][j]
    print(m3)

def matrixmul():
    m1 = [
      [1, 2],
      [3, 4]
    ]
    m2 = [
      [5, 3],
      [2, 7]
    ]
    m3 = [
      [0, 0],
      [0, 0]
    ]

    m3[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    m3[0][1] = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    m3[1][0] = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    m3[1][1] = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    print(m3)

def matrixmul2():
    M = 2
    m1 = [
      [1, 2],
      [3, 4]
    ]
    m2 = [
      [5, 3],
      [2, 7]
    ]
    m3 = [
      [0, 0],
      [0, 0]
    ]

    for i in range(M):                  #rij1
        for j in range(M):              #kol2
            for k in range(M):          #kol1
                m3[i][j] += m1[i][k] * m2[k][j]
                #m3[rij1][kol2] += m1[rij1][kol1] * m2[kol1][kol2]
    print(m3)

def test_matrixmul_generiek():
    m1 = [
      [1, 2],
      [3, 4]
    ]
    m2 = [
      [5, 3, 2],
      [2, 7, 1]
    ]
    m3 = matrixmul_generiek(m1, m2)
    print(m3)
    
def matrixmul_generiek(m1, m2):
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


def test_mensen():
    ams = {'Marie', 'Joop', 'Frits', 'Elsie', 'Geesje'}
    rot = {'Koos', 'Rina', 'Ahmed', 'Cenk', 'Kimberly'}
    meid = {'Marie', 'Elsie', 'Geesje', 'Rina', 'Kimberly'}
    vriend = {'Frits', 'Elsie', 'Rina', 'Cenk'}

    print(ams | rot)            #alle mensen
    print(meid & ams)           #meiden in Amsterdam
    print(rot - meid)           #jongens in Rotterdam
    print((ams | rot) - meid)   #alle jongens
    print(ams - meid | rot - meid)  #idem; duidelijker met prioriteitshaakjes
    print(vriend - rot)         #vrienden niet in Rotterdam
    print((ams | rot) - vriend) #iedereen die geen vriend is.

    ams.add('Nala')
    vriend |= {'Nala'}      #zelfde effect als .add()
    meid.update({'Nala'})   #idem

    print("\nNa toevoegen Nala:")
    print(ams | rot)            #alle mensen
    print(meid & ams)           #meiden in Amsterdam
    print(rot - meid)           #jongens in Rotterdam
    print((ams | rot) - meid)   #alle jongens
    print(ams - meid | rot - meid)  #idem; duidelijker met prioriteitshaakjes
    print(vriend - rot)         #vrienden niet in Rotterdam
    print((ams | rot) - vriend) #iedereen die geen vriend is.
    
r = """\
Hij nam een laatste trek van zijn sigaret en dacht, half mompelend,
bij zichzelf: 'Het wordt tijd een stap vooruit te zetten.' Hij keek
naar beneden naar zijn schoenen en zag daaronder de glibberige rand
van de brugleuning. Hij keek naar beneden langs de brugleuning en
zag in de diepte de rivier kolken. Het was  volle  maan.
"""

def analyseer_tekst():
    s = re.sub(r"[^\w\s]", "", r).lower()
    print(r)
    print(s)

    lst = s.split()
    print("\nAlle woorden:")
    print(lst)
    print("len =", len(lst))
    print("\nAlle verschillende woorden:")
    wdn = set(lst)
    print(wdn)
    print("len =", len(wdn))

    #tel_woorden(lst, wdn)
    tel_woorden2(lst)
    
def tel_woorden(lst, wdn):
    print('\nTel woorden:')
    #for w in wdn:
    for w in sorted(wdn):          #->list; ,reverse=True
        n = lst.count(w)            #tel voor ieder woord in verz hoe vaak het in lst voorkomt
        print('%-20s: %3d' % (w, n))
        #print('%-20s: %3d %s' % (w, n, n * '\u2588'))     #\u2588 geeft zwart blokje ->histogram

def tel_woorden2(lst):
    d = dict()
    
    for w in lst:
        d[w] = d.get(w, 0) + 1
        # volgende manier is iets omslachtiger:
        #if w in d:          #doet d.keys(), als woord al in dict, teller verhogen
        #    d[w] += 1
        #else:
        #    d[w] = 1        #bij nw woord ->w aan dict toevoegen en teller = 1 zetten

    print('\nTel woorden via dict:')
    #for k,v in d.items():
    #for k,v in sorted(d.items()):
    #    print('%-20s: %3d %s' % (k, v, v * '\u2588'))

    # hoogste frequentie bovenaan:
    for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True):    #x is (key,val) tupel
        print('%-20s: %3d %s' % (k, v, v * '\u2588'))
    # of:
    #for w in sorted(d, key=d.get, reverse=True):                #goed
    #    v = d[w]
    #    print('%-20s: %d %s' % (w, v, v * '\u2588'))


#--- script ---

tafel10()
#print(telop(7,2,4,5))
#print(telop())
#print(telop(*[3,6,7]))

#test_naam()
#test_naam2()
    
#test_getallen()
#test_comprehension()
#statistiek()

#autos()
#fruit()

#matrix()
#matrixmul()
#matrixmul2()
#test_matrixmul_generiek()

#test_mensen()
#analyseer_tekst()
