from pcinput import getString

woord1 = getString( "Geef woord 1: " )
woord2 = getString( "Geef woord 2: " )
gemeen = ""
for letter in woord1:
    if (letter in woord2) and (letter not in gemeen):
        gemeen += letter

if gemeen == "":
    print( "De woorden hebben geen tekens gemeen." )
else:
    print( "De woorden delen de volgende tekens:", gemeen )