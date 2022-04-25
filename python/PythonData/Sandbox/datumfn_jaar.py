# datumfuncties
# gebr in tstdatumfn_jaar


huidigJaar = 2016    #twee globale variabelen
_vorigJaar = 2015    #deze alleen onzichtbaar via: from datumfn_jaar import *

def toonHuidigJaar():
    print('toonHuidigJaar: huidigJaar=', huidigJaar)

def toonVorigJaar():
    print('toonVorigJaar: vorigJaar=', _vorigJaar)

#------- testcode:

#voorkom dat onderstaande code draait als deze module geimporteerd wordt
#print(__name__)
if __name__ == "__main__":
    print('---Dit is in datumfn_jaar.py---')
    dag = 27
    mnd = 0
    jr = 2017

    print(huidigJaar)
    toonHuidigJaar()

