#class, subclass, magic methods, @property decorator,
# __getattr__() enz, __getattribute__(),
# descriptor class met __get__() enz

"""
static vars (=attributes) worden in class gedecl, instance vars in __init__ met self.myvar
Python kent geen constanten
private vars beginnen met __, verschijnen in dir(acc1) als _BankAccount__var
client en afgeleide class kan __var niet zien; wel _BankAccount__var
vars met _x zijn gewoon zichtbaar binnen de module
ideologie Python: liever geen getters/setters gebruiken, attribs zijn publiek

geen sealed classes; kan wel metaclass maken en daarin error genereren. gedoe
(zie: http://stackoverflow.com/questions/16564198/pythons-equivalent-of-nets-sealed-class)
overriden gaat op fn naam (zit in __dict__), niet op fn signature

descriptor class:
bepaalde static vars van doel-class SavingsAccount krijgen instance van
descriptor class CreditCard; per static var een singleton instance
->bij 6 instances v SavingsAccount steeds hetzelfde CreditCard-obj
-> de __get__(..) enz zijn instance vd single CreditCard
   krijgen een SavingsAccount-obj mee als 2e arg (na self)

"controlling the dot"
Je gebruikt deze static vars als get/set/del voor instance vars, dus:
sacc1.creditcardNumber = "123456"
in wlh is creditcardNumber een CreditCard-obj
->hij doet: SavingsAccount.creditcardNumber.__set__(sacc1, "123456")
Je mag __delete__ en __get__ of __set__ weglaten, bv alleen setter doen.

Het is het handigst voor ieder type value een aparte validator class te maken;
heb ik NIET gedaan. Bij mij valideert CreditCard 2 verschillende typen props,
nl creditcardNumber (str) en creditcardLimit (float), die ook nog onderling
afh zijn (ccLimit alleen geldig als ccNumber is ingevuld). Daardoor is
CreditCard sterk gebonden aan SavingsAccount en niet zo goed.

Beter is om een descriptor-class voor globale validatie-opties te maken,
bv: value >= 0.0 bij een LineItem class, voor props qty, price, weight, enz.
->worden globale getters/setters, die instance v doel-class meekrijgen.

Locale getter/setter validatie kun je beter maken via @property.
Daarachter zit de ingebouwde fn property(..), die weer een ctor is van
class property, die een descriptor is met __get__(..) enz.

Het descriptor-obj moet de value van __set__() ergens bewaren:
* [a] in de meegegeven instance
  gevolg: type(instance).__dict__ heeft 'myprop' (bevat descriptor-obj)
  EN instance.__dict__ heeft 'myprop' (bevat waarde;
* [b] in eigen dict met instance als key en list v (attrib,value) tupels
  nadeel: descriptor bewaart instance refs in eigen dict ->garbage coll prb.

In beide gevallen moet je tevoren aan de __init__() v descriptor-obj vertellen
bij welke prop/var van doel-obj hij hoort; dat wordt nl NIET meegegeven
aan de __set__() method.
"""

class CreditCard:       #wordt descriptor
    # voor class-props: creditcardNumber, creditcardLimit
    # voorkom recursie door in __get__() NIET instance.myprop
    # of getattr(instance,'myprop') te doen ->die doen __getattribute__()
    # en die doet weer in je descriptor __get__().
    # doe: instance.__dict__.get('myprop') ->okee + None bij geen key
    # doe in __set__(): instance.__dict__['myprop'] = value
    # of: andere propnamen gebr, bv: _cardNumber, _cardLimit;
    # nadeel: je kan deze vanuit main benaderen via sacc1._cardNumber,
    # terwijl sacc1.creditcardNumber ALTIJD via de descriptor loopt.
    # ( props wel altijd te vinden via dict: vars(sacc1) )
    # of: maak eigen propnamen met volgnr; dat wordt globaal vlgnr;
    # dus als je 30 instances maakt met ieder 5 props ->150 vlgnrs.
    # of: bewaar vlgnrbase in instance en verhoog steeds deze
    # ->per doel-obj nieuwe volgnrs!
    # (werkt niet als de props onderling afh zijn, zoals hier)

    def __init__(self, attrib):
        self.attrib = attrib

    def __get__(self, instance, owner):
        #print("## CreditCard:", instance, owner.__name__)
        if instance.__dict__.get('creditcardNumber') is None:
            return None
        return instance.__dict__.get(self.attrib)
        # vlg niet goed wegens gevaar recursie:
        #if getattr(instance, '_cardNumber', None) is None:
        #    return None
        #return getattr(instance, self.attrib)

    def __set__(self, instance, value):
        if self.attrib == 'creditcardNumber':
            value = str(value)
            if len(value) >= 5:
                instance.__dict__['creditcardNumber'] = value
                instance.__dict__['creditcardLimit'] = 0
                #instance._cardNumber = value
                return
            else:
                raise ValueError("Invalid value '%s'" % value)

        if instance.__dict__.get('creditcardNumber') is None:
            raise AttributeError("No valid creditcard")
        
        if self.attrib == 'creditcardLimit':
            if 0 <= value <= 1000:
                instance.__dict__['creditcardLimit'] = value
            else:
                raise ValueError("Invalid limit '%s'" % value)

    def __delete__(self, instance):
        if self.attrib != 'creditcardNumber':
            raise AttributeError("Cannot delete '%s'" % self.attrib)
        instance.__dict__['creditcardNumber'] = None
        #instance._cardNumber = None
        #setattr(instance, '_cardNumber', None)


class BankAccount:
    """Basisclass BankAccount, copyright Zwarte Piet"""
    
    __nextid = 1
    __overdraft = -500                      #static var, op class niveau
    country = "UK"

    #print("Ennnnn dit is BankAccount")     #wordt 1* gedraaid, bij inlezen class

    def getOverdraftLimit():                #static method, want self ontbreekt; PyCharm zeurt
        return BankAccount.__overdraft

    @staticmethod           #->mag aanroepen met obj.|self.getBankName()
    def getBankName():
        return 'LIBOR-Trust Bank Ltd, Gibraltar'

    def __init__(self, name, balance=0.0):   #geen method overloading->gebr default args
        self.__name = name                   #__var's zijn private; mk instance var
        self.__balance = balance            #niet zichtbaar in afgeleide class!
        self.info = ''
        self.__id = BankAccount.__nextid     #static var eist classname of self, anders UnboundLocalError
        BankAccount.__nextid += 1
        print('__init__: %s, id = %d, naam = %s' % (self.getBankName(), self.getId(), self.getName()))
        # doordat je decoration @staticmethod decl, mag je self.getBankName()
        # ipv BankAccount.getBankName() gebr
        # @classmethod ->getBankName(cls) met code: cls.__nextid

    def deposit(self, amount):
        if amount > 0.0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        #mag 500 rood staan
        if amount > 0.0 and self.__balance - amount > BankAccount.__overdraft:
            self.__balance -= amount
            return True
        else:
            return False

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getBalance(self):
        return self.__balance

    def __str__(self):         #magic fn, wordt gedraaid bij str(..) en print(..)
        #return 'BankAccount: %s heeft saldo %.2f' % (self.__name, self.__balance)
        return '%s: %s heeft saldo %.2f' % (type(self).__name__, self.__name, self.__balance)

    def __repr__(self):        #wordt gedraaid bij repr(..) en intypen obj-naam in console en als __str__ ontbreekt
        return 'BankAccnt: id = %d, name = %s, balance = %.2f' % (self.__id, self.__name, self.__balance)

    def __lt__(self, other):    #nodig voor sorteren
        return self.__balance < other.__balance


class SavingsAccount(BankAccount):
    """Afgeleide class van BankAccount, copyright Sinterklaas"""
    
    __INTERESTRATE = 2.3
    creditcardNumber = CreditCard('creditcardNumber')
    creditcardLimit = CreditCard('creditcardLimit')

    def __init__(self, name, balance=0.0):      #nieuwe __init__() in subclass is niet verplicht
        super().__init__(name, balance)         #hier MOET je self weglaten, want fn aanroep
        self.__cumInterest = 0.0
        self.__prefBanking = False
        #self.__hasCreditCard = False

    def withdraw(self, amount):         #overridden method
        #mag op spaarrekening niet rood staan, daarom override
        #overriden gaat op naam (uit __dict__), NIET op naam+args (signature)
        #dus: withdraw(self,amount,msg) komt niet naast, maar ipv withdraw(self,amount)
        #mag niet: self.__balance of super().__balance
        #-> AttributeError: SavingsAccount heeft geen _SavingsAccount__balance
        if amount > 0.0 and self.getBalance() > amount:
            return super().withdraw(amount)     #geeft True of False
        else:
            return False

    def computeInterest(self):
        interest = self.getBalance() * SavingsAccount.__INTERESTRATE * 0.01
        self.deposit(interest)
        self.__cumInterest += interest
        return interest

    def getCumulativeInterest(self):
        return self.__cumInterest

    # getter en setter:
    # Python ideologie: liever GEEN getters/setter gebruiken
    # ->"In Python zijn attributen public"
    # de getter MOET @property decorator hebben; maak je een tweede getter
    # met @preferredBanking.getter, dan wordt die aangeroepen ipv de eerste
    
    # @property zet fn om in propget, bv size ipv size()
    # met .setter kun je daarnaast een propset maken
    # zonder .deleter kan je niet del doen ->AttributeError, cannot delete

    # vlg kunnen ook met ingebouwde fn property:
    #preferredBanking = property(fget, fset, fdel, doc)

    @property
    def preferredBanking(self):
        return self.__prefBanking

    @preferredBanking.setter
    def preferredBanking(self, value):
        if not value:
            self.__prefBanking = False
        elif value and self.getBalance() > 50000:
            self.__prefBanking = True

    @preferredBanking.deleter   #bij del sacc1.preferredBanking, als geen __delattr__()
    def preferredBanking(self):
        self.__prefBanking = False

    # vlg wordt ALLEEN aangeroepen voor onbekende attribs
    # (worden dynamische pseudo-props)
    def __getattr__(self, attrib):
        if attrib == "allowCreditCard":
            return self.getBalance() >= 1000
        elif attrib == "email":
            return "%s@libortrust.co.uk" % self.getName()
        # zonder vlg retval None bij onbekend attrib
        else:
            raise AttributeError("'SavingsAccount' object has no attribute '%s'"
                % attrib)

    """
    # vlg wordt ALTIJD aangeroepen voor alle props, NIET fn's ->vertraagt enorm
    def __setattr__(self, attrib, value):
        print("+", attrib, "<-", value)
        # vlg MOET, anders krijgen attribs geen waarde ->overal errors
        super().__setattr__(attrib, value)

    # vlg wordt ALTIJD aangeroepen, heeft voorrang boven prop deleter
    def __delattr__(self, attrib):
        print("-", attrib, "<--del-")

    # vlg wordt ALTIJD aangeroepen, ook intern, voor ALLE fn's en props
    # (intern: om attribs uit attrib-dict te halen)
    def __getattribute__(self, attrib):
        print("?", attrib)
        return super().__getattribute__(attrib)
    """



#--- globals en functies voor script ---

acc1 = None
acc2 = None
sacc1 = None

def laad_globals():
    global acc1, acc2, sacc1
    acc1 = BankAccount('Joop', 350.25)
    acc1.info = 'trouwe klant'

    acc2 = BankAccount('Jaap')
    acc2.info = 'degelijke klant'
    acc2.deposit(260)

    sacc1 = SavingsAccount('Els', 1270)

def classinfo_BankAccount():
    print("\nfn classinfo_BankAccount():")
    print(acc1)             #doet acc1.__str__(), anders __repr__()
    print(acc2)             #als geen v beide, dan: <__main__.BankAccount object at 0x02A84FF0>
    print(repr(acc1))
    print(repr(acc2))

    print()
    print(BankAccount.__doc__)
    print(BankAccount.__name__)         #BankAccount
    print(BankAccount.__module__)       #__main__
    print(BankAccount.__class__)        #<class 'type'>, dwz het type v class-type
    print(BankAccount.__bases__)        #(<class 'object'>,), tupel v base classes

    #print(BankAccount.__dict__)         #dict, alle class vars + fn's met waarden
    #print(acc1.__dict__)                #dict, alle instance vars met waarden
    #print(dir(BankAccount))             #kist, alle attribs
    #print(dir(acc1))
    print("class - instance:", set(dir(BankAccount))-set(dir(acc1)))    #leeg
    print("instance - class:", set(dir(acc1))-set(dir(BankAccount)))
    #->{'_BankAccount__balance', '_BankAccount__id', 'info', '_BankAccount__name'}

    #print(acc1.__name__)       #AttributeError, alleen voor classes
    #print(acc1.__bases__)      #AttributeError, idem
    print(acc1.__class__)       #<class '__main__.BankAccount'>
    #print(type(acc1))           #<class '__main__.BankAccount'>
    print(acc1.__class__.__name__)     #BankAccount
    #print(type(acc1).__name__)         #BankAccount

    #print("\nhelp(BankAccount):")
    #help(BankAccount)       #docstr + fn's + class vars excl __nexid enz

    print("\nsacc1:")
    print(sacc1.__dict__)   #instance vars, incl base class;
    # toont niet dyn props: preferredBanking, allowCreditCard, email

    print(isinstance(sacc1, SavingsAccount))        #True
    print(isinstance(sacc1, BankAccount))           #True
    print(issubclass(SavingsAccount, BankAccount))  #True
    print(issubclass(SavingsAccount, object))       #True; niet: Object

    #print(sacc1 is BankAccount)                     #False, bedoeld voor identieke ptrs

def classwide_props_methods():
    print('acc1.country:', acc1.country)                #goed, UK
    print('BankAccount.country:', BankAccount.country)  #goed, UK
    acc1.country = "Spain"     #mkt nwe instance attrib, alleen voor acc1
    print('acc2.country:', acc2.country)                #UK
    BankAccount.country = "Marocco"
    print('acc1.country:', acc1.country)                #Spain
    print('acc2.country:', acc2.country)                #Marocco
    del acc1.country
    print('acc1.country:', acc1.country)                #Marocco
    print('acc2.country:', acc2.country)                #Marocco

    print()
    print('bankname:', BankAccount.getBankName())     #static/class method
    print('bankname:', acc1.getBankName())       #gaat goed wegens @staticmethod
    print('overdraftlimit:', BankAccount.getOverdraftLimit())
    #print('overdraftlimit: %d' % acc1.getOverdraftLimit())     #TypeError: teveel args meegegeven

def geldopnemen_enz_BankAccount():
    print('\n--geld opnemen, enz:')
    totsaldo  = sum(x.getBalance() for x in [acc1,acc2])
    print('totaalsaldo vd bank = %.2f' % totsaldo)

    print('%s: %.2f, info=%s' % (acc1.getName(), acc1.getBalance(), acc1.info))
    print('%s: %.2f, info=%s' % (acc2.getName(), acc2.getBalance(), acc2.info))
    print('Geld opnemen gelukt:', acc2.withdraw(125))
    print('%s: %.2f, info=%s' % (acc2.getName(), acc2.getBalance(), acc2.info))
    print('Geld opnemen gelukt:', acc2.withdraw((950)))
    print('%s: %.2f, info=%s' % (acc2.getName(), acc2.getBalance(), acc2.info))

    totsaldo  = sum(x.getBalance() for x in [acc1,acc2])
    print('totaalsaldo vd bank = %.2f' % totsaldo)

def list_bank_saving():
    print('\n--list met bankaccounts en savingsaccount:')
    lst = [acc1, acc2, BankAccount("Gerdie", 150)]
    lst[2].info = "heeft modewinkel"
    lst[2].withdraw(340)

    lst.append(sacc1)

    for a in lst:
        print(a, a.info)

    print('\nomgekeerd sorteren op saldo:')
    #vlg gaat alleen goed als je __lt__() implementeert in BankAccount
    #anders: TypeError: unorderable types: BankAccount() < BankAccount()
    lst.sort(reverse=True)
    for a in lst:
        print(a)

    print('\ngewoon sorteren op naam:')
    lst.sort(key=lambda ac : ac.getName())
    for a in lst:
        print(a)

def list_bank_copy():
    import copy
    
    lst1 = [acc1, acc2, sacc1]
    print("\nid's lst1:")
    for a in lst1:
        print(id(a), end=' ')

    print("\n\nna lst2 = lst1:")
    lst2 = lst1
    print("lst1 is lst2:", lst1 is lst2)
    print("lst1 == lst2:", lst1 == lst2)
    print("id's lst2:")
    for a in lst2:
        print(id(a), end=' ')

    print("\n\nna lst2 = lst1.copy():")
    lst2 = lst1.copy()
    #lst2 = list(lst1)
    #lst2 = lst1[:]
    #lst2 = copy.copy(lst1)
    print("lst1 is lst2:", lst1 is lst2)
    print("lst1 == lst2:", lst1 == lst2)
    print("id's lst2:")
    for a in lst2:
        print(id(a), end=' ')

    print("\n\nna lst2 = copy.deepcopy(lst1):")
    lst2 = copy.deepcopy(lst1)
    print("lst1 is lst2:", lst1 is lst2)
    print("lst1 == lst2:", lst1 == lst2)
    print("id's lst2:")
    for a in lst2:
        print(id(a), end=' ')

    print("\n\nlst1 accounts:")
    for a in lst1:
        #print(a)
        print(repr(a))

    print("\nlst2 accounts:")
    for a in lst2:
        #print(a)
        print(repr(a))
        
def info_SavingsAccount():
    print("\sacc1.info:")
    #print(sacc1.info)           #wordt lege regel, want bevat ''
    sacc1.info = 'Geheime spaarrekening in Zwitserland'
    print(sacc1.info)
    print(sacc1)

    print('preferredBanking:', sacc1.preferredBanking)
    print("zet preferredBanking=True bij te laag saldo:")
    sacc1.preferredBanking = True       #wordt alleen gezet als balance > 50000
    print('preferredBanking:', sacc1.preferredBanking)
    sacc1.deposit(50000)
    print('zet preferredBanking=True na deposit met saldo:', sacc1.getBalance())
    sacc1.preferredBanking = True
    print('preferredBanking:', sacc1.preferredBanking)

    # vlg geeft zonder .deleter een AttributeError: can't delete attribute
    # (maar __delattr__(..) heeft voorrang boven de deleter)
    del sacc1.preferredBanking      #.deleter zet False ipv del attrib
    print('na del sacc1.preferredBanking: %s' % (sacc1.preferredBanking))

    print("\ninfo, allowCreditCard, email, city:")
    try:
        print(sacc1.info)
        print(sacc1.allowCreditCard)
        print(sacc1.email)
        print(sacc1.city)
    except AttributeError as ex:
        print("AttributeError:", ex)

    #del sacc1.info         #draait __delattr__(..) indien aanwezig
    
    print("\ndescriptor class CreditCard:")
    print(sacc1.creditcardNumber)       #None
    print(sacc1.creditcardLimit)        #None

    #sacc1.creditcardLimit = 500        #door mij gegen AttributeError
    sacc1.creditcardNumber = "123456"
    print(sacc1.creditcardNumber)       #123456
    print(sacc1.creditcardLimit)        #0
    #sacc1.creditcardLimit = 1400        #door mij gegen ValueError
    sacc1.creditcardLimit = 700
    print(sacc1.creditcardNumber)       #123456
    print(sacc1.creditcardLimit)        #700

    #del sacc1.creditcardLimit          #door mij gegen AttributeError
    del sacc1.creditcardNumber
    print(sacc1.creditcardNumber)       #None
    print(sacc1.creditcardLimit)        #None

def geldopnemen_enz_SavingsAccount():
    sacc1.deposit(50000)
    print(sacc1)

    print("\ncomputeInterest:")
    rente = sacc1.computeInterest()
    print('%s kreeg rente: %.2f' % (sacc1.getName(),rente))
    rente = sacc1.computeInterest()
    print('%s kreeg rente: %.2f' % (sacc1.getName(),rente))
    print('%s heeft cumulatieve rente: %.2f' % (sacc1.getName(),sacc1.getCumulativeInterest()))
    print('%s neemt op van spaarrekening: %s' % (sacc1.getName(),sacc1.withdraw(375)))

def lees_hidden_attrib():
    print("\nfn lees_hidden_attrib():")
    #print(acc1.__balance)       #AttributeError: 'BankAccount' object has no attribute '__balance'
    print(acc1._BankAccount__balance)

    print(acc1)
    acc1.__balance = 5.05		#LET OP: mkt nw attrib __balance
    print('acc1:', acc1.__balance)
    print(acc1)
    print(dir(acc1))
    del acc1.__balance

def attrib_toevoegen():
    print("\nfn attrib_toevoegen():")
    print('\n--achteraf attrib toevoegen aan object:')
    acc1.stad = 'Almelo'        #goed; manier 1
    print(acc1.stad)
    #print(acc2.stad)            #AttributeError: 'BankAccount' object has no attribute 'stad'
    BankAccount.rente = 5.3
    print("BankAccount.rente = %f" % BankAccount.rente)

    setattr(acc2, 'stad', 'Hengelo')    #goed; manier 2
    print(acc2.stad)
    #acc2['stad'] = 'Hengelo'    #TypeError: 'BankAccount' object does not support item assignment
    #als je __setitem__ zou implementeren, zou het wel goed gaan...

    delattr(acc1, 'stad')       #je mag ook bv acc1.info deleten
    del acc2.stad               #idem

    if hasattr(acc1, 'stad'):
        print('acc1.stad=', acc1.stad)
    else:
        print('acc1.stad bestaat niet')

    #del acc1.info               #goed
    #print(acc1.info)            #geeft nu AttributeError

    print('\n--achteraf instance method toevoegen aan class en object (beetje vies):')
    # de lambda expr doet een return print(..); retval wordt None
    # niet: self.__name, want AttributeError
    BankAccount.sayHello = lambda self : print("Hello %s!" % self.getName())
    acc1.sayHello()
    #print(acc1.sayHello())     #deze drukt eerst Hello ... af en daaronder None
    acc1.hi = lambda : print("Hi!")     #nog viezer: obj method bij 1 instance
    #acc1.hi = lambda : print("Hi", BankAccount.getName(acc1))
    acc1.hi()
    #BankAccount.hi()      #AttributeError: 'BankAccount' object has no attribute 'hi'
    #acc2.hi()              #idem
    BankAccount.ho = lambda : print("Ho!")      #class method
    BankAccount.ho()

#--- script ---

laad_globals()

classinfo_BankAccount()
#classwide_props_methods()

#geldopnemen_enz_BankAccount()
#list_bank_saving()
#list_bank_copy()

#info_SavingsAccount()
#geldopnemen_enz_SavingsAccount()

#lees_hidden_attrib()
#attrib_toevoegen()

