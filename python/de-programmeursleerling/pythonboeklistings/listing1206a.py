def mix_key( element ):
    if isinstance( element, str ):
        return 1, element
    return 0, element

mixedlist = ["appel", 0, "aardbei", 5, "banaan", 2, \
"moerbei", 9, "kers", "banaan", 7, 7, 6, "mango"]
mixedlist.sort( key=mix_key )
print( mixedlist )