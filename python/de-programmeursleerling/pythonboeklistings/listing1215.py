def wijziglist( x ):
    if len( x ) > 0:
        x[0] = "FRUIT!"

fruitlist = ["appel", "banaan", "kers", "doerian"]
wijziglist( fruitlist )
print( fruitlist )