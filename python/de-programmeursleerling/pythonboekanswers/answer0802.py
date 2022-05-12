from pcinput import getString

# gemeen krijgt twee strings als parameters. Het retourneert
# het aantal tekens dat de strings gemeen hebben.
def gemeen( w1, w2 ):
    tekens = ""
    for letter in w1:
        if (letter in w2) and (letter not in tekens):
            tekens += letter
    return len( tekens )

woord1 = getString( "Geef woord 1: " )
woord2 = getString( "Geef woord 2: " )

num = gemeen( woord1, woord2 )
if num <= 0:
    print( "De woorden delen geen tekens." )
elif num == 1:
    print( "De woorden hebben 1 teken gemeen" )
else:
    print( "De woorden hebben", num, "tekens gemeen" )