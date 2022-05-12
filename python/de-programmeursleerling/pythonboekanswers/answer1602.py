def schoon( s ):
    nieuws = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            nieuws += c
        else:
            nieuws += " "
    return nieuws

wdict = {}
fp = open( "pc_woodchuck.txt" )
while True:
    regel = fp.readline()
    if regel == "":
        break
    for woord in schoon( regel ).split():
        wdict[woord] = wdict.get( woord, 0 ) + 1
fp.close()
    
keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )