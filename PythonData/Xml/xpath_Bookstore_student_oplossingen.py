# Gegevens uit Bookstore.xml lezen met Python lxml.etree en xpath

# De lxml library moet apart geinstalleerd worden van internet in Python:
# Open daartoe in de Python-directory een dosbox en ga naar de subdir Scripts
# Geef het commando: pip install lxml

# lxml wordt nu van het internet geinstalleerd
# verdere info op website: http://lxml.de/

# de standaard ingebouwde xml.etree xpath module is beperkt
# root.find(xpad)/.findall(xpad) ondersteunt beperkte xpad

#import xml.etree.ElementTree as ET
import lxml.etree as ET

tree = ET.parse("Bookstore.xml")        # -> /bookstore
# vor: xml.etree.ElementTree.ElementTree | lxml.etree._ElementTree 
root = tree.getroot()			# ->documentelement /bookstore ipv root /
# vor: Element

#Student: kies hier eventueel een andere current node:

current = root
#current = root.find("book[3]/author[2]")
#current = root.find("book[3]")

print("current.tag:", current.tag)        #bookstore, of andere current node
print()

#---------------

#Student: maak hieronder zelf een xpath expressie, en zet de andere uit met #
# (het # maakt van een regel commentaar)

#0.begin:
#xpad = "."                  #goed, toont alles
#xpad = "/bookstore"         #is deze goed? zo ja, wat wordt getoond?

#1. toon alle boeken:
#xpad = "book"
#xpad = "/bookstore"        #ook goed

#2. toon alle boektitels:
#xpad = "book/title"

#3. toon het 3e boek:
#xpad = "book[3]"

#4. toon van het 3e boek de auteur(s):
#xpad = "book[3]/author"

#5. toon van alle boeken de achternamen van de auteurs:
#xpad = "book/author/lastname"

#6. toon alle isbn'nen:
#xpad = "book/@isbn"

#7. toon van alle boeken die een isbn hebben, de titel:
#xpad = "book[@isbn]/title"

#8. toon van het boek met isbn = '1-861005-59-8' de titel:
#xpad = "book[@isbn='1-861005-59-8']/title"

#9. toon van alle boeken die een stock en een prijs hebben, de titel:
#xpad = "book[price and stock]/title"
#xpad = "book[price][stock]/title"

#10. toon van alle boeken met een prijs > 40 de titel:
#xpad = "book[price > 40]/title"

#11. toon alle boeken van auteurs met voornaam 'Andrew':
#xpad = "book[author/firstname='Andrew']"

#12. toon alle boektitels die beginnen met een A:
#xpad = "book/title[starts-with(., 'A')]"
#xpad = "book/title[substring(., 1, 1)='A']"
#xpad = "book[starts-with(title, 'A')]/title"

#13. toon all boektitels die eindigen op s:
#xpad = "book/title[substring(., string-length(.))='s']"

#14. toon van alle boeken die voor het boek met titel Athos staan, de titel
#xpad = "book[title='Athos']/preceding-sibling::book/title"
#xpad = "book[title='Athos']/preceding::title"
#xpad = "book[title='Athos']/preceding::book/title"

#15. toon alle boeken met een prijs tussen 20 en 50:
#xpad = "book[price>20 and price<50]"

#16. hoeveel boeken hebben een prijs:
#xpad = "count(book[number(price)>=0])"
#xpad = "count(book[price])"
#xpad = "count(book/price)"         #hmm, telt boek 2* als het 2 prijzen heeft
# vergelijk:
#xpad = "count(book[author])"        #5.0
#xpad = "count(book/author)"         #8.0

#17. wat is het totaalbedrag van de prijzen van de boeken?
#xpad = "sum(book/price)"           #nan bij price='nvt'
#xpad = "sum(book[number(price)>=0]/price)"      #slaat 'nvt' over
xpad = "sum(book[price>=0]/price)"  #slaat 'nvt' over
#xpad = "book/price"

#18. toon de boeken met 1 auteur; daarna die met meer dan 1 auteur:
#xpad = "book[author[last()=1]]"    #1 auteur
#xpad = "book[count(author)=1]"

#xpad = "book[author[last()>1]]"    #meer dan 1 auteur
#xpad = "book[author[2]]"
#xpad = "book[count(author)>1]"
#xpad = "book[author[count(../author)>1]]"
#xpad = "book[author[count(.)>1]]"       #niet goed, 0 boeken, deze auteur heeft cnt=1

#19. hoeveel dvd's zijn er?
#xpad = "count(dvd)"

#20. geef de totale lengte van alle films
#xpad = "sum(dvd/length)"

#21. hoeveel liedjes heeft de elpee van Leonard Cohen?
#xpad = "count(record[artist/lastname='Cohen' and artist/firstname='Leonard']/song)"
#xpad = "count(record/artist[lastname='Cohen' and firstname='Leonard']/../song)"

#22. hoeveel liedjes zijn er in totaal?
#xpad = "count(record/song)"

#23. tenslotte. hoeveel elpees dateren van na 1990?
#nul. na 1990 is geen popmuziek meer gemaakt.

#---------------

#Student: hieronder niets wijzigen

if ET.__name__ == 'xml.etree.ElementTree':
    lst = current.findall(xpad)       #->lst met elems, niet nodes of attribs
    for nod in lst:
        #print(nod.text)
        print(ET.dump(nod))
    print("\n%d nodes" % len(lst))
else:           #lxml
    lst = current.xpath(xpad)          #.xpath alleen bij lxml, gebr libs libxml2 and libxslt
    if isinstance(lst, list):
        if lst:
            if isinstance(lst[0],ET._Element):
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

