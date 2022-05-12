import sys

totaal = 0
for i in sys.argv[1:]:
    try:
        totaal += float( sys.argv[i] )
    except TypeError:
        print( sys.argv[i], "is geen getal." )
        sys.exit(1)

print( "The arguments add up to", totaal )