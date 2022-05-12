from pcinput import getFloat

grade = getFloat( "Geef een cijfer: " )
check = int( grade * 10 )
if grade < 0 or grade > 10:
    print( "Cijfers liggen tussen 0 en 10." )
elif check%5 != 0 or check != grade*10:
    print( "Cijfers zijn afgerond op halve punten." )
elif grade >= 8.5:
    print( "A" )
elif grade >= 7.5:
    print( "B" )
elif grade >= 6.5:
    print( "C" )
elif grade >= 5.5:
    print( "D" )
else:
    print( "F" )