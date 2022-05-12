flessen = 10
s = "s"
while flessen != "geen":
    print( "{0} flesje{1} met bier op de muur, "\
        "{0} flesje{1} met bier.".format( flessen, s ) )
    flessen -= 1
    if flessen == 1:
        s = ""
    elif flessen == 0:
        s = "s"
        flessen = "geen"
    print( "Open er een, drink hem meteen, {} flesje{} "\
        "met bier op de muur.".format( flessen, s ) )