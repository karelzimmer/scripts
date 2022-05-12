#saxparser, voor bookstore.xml
#als je halverwege wilt stoppen, moet je in je handler een error genereren

import xml.sax, xml.sax.handler


class BookEventHandler(xml.sax.handler.ContentHandler):
    """ContentHandler voor sax parser, voor bookstore.xml"""

    def __init__(self):
        pass

    def startDocument(self):
        self.numElems = 0
        self.numTextElems = 0
        print('startDocument')

    def startElement(self, name, attribs):
        self.numElems += 1
        print('%s\nEl: %s' % ('\n' if name=='book' else '', name))
        for k,v in attribs.items():
            print('  Att: %s=%s' % (k,v))

    def characters(self, content):      #content is str
        #voor iedere crlf en std ws krijg je nwe content ->uitfilteren
        #als de tekst binnen elem zelf crlf bevat, krijg je 2* content
        #gaat hier goed, omdat je dan ook 2* print() krijgt, maar
        #numTextElems wordt dan te hoog!
        #je kan NIET makkelijk zien bij welk elem de content hoort;
        #bij mixed elems kan een omsluitend elem ook tekst bevatten
        s = content.strip()
        if s:
            self.numTextElems += 1
            print(s)
        
    def endElement(self, name):
        pass

    def ignorableWhitespace(self, ws):
        print(' [ws] ')

    def endDocument(self):
        print('\nendDocument')


class FoundBookException(xml.sax.SAXException):
    def __init__(self,msg=''):      #verplicht met msg
        super().__init__(msg)


class FindIsbnBookEventHandler(xml.sax.handler.ContentHandler):
    """Zoek een boek op isbn"""

    def __init__(self, isbn=None):
        self.isbn = isbn

    def startDocument(self):
        self.numElems = 0
        self.numTextElems = 0
        if not self.isbn:
            raise xml.sax.SAXException('Geen isbn opgegeven.')
        self.isGevonden = False
        print('startDocument')

    def startElement(self, name, attribs):
        self.numElems += 1
        if self.isGevonden:
            print('\nEl: %s' % name)
            for k,v in attribs.items():
                print('  Att: %s=%s' % (k,v))
        elif name == 'book' and attribs.get('isbn') == self.isbn:
            self.isGevonden = True
            print('\nEl: book')
            for k,v in attribs.items():
                print('  Att: %s=%s' % (k,v))

    def characters(self, content):      #content is str
        if not self.isGevonden:
            return
        s = content.strip()
        if s:
            self.numTextElems += 1
            print(s)
        
    def endElement(self, name):
        if self.isGevonden and name == 'book':
            raise FoundBookException

    def endDocument(self):
        print('\nendDocument\nBoek niet gevonden, snif...')


def showBooks():
    sax = xml.sax.make_parser()     #gebr xml.sax.expatreader.ExpatParser
    handler = BookEventHandler()
    sax.setContentHandler(handler)
    #sax.setErrorHandler(BookErrorHandler())    #moet je zelf definieren

    sax.parse('bookstore.xml')      #alleen met byte streams?
    #sax.parse('bookstore.xml')     #je mag 2 keer parsen!

    print('handler: numElems=%d' % handler.numElems)
    print('handler: numTextElems=%d' % handler.numTextElems)


def findBook():
    #isbn =''
    #isbn = '0-09-111721-6'
    #isbn = '1-861005-59-8'
    #isbn = '90-5911-024-2'
    #isbn = '0-300-06463-2'
    isbn = '91-5912-024-3'
    sax = xml.sax.make_parser()     #gebr xml.sax.expatreader.ExpatParser
    handler = FindIsbnBookEventHandler(isbn)
    sax.setContentHandler(handler)

    try:
        sax.parse('bookstore.xml')
    except FoundBookException:
        print('\nBoek gevonden!!')
    except xml.sax.SAXException as ex:
        print(ex)

    print('handler: numElems=%d' % handler.numElems)
    print('handler: numTextElems=%d' % handler.numTextElems)

    
#--- script ---

showBooks()
#findBook()

