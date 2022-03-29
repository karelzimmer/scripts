# Gegevens uit Bookstore.xml lezen met Python ElementTree en xpath

# std xml:
# de ingebouwde xml.etree xpath module is beperkt
# root.find(xpad)/.findall(xpad) ondersteunt beperkte xpad

# lxml:
# lxml.etree is veel sneller; heeft ook root.xpath(xpad) ->wel std compliant
# website: http://lxml.de/
# gewoon installeren met: pip install lxml
# voor win geen wheel nodig, ondanks C-libraries
# gebruikt libs libxml2 and libxslt

#import xml.etree.ElementTree as ET
import lxml.etree as ET

tree = ET.parse("Bookstore.xml")        # -> /bookstore
# vor: xml.etree.ElementTree.ElementTree | lxml.etree._ElementTree 
root = tree.getroot()			# ->documentelement /bookstore ipv root /
# vor: Element

current = root
#current = root.find("book[3]/author[2]")
#current = root.find("book[3]")

print("current.tag:", current.tag)        #bookstore, of andere current node
print()

#xpad = "."                  #goed, toont alles
#xpad = "/bookstore"         #std SyntaxError, wil niet / vooraan; lxml ok
#xpad = "../bookstore"       #std niks; lxml goed
#xpad = "../../bookstore"
#xpad = "bookstore"

#xpad = "book"
#xpad = "/book"
#xpad = "./book"
#xpad = "//book"

#xpad = "/bookstore/book"
#xpad = "bookstore/book"
#xpad = "../bookstore/book"

#xpad = "book[4]"	        #4e boek, telt vanaf 1; bij book[0] toont ie niks
#xpad = "*[position()=2]"    #std SyntaxError: kent position() niet
#xpad = "//*[position()=2]"    #bagger
#xpad = "book[position()=3]"
#xpad = "book[last()]"          #goed; kent wel last()
#xpad = "book[first()]"         #error, bestaat niet
#xpad = "book[last()-1]"

#xpad = "book/@isbn"
#xpad = "book[@isbn]"
#xpad = "book[not(@isbn)]"
#xpad = "book[@isbn='']"
#xpad = "book[@*]"

#xpad = "title"
#xpad = "child::title"
#xpad = "//title"               #alle titels, ook van films
#xpad = "descendant::title"     #zelfde als //
#xpad = ".//title"               #idem

#xpad = "book/title"
#xpad = "book[3]/title"         #van 3e boek de titel
#xpad = "book/*"		#van alle boeken alle subnodes los

#xpad = "book/title|book/price"
#xpad = "book/(title|price)"         #altijd error; klopt, hoort ook zo
#xpad = "book(/title|/price)"         #altijd error; klopt, hoort ook zo
#xpad = "(book/title | book/price)"

#xpad = "book[3]/ancestor-or-self::*"

#xpad = "book[@isbn='1-861005-59-8']/title"
#xpad = "book/title[@remark]"
#xpad = "book[title/@remark]"
#xpad = "book[@*]"      #goed
#xpad = "book/title[.='Athos']"
#xpad = "book[title='Athos']/title"
#xpad = "book[title='Athos']"

#xpad = "book/author"           	#alle auteurs
#xpad = "book/author/*" 	        #alle voor- en achternamen
#xpad = "book/author[2]"	        #van ieder boek de 2e auteur
#xpad = "book[author[2]]"
#xpad = "(book/author)[4]"
#xpad = "(book/author[1])[4]"           #alle bkn met 1e auteur, daarvan de 4e: Andrew Duthie
#xpad = "book[author][4]/author[1]"     #Andrew Duthie
#xpad = "book[3]/author"    	        #van 3e boek de auteur(s)
#xpad = "book/author[last()]"           #van ieder boek de laatste auteur
#xpad = "(book/author)[last()]"
#xpad = "book[not(author)]/title"       #alle bk zonder auteur, daarvan de titel
#xpad = "book/title[../author/firstname='Andrew']"
#xpad = "book[author/firstname='Andrew']/title"

#xpad = "book[price]/title"
#xpad = "book/price"
#xpad = "book[stock]/title"
#xpad = "book[price][stock]/title"
#xpad = "book[price=45.75]/title"

#xpad = "book[price and stock]/title"
#xpad = "book[price or stock]/title"
#xpad = "book[@pubdate or stock]/title"
#xpad = "book[@pubdate | stock]/title"

#xpad = "book[price<50]/title"
#xpad = "book[price > 50]/title"
#xpad = "book[price &gt; 50]/title"        #altijd error
#xpad = "book[number(price)>=0]/price"
#xpad = "book[price>=0]/price"
#xpad = "book[price>=10]/price"
#xpad = "sum(book[number(price)>=0]/price)"      # 125.07
#xpad = "sum(book[price>0.0]/price)"             # 125.07
#xpad = "sum(book/price)"                        #nan, vanwege 1 bk met price='nvt'
#xpad = "count(book[number(price)>=0])"          # 3.0, dwz 3 nodes

#xpad = "book/*[not(self::price)]"  	    #ok, alles behalve de prijs-node
#xpad = "book/*[not(local-name()='price')]"	#idem
#xpad = "book/*[local-name() != 'price']"       #idem

#xpad = "book[3]/preceding-sibling::book"	#de 1e twee book-nodes
#xpad = "book[3]/preceding-sibling::book[1]"	#2e book-node, dus 1 terug
#xpad = "book[3]/preceding-sibling::*"		#idem
#xpad = "book[3]/preceding-sibling::title"	#niks, title is geen sibling van book
#xpad = "book[3]/preceding::book"		#de 1e twee book-nodes
#xpad = "book[3]/preceding::bookstore"          #niks
#xpad = "book[3]/preceding::title"		#3 nodes
#xpad = "book[3]/preceding::book/title"		#2 nodes
#xpad = "book[3]/preceding::*"			#geeft van de 1e twee boeken alle nodes los
#xpad = "book[3]/title/preceding::*"
#xpad = "book[title='Athos']/preceding-sibling::book/title"

#xpad = "book[3]/following-sibling::book"	#de latere book-nodes
#xpad = "book[3]/following-sibling::*"
#xpad = "book[3]/following-sibling::book[1]"
#xpad = "book[3]/following-sibling::record"
#xpad = "book[3]/following-sibling::record/title"
#xpad = "book[3]/following-sibling::book[stock]" #2 vlg bkn met stock
#xpad = "book[3]/following-sibling::*[stock]"    #idem
#xpad = "book[3]/following-sibling::[stock]"     #error
#xpad = "book[3]/following-sibling::title"       #niets
#xpad = "book[3]/following-sibling::*/title"     #alle vlg titels incl lp en dvd
#xpad = "book[3]/following-sibling::book/title"  #3 vlg boektitels
#xpad = "book[3]/following::title"               #alle vlg titels (15), op alle niveaus
#xpad = "book[3]/following::book/title"
#xpad = "book[3]/following::song/title"
#xpad = "book[3]/author[2]/following::*"         #vanaf 3e auteur alle elems,
    #eerst volledig <author>, dan <firstname> enz; dan vlg <book> geheel, dan subitems enz

#xpad = "book[3]/descendant::lastname"		#de drie lastname-nodes van Beginning XML
#xpad = "book[3]//lastname"                     #idem, gewone notatie
#xpad = "book//lastname[contains(.,'ix')]"
#xpad = "book/author[lastname[contains(.,'ix')]]"
#xpad = "book/author[contains(lastname,'ix')]"
#xpad = "book[author[contains(lastname,'ix')]]"
#xpad = "book/stock | book/author/lastname[contains(.,'per')][contains(.,'P')]"
    #de 2e [..] vw hoort bij lastname, heeft prioriteit tov |
#xpad = "book/author[lastname >= 'H']"                   #niks
#xpad = "book/author[starts-with(lastname, 'H')]"
#xpad = "book[starts-with(author/lastname, 'H')]/title"
#xpad = "book/author[starts-with(lastname, 'H')]/../title"

#xpad = "book[3]/ancestor::dvd"                 #niets
xpad = "book[3]/ancestor::*/dvd"                #alle dvd's
#xpad = "book[3]/ancestor::bookstore/dvd"        #idem
#xpad = "book[3]/../dvd"                         #idem
#xpad = "name(book[3]/ancestor::*/dvd)"          #value=dvd
#xpad = "name(book[3]/ancestor::*/*)"            #value=book, want neemt 1e boek

#xpad = "book/title[starts-with(., 'A')]"   #std SyntaxError
#xpad = "book/title[substring(., 1, 1)='A']"    #idem
#xpad = "book/title[starts-with(text(), 'A')]";	#std SyntaxError; lxml ok
#xpad = "book/title[substring(., string-length(.))='s']"    #lxml ok, eindigt op...; geen ends-with(..)
#xpad = "book/title[substring(., string-length(.)-1)='os']"

#xpad = "book/title[../author[starts-with(lastname, 'H')]]"         #ok, dubbele []
#xpad = "book/title[starts-with(../author/lastname, 'H')]"          #ok
#xpad = "book/title[starts-with(parent::author/lastname, 'H')]"     #niks, author geen parent v title
#xpad = "book/title[starts-with(parent::book/author/lastname, 'H')]"    #ok
#xpad = "substring(book[1]/title, 5, 3)"         #beg (vanaf 1), len

#xpad = "book[price > '20' and price < '50']/title"         #ok
#xpad = "book[price > 20 and price < 50]/title"              #ok
#xpad = "book[price > 20][price < 50]/title"
#xpad = "book[price <= 50 and starts-with(title, 'A')]/title"
#xpad = "book[price <= 50 or starts-with(title, 'A')]/title"

#xpad = "book[author[last()=1]]"        #bkn met 1 auteur
#xpad = "book[count(author)=1]"          #goed!!!
#xpad = "book[count(author)>1]"          #goed!!!
#xpad = "book[author[1]]"                #bkn met tenminste 1 auteur, vgl book[author]
#xpad = "book[author[2]]"                #bkn met tenminste 2 auteurs
#xpad = "book[author[last()>1]]"        #meer dan 1 auteur
#xpad = "book[author[count(.)>1]]"          #0 nodes, want huidige author is altijd 1
#xpad = "book[author[count(../author)>1]]"   #terug naar boek v huid auteur, dan auteurs tellen

#xpad = "number(book[3]/price) * number(book[3]/stock)"
#xpad = "book[3]/price * book[3]/stock"         #166.8
#xpad = "book[1]/price * book[1]/stock"         #nan
#xpad = "sum(book[number(price)>=0]/price)"      #127.85
#xpad = "sum(book[price>0.0]/price)"            #127.85
#xpad = "sum(book/price)"                       #nan, vanwege 1 bk met price='nvt'
#xpad = "sum(number(book/price))"               #error, kan niet number->nodelist
#xpad = "count(book[number(price)>=0])"         #3.0, dwz 3 nodes

#xpad = "book[3]/price"
# vlg 3 error in Java en Python; spec zegt: fn zit niet in dom-xpath, wel in xslt-xpath 1.0
#xpad = "format-number(book[3]/price,'0.00')"
#xpad = "format-number(book[3]/price,'0.00;(0.00)')"		#neg getallen in (..) ipv minteken
#xpad = "format-number(book[3]/price,'#,##0.00')"		#duizendtallen


#xpad = "count(dvd)"
#xpad = "sum(dvd/length)"
#xpad = "dvd/sum(length)"        #error

#xpad = "count(record/song)"         #18
#xpad = "count(record[artist/lastname='Cohen'][artist/firstname='Leonard']/song)"
#xpad = "count(record[artist/lastname='Cohen' and artist/firstname='Leonard']/song)"
#xpad = "count(record/artist[lastname='Cohen' and firstname='Leonard']/../song)"


if ET.__name__ == 'xml.etree.ElementTree':      #std xml
    lst = current.findall(xpad)       #->lst met elems, niet nodes of attribs
    for nod in lst:
        #print(nod.text)
        print(ET.dump(nod))
    print("\n%d nodes" % len(lst))
else:                                  #lxml
    lst = current.xpath(xpad)          #.xpath alleen bij lxml
    if isinstance(lst, list):
        if lst:
            if isinstance(lst[0], ET._Element):
                for nod in lst:          #voor elems
                    #print(nod.text)
                    print(ET.dump(nod))
            else:
                for nod in lst:          #voor attribs
                    print(nod)
        print("\n%d nodes" % len(lst))
    else:
        print("value=", lst)            #bv bij xpad="sum(..)"


"""
lxml xpath met namespaces:
r = doc.xpath('/x:foo/b:bar', namespaces={
    'x': 'http://codespeak.net/ns/test1',
    'b': 'http://codespeak.net/ns/test2'})

"""

