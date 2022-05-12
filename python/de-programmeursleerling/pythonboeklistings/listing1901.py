def getRGB( color ):
    blauw = color & 255
    groen = (color >> 8) & 255
    rood = (color >> 16) & 255
    return rood, groen, blauw
    
r, g, b = getRGB( 223567 )
print( "rood={}, groen={}, blauw={}".format( r, g, b ) )