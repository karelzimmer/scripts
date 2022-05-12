fruitlist = ["appel", "aardbei", "banaan", "framboos", 
    "kers", "banaan", "doerian", "mango"]
fruitlist.sort( key=lambda x: (len(x),x) )
print( fruitlist )