from pcmaze import entrance, exit, connected

def leidt_naar_uitgang( komtvan, cel ):
    if cel == exit():
        return "{}".format( exit() )
    for i in range( entrance(), exit()+1 ):
        if i == komtvan:
            continue
        if not connected( cel, i ):
            continue
        check = leidt_naar_uitgang( cel, i )
        if check != "":
            return "{} -> {}".format( cel, check )
    return ""

check = leidt_naar_uitgang( 0, entrance() )
if check != "":
    print( "Pad gevonden!", check )
else:
    print( "Pad niet gevonden" )