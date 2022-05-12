GROOTTE = 4

def hanoi( p_van, p_tmp, p_naar, grootte ):
    if grootte == 1:
        print( "Schijf 1 van", p_van, "naar", p_naar )
        return 1
    stappen = hanoi( p_van, p_naar, p_tmp, grootte-1 )
    print( "Schijf", grootte, "van", p_van, "naar", p_naar )
    stappen += 1+hanoi( p_tmp, p_van, p_naar, grootte-1 )
    return stappen

stappen = hanoi( 'A', 'B', 'C', GROOTTE )
print( stappen, "stappen gedaan" )