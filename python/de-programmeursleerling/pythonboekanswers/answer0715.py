PIRATES = 5
kokosnoten = 0
while True:
    kokosnoten += 1
    stapel = kokosnoten
    for i in range( PIRATES ):
        if stapel % PIRATES != 1:
            break
        stapel = (PIRATES-1) * int( (stapel - 1) / PIRATES )
    if stapel % PIRATES == 1:
        break
print( kokosnoten )