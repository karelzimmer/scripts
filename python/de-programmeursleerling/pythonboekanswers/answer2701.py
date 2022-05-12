from collections import Counter

z = "Je moeder was een hamster en je vader rook naar vlierbessen"
zin2 = ""
for c in z.lower():
    if c >= 'a' and c <= 'z':
        zin2 += c

clist = Counter( zin2 ).most_common( 5 )
for c in clist:
    print( "{}: {}".format( c[0], c[1] ) )