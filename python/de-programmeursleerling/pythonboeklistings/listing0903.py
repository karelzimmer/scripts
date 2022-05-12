from pcmaze import entrance, exit, connected

def leidt_naar_uitgang( komtvan, cel, diepte ):
    inspringing = diepte * 4 * " "
    if cel == exit():
        return True
    for i in range( entrance(), exit()+1 ):
        if i == komtvan:
            continue
        if not connected( cel, i ):
            continue
        print( inspringing + "Controleer", cel, "->", i )
        if leidt_naar_uitgang( cel, i, diepte + 1 ):
            print( inspringing + "Pad gevonden:", cel, "->", i )
            return True
    return False

if leidt_naar_uitgang( 0, entrance(), 0 ):
    print( "Pad gevonden!" )
else:
    print( "Pad niet gevonden" )