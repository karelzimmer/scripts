tekst = """Kapper Knap, de knappe kapper, knipt en kapt heel 
knap, maar de knecht van kapper Knap, de knappe kapper, knipt 
en kapt nog knapper dan kapper Knap, de knappe kapper."""

def schoon( s ):
    ns = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            ns += c
        else:
            ns += " "
    return ns

wdict = {}
for woord in schoon( tekst ).split():
    wdict[woord] = wdict.get( woord, 0 ) + 1
    
keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )