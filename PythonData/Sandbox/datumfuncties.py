# datumfuncties
# gebr in tstdatumfuncties

# 1904 is geldig schrikkeljaar, want 1904 % 4 == 0 en 1904 % 100 != 0
# 1900 is ongeldig, want 1900 % 4 == 0 (goed) en 1900 % 100 == 0 (fout)
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def getDaysInMonth(month,year):
    if month == 2:
        maxDay = 29 if isLeapYear(year) else 28
    elif month in (1,3,5,7,8,10,12):
        maxDay = 31
    else:
        maxDay = 30
    return maxDay

def isValidDate(day,month,year):
    numDays = getDaysInMonth(month,year)
    return day >= 1 and day <= numDays and month >= 1 and month <= 12 and year >= 0

def monthName(month):
    if 1 <= month <= 12:
        mnd = ('dummie','jan','feb','mrt','apr','mei','jun','jul','aug','sep','okt','nov','dec')
        return mnd[month]
    else:
        return None

def printMonthName(month):
    print(monthName(month))

#--- script ---

if __name__ == "__main__":
    print("test datumfuncties.py")
    print(__name__)
    printMonthName(5)
    print(isValidDate(29,2,2020))
