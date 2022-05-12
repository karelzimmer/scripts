fruitlist = ["appel", "banaan", "kers", "doerian"]
fruitlist2 = fruitlist
fruitlist3 = fruitlist[:]

print( id( fruitlist ) )
print( id( fruitlist2 ) )
print( id( fruitlist3 ) )

fruitlist[2] = "mango"
print( fruitlist )
print( fruitlist2 )
print( fruitlist3 )