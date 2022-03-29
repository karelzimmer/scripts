# datumfuncties
# gebr in tstdatumfuncties

# 1904 is geldig schrikkeljaar, want 1904 % 4 == 0 en 1904 % 100 != 0
# 1900 is ongeldig, want 1900 % 4 == 0 (goed) en 1900 % 100 == 0 (fout)
def isSchrikkelJaar(jaar):
    return jaar % 400 == 0 or (jaar % 4 == 0 and jaar % 100 != 0)

def getDagenInMaand(maand, jaar):
    if maand == 2:
        maxDag = 29 if isSchrikkelJaar(jaar) else 28
    elif maand in (4,6,9,11):
        maxDag = 30
    else:
        maxDag = 31
    return maxDag

def isGeldigeDatum(dag, maand, jaar):
    """Test datum, rekent met schrikkeljaar; ret: bool"""
    
    maxDag = getDagenInMaand(maand, jaar)
    #return dag >= 1 and dag <= maxDag and maand >= 1 and maand <= 12 and jaar >= 0
    return 1 <= dag <= maxDag and 1 <= maand <= 12 and jaar >= 0

#extra functie
def maandNaam(maand):
    if 1 <= maand <= 12:
        mnd = ('dummie','jan','feb','mrt','apr','mei','jun','jul','aug','sep','okt','nov','dec')
        return mnd[maand]
    else:
        return None

def printMaandNaam(maand):
    print(maandNaam(maand))

if __name__ == "__main__":
    print("Dit is datumfuncties, __name__ =", __name__)
    print(isSchrikkelJaar(2001))
    #print(getDagenInMaand(4, 2007))
    #print(isGeldigeDatum(29, 2, 2000))
    #print(isGeldigeDatum(30, 2, 2000))
    #print(maandNaam(3))

