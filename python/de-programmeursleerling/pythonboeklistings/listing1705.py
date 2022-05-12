fruitlist = ["appel", "banaan", "kers"]
try:
    num = input( "Geef een getal: " )
    if "." in num:
        num = float( num )
    else:
        num = int( num )
    print( fruitlist[num] )
except:
    print( "Er ging iets fout" )    