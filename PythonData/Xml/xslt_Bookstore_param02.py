# xslt met Bookstore.xml en Bookstore.xsl
# gebruikt lxml: pip install lxml
# http://lxml.de/

import lxml.etree as ET

xsl = ET.parse("Bookstore_boeken_param02.xsl")
tree = ET.parse("Bookstore.xml")        #lxml.etree._ElementTree

#transform = ET.XSLT(xsl)
#res = transform(tree)                      #lxml.etree._XSLTResultTree
#res = transform(tree, anaam = "'Dix'")     #eist quotes, want is string
#res = transform(tree, anaam = "'Popper'")
# of korter:
res = tree.xslt(xsl)
#res = tree.xslt(xsl, anaam = "'Dix'")
#res = tree.xslt(xsl, anaam = "'Popper'")

b = ET.tostring(res, pretty_print=True)     #default: method="xml" ->nwe rg + inspr

print(str(b, 'utf-8'))                     #goed; 'utf-8' moet

print('\n*** klaar ***')

