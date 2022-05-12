NAAM = "pc_rose_copy.txt"

def toon_inhoud( filename ):
    fp = open( filename, "rb" )
    print( fp.read() )
    fp.close()
    
def encryptie( filename ):
    fp = open( filename, "r+b" )
    buffer = fp.read()
    fp.seek(0)
    for c in buffer:
        if c >= 128:
            fp.write( bytes( [c-128] ) )
        else:
            fp.write( bytes( [c+128] ) )
    fp.close()
    
toon_inhoud( NAAM )
encryptie( NAAM )
toon_inhoud( NAAM )