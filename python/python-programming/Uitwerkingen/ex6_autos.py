# auto's

class Auto:
    """Een Auto met eigenaar enz."""

    __garage = 'Hendrikse'

    def getGarage():
        return Auto.__garage

    def setGarage(naam):
        Auto.__garage = naam

    def __init__(self, eigenaar='Anon'):
        print("Auto: __init__()")
        self.tank = 0
        self.motor = 'uit'
        self.merk = '--onbekend--'
        self.eigenaar = eigenaar
        
    def tanken(self, liters):
        if liters < 1:
            print('Auto van %s: niet getankt.' % self.eigenaar)
            return
        if self.tank + liters > 40:
            liters = 40 - self.tank
        self.tank += liters
        print('Auto van %s: %d liters getankt.' % (self.eigenaar,liters))

    def starten(self):
        if self.motor == 'aan':
            print('Auto van %s: motor staat al aan.' % self.eigenaar)
        elif self.tank <= 0:
            print('Auto van %s: tank leeg. Kan niet starten.' % self.eigenaar)
        else:
            self.motor ='aan'
            print('Auto van %s: motor aangezet.' % self.eigenaar)

    def stoppen(self):
        if self.motor == 'uit':
            print('Auto van %s: motor staat al uit.' % self.eigenaar)
        else:
            self.motor = 'uit'
            print('Auto van %s: motor uitgezet.' % self.eigenaar)

    def rijden(self):
        if self.motor == 'uit':
            print('Auto van %s: motor uit. Eerst starten.' % self.eigenaar)
        elif self.tank <= 0:
            print('Auto van %s: tank leeg. Eerst tanken.' % self.eigenaar)
        else:
            self.tank -= 1
            print('Auto van %s: we rijden.' % self.eigenaar)
    
    # vlg met 'this' gedaan ipv 'self', niet netjes, kan wel
    def sturen(this, koers):
        if this.motor == 'uit':
            print('Auto van %s: motor uit. Eerst starten.' % this.eigenaar)
        elif this.tank <= 0:
            print('Auto van %s: tank leeg. Eerst tanken.' % this.eigenaar)
        else:
            print('Auto van %s: sturen: %s.' % (this.eigenaar,koers))
    
    def __str__(self):
        return 'Auto: %s heeft een %s.' % (self.eigenaar,self.merk)

    def __repr__(self):
        return 'Auto: eig=%s, merk=%s, tank=%d, motor: %s.' \
            % (self.eigenaar, self.merk, self.tank, self.motor)


class VrachtAuto(Auto):
    """VrachtAuto is Auto met lading"""

    # als je vlg weglaat, draait ie wel Auto.__init__(), maar heb je geen lading
    def __init__(self, eigenaar='Anon'):
        super().__init__(eigenaar)
        self.__lading = '(leeg)'
        
    def inladen(self, lading):
        if self.motor == 'aan':
            print('VrachtAuto van %s: motor aan. Eerst uitzetten.' % self.eigenaar)
        else:
            self.__lading = lading
            print('VrachtAuto van %s: %s ingeladen.' % (self.eigenaar,lading))

    def uitladen(self):
        ret = None
        if self.motor == 'aan':
            print('VrachtAuto van %s: motor aan. Eerst uitzetten.' % self.eigenaar)
        elif self.__lading == '(leeg)':
            print('VrachtAuto van %s: leeg. Kan niets uitladen.' % self.eigenaar)
        else:
            ret = self.__lading
            self.__lading = '(leeg)'
            print('VrachtAuto van %s: %s uitgeladen.' % (self.eigenaar,ret))
        return ret

    def toonLading(self):
        print('VrachtAuto van %s: lading = %s.' % (self.eigenaar,self.__lading))


#--- script ---

def testGarage():
    print(Auto.getGarage())
    Auto.setGarage('Van der Veen')
    print(Auto.getGarage())
    #print(Auto.__garage)           #AttributeError

def testAuto():
    a1 = Auto('Jan')
    a1.merk = 'Volvo'
    print('%s: merk is %s' % (a1.eigenaar,a1.merk))
    print('tank = %d, motor = %s' % (a1.tank, a1.motor))

    print()
    a1.tanken(30)       #hij doet: Auto.tanken(a1, 20)
    a1.tanken(20)
    print('%s: tank bevat %d liter' % (a1.eigenaar,a1.tank))

    a1.stoppen()        #motor staat al uit
    a1.starten()
    a1.starten()        #motor staat al aan
    a1.stoppen()

    print()
    a1.rijden()         #hij wil niet rijden, want motor nog uit...
    a1.starten()
    a1.rijden()
    a1.rijden()
    a1.rijden()
    print('%s: tank bevat %d liter' % (a1.eigenaar,a1.tank))

    print()    
    a1.sturen('linksaf')
    a1.rijden()
    a1.sturen('rechtdoor')
    a1.rijden()
    a1.stoppen()
    print('%s: tank bevat %d liter' % (a1.eigenaar,a1.tank))

    print('\nNu auto verkopen')
    a1.eigenaar = 'Greetje'
    print('%s: merk is %s' % (a1.eigenaar,a1.merk))

    print()
    print(a1)               #doet: a1.__str__()
    print(repr(a1))         #doet: a1.__repr__()
    print(Auto.__doc__)
    print(a1.__doc__)

def listAutos():
    #global lst
    lst = [Auto('John'), Auto('Paul'), Auto('Mary')]    #doet __repr__()
    #print(lst[0])       #doet __str__()
    #print(lst)

    lst[0].merk = 'Porsche'
    lst[0].tanken(38)
    lst[1].merk = 'BMW'
    lst[1].tanken(34)
    lst[2].merk = 'Trabant'
    lst[2].tanken(5)

    print()
    #del lst[1]
    lst.pop(1)              #idem, .pop(-1) is laatste auto (die van Marie)

    for a in lst:
        print(a)            #doet: print(a.__str__())
        #print(repr(a))
        a.starten()
        a.rijden()
        a.sturen("rechtdoor")
        a.rijden()
        a.stoppen()

def testVrachtAuto():
    print(VrachtAuto.__doc__)
    print('Garage:', Auto.getGarage())
    print('Garage:', VrachtAuto.getGarage())
    
    v1 = VrachtAuto('Vladimir')
    v1.merk = 'Daf'
    v1.toonLading()
    v1.inladen('25 koelkasten')
    v1.toonLading()
    v1.tanken(40)

    print()
    v1.starten()
    v1.rijden()
    v1.sturen('naar Kiev')
    v1.rijden()
    v1.rijden()
    lad = v1.uitladen()
    print('lad:', lad)
    v1.toonLading()
    v1.stoppen()
    lad = v1.uitladen()
    print('lad:', lad)
    v1.toonLading()

def testInstanceStaticMethod():
    a1 = Auto('Willemijn')
    a1.merk = 'Wolseley'
    a1.tanken(20)
    Auto.tanken(a1, 5)      #goed; instance als static method met a1 op plek van self
    print('%s: tank bevat %d liter' % (a1.eigenaar,a1.tank))

    print('Garage:', Auto.getGarage())     #goed
    # vlg gaat alleen goed als je boven getGarage() de annotatie @staticmethod zet
    #print(a1.getGarage())   #TypeError: getGarage() takes 0 positional arguments but 1 was given

    # bij vlg doet hij: Auto.setGarage(a1) ->zet a1 in static var __garage !!!
    a1.setGarage()              #dit gaat goed fout!
    print('Garage:', Auto.getGarage())     # <__main__.Auto object at 0x029B9BD0>

    Auto.setGarage('Morgen klaar!')     #dwz nooit klaar, want altijd morgen...
    print('Garage:', Auto.getGarage())

    #print(Auto.__garage)       #AttributeError, vanwege de __
    print('Garage:', Auto._Auto__garage)   #ah, wel goed...


testGarage()
#testAuto()
#listAutos()
#testVrachtAuto()
#testInstanceStaticMethod()

