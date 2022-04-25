# datumfuncties2
# andere versie van functie monthName() uit datumfuncties
# gebr in tstdatumfuncties

def monthName(month):
    if 1 <= month <= 12:
        mnd = ('dummie','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
        return mnd[month]
    else:
        return None

