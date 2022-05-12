from datetime import datetime, timedelta

ditjaar = datetime.now().year
xmasditjaar = datetime( ditjaar, 12, 25, 23, 59, 59 )
dezedag = datetime.now()
dagen = xmasditjaar - dezedag

if dagen.days < 0:
    print( "Kerst komt volgend jaar weer." )
elif dagen.days == 0:
    print( "Het is Kerst!" )
else:
    print( "Slechts", dagen.days, "dagen tot Kerst!" )