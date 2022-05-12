fruitlist = ["appel", "Aardbei", "banaan", "framboos", 
    "KERS", "banaana", "doerian", "mango"]
fruitlist.sort() 
print( fruitlist )
fruitlist.sort( key=str.lower ) # case-insensitive sort
print( fruitlist )