from pcmaze import entrance, exit, connected

def leidt_naar_uitgang( komtvan, cel ):
    if cel == exit():
        return True
    for i in range( entrance(), exit()+1 ):
        if i == komtvan:
            continue
        if not connected( cel, i ):
            continue
        if leidt_naar_uitgang( cel, i ):
            print( cel, "->", i )
            return True
    return False

if leidt_naar_uitgang( 0, entrance() ):
    print( "Pad gevonden!" )
else:
    print( "Pad niet gevonden" )