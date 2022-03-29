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
# (de # maakt van een regel commentaar)

#0. begin:
xpad = "."                  #goed, toont alles
#xpad = "/bookstore"         #is deze goed? zo ja, wat wordt getoond?

#1. toon alle boeken:
#xpad =

#2. toon alle boektitels:
#xpad =

#3. toon het 3e boek:
#xpad =

#4. toon van het 3e boek de auteur(s):
#xpad =

#5. toon van alle boeken de achternamen van de auteurs:
#xpad =

#6. toon alle isbn'nen:
#xpad =

#7. toon van alle boeken die een isbn hebben, de titel:
#xpad =

#8. toon van het boek met isbn = '1-861005-59-8' de titel:
#xpad =

#9. toon van alle boeken die een stock en een prijs hebben, de titel:
#xpad =

#10. toon van alle boeken met een prijs > 40 de titel:
#xpad =

#11. toon alle boeken van auteurs met voornaam 'Andrew':
#xpad =

#12. toon alle boektitels die beginnen met een A:
#xpad =

#13. toon all boektitels die eindigen op s:
#xpad =

#14. toon van alle boeken die voor het boek met titel Athos staan, de titel
#xpad =

#15. toon alle boeken met een prijs tussen 20 en 50:
#xpad =

#16. hoeveel boeken hebben een prijs:
#xpad =

#17. wat is het totaalbedrag van de prijzen van de boeken?
#xpad =

#18. toon de boeken met 1 auteur; daarna die met meer dan 1 auteur:
#xpad = 
#xpad = 

#19. hoeveel dvd's zijn er?
#xpad =

#20. geef de totale lengte van alle films
#xpad =

#21. hoeveel liedjes heeft de elpee van Leonard Cohen?
#xpad =

#22. hoeveel liedjes zijn er in totaal?
#xpad = 

#23. tenslotte. hoeveel elpees dateren van na 1990?


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

