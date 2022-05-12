#filehandling - dirs enz

"""
os:
mkdir(path)
makedirs(path)        mkt autom subdirs
rmdir(path)           dir moet leeg zijn
removedirs(path)      wis dirs v laag naar hoog; moeten leeg zijn
remove(fpath)         wis file

rename(src,dst)       als dst=file->rename; als dst=dir->move file; copy bij andere schijf
replace(fsrc,fdst)
stat/lstat(path)      file attribs

os.path.exists(path)  voor dirs en bestanden

shutil:
copy(src,dst)           dst is dir of file, geen metadata (owner, filedatum)
copy2(src,dst)          idem, wel metadata
copyfile(fsrc,fdst)     beide file
copyfileobj(osrc,odst)  beide file obj
copytree(src,dst)       beide dir
rmtree(dir)             wis dirs, hoeven niet leeg te zijn
move(src,dst)           beide dir of file

pathlib:
Path ->OO-versie v zoekpaden + attribs

glob:
glob(path)             incl wildcards; ->list met voll pad
iglob                  idem; ->iterator
"""

import os, os.path as op        #je hoeft os.path niet apart te importeren
import glob
import time
import stat                     #voor os.stat(pad)->info->.st_mode bitvlaggen
from pathlib import Path

def test_listdir():
    print(os.getcwd(),'\n') #curr work dir
    #pad = None              #->wordt dflt "."; bij pad=""->FileNotFoundError
    #pad = ".."
    pad = r"..\doc"
    #pad = r"..\doc\*.txt"       #os.listdir()->OSError; glob.glob()->goed

    print("path:", pad)
    print("(%s)" % op.abspath(pad))         #geen error als pad niet bestaat
    print("path exists:", op.exists(pad))
    if not op.exists(pad):
        return
    #print(os.listdir(pad))
    print("name" + " "*24 + " type       size  time")
    for f in os.listdir(pad):       #->list met file/dir namen
        #p = pad + '\\' + f
        p = op.join(pad, f)         #wordt ..\doc\annual.dat, enz
        printfileinfo(p, f)
        #printfileinfo_stat(p, f)

def printfileinfo(p, f):
    # voor ieder file attrib aparte fn aanroep ->opnieuw file access
    if op.isdir(p):
        tp = "D"
    elif op.isfile(p):
        tp = "F"
    else:
        tp = "-"
    sz = op.getsize(p)          #dir krijgt size 0
    secs = op.getmtime(p)       #->secs; last modified time
    #secs = op.getatime(p)       #->secs; last access time (bij kopieren->alle files hetzelfde)
    #dt = time.ctime(secs)      #str
    dt = time.strftime('%d-%m-%Y %H:%M:%S',time.localtime(secs))    #str
    print("%-28s %-4s %10d  %s" % (f,tp,sz,dt))

def printfileinfo_stat(p, f):
    # haal in 1 keer alle file attribs op
    info = os.lstat(p)      #volg niet linkjes; met .stat(p) wel
    #print(info)            #->namedtuple
    mod = info.st_mode      #bitvlaggen
    if stat.S_ISDIR(mod):
        tp = "D"
    elif stat.S_ISREG(mod):       #REG = regular file
        tp = "F"
    else:
        tp = "-"
    sz = info.st_size
    secs = info.st_mtime       #last modified time
    #secs = info.st_atime       #last access time (bij kopieren->alle files hetzelfde)
    #dt = time.ctime(secs)
    dt = time.strftime('%d-%m-%Y %H:%M:%S',time.localtime(secs))
    print("%-28s %-4s %10d  %s" % (f,tp,sz,dt))
    
def test_glob():
    # glob gebr intern module fnmatch met fn's:
    # fnmatch(fname,pattern) ->True/False
    # filter(lst,pattern) ->list met matches
    # pattern: *,?,[aeo],![aeo],[0-9]
    # Python 3.5: ook recurs subdirs met \**\ in pad + ,recursive=True
    #pad = None              #->wordt dflt "."; bij pad=""->FileNotFoundError
    #pad = ".."
    #pad = r"..\doc"
    pad = r"..\doc\*.txt"       #os.listdir()->OSError; glob.glob()->goed
    #pad = "..\\doc\\*.txt"
    #pad = "..\doc\*.txt"        #gaat toevallig goed want \d geen escape-char
    #pad = "../doc/*.txt"        #goed
    #pad = r"..\doc\finance\*.dat"
    #pad = "..\doc\finance\*.dat"    #\f esc-char ->zkt ..\docinance\*.dat ->niks
    #pad = r"..\doc\*\*.txt"     #alle directe subdirs v doc
    #pad = r"..\doc\*\*.dat"
    #pad = r"..\doc\*.htm?"         #? = exact 1 teken
    #pad = r"..\doc\*.htm*"         #* = 0 of meer tekens
    #pad = r"..\doc\*.htm[ l]"      #geen .htm, want wil htm[sp] of html
    #pad = r"..\doc\* *.*"          #alle files met spatie, kan ook met [ ]
    #pad = r"..\doc\*[0-9]*.*"      #idem met cijfers
    #pad = r"..\doc\*[!0-9]*.*"     #toont alles

    print("path:", pad)
    print("name" + " "*24 + " type       size  time")
    for p in glob.glob(pad):       #->list met voll pad; iglob()->iterator
        f = op.basename(p)          #filename
        #print(p)
        #print(op.dirname(p))        #dirname zonder laatste '\'|'/'
        #print(op.splitext(p)[1])       #.txt

        printfileinfo(p, f)
        #printfileinfo_stat(p, f)

def test_walk():
    # recursief door subdirs lopen; geeft voor elke dir een tupel
    # met (dir,[subdirs],[files]), dus str,list,list
    pad = r"..\doc"
    #for t in os.walk(pad): print(t)        #->generator-obj; ,topdown=True

    for dir, dirs, files in os.walk(pad):      #dir->str; dirs,files->list
        print('\n%s' % dir)
        for f in files:
            print(" ", f)
        #if 'finance' in dirs:
        #    dirs.remove('finance')         #deze subdir overslaan

def test_walk_compreh():
    pad = r"..\doc"
    #files = [fnm for t in os.walk(pad) for fnm in t[2]]
    #files = [fnm for t in os.walk(pad) for fnm in t[2] if fnm.endswith('.txt')]
    files = [fnm for t in os.walk(pad) for fnm in glob.glob(op.join(t[0],'*.txt'))]
    for f in files: print(f)

def test_walk_recurs():
    # eigenvariant met recurs fn aanroep en os.listdir()
    pad = r"..\doc"
    walk_recurs(pad)

def walk_recurs(dir):
    dirs = []
    print('\n%s' % dir)
    for f in os.listdir(dir):
        p = op.join(dir, f)     #of: dir + '\\' + f
        if op.isdir(p):
            dirs.append(f)
        else:
            print(" ", f)
    for d in dirs:
        walk_recurs(op.join(dir, d))

def test_Path():
    print(Path.cwd())           #->Path-obj, wordt WindowsPath

    pad = r"..\doc\annual.dat"
    #pad = r"D:\PythonData\doc\annual.dat"

    pa = Path(pad)
    print(pa)
    print(pa.is_absolute())
    print(pa.exists())
    print(pa.is_dir(), pa.is_file())        #enz
    # ook pa.mkdir()|.rmdir()|.rename(dst)|.replace(dst)
    # .open(..) ->open best

    pa = pa.resolve()           #mk abs path; resolve links
    print(pa)
    print(pa.parts)
    print(pa.drive, pa.root, pa.anchor)     #anchor = drive + root ('\')
    print(pa.parent, pa.name, pa.suffix)
    print()
    
    pa = Path("../doc")
    pa2 = pa / "finance" / "datum.htm"
    print(pa2)
    print(pa2.stat())

def test_Path_dir():
    pa = Path("../doc")
    print(pa)
    for p in pa.iterdir():
        print(p)                #Path met voll relat pad
    print()

    #zk = "*.htm*"              #huid dir
    #zk = r"*\*.dat"            #subdirs
    zk = r"**\*.dat"            #huid dir + recurs subdirs, ook Python 3.4
    for p in pa.glob(zk):       #generator obj
        print(p)                #Path met voll relat pad

#--- script ---

test_listdir()
#test_glob()
#test_walk()
#test_walk_compreh()
#test_walk_recurs()
#test_Path()
#test_Path_dir()

