import sys

# 3 variabelen die de command line parameters bevatten
invoer = "input.txt"
uitvoer = "output.txt"
shift = 3

# Verwerken van command line parameters
# (werkt met 0, 1, 2, of 3 parameters)
if len( sys.argv ) > 1:
    invoer = sys.argv[1]
if len( sys.argv ) > 2:
    uitvoer = sys.argv[2]
if len( sys.argv ) > 3:
    try:
        shift = int( sys.argv[3] )
    except TypeError:
        print( sys.argv[3], "is geen getal." )
        sys.exit(1)