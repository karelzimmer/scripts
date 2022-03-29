"""
filehandling

moet eigenlijk met try..except.. finally.. of met with.. as..
tekst/binair; struct
lezen/schrijven .csv file; collections.namedtuple

print('d:\\klad\\')        #goed
print(r'd:\klad\')         #cp error, EOL while scanning string literal
 zie helpfile, Python Lang Ref, Lexical Analysis, par 2.4.1:
"Specifically, a raw literal cannot end in a single backslash (since the backslash
would escape the following quote character). Note also that a single backslash
followed by a newline is interpreted as those two characters as part of the literal,
not as a line continuation."

encoding:
bestandsnamen     python t/m 3.5: mbcs; 3.6: utf-8
bestandsinhoud    win: cp1252, apple: utf-8
is locale.getpreferredencoding()

sys.stdout.encoding:
in console:      utf.8
in IDLE-shell:   cp1252 (win), utf-8 (apple)

sys.getdefaultencoding():  utf-8
deze wordt gebr bij s.encode() en b.decode() zonder args

ascii accepteert alleen chars < 128
iso-8859-1 == latin-1: soort ansi met error in bereik \x80 - \x9F
cp1252 vult meeste chars in dit bereik in, bv euro is \x80
veiliger: euro altijd schrijven als \u20ac of '€'.
zie tst_string_bytes_enz.py

"""

import struct               #voor binair schrijven/lezen v doubles, enz
import csv                  #lezen/schrijven Excel .csv bestand

fnaamTekst = "test.txt"
fnaamBin = "data.bin"

def schrijf_tekst():
    fh = open(fnaamTekst, "w")      #default "r"=read, eig: "rt"
    # "w"=write truncate
    # "x"=write, als bestaat ->FileExistsError
    # "a"=append, pos=end
    # "r+"=r/w notrunc, pos=0
    # "w+"=r/w trunc, pos=0
    # "a+"=r/w notrunc, pos=end
    # binary: "rb", "r+b", "wb", w+b", "ab", "a+b"
    #print(type(fh))                 #_io.TextIOWrapper, encoding='cp1252'
    fh.write("Jan\n")
    fh.write("Marie\n")
    fh.write("Geesje\n")
    fh.write("En dan hebben we nog Willem, die altijd te laat komt.")

    fh.close()
    print("\n*** Klaar met schrijven van: %s ***" % fnaamTekst)

def schrijf_tekst_with():
    with open(fnaamTekst, "w") as fh:
        fh.write("Jan\n")
        fh.write("Marie\n")
        fh.write("Geesje\n")
        fh.write("En dan hebben we nog Willem, die altijd te laat komt.\n")

    #je hoeft geen fh.close() te doen, gebeurt automatisch
    print("\n*** Klaar met schrijven van: %s ***" % fnaamTekst)

def lees_tekst():
    fh = open(fnaamTekst)

    #print(fh.read())            #leest alles in 1 keer ->str; bij bin: bytes
    #print(fh.read(6))           #lees 6 teks, ziet crlf als 1 tek
    for regel in fh:
        print(regel, end='')    #zonder end='' krijg je dubbele regelafstand
    #(want file bevat crlf ->wordt afgedrukt->nwe regel + print() ook nwe regel)

    #s = fh.readline()           #wordt "", niet None
    #print(s == '')
    
    fh.close()
    print("\n*** Klaar met lezen van: %s ***" % fnaamTekst)

def lees_tekst_with():
    #print(open(fnaamTekst).read())  #Python sluit deterministisch, zodra fh weg kan
    # of:
    with open('test.txt') as fh:
        print(fh.read())            #leest alles in 1 keer

def lees_tekst_try():
    #fh = None
    try:
        fh = open('test.txt')      #'trala.txt', 'test.txt'
        print(fh.read())
        print(fh.readline())        #wordt "", niet None
        print(fh.readline())
        print(fh.write('Peer\n'))   #wel rt ex
    except FileNotFoundError as ex:
        #print(type(ex).__name__)        #FileNotFoundError
        #print(ex.__class__.__name__)    #FileNotFoundError
        
        print(ex)           #[Errno 2] No such file or directory: 'testt.txt'
        #print(repr(ex))    #FileNotFoundError(2, 'No such file or directory')
        #print(ex.strerror)      #No such file or directory
        #print(ex.winerror)      #None
        #print(ex.args)          #(2, 'No such file or directory')
        #print(ex.errno)         #2
        #print(ex.filename)      #testt.txt
    except OSError as ex:
        print(ex)
    finally:
        print(fh)
        if fh is not None:
            fh.close()
    print("\n*** Klaar met lezen van: %s ***" % fnaamTekst)

def lees_tekst_with_try():
    try:
        with open('tralala.txt') as fh:     #'test.txt', 'tralala.txt'
            print(fh.read())
    except OSError as ex:
        print(ex.__class__.__name__)   #FileNotFoundError
        print(ex)

def append_tekst():
    fh = open(fnaamTekst, "r+")     #'a', 'a+', 'r+', 'w+' 
    #fh.seek(0)             #bij 'a' geen effect, nwe txt altijd achteraan
    fh.write("bad")

    fh.close()
    print("\n*** Klaar met toevoegen aan: %s ***" % fnaamTekst)

def update_tekst():
    # in tekstmode alleen seek(0 [,0]) ->naar begin, seek(0,2) ->achteraan
    fh = open(fnaamTekst, "r+")
    print(fh.read(6))
    fh.seek(0)
    fh.write("qq")          #na read komt write achteraan, tenzij fh.seek(0)
    #fh.seek(0)             #na write komt read wel vanaf curpos, dus na nwe "qq"
    print("---verder lezen---")
    print(fh.read())
    print("\npos =", fh.tell())
    #fh.seek(-14, 1)
    #fh.write("op tijd")

    fh.close()
    print("\n*** Klaar met update van: %s ***" % fnaamTekst)

def lees_schrijf_salaris():
    # lees oude salaristabel in en schrijf nieuwe salarissen
    # formaat: naam \t salcode \t salaris
    # salcode: 1->10%, 2->5%, 3->1% salarisverhoging
    # (de rijken krijgen meer verhoging, omdat ze meer belasting betalen)

    salcodes = {"1": 1.1, "2": 1.05, "3": 1.01}
    fnm_oud = "salaris_oud.txt"
    fnm_nieuw = "salaris_nieuw.txt"
    fhr = open(fnm_oud, "r")
    fhw = open(fnm_nieuw, "w")

    for regel in fhr:       #regel eindigt met '\n'; float(..) filtert \n uit
        oud = regel.split('\t')     #maakt van regel een list met 3 str-items
        #print(oud)
        oud[2] = "%.2f\n" % (float(oud[2]) * salcodes[oud[1]])
        #oud[2] = format(float(oud[2]) * salcodes[oud[1]], ".2f") + "\n"
        #print(oud)
        fhw.write("\t".join(oud))       #.join() maakt van list weer regel

    fhr.close()
    fhw.close()
    print("Salaris verhoging: %s -> %s" % (fnm_oud, fnm_nieuw))

def lees_schrijf_salaris_with_try():
    # lees oude salaristabel in en schrijf nieuwe salarissen

    salcodes = {"1": 1.1, "2": 1.05, "3": 1.01}
    fnm_oud = "salaris_oud.txt"
    fnm_nieuw = "salaris_nieuw.txt"

    try:
        with open(fnm_oud, "r") as fhr, open(fnm_nieuw, "w") as fhw:
            for regel in fhr:
                oud = regel.split('\t')
                oud[2] = "%.2f\n" % (float(oud[2]) * salcodes[oud[1]])
                fhw.write("\t".join(oud))
        print("Salaris verhoging: %s -> %s" % (fnm_oud, fnm_nieuw))
    except Exception as ex:
        print("%s: %s" % (ex.__class__.__name__, ex))

def lees_schrijf_salaris_with_try_try():
    # lees oude salaristabel in en schrijf nieuwe salarissen

    salcodes = {"1": 1.1, "2": 1.05, "3": 1.01}
    fnm_oud = "salaris_oud.txt"
    fnm_nieuw = "salaris_nieuw.txt"

    try:
        with open(fnm_oud, "r") as fhr, open(fnm_nieuw, "w") as fhw:
            for regel in fhr:
                oud = regel.split('\t')
                try:
                    oud[2] = "%.2f\n" % (float(oud[2]) * salcodes[oud[1]])
                except ValueError:
                    oud[2] = "ERROR no float: %s" % oud[2]      #oud[2] eindigt zelfop \n
                fhw.write("\t".join(oud))
        print("Salaris verhoging: %s -> %s" % (fnm_oud, fnm_nieuw))
    except Exception as ex:
        print("%s: %s" % (ex.__class__.__name__, ex))
        

def schrijf_tekst_encoding():
    # alle coderingen in bereik \x80-\x9F gaan in Python fout; \xA0 is harde sp
    # ansi euro=\x80 gaat fout ->gebr in str altijd \u20ac of '€'
    # é=\xE9, ä=\xE4 gaan wel goed
    # euro gaat fout met cp850, latin-1, iso-8859-1
    # utf-8 ->geen sig; utf_8_sig ->wel sig \xef\xbb\xbf
    # C# en Notepad maken bij utf-8 altijd sig; andere progs niet
    # utf-16 ->wel sig, sys afh ->op win \xff\xfe, op unix \xfe\xff
    # (sig = bom, byte order mark)
    # 'utf_16_le/be', 'utf-16-le/be' ->geen sig (gruweldegrotsel)
    # -> zelf toev met voor le: fh.write("\xff\xfe"); be: "\xfe\xff"
    # of codecs.BOM_LE/BE (utf16), .BOM_UTF32_LE/BE; .BOM_UTF8 gaat via codec

    fh = open("test_cp1252.txt", "w")
    #fh = open("test_mbcs.txt", "w", encoding='mbcs')
    #fh = open("test_utf8.txt", "w", encoding='utf-8')          #geen sig
    #fh = open("test_utf8_sig.txt", "w", encoding='utf_8_sig')   #sig \xef\xbb\xbf
    #fh = open("test_utf16.txt", "w", encoding='utf-16')        #sig \xff\xfe
    #fh = open("test_utf16be.txt", "w", encoding='utf_16_be')   #geen sig

    print(fh.encoding)
    fh.write("Eén euro: \u20ac")        #\u20ac
    # r-apos: cp1252=\x20\x18, utf-8=\xe2\x80\x98

    fh.close()
    print("klaar")

def lees_tekst_encoding():
    #fh = open("test_utf16le_sig.txt", "rb")

    fh = open("test_cp1252.txt", "r")       #default cp1252
    #fh = open("test_mbcs.txt", "r", encoding='mbcs')
    
    #fh = open("test_utf8.txt", "r", encoding='utf-8')
    #fh = open("test_utf8_sig.txt", "r", encoding='utf-8')   #herkent zelf sig

    #fh = open("test_utf16le_sig.txt", "r", encoding='utf_16_le')    #goed
    #fh = open("test_utf16le_sig.txt", "r", encoding='utf-16')       #goed
    #fh = open("test_utf16be_sig.txt", "r", encoding='utf_16_be')    #goed
    #fh = open("test_utf16be_sig.txt", "r", encoding='utf-16')       #goed
    
    #fh = open("test_utf16le.txt", "r", encoding='utf_16_le')        #goed, geen sig
    #fh = open("test_utf16le.txt", "r", encoding='utf-16')       #UnicodeError, geen BOM
    #fh = open("test_utf16be.txt", "r", encoding='utf_16_be')        #goed
    #fh = open("test_utf16be.txt", "r", encoding='utf-16')        #UnicodeError
    print(fh.read())

    fh.close()
    print("klaar")


def schrijf_bin():
    fh = open(fnaamBin, "wb")

    #schrijf 2 ints
    fh.write(bytes([97,0,0,0]))
    fh.write((98).to_bytes(4, byteorder='little'))   #of 'big'; Python 3.2
    #schrijf een double
    data = struct.pack("d", 36.75)      #geeft bytes, "<d"|">d" little|big endian
    # c=char(1); b=byte(1), h=short(2), i=int(4), l=long(4), q=longlong(8)
    # B-Q unsigned versie; f=float(4), d=double(8); s=p=char[], P=void *
    # @: native order+native size (alignment); =: native+std; <|>: little|big+std; !: network (big)+std
    #print(len(data), data.hex())
    fh.write(data)
    #schrijf 2 booleans
    fh.write(bytes([True]))
    fh.write(bytes([False]))
    
    fh.close()
    print("\n*** Klaar met schrijven van: %s ***" % fnaamBin)

def lees_bin():
    fh = open(fnaamBin, "rb")

    b1 = fh.read(4)         #wordt bytes, bevat int
    b2 = fh.read(4)         #idem
    b3 = fh.read(8)         #wordt bytes, bevat double
    b4 = fh.read(1)         #wordt bytes, bevat bool
    b5 = fh.read(1)         #idem

    fh.close()

    #print(type(b1))     #bytes
    #print(b1)           #b'a\x00\x00\x00'
    print("int1 = %d, int2 = %d, double = %f, bool1 = %d, bool2 = %d" %
        (int.from_bytes(b1, byteorder='little'),
         int.from_bytes(b2, byteorder='little'),
         struct.unpack("d", b3)[0],      #unpack->tuple, die hier 1 item bevat
         b4[0], b5[0]
    ))
    print("\n*** Klaar met lezen van: %s ***" % fnaamBin)

def schrijf_bin2():
    fh = open(fnaamBin, "wb")

    # schrijf 2 ints, 1 double, 2 booleans
    # std alignment 4 bytes ->bij "ihdbb" (h=short) toch len=18
    # als vooraan ">"|"<"|"=" (native byte order) geen alignment ->len=16
    data = struct.pack("iidbb", 97, 98, 36.75, True, False)    #geeft bytes
    #print(len(data), data)                 #18
    #print(struct.calcsize("iidbb"))        #18
    fh.write(data)
    
    fh.close()
    print("\n*** Klaar met schrijven van: %s ***" % fnaamBin)

def lees_bin2():
    fh = open(fnaamBin, "rb")

    data = fh.read()          #lees hele file in byte-string, wordt bytes
    fh.close()

    #print(type(data))     #bytes
    #print(data)           #b'a\x00\x00\x00' enz
    items = struct.unpack("iidbb", data)
    print("int1 = %d, int2 = %d, double = %f, bool1 = %d, bool2 = %d" %
        (items[0], items[1], items[2], items[3], items[4]))
    print("\n*** Klaar met lezen van: %s ***" % fnaamBin)


def update_bin():
    fh = open(fnaamBin, "r+b")

    #wijzig 2 ints
    fh.write(bytes([99]))
    #fh.seek(4)                  #ga naar abs pos 4 vanaf begin
    fh.seek(3, 1)               #idem, 3 vooruit tov curpos
    fh.write(bytes([100]))
    #wijzig 2 booleans
    fh.seek(-2, 2)              #ga naar einde - 2
    #fh.seek(-2, 1)             #2 terug tov curpos
    fh.write(b"\x00\x01")       #schrijf False, True; moet met b".."
    
    fh.close()
    print("\n*** Klaar met wijzigen van: %s ***" % fnaamBin)


def lees_csv_1():
    fh = open("Koffie_recensies.csv", 'r')       #, newline=''
    for regel in fh:
        print(regel, end='')
    fh.close()

def lees_csv_2():
    fh = open("Koffie_recensies.csv", 'r')       #, newline=''; toont header
    #fh = open("Shippers.csv", 'r')
    rd =  csv.reader(fh)    # (.., delimiter='|')
    for rij in rd:
        print(rij)
        #print(rij[0], rij[1])
    fh.close()

def lees_csv_dict_Koffie():
    fh = open("Koffie_recensies.csv", 'r')       #, newline=''
    rd =  csv.DictReader(fh)            #->dict
    # , delimiter='|', skipinitialspace=True, dialect='excel'|'excel_tab'
    # Python 3.4/3.5: dict ongeordend ->1e item kan bv Schoon zijn
    # Python 3.6: dict wel geordend ->altijd Vestiging als 1e veld
    # in alle gevallen vervolgregels zelfde volgorde als eerste regel
    
    # DictReader toont niet automatisch de kolomkoppen!
    #print(rd.fieldnames)
    #for rij in rd:
    #   print(rij)
    
    print('%-12s %s  %s' % ('Vestiging', 'Schoon', 'Service'))
    for rij in rd:
        print('%-12s %6s  %7s' % (rij['Vestiging'], rij['Schoon'], rij['Service']))

    fh.close()

def lees_csv_dict_Shippers():
    fh = open("Shippers.csv", 'r')

    #Shippers.csv heeft geen header/veldlijst ->apart opgeven
    rd = csv.DictReader(fh, ['ShipperID','CompanyName','Phone'])

    #print(rd.fieldnames)
    #for rij in rd:
    #   print(rij)
    
    print('%-24s %s' % ('CompanyName', 'Phone'))
    for rij in rd:
        print('%-24s %s' % (rij['CompanyName'], rij['Phone']))

    fh.close()

def lees_csv_namedtuple_Shippers():
    from collections import namedtuple

    fh = open("Shippers.csv", 'r')
    #vlg veldlijst mag ook met , of als list met velden
    Shipper = namedtuple('Shipper','ShipperID CompanyName Phone')
    rd =  csv.reader(fh)            #iedere regel wordt een list
    for shp in map(Shipper._make, rd):  #._make: list -> namedtuple
        #print(shp)          # Shipper(ShipperID='1', CompanyName=..' enz)
        print('%2s:  %-24s %s' % (shp.ShipperID, shp.CompanyName, shp.Phone))

    fh.close()

def lees_csv_Sniffer():
    #Shippers.csv geen header/veldlijst; Koffie_recensies wel
    # Koffie_recensies heeft tekstvelden in quotes ".."
    fnaam = "Shippers.csv"
    #fnaam = "Koffie_recensies.csv"

    fh = open(fnaam, 'r')       #, newline=''

    s = fh.read(1024)
    fh.seek(0)
    snf = csv.Sniffer()
    print('heeft headers:', snf.has_header(s))
    dl = snf.sniff(s)       #dialect

    #if dl is not None:
    #print(dl)
    print("skipinitsp=%s\ndelim=%s\nquot=%s\nquoting=%d" %
        (dl.skipinitialspace, dl.delimiter, dl.quotechar, dl.quoting))
    #dl.skipinitialspace = True      #sla ws na delim over; default False
    
    fh.close()
    print("\n*** Klaar met lezen van: %s ***" % fnaam)

def schrijf_csv():
    data = [
        ['Jitske', 7.0, 6.3, 8.5, 6.9],
        ['Jitse', 5.8, 5.4, 6.3, 9.8],
        ['Oetse', 5.9, 5.5, 6.4, 9.7],
        ['Tjerk', 8.5, 8.5, 8.5, 8.6]
    ]

    fnaam = "Cijfers.csv"
    fh = open(fnaam, 'w', newline='')   #zonder deze krijg je cr,cr,lf

    wr = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)     #, quoting=csv.QUOTE_NONNUMERIC (=2)
    wr.writerow(['Naam','Nederlands','Frans','Duits','Engels'])     #kolomkoppen
    wr.writerows(data)
    #for row in data:
    #    wr.writerow(row)

    fh.close()
    print("\n*** Klaar met schrijven van: %s ***" % fnaam)


#------------ hoofdprogramma

schrijf_tekst()
#schrijf_tekst_with()
#lees_tekst()
#lees_tekst_with()
#lees_tekst_try()
#lees_tekst_with_try()

#append_tekst()
#update_tekst()
#lees_schrijf_salaris()
#lees_schrijf_salaris_with_try()
#lees_schrijf_salaris_with_try_try()

#schrijf_tekst_encoding()
#lees_tekst_encoding()

#schrijf_bin()
#lees_bin()
#schrijf_bin2()
#lees_bin2()

#update_bin()

#lees_csv_1()
#lees_csv_2()
#lees_csv_dict_Koffie()
#lees_csv_dict_Shippers()
#lees_csv_namedtuple_Shippers()
#lees_csv_Sniffer()

#schrijf_csv()
