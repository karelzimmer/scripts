# xslt met Bookstore.xml en Bookstore.xsl
# gebruikt lxml: pip install lxml
# http://lxml.de/

import lxml.etree as ET
import os

# vlg extension function voor xsl
# nodeset -> list
# string -> ET._ElementUnicodeResult
# number -> float
# boolean -> bool
def upper(context, nod=None):
    if not nod:
        return None
    #print(type(nod))
    if isinstance(nod, list):
        nod = nod[0]
    if isinstance(nod, ET._Element):      #bv book[1]/title
        nod = nod.text.strip()
    if isinstance(nod, ET._ElementUnicodeResult):    #string
        return nod.upper()
    else:
        return nod              #number, boolean

ns = ET.FunctionNamespace("urn:ecr:python-functions")   #namespace moet
ns.prefix = 'py'       #alleen nodig voor xpath buiten xsl; gedecl in .xsl
ns['upper'] = upper     #registreer Python fn in namespace

xslfile = "Bookstore_boeken_select01_exslt_pyfn.xsl"

#xslfile = "Bookstore_boeken_apply01.xsl"
#xslfile = "Bookstore_boeken_select02.xsl"
#xslfile = "Bookstore_boeken_films01_exslt_nodeset.xsl"
#xslfile = "Bookstore_boeken_param02.xsl"

xsl = ET.parse(xslfile)
tree = ET.parse("Bookstore.xml")            #lxml.etree._ElementTree

#transform = ET.XSLT(xsl)
#res = transform(tree)                      #lxml.etree._XSLTResultTree
#res = transform(tree, anaam = "'Dix'")     #param
#res = transform(tree, anaam = "'Popper'")

# of korter:
#res = tree.xslt()           #error, eist xsl; xsl-decl in xml wordt overgeslagen
res = tree.xslt(xsl)
#res = tree.xslt(xsl, anaam = "'Dix'")      #param
#res = tree.xslt(xsl, anaam = "'Popper'")

b = ET.tostring(res, pretty_print=True)     #dflt: method="xml" ->nwe rg + inspr

print(str(b, 'utf-8'))                     #goed; 'utf-8' moet

print('\n*** klaar ***')

