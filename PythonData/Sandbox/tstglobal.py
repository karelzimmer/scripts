# je mag binnen een fn verwijzen naar een glob var voor uitlezen, maar niet direct
# voor wijzigen; wil je de glob var wijz binnen de fn, dan moet je hem binnen de
# fn declareren met het keyword global

_mini = 100            #deze var is vanwege _ pseudo private binnen module; bij import in andere module niet zichtbaar
maxi = 1000             #deze var is bij import wel zichtbaar in andere modules
turbo = 0

def toonMaxi():
    print('toonMaxi: maxi=', maxi)


def testGlobal():
    #maxi = 25
    global maxi, turbo, _mini
    print('testGlobal: _mini=', _mini)     #global var uitlezen ook goed zonder global decl
    print('testGlobal: maxi=', maxi)       #idem, maar wel warning:
    # SyntaxWarning: name 'maxi' is used prior to global declaration
    # beter: eerst global decl, daarna uitlezen en/of wijzigen

    #global maxi             #met deze erbij gaat maxi += 2 goed
    maxi = 1002               #global var wijzigen eist decl global ...
    #zonder global decl krijg je UnboundLocalError
    # op regel: print('testGlobal: maxi=', maxi)
    #bij het compileren loopt hij dus je hele code door en zet alle
    #door jou gemaakte locale vars bovenaan in de functie
    print('testGlobal: maxi=', maxi)       #idem

    #global turbo
    turbo = 6               #creëer glob var turbo die nog niet gedef is in module
			    #(onduidelijke code!)
    print('testGlobal: turbo=', turbo)

#de globale var's mag je ook hier decl

#---------- hoofdprogramma

print('maxi=', maxi)
#print('turbo=', turbo)         #NameError, turbo onbekend
toonMaxi()
testGlobal()            #deze fn creeert met global-decl de global var turbo
print('maxi=', maxi)
toonMaxi()
print('turbo=', turbo)

#de globale var's mogen NIET hier
