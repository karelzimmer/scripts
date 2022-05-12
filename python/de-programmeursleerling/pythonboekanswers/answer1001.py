text = """En Sint Atilla hief de handgranaat ten hemel, en
zeide, "O Here, zegen deze handgranaat, zodat daarmee u uw
vijanden tot kleine stukjes kunt blazen, in uwer genade."
En de Here grinnikte. En het volk laafde zich aan lammeren,
en luiaards, en karpers, en anchovis, en orang oetans, en
cornflakes, en fruitvliegjes, en grote stu..."""

tela, tele, teli, telo, telu = 0, 0, 0, 0, 0
for c in text:
    if c.upper() == "A":
        tela += 1
    elif c.upper() == "E":
        tele += 1
    elif c.upper() == "I":
        teli += 1
    elif c.upper() == "O":
        telo += 1
    elif c.upper() == "U":
        telu += 1
        
print( "tels: a={}, e={}, i={}, o={}, u={}".format( 
    tela, tele, teli, telo, telu ) )