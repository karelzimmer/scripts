# gregoryLeibnitz benadert pi middels de Gregory-Leibnitz 
# reeks. Hij krijgt 1 parameter, een integer, die aangeeft
# hoeveel termen berekend worden. De benadering wordt als
# float geretourneerd.
def gregoryLeibnitz( num ):
    appr = 0
    for i in range( num ):
        if i%2 == 0:
            appr += 1/(1 + i*2)
        else:
            appr -= 1/(1 + i*2)
    return 4*appr

print( gregoryLeibnitz( 50 ) )