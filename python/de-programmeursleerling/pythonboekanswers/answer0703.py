from pcinput import getInteger

AANTAL = 10
grootste = 0
kleinste = 0
deelbaar3 = 0

for i in range( AANTAL ):
    num = getInteger( "Geef nummer "+str( i+1 )+": " )
    if num%3 == 0:
        deelbaar3 += 1
    if i == 0:
        kleinste = num
        grootste = num
        continue
    if num < kleinste:
        kleinste = num
    if num > grootste:
        grootste = num
        
print( "Kleinste is", kleinste )
print( "Grootste is", grootste )
print( "Deelbaar door 3 is", deelbaar3 )