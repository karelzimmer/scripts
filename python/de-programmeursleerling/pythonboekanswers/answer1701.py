numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int( input( "Geef een index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ValueError:
    print( "Je gaf geen geheel getal" )
except IndexError:
    print( "De index moet tussen -5 en 4 liggen" )
except ZeroDivisionError:
    print( "Het lijkt erop dat de list een 0 bevat" )
except TypeError:
    print( "Het lijkt erop er een niet-numeriek element is" )
except:
    print( "Iets onverwachts is gebeurd" )
    raise