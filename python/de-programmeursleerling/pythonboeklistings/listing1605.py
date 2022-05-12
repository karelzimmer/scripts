fp = open( "pc_jabberwocky.txt" )
teller = 0
while teller < 5:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer, end="" )
    teller += 1
fp.close()