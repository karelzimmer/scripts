# datumfuncties2
# gebr in tstdatumfn_jaar
# kijk wat er gebeurt bij dubbele import datumfn_jaar, datumfn_jaar2

huidigJaar = 1961    #twee globale variabelen
_vorigJaar = 1960    #deze alleen onzichtbaar via: from datumfn_jaar2 import *

def toonHuidigJaar():		#test ook met toonHuidigJaar2()
    print('toonHuidigJaar (2): huidigJaar=', huidigJaar)

def tralala():
    print("tralala, hopsasa (2)")

