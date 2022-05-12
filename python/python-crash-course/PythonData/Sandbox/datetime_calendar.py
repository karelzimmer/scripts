# testen met ingebouwde datum/tijd functies

"""
time:
Clocks/timers vroeger gebaseerd op win GetTickCount() ->wrap na 49.7 dgn;
monotonic() bewaart interne wrap-teller, zodat ie niet terugkeert naar 0.
Tegenwoordig allemaal monotonic behalve time(), want systeemtijd instelbaar,
dus ook op oudere datum.

get_clock_info('<kloknaam>')
clock      ->deprecated, gaat weg in 3.8
namespace(adjustable=False, implementation='QueryPerformanceCounter()', monotonic=True, resolution=1.0261556821831668e-06)

perf_counter
namespace(adjustable=False, implementation='QueryPerformanceCounter()', monotonic=True, resolution=1.0261556821831668e-06)
monotonic
namespace(adjustable=False, implementation='GetTickCount64()', monotonic=True, resolution=0.015600099999999999)
process_time
namespace(adjustable=False, implementation='GetProcessTimes()', monotonic=True, resolution=1e-07)
time
namespace(adjustable=True, implementation='GetSystemTimeAsFileTime()', monotonic=False, resolution=0.015600099999999999)


class struct_time(builtins.tuple) ->namedtuple; kan opgeven als 9-tuple
    tm_year      jaar in 4 cijfers
    tm_mon       [1, 12]
    tm_mday      [1, 31], dag vd maand
    tm_hour      [0, 23]
    tm_min       [0, 59]
    tm_sec       [0, 61], let op: kan dus 61 sec geven
    tm_wday      [0, 6], dag vd week, 0 = Monday
    tm_yday      [1, 366], dag vh jaar
    tm_isdst     daylight saving time    1, 0, -1 = onbekend

time() ->secs
ctime([secs]) ->str
asctime([t]) ->str, dflt localtime(); geen error bij foute t, bv 30 feb
localtime([secs]) ->t, default time()
gmtime([secs]) ->t
mktime(t) ->secs, hele secs want t bevat geen msecs; kan 9-tupel opgeven

strftime(outputfmt, t) ->str
strptime(str, inputfmt) ->t

%Y  jaar 4 cijfers
%y  jaar 2 cijfers
%m  maand [01,12]
%d  dag vd maand [01,31]
$w  dag vd week [0,6], 0 = zo
%j  dag vh jaar [001,366]
%U  weeknr jaar [00,53], zo=0, alle dgn voor zo in nwe jr ->week 00, bv: 18
%W  weeknr jaar [00,53], ma=0, alle dgn voor ma ->week 00, bv: 19

%H  uur 24 uur [00,23]
%I  uur 12 uur [01,12]
%p  locale equivalent v AM/PM
%M  minuut [00,59]
%S  seconde [00,61]
%Z  tijdzone string: 'W. Europe Daylight Time'
%z  tijdzone string, is bug, vlg doc moet dit [-23:59, +23:59] geven
    bij dt.strftime('%z') ->'+0200'

vlg Locale betekent: tijd v je regio, NIET opmaak v je win region settings
%a  locale korte weekdag: 'Mon'
%A  locale lange weekdag
%b  locale korte maand
%B  locale lange maand
%c  locale datum + tijd:  '05/07/18 15:28:24', us-fmt mm/dd/yy
%x  locale datum: '05/07/18'
%X  locale tijd: '15:28:24'

tzinfo is abstract base class
timezone is afgeleide impl.

calendar.Calendar en andere classes dienen om kalenders af te drukken,
dus week- en maandoverzichten. Kan ook naar html-table

"""

import time
import datetime as dti
import locale

def time_timers():
    #time.sleep(3)
    #print(time.clock())             #deprecated, gaat weg in 3.8
    print(time.perf_counter())      #float, secs sinds eerste aanroep
    print(time.monotonic())         #float, ander startpunt

    print(time.process_time())      #cpu+user time dit process, excl idle ->laag
    print(time.time())              #float, secs sinds 1 jan 1970

    print(time.mktime(time.localtime()))    #arg: t ->secs, hele secs want t geen ms

    print('\ntime.get_clock_info(..)')
    for s in ['perf_counter','monotonic','process_time','time']:
        print(s)
        print(time.get_clock_info(s))       #'clock'


def test_locale():
    # als je zelf geen locale zet, krijg je als dflt de portable 'c' locale

    # vlg zet Dutch Netherlands + ->str 'Dutch_Netherlands.1252'
    #locale.setlocale(locale.LC_ALL,'')     #->Dutch_Netherlands.1252
    #locale.setlocale(locale.LC_TIME,'')     #alleen datum naar locale
    #locale.setlocale(locale.LC_ALL, 'Dutch_Netherlands.1252')   #goed
    #locale.setlocale(locale.LC_ALL,'dutch')     #('Dutch_Netherlands', '1252')
    #locale.setlocale(locale.LC_ALL,'nl')        #('nl_NL', 'ISO8859-1')

    #locale.setlocale(locale.LC_ALL, 'German_Germany.1252') #('de_DE', 'cp1252')
    locale.setlocale(locale.LC_ALL, 'deu')          #('de_DE', 'cp1252')
    #locale.setlocale(locale.LC_ALL, 'de')           #('de_DE', 'ISO8859-1')
    #locale.setlocale(locale.LC_ALL, ['de','1252'])      #error
    #locale.setlocale(locale.LC_ALL, ['de','de'])        #error
    #locale.setlocale(locale.LC_ALL, 'deutsch')          #error

    #d = locale.localeconv()            #->dict, euro symbool, dec komma, etc
    print("setlocale:", locale.setlocale(locale.LC_ALL))   #uitlezen
    #->dflt: LC_COLLATE=C;LC_CTYPE=Dutch_Netherlands.1252;LC_MONETARY=C;LC_NUMERIC=C;LC_TIME=C
    #->Ned: Dutch_Netherlands.1252

    print("getlocale:", locale.getlocale())      #('Dutch_Netherlands', '1252')
    print()
    print("dflt loc:", locale.getdefaultlocale())          #->('nl_NL', 'cp1252')
    print("pref enc:", locale.getpreferredencoding())      #cp1252
    print()
    
    print(time.asctime())               #blijft US format
    print(time.strftime('%A %d %B %Y', time.localtime()))   #locale afh
    print(time.strftime('%x %X', time.localtime()))
    print(locale.str(3.45))                   #bij Ned: 3,45
    #a = locale.atof("3,45")                  #bij Ned: 3.45
    #a = locale.atoi("3.410.568")             #bij Ned: 3410568

def time_string_struct():
    # vlg ->str; zelfde output
    print(time.asctime())                #[t] ->str; bij leeg localtime()
    print(time.ctime())                  #[secs] ->str; is: asctime(localtime())

    # vlg ->struct_time t
    print(time.localtime())              #[secs] ->t; bij leeg time()
    print(time.gmtime())                 #[secs] ->t; bij leeg time() met tijdverschil

    print("\nVandaag:")
    t = time.localtime()        #time_struct is een namedtuple
    print("dagen: mnd=%d, wk=%d jr=%d" % (t.tm_mday,t.tm_wday,t.tm_yday))
    print("datum: %d-%d-%d" % (t.tm_mday,t.tm_mon,t.tm_year))
    print("datum: %d-%d-%d" % (t[2],t[1],t[0]))
    print("datum: {0.tm_mday}-{0.tm_mon}-{0.tm_year}".format(t))

def time_format_input():
    #locale.setlocale(locale.LC_ALL,'')      #zet Dutch_Netherlands.1252
    locale.setlocale(locale.LC_ALL, 'deu')

    #print("Local time:")
    #fmt = '%d-%m-%Y %H:%M:%S'
    #fmt = '%I:%M:%S %p'
    #fmt = '%d-%m-%Y %I:%M:%S %p %z'     #win: %z werkt niet
    #fmt = '%x %X'           #12/31/20 13:28:59
    #fmt = '%c'              #Thu Dec 31 13:40:02 2020
    #fmt = '%A %x %X'        #%a->Thu, %A->Thursday
    #fmt = '%A, %B %d, %Y'    #Thursday, December 31, 2020
    #fmt = '%A %d %B %Y'     #bij locale Ned: donderdag 31 december 2020
    fmt = '%a %d %b %Y'     #bij locale Ned: do 31 dec 2020
    #print(time.strftime(fmt, time.localtime()))     #outputfmt,t -> str

    #return
    s = '23-03-2016'
    print("\nOpgegeven datum:", s)
    t = time.strptime(s, '%d-%m-%Y')    #str,inputfmt -> t
    #t = time.struct_time(tm_year=2016,tm_mon=3,tm_mday=23)  #error
    #print(time.asctime(t))              #t ->str
    print(time.strftime(fmt, t))

    return
    #struct_time tuple eist 9 items
    #t = (2016,3,23, 0,0,0,0,0,-1)       #geeft eist 9 items
    #t = (2016,3,23, 0,0,0,3,0,-1)       #wkdag=3 ->woensdag (correct)
    #t = (2019,3,28, 0,0,0,0,0,-1)       #is een donderdag ->foute wkdag
    #t = (2019,2,29, 0,0,0,0,0,-1)       #asctime(t) vindt dit goed!
    t = (2019,2,31, 0,0,0,0,0,-1)       #asctime(t) vindt dit goed!
    print(time.asctime(t))              #t ->str; foute dagnm
    # asctime(t) controleert t niet;
    # mktime(t) wel -> zet 31-2-2019 om in 3-3-2019

    secs = time.mktime(t)               #t ->secs; negeert wkdag ->goed
    print(time.ctime(secs))             #secs ->str; wel goede dag


#--- datetime(dti) ---

# date, time, datetime, timezone allemaal immutable

def dti_date():
    global d
    
    #d = dti.date(2012, 9, 4)        #eist yy,mm,dd; geen dflt args
    #d = dti.date.fromtimestamp(time.time())     #secs, float
    #d = dti.date.fromordinal(736821)   #soms crash bij fmt %x, error bij %y
    # (2-cijf jr ->prb als jaar buiten window 19xx-20yy valt)
    #d = dti.date.fromisoformat("2021-04-03")    #3 april 2021; Python 3.7
    d = dti.date.today()
    print(type(d))

    print(d)                        #'2012-09-04', doet .isoformat()
    print(d.isoformat())            #idem
    print(d.ctime())                #'Tue Sep  4 00:00:00 2012'
    #print(d.strftime('%x'))
    print(d.strftime('%d-%m-%Y'))
    print(d.month)                  #.day, .month, .year ->int
    print(d.weekday())              #maandag = 0
    print(d.isoweekday())           #zondag = 0
    print(d.isocalendar())          #(2018, 19, 1) bij ma 7 sep 2018
    
    print(d.toordinal())            #737885
    print(d.replace(month=5, day=23))
    
def dti_time():
    global t

    #t = dti.time()                  #mag hh,MM,ss weglaten, usecs, tzinfo
    # ->0,0,0 etc
    #t = dti.time(15,32,16)
    #t = dti.time.fromisoformat("15:33:17")
    t = dti.time.fromisoformat("15:33:17.123456")  #usecs
    #t = dti.time.fromisoformat("15:33:17.123")      #ms, wordt 123000 usecs

    print(t)
    print(t.isoformat())
    print(t.isoformat('seconds'))       #toon t/m secs
    print(t.replace(minute=49))

def dti_datetime():
    #dt = dti.datetime(2012, 9, 4, 16, 34, 20)    #mag hh,MM,ss weglaten, usecs, tzinfo
    dt = dti.datetime.strptime("04-09-2012 16:34:21",'%d-%m-%Y %H:%M:%S')
    #dt = dti.datetime.today()       #date+time, geen tzinfo
    #dt = dti.datetime.utcnow()       #idem, geen tzinfo
    #dt = dti.datetime.now()          #dflt tz=None
    # .fromtimestamp(secs, [tzinfo])
    print(type(dt))

    print(dt)                        #'2018-05-07 19:17:05.896894'
    print(dt.isoformat())            #'2018-05-07T19:26:03.567432', evt sep=' ' ipv 'T'
    print(dt.ctime())                #'Mon May  7 19:17:05 2018'
    print(dt.dst())                  #None
    print(dt.tzname())
    print(dt.utcoffset())

    t = dt.time()                    #ook .date()
    print(type(t))
    print(t)                        #'19:17:05.896894'

def dti_timedelta():
    global d1,d2,td
    
    d1 = dti.date.today()
    d2 = dti.date(2019, 6, 7)
    td = d1 - d2            #timedelta
    #td = d2 - d1
    print(td)               #.days, .seconds, .microseconds, .total_seconds()
    print(d1 + dti.timedelta(weeks=1))      #geen month=, year=
    # vor mag ook week=0.5, week=-3
    # input: weeks, days, hours, minutes, seconds, milliseconds, microseconds
    print(d1 - dti.timedelta(days=1, hours=12))

def dti_timezone():
    tzu = dti.timezone.utc          #UTC
    print(tzu)                      #UTC+00:00
    dtu = dti.datetime.now(tzu)     #utc dt
    dtl = dtu.astimezone()          #local dt met offset tov utc; eist dt met tzinfo
    dt = dti.datetime.now()         #dt zonder tzinfo
    print(dtu)                      #'2018-05-07 21:27:10.796041+00:00'
    print(dtl)                      #'2018-05-07 23:27:10.796041+02:00'
    print(dt)                       #'2018-05-07 23:27:10.796041'
    
    print(dtu.tzname())             #'UTC+00:00'
    print(dtl.tzname())             #'W. Europe Daylight Time'
    print(dtl.strftime('%Z'))       #idem
    print(dtl.strftime('%z'))       #'+0200'
    print(type(dtl.tzinfo))         #<class 'datetime.timezone'>
    print(dtl.utcoffset())          #timedelta, '2:00:00'
    print(dtl.dst())                #None
    print(dt.utcoffset())           #None, want geen tzinfo
    
    

#--- script ---


#time_timers()

#test_locale()
#time_string_struct()
#time_format_input()

#dti_date()
dti_time()
#dti_datetime()
#dti_timedelta()
#dti_timezone()

