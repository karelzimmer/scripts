"""
test regex

email: RFC 822
toegelaten kars:
!"#$%&'*+-/0123456789=?
@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_
`abcdefghijklmnopqrstuvwxyz{|}~

Vaak biedt \w+ te weinig toegelaten kars dan kun je bv \S+ kiezen, dus niet-spaties.
Soms mag alles behalve bv een afsluitend vishaakje >, kies dan: [^>]+

email: \w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*

regex flags (re.DOTALL enz; combineren met | ):
ASCII, A		a
DOTALL, S		s
IGNORECASE, I		i
LOCALE, L		L
MULTILINE, M		m
UNICODE, U		u
VERBOSE, X		x
"""


import re
import time

def getPattern():
    #pat = r"\d+"                     #getal-patroon
    #pat = r"\d*"                #slecht! niks geeft ook match!
    #pat = r"\d+$"
    #pat = r"\b\d*"
    #pat = r"\b\d+"
    #pat = r"\d*\w"
    #pat = r"\d*\D"
    #pat = r"\d{2}\w\d"
    #pat = r".*\d{2}\.*"
    #pat = r"^\d{2}\D*"
    #pat = r"\d{2}\D*"
    #pat = r".*\d{2}\D*"
    #pat = r"^\d{2}"
    #pat = r"\b\d{2}"
    #pat = r"\b\d{2}\b"
    #pat = r"\d{2,4}"
    #pat = r"\d{2,4}\b"
    #pat = r"\b\d{2,4}\b"
    #pat = r"\b\d{2}\b"
    #pat = r"\d{0,2}\b"		#deze is niks, geeft een match voor elke niet-digit

    #pat = r"\d\d[-/]\d\d[-/]\d{4}"       #geen ^,$, geen back ref
    pat = r"(\d\d)([-/])(\d\d)\2(\d{4})"       #geen ^,$, wel back ref
    #pat = r"(\d\d)[-/](\d\d)[-/](\d{4})"
    #pat = r"^(\d\d)([-/])(\d\d)\2(\d{4})$"	#datum-patroon met groepen en ^,$
    #pat = r"^(\d\d)([-/])(?:\d\d)\2(\d{4})$"    #idem, non-capturing group
    #pat = r"^(\d\d)([-/])(?:\d\d)\2(\w)?(\d{4})$"   #idem, incl dummie group (\w)
    #pat = "^(\\d\\d)[-/](\\d\\d)[-/](\\d{4})$"      #geen raw str r"  "
    #pat = r"^(?P<dag>\d\d)([-/])(?P<mnd>\d\d)\2(?P<jr>\d{4})$"  #named groups
    #pat = r"^(\d\d)(?P<sep>[-/])(\d\d)(?P=sep)(\d{4})$"      #idem, 1 grp + backref
    # vor (?P=sep) wordt non-capturing group, idem \2, kan ook met \2

    #pat = r"\d{4} ?[A-Z]{2}"			#postcode-patroon
    #pat = r"\b\d{4} ?[A-Z]{2}\b"
    #pat = r"\b\d{4} ?[A-Z]{2}"
    #pat = r"\b\d{4}\b[A-Z]{2}\b"
    #pat = r"\b[1-9]\d{3} ?[A-Z]{2}\b"
    #pat = r"\b([1-9]\d{3}) ?([A-Z]{2})\b"

    #pat = r"\w+@\w+"				#email-patroon
    #pat = r"\b\w+@\w+\b"
    #pat = r"^\w+@\w+$"
    #pat = r"^\w+(\.\w+)*@\w+([-.]\w+)*$"
    #pat = r"^(\w+\.?)+\w@(\w+[-.]?)+\w$"
    #pat = r"^((?:\w+\.?)+)\w@((?:\w+[-.+]?)+)\w$"
    #pat = r"\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*"
    #pat = r"\A\w+@\w+\Z"
    #pat = r"\A\w+@\w+\z"

    #pat = "niet$"                              #andere patronen
    #pat = r".*\.\w*\(\)"
    #pat = r".*[.]\w*\(\)"
    #pat = r".*spider[- ]?man.*"
    #pat = r"spider[- ]?man"
    #pat = r"(?i).*spider[- ]?man.*"		#(?i)->case insensitive

    return pat

def getText():
    #text = "12345"
    #text = "12345a"
    #text = "23a1"
    #text = "getal: 23a1"
    #text = "176.45"
    #text = "-176.45"
    #text = "176.-45"
    #text = "--176.45"
    #text = "peer"
 
    #text = "Er zijn 152375 of meer sterren in het melkwegstelsel"
    #text = "Op de 15e dag zag hij het licht."
    #text = "Marie heeft 12 boeken"
    #text = "Voor de 12e keer zeg ik: er zijn 11 boeken!"
    #text = "12 boeken"
    #text = "Marie heeft boeken"
    #text = "Marie heeft er 12"
    #text = "De code is beq31zz5f geloof ik."

    #text = "Postcode: 2315 BK"
    #text = "Adres 2315 CK  Amsterdam"
    #text = "Adres 2315  DK  Amsterdam"
    #text = "Piet woont in Rotterdam."
    #text = "Postcode: 2315EK"
    #text = "Postcode: 10104 NE"
    #text = "Postcode: 1015 ne"
    #text = "De 12 22 ste keer"
    #text = "Ik woon op 2345 NE huisnumer 1212hs"

    #text = "23/05/2006"
    #text = "23-05-2006"
    #text = "23-05/2006"
    #text = "23-05-2006 is de juiste datum."
    #text = "Het is vandaag 23/05/2006, geloof ik."
    text = "Het is vandaag 23/05/2006, geloof ik. Oh nee, 24-07-2007."

    #text = "pjansen@microsoft.com"
    #text = "PJansen@microsoft.com"
    #text = "p.jansen@microsoft.com"	#met @"\w+@\w+" -> jansen@microsoft
    #text = "p.h.jansen@microsoft.com"
    #text = "p h jansen@microsoft.com"
    #text = "h.vdveen@szk.amsterdam-west-publiek.nl"
    #text = "h.vdveen@szk.amsterdam-west-publiek.nl"
    #text = "h.vdveen@szk.amsterdam-west--publiek.nl"
    #text = "h.vdveen@szk..amsterdam-west-publiek.nl"
    #text = "updateklanten(@klantid)"
    #text = "Mark de Vries"
    #text = "-27.35"

    #text = "hoe het kon wist hij niet\nmaar dat het kon\r\nwas niet zeker"
    #text = "dog.bark()"
    #text = "Spider-Man Menaces City!"

    return text


def findFirstMatch():
    text = getText()
    pat = getPattern()

    print("text  :", text)
    print("pattern:", pat)

    #m = re.match(pat, text)		#begin text moet matchen ->match-obj; alsof je begint met ^
    #m = re.match(pat, text, re.IGNORECASE)    #of re.I; flags combi met |
    m = re.search(pat, text)		#zkt vanaf begin text naar 1e match
    #m = re.fullmatch(pat,text)		#hele text moet matchen, vgl ^..$ [vanaf 3.4]

    #p = re.compile(pat)
    #p = re.compile(getPattern(), re.IGNORECASE)    # flags combi met |
    #print("aantal capturing groups:", p.groups)
    #m = p.match(text)             #,pos,endpos
    #m = p.search(text)            #idem
    #m = p.fullmatch(text)         #idem
            
    if m:
        #print(m)                #<_sre.SRE_Match object; span=(0, 10), match='23/05/2006'>
        print(m.group())	#m.group() == m.group(0), hele match
    else:
        print("Geen match")
	
def finditerMatchesAndGroups():
    text = getText()
    pat = getPattern()

    print("text  :", text)
    print("pattern:", pat)

    p = re.compile(pat)
    #p = re.compile(pat, re.IGNORECASE)
    print("aantal capturing groups:", p.groups)
    print("groupindex:", p.groupindex)      #dict: named groups + group nrs

    #for m in re.finditer(pat, text):      #iterator-obj
    #for m in re.finditer(pat, text, re.IGNORECASE):
    for m in p.finditer(text):     #,pos,endpos (zoek van .. tot)
        toonMatch(m)

def toonMatch(m):
    if m is None:
        print("Geen match")
        return
    #print("pattern=", m.re.pattern)
    #print("text  =", m.string)

    #m.start(i)/.end(i)/.group(i); group(0) = group() = hele match,            
    print("Match: start=%d, end=%d, value=%s" % (m.start(), m.end(), m.group()))
    print(m.groups())           #->tupel v strings
    #print(m.groups('QQ'))      #dflt voor groups die niet meedoen, bv (\w)?
    #print(m.groupdict())        #->dict: alle named groups + values
    for g in m.groups():
        print("  %s" % g)           #->str


def tstDatumFindall():
    #text = "05/01/2006"
    text = "Dates between 05/01/2006 and 08/31/2007."
    #pat = r"\d\d[-/]\d\d[-/]\d{4}"          #->['05/01/2006', '08/31/2007']
    #pat = r"\d\d([-/])\d\d\1\d{4}"          #->['/', '/']
    pat = r"(\d\d)([-/])(\d\d)\2(\d{4})"    #prut uitkomst
    # ->[('05', '/', '01', '2006'), ('08', '/', '31', '2007')]

    # re.findall ->list, met:
    # als pat zonder groepen ->alle match-str
    # als pat met 1 groep ->alle groep-str
    # als pat meer groepen ->per match tupel met alle groep-str
    s = re.findall(pat,text)   #,flags; ->list
    print(s)

def tstDatumSplit():
    #text = "Dates between 05/01/2006 and 08/31/2007."
    #text = "appel, peer, banaan, kiwi, citroen."
    #text = "appel en peer en banaan en kiwi of citroen."
    text = "words... words... words..."
    #pat = r"\d\d[-/]\d\d[-/]\d{4}"          #->['05/01/2006', '08/31/2007']
    #pat = r"\d\d([-/])\d\d\1\d{4}"          #->['/', '/']
    #pat = r"(\d\d)([-/])(\d\d)\2(\d{4})"    #prut uitkomst

    #s = text.split()
    #s = text.split(" en ")      #"en", " en "

    s = re.split(r"\W+", text)
    #s = re.split(r"[,.]", text)
    print(s)

def tstDatumReplace():
    #text = "05/23/2006"
    text = "Dates between 05/01/2006 and 08/31/2006."

    pat = r"(\d\d)([-/])(\d\d)\2(\d{4})"	#datum met groepen
    repl = r"\3-\1-\4"         #goed, let op: repl-groep met \1 ipv $1 enz
    #repl = r"$3-$1-$4"          #niks; wel goed bij Java, C#

    #pat = r"(?P<mnd>\d\d)([-/])(?P<dag>\d\d)\2(?P<jr>\d{4})"  #named groups
    #repl = r"\g<dag>-\g<mnd>-\g<jr>"            #goed
    #repl = r"(?P=dag)-(?P=mnd)-(?P=jr)"        #niks

    print("text:\n%s" % text)
    
    print("\nre.sub():")
    print(re.sub(pat,repl,text))        #,count,flags; ->str
    #print(re.subn(pat,repl,text))       #idem; ->(str,count_repl)

    print("\nre.finditer() met m.expand():")
    #m = re.match(pat, text)        #match begin
    #m = re.search(pat, text)        #zk 1 match vanaf begin
    #if m:
    for m in re.finditer(pat, text):
        print(m.group())                                #05/23/2006
        print("  ", m.group(1), m.group(3), m.group(4))       #05 23 2006
        #print(m.group('mnd'), m.group('dag'), m.group('jr'))
        print("  ", m.group(1, 3, 4))                 #('05', '23', '2006')
        print("  ", m.expand(repl))                   #23-05-2006

def tstDatumReplace_fn():
    def onmatch(m):             #repl-fn
        try:
            t = time.strptime(m.group(), "%m/%d/%Y")    #struct_time
            return time.asctime(t)
        except ValueError:
            return "##Error##"
    
    #text = "05/23/2006"
    #text = "05/32/2006"
    #text = "11/28/1956"
    text = "Dates between 05/01/2006 and 08/31/2006."

    pat = r"(\d\d)([-/])(\d\d)\2(\d{4})"	#datum met groepen

    print("text:\n%s" % text)
    
    print("\nre.sub():")
    print(re.sub(pat,onmatch,text))        #,count,flags; ->str

def tstVerwoerdReplace():
    # test met re.sub() en re.finditer(); geen named groups

    # vlg eerste \ werkt wel, want geen raw str
    text = """\
12,"Botha","020-4573321",1630.45
13,"Verwoerd","010-4571111",2250
14,"de Klerk","030-4571818",4510.90
"""

    # vlg werkt niet met naam "de Klerk", want \w geen spatie ->doe: [ \w]+
    #pat = r'(?m)^(\d+),"(\w+)","(\d+-\d+)",(\d+(\.\d\d)?)$'     #multiline: (?m)
    pat = r'(?m)^(\d+),"([ \w]+)","(\d+-\d+)",(\d+(\.\d\d)?)$'   #ok met "de Klerk"
    #pat = r'^(\d+),"([ \w]+)","(\d+-\d+)",(\d+(\.\d\d)?)$'      #eist vlag re.M
    
    #pat = r"^(\d+),\"([ \w]+)\",\"(\d+-\d+)\",(\d+(\.\d\d)?)$"     #goed, met \"
    #pat = r"^(\d+),""([ \w]+)"",""(\d+-\d+)"",(\d+(\.\d\d)?)$"     #niks
    # vor "" binnen str geen escape, maar concatenated strings

    # vlg raw str -> een \ voor "blijf op zelfde regel" werkt niet
    # mag ook \g<1> ipv \1; handig bij bv \20 (grp 20) vs \g<2>0 (grp 2 + '0')
    repl = r"""id=\1
nm=\2
tel=\3
sal=\4
"""

    print("Met re.sub(..):")
    print(re.sub(pat,repl,text))        #,count,flags; ->str
    #print(re.sub(pat,repl,text, flags=re.M))       #re.MULTILINE

    print("Met re.finditer(..):")
    it = re.finditer(pat, text)
    #it = re.finditer(pat, text, flags=re.M)
    for m in it:
        #print(m.group())           #12,"Botha","020-4573321",1630.45
        #print(m.group(1,2,3,4))     #('12', 'Botha', '020-4573321', '1630.45')
        print(m.expand(repl))           #toon resultaat v repl-str

def tstVerwoerdReplace2():
    # test met re.compile() en p.sub(); wel named groups

##    text = """\
##12,"Botha","020-4573321",1630.45
##13,"Verwoerd","010-4571111",2250
##14,"de Klerk","030-4571818",4510.90"""

##    text = """\
##12,'Botha','020-4573321',1630.45
##13,"Verwoerd","010-4571111",2250
##14,'de Klerk','030-4571818',4510.90"""

    text = """\
12,'Botha','020-4573321',1630.45
13,"Verwoerd","010-4571111",2250
14,de Klerk,030-4571818,4510.90"""

    # vlg met " als string-symbool ->werkt niet bij 'Botha' of Botha
    #pat = r'^(?P<id>\d+),"(?P<nm>[ \w]+)","(?P<tel>\d+-\d+)",(?P<sal>\d+(\.\d\d)?)$'
    # vlg met ([\'\"]?) of ([\'"]?) als string-symbool ->werkt wel
    # zonder ? werkt laatste rg met de Klerk (zonder quotes) niet
    # (kijkt per text-rg naar 1e string-symbool + allemaal backrefs)
    pat = r'^(?P<id>\d+),(?P<sym>[\'\"]?)(?P<nm>[ \w]+)(?P=sym),(?P=sym)(?P<tel>\d+-\d+)(?P=sym),(?P<sal>\d+(\.\d\d)?)$'

    # vlg if-test niet nodig: test of sep-grp bestaat, zoja, toon sep-grp
    #pat = r'^(?P<id>\d+),(?P<sym>[\'\"]?)(?P<nm>[ \w]+)(?(sym)(?P=sym)),(?(sym)(?P=sym))(?P<tel>\d+-\d+)(?(sym)(?P=sym)),(?P<sal>\d+(\.\d\d)?)$'
    #print(pat)

    repl = r"""id=\g<id>
nm=\g<nm>
tel=\g<tel>
sal=\g<sal>
"""

    p = re.compile(pat, flags=re.M)     #re.MULTILINE
    print("group count: %d\n" % p.groups)
    #print(p.groupindex)
    s = p.sub(repl,text)
    print(s)

def tstGreedyLazyQuantifier():
    text = "Java 7, Java 6"
    #p = re.compile(r"Java.+\d")         #greedy quantifier .+
    p = re.compile(r"Java.+?\d")       #lazy quantifier .+?
    for m in p.finditer(text):
        print(m.group())

def tstLookBehindForward():
    text = "We werken met Java 7 of Java 8 of Java9, niet VB 5 of VB 6 of CPP 11."
    #pat = r"\d+"
    #pat = r"(?<=Java\s)\d+"         #goed, look behind
    #pat = r"\d+(?<=Java\s)"          #niks
    #pat = r"\w+(?=\s\d+)"           #goed, look forward
    #pat = r"\w+(?=\s?\d+)"          #niet goed, geeft laatste match=1
    pat = r"[a-zA-Z]+(?=\s?\d+)"    #goed
    #pat = r"(?=\s\d+)\w+"           #niks
    for m in re.finditer(pat, text):
        print("pos=%d, match=%s" % (m.start(), m.group()))
    

def tstEscape():
    import string
    #s = string.punctuation
    #->\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^_\`\{\|\}\~
    s = "Crystal (Williams_syndrome) speaks out!"
    #->Crystal\ \(Williams\ syndrome\)\ speaks\ out\!
    t = re.escape(s)        #zet \ voor alle \W teks
    print(t)

def zkDubbele():
    #text = "zo zo, die zit in in de pan"
    text = "Zo zo, die zit in in de pan"
    pat = r"(\b\w+\b)\s+\1"

    # vlg zonder apart compileren
    # match() en search() geven 1 match
    #m = re.match(pat, text)
    #m = re.search(pat, text)
    #m = re.search(pat, text, re.IGNORECASE)
    #toonMatch(m)

    lst = re.findall(pat, text, re.IGNORECASE)
    print(lst)              # ['Zo', 'in'], dus toont groepen indien aanwezig


#---- script: ----

#findFirstMatch()
#finditerMatchesAndGroups()

#tstDatumFindall()
tstDatumSplit()

#tstDatumReplace()
#tstDatumReplace_fn()

#tstVerwoerdReplace()
#tstVerwoerdReplace2()

#tstGreedyLazyQuantifier()
#tstLookBehindForward()
#tstEscape()
#zkDubbele()


