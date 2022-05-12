try:
    print( 3 / int( input( "Geef een getal: " ) ) )
except ZeroDivisionError:
    print( "Je kunt niet delen door nul" )
except ValueError:
    print( "Je gaf geen getal" )
except:
    print( "Iets onverwachts ging fout" )
print( "Tot ziens!" )