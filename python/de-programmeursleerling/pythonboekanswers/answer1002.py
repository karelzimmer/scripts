tekst = """En ze stu[re]n [i]ngekleurde prentbriefkaarten van 
plekken waarvan ze zich niet reali[s]eren dat ze er nooit 
geweest zijn [a]an 'Iedereen op nummer 22, weer is prachti[g], 
onz[e] kamer is aa[n]gekruisd. Missen jullie. E[t]en[ ]i[s] 
vettig, maar we hebben een geweldig leuk restaurantje gevonden 
in de achterstraatjes waar ze Heine[ke]n hebben en kaas en 
uien chips en iemand die "Een beetje verliefd" speel[t] op een 
a[c]cordeon' en je zit vier dagen vast op Schip[h]ol voor je 
vijfdaagse vliegvakantie met niks anders te eten dan 
uitgedroogde voorverpakte boterhammen..."""

start = -1
while True:
    start = tekst.find( "[", start+1 )
    if start < 0:
        break
    eind = tekst.find( "]", start )
    if eind < 0:
        break
    print( tekst[start+1:eind], end="" )
    start = eind 
print()