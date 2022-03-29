#tkinter en multithreading

"""

"""

import threading as th
import time
import queue                        #sync queue voor multithreading
from tkinter import *
from tkinter import messagebox      #moet apart in 3.6


class Counter_after:
    """teller met .after()-loop"""

    def __init__(self):
        self.count = 0
        self.fContinue = False
        self.isStarted = False
        self.sleeptime = 1500        #msecs
        self.idupd = None

        self.root = Tk()
        self.root.title("Counter")
        self.root.geometry('140x80+340+150')
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)  #kan annuleren
        # root.bind("<Destroy>", onClosed) ->kan niet meer annuleren

        self.lbl = Label(self.root, text="<leeg>", font=('comic sans ms', 14))
        self.lbl.pack(pady=8)

        fra1 = Frame(self.root)
        fra1.pack(padx=2,pady=2)
        fnt = ('TkDefaultFont', 9)      #dflt 8, priegelig
        Button(fra1, text=' Start ', font=fnt, command=self.doStart).pack(side=LEFT,padx=4)
        Button(fra1, text=' Stop  ', font=fnt, command=self.doStop).pack(side=RIGHT,padx=4)

        #print("__init__(): [%d]" % th.get_ident())     #main/gui thread

    def onClosing(self):
        if messagebox.askyesno(message="Afsluiten?"):
            self.doStop()
            self.root.destroy()

    def doStart(self):
        # zonder vlg gaat ie bij iedere klik een extra lus starten
        if not self.isStarted:
            self.isStarted = True
            self.fContinue = True
            #self.root.after(100, self.update_count)
            self.idupd = self.root.after(100, self.update_count)
            #print("doStart(): idupd =", self.idupd)    # after#0 enz
            #time.sleep(4)      #blokkeer gui 4 secs ->after() draait niet

    def doStop(self):
        if self.isStarted:
            self.fContinue = False
            self.isStarted = False
            if self.idupd:
                #print("doStop(): idupd =", self.idupd)
                self.root.after_cancel(self.idupd)
                self.idupd = None

    def update_count(self):
        #print("update_count(): [%d]" % th.get_ident())     #main/gui thread
        #print("update_count(): idupd =", self.idupd)
        self.count += 1
        self.lbl['text'] = str(self.count)
        if self.fContinue:
            self.idupd = self.root.after(self.sleeptime, self.update_count)
        

class Counter_thread:
    """teller met thread, zonder event_generate"""

    def __init__(self):
        self.count = 0
        self.fContinue = False
        self.sleeptime = 1.5        #secs
        self.t = None               #thread

        self.root = Tk()
        self.root.title("Counter")
        self.root.geometry('140x80+340+150')
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.lbl = Label(self.root, text="<leeg>", font=('comic sans ms', 14))
        self.lbl.pack(pady=8)

        fra1 = Frame(self.root)
        fra1.pack(padx=2,pady=2)
        fnt = ('TkDefaultFont', 9)
        Button(fra1, text=' Start ', font=fnt, command=self.doStart).pack(side=LEFT,padx=4)
        Button(fra1, text=' Stop  ', font=fnt, command=self.doStop).pack(side=RIGHT,padx=4)

        print("__init__(): [%d]" % th.get_ident())      #main/gui thread

    def onClosing(self):
        if messagebox.askyesno(message="Afsluiten?"):
            # vlg moet synchroon, want worker threads MOETEN klaar zijn
            # voor hfdvenster + prog afsluiten
            self.realStop()     #moet hier synchrone call
            self.root.destroy()

    def doStart(self):
        if not self.t:
            self.fContinue = True
            self.t = th.Thread(target=self.update_count)
            self.t.start()

    def doStop(self):
        # de stop-knop blijft even ingedrukt hangen vanwege t.join()
        # met: self.root.after(10, self.realStop) doen->async ->knop ok
        if self.fContinue:
            self.fContinue = False          #niet 2 keer klikken
            self.root.after(10, self.realStop)

    def realStop(self):
        # als t een daemon-thread is, breekt ie autom af; niet netjes,
        # maar dan vlg sync niet nodig
        if self.t:
            self.fContinue = False
            self.t.join()           #blokkeert gui
            self.t = None
            print("doStop(): na t.join()")
        print("doStop(): einde")

    def update_count(self):         #draait op 2e thread
        while self.fContinue:
            print("update_count(): [%d]" % th.get_ident())     #2e thread
            self.count += 1
            # vlg eig slecht, want worker thread update user interface
            self.lbl['text'] = str(self.count)
            time.sleep(self.sleeptime)      #secs
        

class Counter_thread_invoke:
    """teller met thread, met event_generate"""

    def __init__(self):
        self.count = 0
        self.fContinue = False
        self.sleeptime = 1.5        #secs
        self.t = None               #thread

        self.root = Tk()
        self.root.title("Counter")
        self.root.geometry('140x80+340+150')
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.root.bind("<<Tralala>>", self.onLabelUpdate)

        self.lbl = Label(self.root, text="<leeg>", font=('comic sans ms', 14))
        self.lbl.pack(pady=8)

        fra1 = Frame(self.root)
        fra1.pack(padx=2,pady=2)
        fnt = ('TkDefaultFont', 9)
        Button(fra1, text=' Start ', font=fnt, command=self.doStart).pack(side=LEFT,padx=4)
        Button(fra1, text=' Stop  ', font=fnt, command=self.doStop).pack(side=RIGHT,padx=4)

        print("__init__(): [%d]" % th.get_ident())      #main/gui thread

    def onClosing(self):
        if messagebox.askyesno(message="Afsluiten?"):
            self.realStop()
            self.root.destroy()

    def onLabelUpdate(self, ev):
        print("onLabelUpdate(): [%d]" % th.get_ident())     #main/gui thread
        self.lbl['text'] = str(self.count)
        

    def doStart(self):
        if not self.t:
            self.fContinue = True
            self.t = th.Thread(target=self.update_count)
            self.t.start()

    def doStop(self):
        # de stop-knop blijft even ingedrukt hangen vanwege t.join()
        if self.fContinue:
            self.fContinue = False          #niet 2 keer klikken
            self.root.after(10, self.realStop)

    def realStop(self):
        if self.t:
            self.fContinue = False
            self.t.join()
            self.t = None
            print("doStop(): na t.join()")
        print("doStop(): einde")

    def update_count(self):         #draait op 2e thread
        while self.fContinue:
            print("update_count(): [%d]" % th.get_ident())     #2e thread
            self.count += 1
            self.root.event_generate("<<Tralala>>")     #, when='tail'
            # vor when='now'|'tail'|'head'|'mark', of weglaten (='now')
            # vlg docs doet 'now' direct call op 2e thread,
            # en when='tail'|'head'|'mark' een post ->naar gui-thread
            # maar bij mij in Python 3.4 altijd post ->naar gui-thread
            time.sleep(self.sleeptime)      #secs

class Counter_queue:
    """teller met .after()-loop"""

    def __init__(self):
        self.fContinue = False
        self.isStarted_aft = False
        # consumer (gui, after) kan meer/minder vaak kijken dan producer (t)
        self.sleeptime_aft = 500       #msecs, consumer
        self.sleeptime_thr = 1.5        #secs, producer
        self.t = None                   #thread

        self.q = queue.Queue(1)         #fifo; max 1 item; leeg=unlimited
        #self.q = queue.LifoQueue(1)
        #self.q = queue.PriorityQueue(1)    #laagste eerst, vaak tupel: (nr,item)

        self.root = Tk()
        self.root.title("Counter")
        self.root.geometry('140x80+340+150')
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)  #kan annuleren
        # root.bind("<Destroy>", onClosed) ->kan niet meer annuleren

        self.lbl = Label(self.root, text="<leeg>", font=('comic sans ms', 14))
        self.lbl.pack(pady=8)

        fra1 = Frame(self.root)
        fra1.pack(padx=2,pady=2)
        fnt = ('TkDefaultFont', 9)
        Button(fra1, text=' Start ', font=fnt, command=self.doStart).pack(side=LEFT,padx=4)
        Button(fra1, text=' Stop  ', font=fnt, command=self.doStop).pack(side=RIGHT,padx=4)

        print("__init__(): [%d]" % th.get_ident())     #main/gui thread

    def onClosing(self):
        if messagebox.askyesno(message="Afsluiten?"):
            self.realStop()
            self.root.destroy()

    def doStart(self):
        # zonder vlg gaat ie bij iedere klik een extra lus starten
        if not self.isStarted_aft:
            self.isStarted_aft = True
            self.fContinue = True
            self.t = th.Thread(target=self.update_count_thr)    #producer
            self.t.start()
            self.root.after(100, self.update_count_aft)         #consumer

    def doStop(self):
        # de stop-knop blijft even ingedrukt hangen vanwege t.join()
        if self.fContinue:
            self.fContinue = False          #niet 2 keer klikken
            self.root.after(10, self.realStop)

    def realStop(self):
        # deze fn MOET synchroon, want kan worden aangeroepen in window closing
        # ->alle worker threads MOETEN klaar zijn voor deze terugkeert!
        if not self.isStarted_aft:
            return

        self.fContinue = False
        self.isStarted_aft = False

        if self.t:
            # thread t zit misschien in sleep- of wachtstand
            # het is dus mogelijk dat q op dit moment leeg is (t slaapt),
            # maar straks nog gevuld gaat worden met q.put(count)
            # ->moet eerst q leegmaken, zodat q.put(count) niet blokkeert
            # ->kan daarna wachten met t.join()
            # dit werkt alleen omdat mijn q maar 1 item kan bevatten en
            # t wacht totdat die plek vrij is
            # bij t.join() zonder eerst lege q ->deadlock:
            # t sleep, gui wacht in join, t wordt wakker, wil q.put(..) doen,
            # maar blokkeert omdat q vol is ->beide wachten op elkaar

            self.update_count_aft()     #mk q evt leeg ->ruimte voor 1 put
            # vlg blokkeert gui:
            self.t.join()               #wacht op evt laatste put
            self.t = None

            # bij grotere q en/of meerdere producers moet je in een lus
            # steeds de q leegmaken, net zo lang tot alle threads klaar zijn
            
##            while self.t.is_alive():      # or self.t2.is_alive() or ... enz
##                try:
##                    self.q.get_nowait()
##                    time.sleep(0.2)
##                except queue.Empty:
##                    pass
##            self.t = None

    def update_count_aft(self):         #consumer
        print("update_count_aft(): [%d]" % th.get_ident())     #main/gui thread
        # vlg niet q.get(), want dan blokkeert gui thread!
        try:
            cnt = self.q.get_nowait()        #=q.get(False)
            self.lbl['text'] = str(cnt)
        except queue.Empty:
            pass
        if self.fContinue:
            self.root.after(self.sleeptime_aft, self.update_count_aft)

    def update_count_thr(self):         #producer
        count = 0
        while self.fContinue:
            print("update_count_thr(): [%d]" % th.get_ident())     #2e thread
            count += 1
            time.sleep(self.sleeptime_thr)          #zg lange taak
            self.q.put(count)                      #blocking


#--- script ---

print('main, start; threads =', th.active_count())      # 2

#c = Counter_after()
#c = Counter_thread()
#c = Counter_thread_invoke()
c = Counter_queue()

c.root.mainloop()           #blocking

print('main, klaar; threads =', th.active_count())

