def tafel10():
    for i in range(1,11):
#        print('%2d maal 10 is %3d' % (i, i*10)) # "oude" manier
        print(f"{i:2d} maal 10 is {i*10:3d}") # nieuwe manier


def telop(*som):
    totaal = 0
    for getal in som:
        totaal = totaal + getal
    totaal2 = sum(som)
    return totaal, totaal2


def test_naam():
    naam = 'Pieter-Jan van den Hoogenbandt'
    print('Naam:'.ljust(23), naam)
    print('Lengte naam:'.ljust(23), len(naam))
    print('Oneven letters in naam:'.ljust(23), naam[0:len(naam):2])
    #print('Oneven letters in naam:'.ljust(23), naam[::2])  # mag ook

    print('\n<Letter>: <Unicode-codepunt>')
    for c in naam:
        print(f'      {c} : {ord(c)}')


def test_getallen():

    lst = [1, 2, 3, 4, 5]
#    print(lst)         # Print ook [ en ] waarom? om verschil te tonen
#    print(repr(lst))   # Print ook [ en ] uiteraard!
    mini = min(lst)
    som = sum(lst)
    print(lst, mini, som)


def test_comprehension():

    lst = [3, 5, 8, -4, 2]
    print(lst)
#    lst2 = [x ** 2 for x in lst]
    # kwadraat pos. getallen
    lst2 = [x ** 2 for x in lst if x > 0]
#    print(lst2)
    # 3e macht
    lst3 = list(map(lambda x : x ** 3, lst))
#    print(lst3)
    # pos. getallen
    lst4 = list(filter(lambda x : x > 0, lst))
#    print(lst4)
    # wortel pos. getallen
    lst5 = list(map(lambda x : round(x ** 0.5,2), filter(lambda x : x > 0, lst)))
    print(lst5)


def statistiek():
    # list
    import statistics

    i=1
    lst = list()
    while True:
        invoer = input(f"Voer geheel getal {i} in, max. 6 of 'stop': ")
        if invoer == 'stop':
            break
        if not invoer.isdigit():
            print('foute invoer')
        else:
            lst.append(int(invoer))
            i += 1
        if i == 7:
            break
    if i == 1:
        print('geen uitvoer')
        return
    br=10
    print('Invoer'.ljust(br), lst)
    print('Kleinste'.ljust(br), min(lst))
    print('Grootste'.ljust(br), max(lst))
    print('Som'.ljust(br), sum(lst))
    gem = sum(lst) / len(lst)
    print('Gemiddelde'.ljust(br), float(gem))
    var = statistics.variance(lst)
    print('Variantie'.ljust(br), var)


def autos():
    # dictionary
    d = {'opel':7500, 'nissan':7000, 'toyota':12500, 'mazda':8500}
    print(d)
    for merk,prijs in d.items():
        print(f'Een {merk} kost {prijs}')
    gem = sum(d.values()) / len(d)
    print('Gemiddelde prijs is ', gem)

def fruit():
    br=11
    # set
    f1 = {'peer', 'banaan', 'appel', 'citroen'}
    print('Set f1:'.ljust(br), f1)
    f2 = {'framboos', 'aardbei', 'peer'}
    print('Set f2:'.ljust(br), f2)
    # vereniging
    fx = f1 | f2
    print('Vereniging:'.ljust(br), fx)
    # doorsnede
    fx = f1 & f2
    print('Doorsnede:'.ljust(br), fx)
    # verschil
    fx = f1 - f2
    print('Verschil:'.ljust(br), fx)
    # toevoegen
    #f1.add('meloen', 'banaan', 'bonono')
    #TypeError: add() takes exactly one argument (3 given)
    f1 |= {'meloen', 'banaan', 'bonono'}
    print('Toegevoegd:'.ljust(br), f1)

# --- script ---

#tafel10()

#print(telop(7,2,5,5))
#print(telop(*[7,2,5,5]))
#print(telop())

#test_naam()

#test_getallen()

#test_comprehension()

# retunr levert afsluitwaarde None
#a = statistiek()
#print(a)
#print('\nAfsluitwaarde = ', statistiek())

#autos()

fruit()
