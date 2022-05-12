def len_alfabetisch( element ):
    return len( element ), element 

fruitlist = ["appel", "aardbei", "banaan", "framboos", 
    "kers", "banaan", "doerian", "mango"]
fruitlist.sort( key=len_alfabetisch )
print( fruitlist )