# xslt met adressen.xml en adressen.xsl
# gebruikt lxml: pip install lxml
# http://lxml.de/

import lxml.etree as ET
import os

#xsl = ET.parse("adressen.xsl")      #bevat xsl param zkid
xsl = ET.parse("adressen.xsl")      #bevat xsl param zkid
tree = ET.parse("adressen.xml")

#xf = ET.XSLT(xsl)
#res = xf(tree)
#res = xf(tree, zkid="5")            #param ingevuld, mag niet "" of " "
#res = xf(tree, zkid="'Klaas Hansen'")   #moet '..' in ".." voor strings
#  quotestr_obj = ET.XSLT.strparam(""" It's "Monty Python" """)
#  res = xf(tree, zkid=quotestr_obj)

# of korter:
#res = tree.xslt(xsl)
res = tree.xslt(xsl, zkid="5")

#print(str(res))
#s = str(res)                        #tekst op nwe regel, geen inspr

b = ET.tostring(res, pretty_print=True)     #default: method="xml" ->nwe rg + inspr
s = str(b, 'utf-8')                     #goed

antw = input("html tonen in IE? (Y/N) ")
if antw in 'yY':
    fh = open('adressen.html', "w")
    fh.write(s)
    fh.close()
    os.startfile('adressen.html')
else:
    print(s)

print('\n*** klaar ***')

