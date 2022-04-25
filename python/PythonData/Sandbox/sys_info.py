#sys info

import sys, platform, os, locale

def test_Python_info():
    print(sys.copyright,'\n')
    print(sys.executable)       #huid python exec, bv: pad\pythonw.exe
    print(sys.implementation,'\n')
    print(sys.hexversion, hex(sys.hexversion))  #50595056 ->PYPV, 0x30404f0
    print(sys.version)
    print(sys.version_info)
    print(sys.winver)           #3.4 ->Python-versie

    print('\nsys.path:')
    print(sys.path)             #list

    #print(sys.builtin_module_names)     #ingebouwde C-modules
    
    #print(sys.modules.keys())      #keys v enorme dict met alle geladen modules

def test_sys_platform():
    print(sys.platform)         #win32
    ver = sys.getwindowsversion()      #obj met win-info
    print(ver)
    print(ver.major,ver.minor, ver.platform)        #6 1 2
    print(sys.byteorder)            #little
    print(sys.float_info)
    print(sys.int_info)     #sys.int_info(bits_per_digit=15, sizeof_digit=2)
    print(sys.maxsize)      #2147483647 (op win32)

def test_platform():
    print(platform.architecture())      # ('32bit', 'WindowsPE')
    print(platform.system())            # Windows
    print(platform.version())           # 6.1.7601
    print(platform.platform())          # Windows-7-6.1.7601-SP1
    print(platform.win32_ver())         # ('7', '6.1.7601', 'SP1', 'Multiprocessor Free')
    print(platform.node())              # NETBOOK
    print(platform.machine())           # x86
    print(platform.processor())         # x86 Family 20 Model 2 Stepping 0, AuthenticAMD

    print()
    print(platform.python_version())    # 3.4.4 [nog andere python_.. fn's]
    #print(platform.java_ver())          #lege tupels
    #print(platform.libc_ver())          #lege tupel

def test_locale():
    print(sys.getfilesystemencoding())  #mbcs
    print(sys.getdefaultencoding())     #utf-8
    print(locale.getdefaultlocale())    #('nl_NL', 'cp1252')
    print(locale.getpreferredencoding(do_setlocale=False))  #cp1252
    print(locale.getlocale())          #('Dutch_Netherlands', '1252')
    print(locale.getlocale(locale.LC_CTYPE))    #idem
    print(locale.getlocale(locale.LC_NUMERIC))  #(Noene, None)
    print()
    print(locale.localeconv())

##    print(os.getcwd())
##    print(sys.path)


#--- script ---

test_Python_info()
#test_sys_platform()
#test_platform()
#test_locale()

