#Oefeningen met filehandling


import csv                  #lezen/schrijven Excel .csv bestand
import struct               #voor binair schrijven/lezen v doubles, enz
import os
import time
import glob

def schrijf_tekst():
    fh = open("supergroep.txt", "w")      #default "r"=read, "w"=write truncate
    # "a"=append; "r+"=r/w notrunc, pos=0; "w+"=r/w trunc, pos=0;
    # "a+"=r/w notrunc, pos=end; binary: "rb", "r+b", "wb", w+b"
    #print(fh)              #<_io.TextIOWrapper name='supergroep.txt' mode='w' encoding='cp1252'>
    #print(type(fh))        #_io.TextIOWrapper, encoding='cp1252'
    fh.write("Crosby\n")
    fh.write("Stills\n")
    fh.write("Nash\n")
    fh.write("and Young, who always comes lately.")

    fh.close()
    print("\nKlaar met schrijven")

def lees_tekst():
    fh = open("supergroepp.txt")

    print(fh.read())            #leest alles in 1 keer ->str; bij bin: bytes
    #print(fh.read(6))           #lees 6 teks, ziet crlf als 1 tek
    #for regel in fh:
    #    print(regel, end='')    #zonder end='' krijg je dubbele regelafstand
    # (want file bevat crlf ->wordt afgedrukt->nwe regel + print() ook nwe regel)

    #s = fh.readline()           #wordt "", niet None
    #print(s == '')
    
    fh.close()
    print("\nKlaar met lezen")

def lees_tekst_try():
    fh = None      #zonder deze bij finally UnboundLocalError: local variable 'fh' referenced before assignment
    try:
        #fh = None      #ook goed
        #fh = open('super.txt')
        fh = open('supergroep.txt')
        print(fh.read())
    except FileNotFoundError as ex:
        #print(type(ex).__name__)       #FileNotFoundError
        #print(ex.__class__.__name__)   #FileNotFoundError

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
        if fh is not None:
            fh.close()
    print("\nKlaar met lezen")

def lees_tekst_with():
    with open('supergroep.txt') as fh:
        print(fh.read())

    # volgende kan ook, want Python sluit fh deterministisch als out of scope
    # maar niet zo netjes:
    #print(open(fnaamTekst).read())

def lees_tekst_with_try():
    try:
        with open('groep.txt') as fh:
            print(fh.read())
    except OSError as ex:
        print(ex.__class__.__name__)   #FileNotFoundError
        print(ex)

def schrijf_tekst_with():
    # with maakt een context manager:
    with open("supergroep.txt", "w") as fh:   #sluit fh automatisch
        fh.write("Crosby\n")
        fh.write("Stills\n")
        fh.write("Nash\n")
        fh.write("and Young, who always comes lately.")

    print("\nKlaar met schrijven")

def lees_csv_1():
    fh = open("Koffie_recensies.csv", 'r')       #, newline=''
    for regel in fh:
        print(regel, end='')
    fh.close()

def lees_csv_2():
    fh = open("Koffie_recensies.csv", 'r')       #, newline=''
    rd =  csv.reader(fh)    # (.., delimiter='|')
    for rij in rd:
        #print(rij)
        print(rij[0], rij[1])
    fh.close()

def lees_csv_dict():
    fh = open("Koffie_recensies.csv", 'r')       #, newline=''
    rd =  csv.DictReader(fh)    # (.., delimiter='|') ->dict
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


def schrijf_bin():
    fh = open("data.bin", "wb")

    #schrijf 2 ints, 1 double, 2 booleans
    data = struct.pack("iidbb", 97, 98, 36.75, True, False)    #geeft bytes
    #print(len(data), data)                 #18
    #print(struct.calcsize("iidbb"))        #18

    fh.write(data)
    
    fh.close()
    print("\nKlaar met schrijven")

def lees_bin():
    fh = open("data.bin", "rb")

    data = fh.read()          #lees hele file in byte-string, wordt bytes
    fh.close()

    #print(type(data))     #bytes
    #print(data)           #b'a\x00\x00\x00' enz
    items = struct.unpack("iidbb", data)
    print(items)
    print("int1 = %d, int2 = %d, double = %f, bool1 = %d, bool2 = %d" %
        (items[0], items[1], items[2], items[3], items[4]))
    print("\nKlaar met lezen")

def test_dir():
    print(os.getcwd())       #curr work dir
    #pad = None              #->wordt dflt "."; bij pad=""->FileNotFoundError
    #pad = ".."
    #pad = r"doc"
    pad = r"doccc"

    print("path:", pad)
    print(os.path.abspath(pad))         #geen error als pad niet bestaat
    print("exists:", os.path.exists(pad))
    print("isdir:", os.path.isdir(pad))
    print("isfile:", os.path.isfile(pad))

def test_listdir():
    pad = r"doc"
    #pad = r"doc\*.txt"       #os.listdir()->OSError; glob.glob()->goed

    print("path:", pad)
    if not os.path.exists(pad):
        return

    #print(os.listdir(pad))
    print("name" + " "*24 + " type       size  time")
    for f in os.listdir(pad):       #->list met file/dir namen
        #print(f)
        #print("exists:", os.path.exists(os.path.join(pad,f)))

        #p = pad + '\\' + f
        p = os.path.join(pad, f)         #wordt doc\annual.dat, enz
        printfileinfo(p, f)
        
def printfileinfo(p, f):
    if os.path.isdir(p):
        tp = "D"
    else:
        tp = "B"
    sz = os.path.getsize(p)          #dir krijgt size 0
    secs = os.path.getmtime(p)       #->secs; last modified time
    #print("%-28s %-4s %10d  %d" % (f,tp,sz,secs))

    dt = time.ctime(secs)      #str
    #dt = time.strftime('%d-%m-%Y %H:%M:%S',time.localtime(secs))    #str
    print("%-28s %-4s %10d  %s" % (f,tp,sz,dt))

def test_glob():
    # Python 3.5: ook recurs subdirs met \**\ in pad + ,recursive=True
    #pad = r"doc\*.txt"
    #pad = "doc\\*.txt"
    #pad = "doc/*.txt"        #goed
    pad = r"doc\*.htm*"         #* = 0 of meer tekens
    #pad = r"doc\finance\*.dat"
    #pad = r"doc\* *.*"          #alle files met spatie, kan ook met [ ]
    #pad = r"doc\*[0-9]*.*"      #idem met cijfers

    print("name" + " "*24 + " type       size  time")
    for p in glob.glob(pad):       #->list met voll pad; iglob()->iterator
        f = os.path.basename(p)          #filename

        printfileinfo(p, f)


#--- script ---

schrijf_tekst()
#lees_tekst()
#lees_tekst_try()
#lees_tekst_with()
#lees_tekst_with_try()
#schrijf_tekst_with()

#lees_csv_1()
#lees_csv_2()
#lees_csv_dict()
#schrijf_csv()

#schrijf_bin()
#lees_bin()

#test_dir()
#test_listdir()
#test_glob()
