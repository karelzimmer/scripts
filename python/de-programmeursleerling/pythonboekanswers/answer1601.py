def schoon( s ):
    nieuws = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            nieuws += c
        else:
            nieuws += " "
    return nieuws

fp = open( "pc_woodchuck.txt" )
tekst = fp.read()
fp.close()

wdict = {}
for woord in schoon( tekst ).split():
    wdict[woord] = wdict.get( woord, 0 ) + 1
    
keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )