fp = open( "pc_rose.txt ")
try:
    buf = fp.read()
    print( buf )
except IOError:
    fp.close()
    raise
fp.close()