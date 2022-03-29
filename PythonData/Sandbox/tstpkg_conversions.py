"""
Testen met pkg conversions

3 manieren om dir voor pkgs toe te voegen:

[1] sys.path.append("D:\\PythonData")
[2] mk env var PYTHONPATH, met daarin: D:\PythonData
    (daarna herstarten of opnieuw inloggen)
[3] mk in site-packages file conversions.pth (of tralala.pth)
    met daarin 1 regel: D:\\PythonData, meer paden op vlg regels
    (daarna Python + IDLE opnieuw starten)

"""

import sys
# vlg is dir die pkgs bevat; kan ook met env var PYTHONPATH
sys.path.append("D:\\PythonData")       #mag ook eindigen op "\\"


import conversions as cv                        #pkg
# vor importeert NIET subpkgs en modules
print(cv.vol_cube(5))
print(cv.vol_box(5,5,2))
print(cv.vol_sphere(5))
print(cv.vol_sphere(50))


##import conversions.colorcodes as col            #module
##print(col.white)
##print(col.rgb2str(255,30,45))
##print(col._yellow)       #goed

##from conversions.colorcodes import *
##print(white)
##print(rgb2str(255,30,45))
###from conversions.colorcodes import _yellow
##print(_yellow)          #zonder vor onbekend

##from conversions.colorcodes import white, blue, rgb2str
##print(white)
##print(rgb2str(255,30,45))
##print(blue)
###print(red)              #NameError: onbekend
###print(_yellow)          #NameError: onbekend


##import conversions.isbn as isbn                 #module, met __all__
##print(isbn.check_isbn("0-7821-1765-1"))
##print(isbn.check_isbn("978-3-88680-843-4"))
##print(isbn.checkISBN10("0-7821-1765-1"))
##print(isbn.checkISBN13("978-3-88680-843-4"))

##from conversions.isbn import *
##print(check_isbn("0-7821-1765-1"))
##print(check_isbn("978-3-88680-843-4"))
###print(checkISBN10("0-7821-1765-1"))
###from conversions.isbn import checkISBN13     #goed
###print(checkISBN13("978-3-88680-843-4"))      #zonder vor onbekend


##import conversions.metric.temperature as tem    #module
##print(tem.cels2fahr(30))
##print(tem.fahr2cels(64))

##import conversions.metric as met                #pkg
##print(met.mile2km(40))
##print(met.temperature.cels2fahr(30))
### vor zonder interne from-import AttributeError: geen temperature
### wel goed als in metric\__init__.py: from . import temperature


##import conversions.finance as fin               #pkg
##print(fin.dollar2euro(10))
##print(fin._pound2euro(10))          #goed

##from conversions.finance import *
##print(dollar2euro(10))
##print(_pound2euro(10))          #NameError

