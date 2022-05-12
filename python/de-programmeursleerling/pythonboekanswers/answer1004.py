tekst = """Kapper Knap, de knappe kapper, knipt en kapt heel 
knap, maar de knecht van kapper Knap, de knappe kapper, 
knipt en kapt nog knapper dan kapper Knap, de knappe kapper."""

def schoon( s ):
    ns = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            ns += c
        else:
            ns += " "
    return ns

tel = 0
for woord in schoon( tekst ).split():
    if woord == "knap":
        tel += 1

print( "Aantal keren dat het woord \"knap\" voorkomt:", tel )