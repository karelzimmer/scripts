tekst = """Let op, het is heel eenvoudig om je te verdedigen 
tegen een man die gewapend is met een banaan. Eerst dwing je 
hem de banaan te laten vallen; dan ontwapen je hem door de 
banaan op te eten. Dat maakt hem onschadelijk."""

def tel_letter( x ):
    return x[0], -ord(x[1]) 

tellist = []
for i in range( 26 ):
    tellist.append( [0, chr(ord("a")+i)] )
    
for letter in tekst.lower():
    if letter >= "a" and letter <= "z":
        tellist[ord(letter)-ord("a")][0] += 1
        
tellist.sort( reverse=True, key=tel_letter )
    
for tel in tellist:
    print( "{:3}: {}".format( tel[0],tel[1] ) )