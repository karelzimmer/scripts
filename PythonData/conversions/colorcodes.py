# kleurcodes


white = "#ffffff"
black = "#000000"
red = "#ff0000"
green = "#00ff00"
blue = "#0000ff"

_yellow = "#ffff00"

def rgb2str(r, g, b, caps=False):
    if not caps:
        return "#%02x%02x%02x" % (r,g,b)
    else:
        return "#%02X%02XX%02X" % (r,g,b)

def rgb2int(r, g, b):
    return (r<<16) | (g<<8) | b
    #return (r<<16) + (g<<8) + b        #idem


if __name__ == "__main__":
    print(rgb2str(13,255,230))
    #print(rgb2str(13,255,230, True))

    print(rgb2int(13,255,230))

