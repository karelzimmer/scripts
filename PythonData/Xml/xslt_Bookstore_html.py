# xslt met Bookstore.xml en Bookstore.xsl
# gebruikt lxml: pip install lxml
# http://lxml.de/

import lxml.etree as ET
import os

xsl = ET.parse("Bookstore.xsl")
tree = ET.parse("Bookstore.xml")        #lxml.etree._ElementTree
#root = tree.getroot()			#Element; hier niet nodig

xf = ET.XSLT(xsl)
res = xf(tree)                      #lxml.etree._XSLTResultTree
# of korter:
#res = tree.xslt(xsl)

#s = str(res)                        #tekst op nwe regel, geen inspr

#b = ET.tostring(res)               #bytes; tekst achter elkaar
#b = ET.tostring(res, method="html", pretty_print=True)  #nwe rg + geen inspr
b = ET.tostring(res, pretty_print=True)     #default: method="xml" ->nwe rg + inspr

#s = str(b)                  #niet goed; toont b als str met letterlijk "\n"
s = str(b, 'utf-8')                     #goed; 'utf-8' moet
#s = bytes.decode(b, 'utf-8')           #idem; 'utf-8' default, kan weg
#s = b.decode()                          #idem; 'utf-8' default, kan weg

antw = input("html tonen in IE? (Y/N) ")
if antw in 'yY':
    fh = open('Bookstore.html', "w")
    fh.write(s)
    fh.close()
    os.startfile('Bookstore.html')
else:
    print(s)

print('\n*** klaar ***')

