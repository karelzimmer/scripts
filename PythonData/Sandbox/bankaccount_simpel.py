# Oefening met class BankAccount

#static vars (=attributes) worden in class gedecl, instance vars in __init__ met self.myvar
#Python kent geen constanten
#private vars beginnen met __, verschijnen in dir(acc1) als _BankAccount__var
#client en afgeleide class kan __var niet zien; wel _BankAccount__var
#vars met _x zijn gewoon zichtbaar binnen de module
#ideologie Python: liever geen getters/setters gebruiken, attribs zijn publiek

class BankAccount:
    """Basisclass BankAccount, copyright Zwarte Piet"""
    
    overdraft = -500                      #static vars, op class niveau
    __nextid = 1                          #"geheime" var

    def getOverdraftLimit():                #static method, want self ontbreekt; PyCharm zeurt
        return BankAccount.overdraft

    def getBankName():
        return 'LIBOR-Trust Bank Ltd, Gibraltar'

    def __init__(self, name, balance=0.0):   #geen method overloading->gebr default args
        self.name = name                     #maak instance var
        self.balance = balance
        self.info = ''
        self.id = BankAccount.__nextid       #static var eist classname, anders UnboundLocalError
        BankAccount.__nextid += 1
        #print('__init__: %s, id = %d, naam = %s' % (BankAccount.getBankName(), self.id, self.name))

    def deposit(self, amount):
        if amount > 0.0:
            self.balance += amount
            return True                     #True = het ging goed
        else:
            return False

    def withdraw(self, amount):
        #mag 500 rood staan
        if amount > 0.0 and self.balance - amount > BankAccount.overdraft:
            self.balance -= amount
            return True
        else:
            return False

    def __str__(self):         #magic method, wordt gedraaid bij str(..) en print(..)
        return '%s heeft saldo %.2f' % (self.name, self.balance)

    def __repr__(self):        #wordt gedraaid bij repr(..) en intypen obj-naam in console en als __str__ ontbreekt
        return 'BankAccnt: id = %d, name = %s, balance = %.2f' % (self.id, self.name, self.balance)

    def __lt__(self, other):    #nodig voor sorteren
        return self.balance < other.balance


class SavingsAccount(BankAccount):
    """afgeleide class van BankAccount, copuright Sinterklaas"""
    
    interestrate = 2.3

    def __init__(self, name, balance=0.0):      #nieuwe __init__() in subclass is niet verplicht
        super().__init__(name, balance)         #hier MOET je self weglaten, want fn aanroep
        self.cumInterest = 0.0
        self.preferredBanking = False

    def withdraw(self, amount):         #overridden method
        #mag op spaarrekening niet rood staan, daarom override
        #overriden gaat op naam (uit __dict__), NIET op naam+args (signature)
        #dus: withdraw(self,amount,msg) komt niet naast, maar ipv withdraw(self,amount)
        if amount > 0.0 and self.balance > amount:
            return super().withdraw(amount)     #geeft True/False
        else:
            return False

    def computeInterest(self):
        interest = self.balance * SavingsAccount.interestrate * 0.01
        self.deposit(interest)
        self.cumInterest += interest
        return interest


#--- functies voor script ---

def test_bankaccounts():
    global acc1
    print('De bank is:', BankAccount.getBankName())
    acc1 = BankAccount('Joop', 350.25)
    acc1.info = 'trouwe klant'

    acc2 = BankAccount('Jaap')
    acc2.info = 'degelijke klant'
    acc2.deposit(260)

    print('%s: %.2f, info=%s' % (acc1.name, acc1.balance, acc1.info))
    print('%s: %.2f, info=%s' % (acc2.name, acc2.balance, acc2.info))

    #print(acc1)
    #print(acc2)
    #print(repr(acc1))
    #print(repr(acc2))

    totsaldo  = sum(acc.balance for acc in [acc1,acc2])
    print('totaalsaldo vd bank = %.2f' % totsaldo)

    print('\n%s neemt geld op:' % acc2.name)
    print('Geld opnemen gelukt:', acc2.withdraw(125))
    print('%s: %.2f' % (acc2.name, acc2.balance))
    print('Geld opnemen gelukt:', acc2.withdraw((950)))
    print('%s: %.2f' % (acc2.name, acc2.balance))

    totsaldo  = sum(acc.balance for acc in [acc1,acc2])
    print('totaalsaldo vd bank = %.2f' % totsaldo)

    print('\nWie heeft meer geld op zijn rekening staan?')
    if acc1 > acc2:
        print(acc1)
    else:
        print(acc2.name)

def test_savingsaccount():
    print('\n--savingsaccount Els:')
    sacc1 = SavingsAccount('Els', 1270)

    print(sacc1.info)           #wordt lege regel, want bevat ''
    sacc1.info = 'Geheime spaarrekening in Zwitserland'
    print(sacc1)
    print('%s: %.2f, info=%s' % (sacc1.name, sacc1.balance, sacc1.info))

    print('%s heeft preferredBanking: %s' % (sacc1.name, sacc1.preferredBanking))
    sacc1.preferredBanking = True
    print('%s heeft preferredBanking: %s' % (sacc1.name, sacc1.preferredBanking))

    sacc1.deposit(50000)

    rente = sacc1.computeInterest()
    print('%s kreeg rente: %.2f' % (sacc1.name,rente))
    rente = sacc1.computeInterest()
    print('%s kreeg rente: %.2f' % (sacc1.name,rente))
    print('%s heeft cumulatieve rente: %.2f' % (sacc1.name,sacc1.cumInterest))
    print('%s neemt op van spaarrekening: %s' % (sacc1.name,sacc1.withdraw(375)))

    print(isinstance(sacc1, SavingsAccount))        #True
    print(isinstance(sacc1, BankAccount))           #True
    print(issubclass(SavingsAccount, BankAccount))  #True
    print(issubclass(SavingsAccount, object))       #True; niet: Object

#--- script ---

#test_bankaccounts()
test_savingsaccount()

