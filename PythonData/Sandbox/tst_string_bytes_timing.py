# testen met string en format
# Python 3.6 f-strings

r"""
Python source file heeft zelf std utf-8 encoding.
Dit kun je wijzigen door bovenin, of als 2e regel na #! ...,
dit commentaar te zetten: # -*- coding: iso-8859-1 -*-
Je mag accenten enz in identifiers gebruiken (brrr).

gewone strings mogen met '..' en ".."
strings met 3 quotes mogen over meerdere regels lopen

encoding:
zie filehandling.py

class string.Formatter bevat de s.format(..) functionaliteit

format tekens met %:
%s   string    %20s ->min 20 tekens rechts uitlijnen, %-20s idem links uitlijnen
%r   repr string, vgl repr(..) ipv str(..)
%c   1 char
%d   int       %10d ->10 pos; %010d voorloopnullen; geen %,d voor duizendtallen
%i   int
%o   octal
%x   hex       %X idem hfdlett

%f   float     %.2f ->2 cijf achter komma
%e   exp (10)  %E idem hfdlett
%g   generic   voor kleine getallen %f, anders %e
%%   een % afdrukken


"""

import string           #bevat string constanten + class Formatter
import codecs           #gebr in test_hex_str_byte()
import binascii         #bytes<->hex; maar ook: uu, binhex, base64, crc, enz

import time
from timeit import timeit,repeat

# vlg tab voor Mies gemaakt in UltraEdit, want IDLE doet <tab> -> 4 sp
s1 = """Aap
Noot
	Mies
\tWim
Zus"""

s2 = """\
appel
peer
ban\
aan
"""

s3 = "Aap\nNoot\n\tMies\n\tWim\nZus"

s4 = "appel" "taart" "en"

s5 = "appel" \
"taart"\
"en"

s6 = "appel\
taart\
en"

s7 = "boek"\
     "en"\
     "bal"

s8 = ("boek"
      "en"
      "bal")

s10 = "d:\bak\data"             #wordt d:ak\data, want \b is bs
s11 = "d:\\bak\\data\\"         #goed, geeft d:\bak\data\

s12 = r"d:\bak\data"            #goed
#s13 = r"d:\bak\data\"          #error, afsluitende enkele \ mag niet
s13 = r"d:\bak\data\\"          #geeft ..data\\
s14 = r"d:\bak\data\x5c"        #geeft ..data\x5c
s15 = r"d:\bak\data" "\\"       #goed, geeft d:\bak\data\

def test_strings():
    s = s1
    #s = s2
    #s = s3
    #s = s4
    #s = s5
    #s = s6
    #s = s7
    #s = s8
    #s = s10
    #s = s11
    #s = s12
    #s = s13
    #s = s14
    #s = s15
    
    print(s)
    print('-'*10)
    print(repr(s))

def test_self_repl():
    s = 's=%r;print(s%%s)';print(s%s)
    
def test_stringmodule():
    print("ascii:")
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.ascii_letters)

    print("\nprintable:")
    print(string.printable)

    print("\ndigits:")
    print(string.digits)
    print(string.hexdigits)
    print(string.octdigits)

    print("\npunctuation:")
    print(string.punctuation)       #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    print("\nwhitespace [repr()]:")
    print(repr(string.whitespace))  #' \t\n\r\x0b\x0c'; \x0b=\v, \x0c=\f=formfeed

    print()
    s = "piet krediet woont hier niet."
    print(s)
    print(s.capitalize())
    print(s.title())                #ieder woord in hfdlett
    print(string.capwords(s))       #idem; ,sep=dflt sep's


def test_format():
    naam = "Jan"
    leeftijd = 34
    getrouwd = True
    #print(naam + " is " + leeftijd + " jaar!")       #error conversie int->str
    #print(naam + " is " + str(leeftijd) + " jaar!")     #goed
    print(naam, "is", leeftijd, "jaar!")            #goed, conv zelf, zet sp bij ,
    print(naam, "is", leeftijd, "jaar!", sep='->')
    #print("  en getrouwd: %d" % getrouwd)          #1, %f ->1.000000
    print("  en getrouwd: %s" % getrouwd)           #True

    #print("Is %s %d jaar?" % (naam,leeftijd))           #goed
    #print("Is %s %d jaar?" % (naam,leeftijd,getrouwd))  #error
    # TypeError: not all arguments converted

    #print("{0} is {1} jaar.".format(naam,leeftijd))     #goed
    print("{0} is {1} jaar.".format(naam,leeftijd,getrouwd))    #goed
    # mag aan .format() meer args meegeven dan velden in fmt-str
    #print("{} is {} jaar.".format(naam,leeftijd))       #ook goed, zonder nrs
    #print("{1} is {0} jaar.".format(leeftijd,naam))     #goed, nrs+args omgekeerd

    #named args:
    #print("%(name)s is %(age)d jaar!" % dict(name=naam,age=leeftijd))   #goed, eist dict
    print("%(name)s is %(age)d jaar!" % {'name': naam, 'age': leeftijd})    #idem
    print("%(name)s is %(age)d jaar!" % {'name': naam, 'age': leeftijd, 'gebonden': getrouwd})
    print("%(naam)s is %(leeftijd)d jaar!" % locals())  #=dict met loc vars
    # dict mag groter zijn dan aantal % in fmt-str

    print("{name} is {age} jaar.".format(name=naam,age=leeftijd))
    print("{name} is {age} jaar.".format(name=naam.upper(),age=leeftijd+1))  #goed
    #print("{name.upper()} is {age+2} jaar.".format(name=naam,age=leeftijd)) #error
    # vor mag alleen met props, niet met methods of expressies
    print("{naam} is {leeftijd} jaar.".format(**locals()))

    # Python 3.6 f-string; mag f en F
    print(f"{naam} is {leeftijd} jaar...")    #kijkt autom naar locals
    print(f"{naam.upper()} is {leeftijd+2}{' en getrouwd' if getrouwd else ''}...")
    # vor goed; f-string veld mag expr bevatten
    # niet handig als data in dict zitten

    print(f"{2 + 3 * 4}")           #14, goed


def test_format_getal():
    prijs = 17.59
    btw = 0.06
    prijsincl = prijs * (1 + btw)

    print("Het boek kost %f euro." % prijsincl)
    print("Het boek kost %.2f euro." % prijsincl)       #afronden 2 decimalen
    print("Het boek kost {0:.2f} euro.".format(prijsincl))
    # vlg arg binnen arg; hier afronden op 3 decimalen:
    print("Het boek kost {0:.{1}f} euro.".format(prijsincl,3))
    #print("Het boek kost %.%df euro." % (prijsincl,3))     #error

    print("q" + format(prijsincl,'.2f') + "q")  #fmt spec geen spaties of teks


def test_format_specs():
    code = 25
    print("Code = [%d]" % code)                 #Code = [25]
    print("Code = [%6d]" % code)                #Code = [    25]
    print("Code = [%06d]" % code)               #Code = [000025]
    print("Code = [%-6d]" % code)               #Code = [25    ]
    print("Code = [%-06d]" % code)              #Code = [25    ]
    #print("Code = [%,d]" % 1234)               #error

    print("Code = [{0:6}]".format(code))        #Code = [    25]
    print("Code = [{0:6d}]".format(code))       #Code = [    25]
    print("Code = [{0:06}]".format(code))       #Code = [000025]
    print("Code = [{0:06d}]".format(code))      #Code = [000025]
    print("Code = [{0:0<6d}]".format(code))     #Code = [250000]
    print("Code = [{0:0^6d}]".format(code))     #Code = [002500]
    print("Code = [{0:0^7d}]".format(code))     #Code = [0025000]
    
    print()
    print("Code = [{0:,}]".format(12345678))    #Code = [12,345,678]
    print("Code = [{0:,}]".format(1234))        #Code = [1,234]
    print("Code = [{0:6,}]".format(1234))       #Code = [ 1,234]
    print("Code = [{0:-6,}]".format(1234))      #Code = [ 1,234]
    print("Code = [{0:<6,}]".format(1234))      #Code = [1,234 ]
    print("Code = [{0:^<6d}]".format(25))       #Code = [25^^^^]
    print("Code = [{0:<^6d}]".format(25))       #Code = [25^^^^]
    
    #print("Code = [{0:,06}]".format(code))     #error


def test_slice():
    naam = 'Frits van Egter'

    print('naam=%s, len=%d' % (naam,len(naam)))
    print(id(naam))
    print(type(naam))

    print(naam[0])          #een letter
    #naam[0] = 'A'          # TypeError, kan string niet wijzigen

    print(naam[0:5])        #een slice, vanaf pos 0 tot aan pos 5
    print(naam[:5])         #idem
    print(naam[0:naam.find(' ',0)] + 'q')   #zoek pos 1e spatie vanaf 0; -1=niet gevonden
    print(naam[0:naam.rfind(' ',0)] + 'q')  #zoekt laatste spatie vanaf 0
    print(naam.find(' ',0), naam.rfind(' ',0))      # 5 9

    print(naam[6:9])
    print(naam[6:])         #vanaf pos 6
    print(naam[0:9:2])      #van:tot:stapgrootte
    print(naam[0:len(naam):3])
    print(naam[::3])
    print(naam[0:6:-1])     #toont niks
    print(naam[6:0:-1])     #van 6 tot aan 0 achterstevoren, laat 'F' weg
    print(naam[6:-1:-1])    #niks, want -1 = laatste letter, NIET links v 1e letter
    print(naam[6::-1])      #van 6 terug t/m 0
    print(naam[::-1])
    print(reversed(naam))   # <reversed object at 0x01F47E30>
    for a in reversed(naam):
        print(a, end='')
    print()


def test_str_fn():
    s = 'bol'.translate({ord('o'):'a'})     #moet met ord()
    print(s)
    t = str.maketrans('aou','uao')  #wordt dict met van:naar als ord():ord()
    print(t)
    print('bullebak'.translate(t))

    s = 'café'
    print('s: %s heeft len %d' % (s, len(s)))   # s: café heeft len 4
    t = s.encode('utf8')
    print('t: %s heeft len %d' % (t, len(t)))   # t: b'caf\xc3\xa9' heeft len 5


def test_str_isXXX():
    print('   '.isspace())              #True
    print(' \t\n\v '.isspace())         #True

    print()
    print('Appel'.isalpha())            #True
    print('Appel '.isalpha())           #False
    print('Appel5'.isalpha())           #False
    print('Appel5'.isalnum())           #True

    print()
    print('appel'.islower())            #True
    print('Appel'.islower())            #False
    print('appel 5'.islower())          #True
    print('Appel'.isupper())            #False

    print()
    print('Appel'.istitle())            #True
    print('Appel Peer'.istitle())       #True
    print('AppelPeer'.istitle())        #False

    print()
    # dec <= dig <= num; heeft met unicode getal-symbolen te maken
    # dec: moet cijfers zijn
    # dig: mag ook super/subscript, (1) [=1 in rondje], enz
    # num: mag ook 1/2, III [=romeins] of (50) [-50 in rondje], enz
    print('123'.isdecimal())            #True
    print('-123'.isdecimal())           #False
    print('123.50'.isdecimal())         #False
    print('123,540'.isdecimal())        #False
    
    print()
    print('123'.isdigit())              #True
    print('020-6203412'.isdigit())      #False
    print('123.50'.isdigit())           #False
    print('123,540'.isdigit())        #False

    print()
    print('123'.isnumeric())            #True
    print('-123'.isnumeric())           #False
    print('123.50'.isnumeric())         #False
    print('123,540'.isnumeric())        #False


def test_split():
    s = "Een klein ongemak ligt op de loer."
    print(s)
    #x = s.split()           #alle space-kars
    #x = s.split(' ')        #['Een','klein','ongemak','ligt','op','de','loer.']
    x = s.split(' ',2)      #2 splits ->3 delen: ['Een', 'klein', 'ongemak ligt op de loer.']
    print(x)
    x = s.rsplit(' ',2)     #['Een klein ongemak ligt op', 'de', 'loer.']
    print(x)
    # vlg .partition eist split-kar, geen dflt
    #x = s.partition(' ')    #('Een',' ','klein ongemak ligt op de loer.')
    x = s.rpartition(' ')    #('Een klein ongemak ligt op de', ' ', 'loer.')
    print(x)

    t = s.replace(' ','\n')
    print(t)
    x = t.splitlines()      #dflt: keepends=False, dwz \n weghalen; splits t op \n
    print(x)


def test_join():
    lst = ['appel','peer','banaan','kiwi']
    #s = ' '.join(lst)
    #s = '\n'.join(lst)
    s = ' en '.join(lst)
    print(s)
    #s = '|'.join(range(5))     #error: str + int
    s = '|'.join(str(i) for i in range(5))      #goed; .join() wil iterable
    print(s)


def test_unicodechars():
    #s = "Montréal"             #len=8
    #s = "Montr\xe9al"          #goed, e-aigu
    #s = "Montr\u00e9al"         #\u eist 4 cijfers
    #s = "Montre\u0301al"        #\u0301 is losse aigu {COMBINING ACUTE ACCENT}
    #s = "Montre\N{COMBINING ACUTE ACCENT}al"     #len=9, de accent is apart teken
    #print(len(s))

    #s = "De -€- is de munt van de EEG"
    #s = "De -\u20ac- is niet de munt van Denemarken"
    s = "Noorwegen heeft ook geen \N{EURO SIGN}"
    #s = "Magic \u0394-Forces everywhere!"
    #s = "Magic \N{GREEK CAPITAL LETTER DELTA}-Forces everywhere!"
    #s = "\u0394\u03a3- of \N{GREEK CAPITAL LETTER SIGMA}\N{greek capital letter delta}-converters worden vaak in moderne DACs gebruikt"
    #s = "ΔΣ zie je ook in ADCs"
    #s = "a \xac \u1234 \u20ac \U00008000"
    #s = "codes: \2 \02 \03 \04 \5 \08 \09"

    print(s)

    #cp = ord('€')           #code point
    #print(cp, hex(cp), chr(cp))
    #import unicodedata
    #print(unicodedata.name('€'))


def test_decoding_byte_str():
    # Jij moet bij decode vertellen welke encoding de bytes hebben;
    # Python ziet alleen een reeks bytes, maar gebr default utf-8:
    # b.decode() == b.decode('utf-8'); s.encode() == s.encode('utf-8')
    # zie sys.getdefaultencoding()
    # LET OP: file encoding is anders!
    # zie locale.getpreferredencoding() ->win: cp1252; apple: utf-8
    # sys.stdout.encoding ->console: utf-8; win IDLE: cp1252

    #b = b'Montr\xe9al'             #iso-8859-1; \xe9 geen utf-8
    #b = b'Montr\xc3\xa9al'         #utf-8, e-aigu
    #b = b'Montr\u00e9al'           #niks, wordt b'Montr\\u00e9al'
    b = b'Het \x80-teken'          #cp1252; \x80 ongeldig in iso-8859-1, utf-8
    # ->weggelaten in 8859, UnicodeDecodeError in utf-8
    #b = b'Het \xe2\x82\xac-teken'   #utf-8, euro
    #b = b'B\xc3\xbccher'            #utf-8, u-umlaut
    
    #s = b.decode()                 #dflt utf-8
    #s = b.decode('utf-8')          #dflt 'strict' ->UnicodeDecodeError
    s = b.decode('utf-8', 'ignore')     #'strict','replace','ignore'
    # 'replace': vervang tek door \ufffd, dat is '�'

    #s = b.decode('iso-8859-1')     #=='latin-1'
    #s = b.decode('cp1252')
    #s = b.decode('utf-16')

    print(b,"->", s)
    print("utf-8 :", s.encode('utf-8'))
    print("utf-16:", s.encode('utf-16'))


def test_encoding_str_byte():
    #s = 'piet'
    #s = 'Montréal'             #goed
    #s = 'Montr\xe9al'          #goed, e-aigu
    #s = 'Montr\u00e9al'         #\u eist 4 cijfers
    #s = 'Montre\u0301al'        #\u0301 is losse aigu (COMBINING ACUTE ACCENT)
    s = 'De -€-'               #goed in cp1252,utf-8; UnicodeError in 8859
    #s = 'De -\x80-'             #wordt leeg teken; in utf-8: b'De -\xc2\x80-'
    #s = 'De -\u20ac-'           #goed
    #s = 'De -\u00ac-'           #De -¬-

    b = s.encode()              #dflt utf-8
    #b = s.encode('utf-8')          #€ ->'\xe2\x82\xac'
    #b = s.encode('iso-8859-1')      #dflt 'strict', € ->UnicodeEncodeError
    #b = s.encode('iso-8859-1','ignore')     #'strict','replace','ignore'
    # 'replace': vervang tek door '?'
    
    #b = s.encode('cp1252')
    #b = s.encode('ascii')      #error cannot encode '\xe9' bij 'Montréal'
    #b = s.encode('iso-8859-1','xmlcharrefreplace')  #8859: € ->'&#8364;', niet utf-8
    #b = s.encode('iso-8859-1','backslashreplace')   #8859: € ->'\\u20ac'

    print(s, "->", b)
    # Montréal -> b'Montr\xc3\xa9al'        #e-aigu
    # Montréal -> b'Montre\xcc\x81al'       #e+losse aigu


def test_hex_str_byte():
    myhex = "3a4a4bc9"
    #myhex = "3A4A4BC9"
    #myhex = "3a 4a 4b c9"

    print("myhex:", myhex)
    b = bytes.fromhex(myhex)           #wel goed met spaties
    #b = codecs.decode(myhex, 'hex')     #niet met spaties
    #b = binascii.unhexlify(myhex)       #niet met spaties
    #b = binascii.a2b_hex(myhex)         #niet met spaties
    print(b)                            #b':JK\xc9'

    s = b.hex()                         #3a4a4bc9 (str); Python 3.5
    #s = codecs.encode(b, 'hex')        #eist bytes, ->b'..'
    #s = binascii.hexlify(b)           #eist bytes, ->b'..'
    #s = binascii.b2a_hex(b)            #hetzelfde
    print(s)

    print("kleur: #%02x%02x%02x" % (13,255,230))

def time_str_join_plus_is():
    N = 100000
    timer = time.perf_counter        #stabieler
    #timer = time.process_time       #minder stabiel

    tst = 4
    if tst == 1:                #Netbook: 0.054-0.064
        lst = []
        t = timer()
        for i in range(N):
            lst.append('x')
        s = " ".join(lst)
        t = timer() - t
        print("len(s)=", len(s))
        print(t)
    elif tst == 2:              #Netbook: 0.050-0.063
        t = timer()
        s = " ".join('x' for i in range(N))
        t = timer() - t
        print("len(s)=", len(s))
        print(t)
    elif tst == 3:
        t = timer()
        s = ""
        for i in range(N):
            s += "x "          #Netbook: 0.088-0.094
            #s = s + "x "        #Netbook: 0.089-0.097
        t = timer() - t
        print("len(s)=", len(s[:-1]))
        print(t)

    elif tst == 4:
        s = ""         #overbodig, moet in setup=
        t = timeit(
'''
for i in range(N):
    s += "x "          #Netbook: 0.088-0.094
    #s = s + "x "        #Netbook: 0.089-0.097
#print(len(s))         #->200000
#print(N)               #->100000
''', globals=locals(), setup='s=""', number=1)
        #print("len(s)", len(s[:-1]))       #->0
        print(t)        #->float
        # let op: bij number > 1 wordt s steeds groter, want setup
        # draait maar 1 keer; tijd wordt totale tijd, niet gem tijd
        # hij herkent N wel vanwege locals(), maar niet s
        print(locals())
    elif tst == 5:
        t = timeit(
'''
s = ""
for i in range(N):
    s += "x "          #Netbook: 0.088-0.094
    #s = s + "x "        #Netbook: 0.089-0.097
#print(len(s))         #->200000
#print(N)               #->100000
''', globals=locals(), number=1)
        print(t)        #->float

    elif tst == 6:
        t = repeat(
'''
for i in range(N):
    s += "x "          #Netbook: 0.088-0.094
    #s = s + "x "        #Netbook: 0.089-0.097
print(len(s))         #->200000
#print(N)               #->100000
''', globals=locals(), setup='s = ""', number=1, repeat=3)
        print(t)        #->list[float]


def time_str_startswith_slice():
    N = 1000
    timer = time.perf_counter        #stabieler
    #timer = time.process_time       #minder stabiel

    lst = ["appel","aardappel","konijn","uitverkoop","magazijn","appeltaart"]*1000
    tel = 0

    tst = 2
    if tst == 1:                #Netbook: 5.31-5.45
        t = timer()
        for i in range(N):
            for s in lst:
                if s.startswith("appel"):
                    tel += 1
        t = timer() - t
        print("tel=", tel)
        print(t)
    elif tst == 2:              #Netbook: 5.33-5.47
        t = timer()
        for i in range(N):
            for s in lst:
                if s[:5] == "appel":
                    tel += 1
        t = timer() - t
        print("tel=", tel)
        print(t)


#--- script ---

#test_strings()
#test_self_repl()
#test_stringmodule()
#test_format()
#test_format_getal()
#test_format_specs()

#test_slice()
#test_str_fn()
#test_str_isXXX()

#test_split()
#test_join()

#test_unicodechars()
#test_decoding_byte_str()
#test_encoding_str_byte()

#test_hex_str_byte()

#time_str_join_plus_is()
time_str_startswith_slice()

