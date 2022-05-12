#eerste programma met tkinter
#als ext = .pyw, dan bij dblklik in explorer pythonw.exe ->geen dosbox

"""
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index
-> Tkinter 8.5 reference
http://www.tcl.tk/software/tcltk/8.6.tml
http://www.tkdocs.com/tutorial/index.html
https://python-forum.io/

bij wheels installeren eerst pip upgraden, anders error:
 "filename.whl is not supported wheel on this platform"
python -m pip install --upgrade pip

pillow/PIL dient om .jpg/.png enz in te kunnen lezen
(tk 8.6 kent zelf al .png, maar nog geen .jpg)
Python 3.7: pip install Pillow
heeft .pyd binaries, dwz Windows dlls met extra Python interface
(niet op mac en linux)
bij 3.4 error: moet C-sources compileren en kan compiler niet vinden

Python 3.7 dus geen wheel meer nodig!
installeren via een wheel met al gecompileerde binaries voor windows:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
en een vd volgende (cp34=Python 3.4):
pip install Pillow-4.1.1-cp34-cp34m-win32.whl
pip install Pillow-4.2.1-cp35-cp35m-win32.whl
pip install Pillow-4.2.1-cp35-cp35m-win_amd64.whl

Wheel hangt samen met 32/64 bit Python-versie, niet van win-versie.
Dus bij 64bit win + 32bit Python ->32bit wheel

Events draaien op de main thread, dus niet op awt-thread zoals in Java

IDLE en tkinter:
IDLE doet 20 keer/sec een root.update()
root.mainloop() std blocking ->je keert terug in Shell na einde gui prog.
Je mag root.mainloop() weglaten binnen IDLE ->meteen weer Shell actief
->kan interactief met gui prog werken.

import platform
platform.architecture()   ->('32bit', 'WindowsPE')
#(32-bit Python op 64-bit Win 7)

Toplevel widgets:
Tk, Toplevel

Other widgets:
Frame, PanedWindow, LabelFrame,
Menu, Menubutton, OptionMenu (soort cbo),
Label, Message, Entry, Text,
Button, Radiobutton, Checkbutton, Spinbox
Scale, Scrollbar, Listbox, Canvas

geen mdi, datagrid, toolbar, statusbar

tkinter.ttk:
overrides ctrls; attribs als kleur, rand niet per ctrl instellen, maar als theme;
daarnaast de volgende extra ctrls (widgets):
Combobox
LabeledScale
Notebook             tab-ctrl met windows
Progressbar
Separator
Sizegrip
Style
Treeview             doet ook listview ->r/o grid, kan colwidth instellen

drie geometry mgrs: pack, grid (rijen & kols), place (abs pos)
hij kent allerlei "constanten", bv LEFT='left'

soms kan je width/height opgeven als str met c (cm), m (mm), i (inch), p (punt)

sommige opties gaan niet via ctor, maar wel via widget.config(..)
bv bij OptionMenu werkt kw-dict in __init__() niet, .config() wel
alle resource-keys zien: widget.keys()

font style = normal, bold, roman, italic, underline, overstrike
relief = FLAT, SUNKEN, RAISED, GROOVE, SOLID, RIDGE

widget.bind() ->Event-obj args:
['char', 'delta', 'height', 'keycode', 'keysym', 'keysym_num', 'num',
'send_event', 'serial', 'state', 'time', 'type', 'widget', 'width',
'x', 'x_root', 'y', 'y_root']

In Python 3.6 MOET je de vlg apart importeren:
(gaat NIET via: from tkinter import *)
    colorchooser
    commondialog
    dialog
    dnd
    filedialog
    font
    messagebox
    scrolledtext
    simpledialog

messagebox.
askokcancel(title=None,message=None,**options)
askquestion       ->'yes'|'no'
askretrycancel
askyesno          ->1|0
askyesnocancel
showerror
showinfo
showwarning

messagebox->options:
default=OK,CANCEL,ABORT,RETRY,IGNORE,YES,NO  [=default button]
icon=INFO,QUESTION,WARNING,ERROR
type=OK,OKCANCEL,RETRYCANCEL,ABORTRETRYIGNORE,YESNO,YESNOCANCEL
title

simpledialog.
askfloat(title,prompt,**kw)    let op: geen defaults ->moet 2 args invullen
askinteger
askstring

filedialog.
askdirectory(**options)
askopenfilename(**options)
askopenfilenames(**options)
asksaveasfilename(**options)
askopenfile(mode='r',**options)   ->fh
askopenfiles(mode='r',**options)   ->[fh1, fh2, ...]
asksaveasfile(mode='w',**options)

filedialog->options:
filetypes=[('Text files','*.txt'), ('All files','*.*'), ..]
initialdir, initialfile, defaultextension, title
parent ->embedded dlg

colorchooser.
askcolor(color=None,**options)   ->tupel: ((160, 160, 160), '#a0a0a0')
->je MOET altijd color str gebr, dus bv "red" of "#ff0000"
  tkinter werkt nooit met kleurtupels (r,g,b)

"""

#import threading
import time
from enum import Enum
import winsound
from tkinter import *
from tkinter import messagebox, simpledialog, filedialog, font   #moet in 3.6
from PIL.ImageTk import PhotoImage, Image    #overrules tkinter classes

#print(TkVersion)            #8.6

def tstLabel1():
    # Label: width, height in kars; kan meerregelig met '\n'
    # default even breed als tekst
    # None ->master (=parentwindow) wordt Tk-topwindow met naam '.'
    # hij kent prop lbl.master, maar niet lbl['master']; geen prop parent
    lbl = Label(None, text='Hehe, ik zit.')   #None = hij mkt Tk-topwindow

    # zonder .pack() krijg je window zonder je labeltekst
    #lbl.pack()
    lbl.pack(side='left', pady=20)  #pady=boven en onder minstens 20px
    #bij 'top' centreert ie li-re, boven 20px
    #bij 'left' centreert ie bo-on, met bo minstens 20px
    lbl['fg'] = '#FF0000'       #rrggbb, of 'kleurnaam'
    # lbl kan niet transparant zijn

    print(vars(lbl))
    print(lbl['bg'])            # SystemButtonFace
    print(lbl['justify'])       # center; bij Message: left

    #print(lbl['master'])       #error: unknown option -master
    print(repr(lbl.master))     #goed: <tkinter.Tk object at 0x0203CC70>
    # vlg ook goed
    parentname = lbl.winfo_parent()
    print(parentname)           # '.'
    parent = lbl.nametowidget(parentname)
    print(repr(parent))         #<tkinter.Tk object at 0x0203CC70>
    
    lbl.mainloop()              #blocking; doet lbl.master.mainloop()
    # als je vor weglaat, draait je code op de mainloop van IDLE!
    # ->fout buiten IDLE


def tstLabel2():
##    options = {'text':'Hello GUI world!', 'fg':'#0033DD'}
##    layout = {'side':'top'}
##    Label(None, **options).pack(**layout)   #dicts uitpakken

    # vlg hele oude notatie; een widget heeft dict-notatie
    # Pack: MOET met hfdlett en zonder quotes
    #Label(None, {'text':'Hello GUI world!', Pack: {'side':'top'}}).mainloop()

    Label(text='Hehe, ik drink.', fg='#0033DD').pack(expand=YES, fill=BOTH)
    #.pack() geeft None terug ->kan niet doen: lbl.pack().mainloop()

    mainloop()      #doet Tk-instance.mainloop()


def tstMessage1():
    # Message is meerregelig Label met autowrap; wel width, geen height
    # width in px, niet aant chars, zoals bij Label
    # aspect=150 -> 1 1/2 breed als hoog;
    # je moet aspect OF width instellen, width overrule't aspect
    txt = "Ik heb me altijd al afgevraagd of ik ooit nog weer de \
standaardintegralen zou kunnen herleren. En die eigenvalues en \
eigenvectoren, die hakken er ook in."
    msg = Message(None, text=txt)       #, aspect=250, width=80
    msg.pack(padx=5, pady=5)
    print(msg['justify'], msg['aspect'], msg['width'])     #left 150 0

    msg.mainloop()


def tstEntry1():
    # Entry is eenregelig invoerveld; wel width (kars), geen height
    # const voor .insert()/.index()/.delete(): END, INSERT (cursorpos), ANCHOR (kar 0 v selectie)
#    txt = "Ik heb me altijd al afgevraagd of ik ooit nog weer de \
#standaardintegralen zou kunnen herleren. En die eigenvalues en \
#eigenvectoren, die hakken er ook in."
    txt = 'Hoi!\tHai!'      #\t kan; \r|\n niet; kan geen tab zetten met Ctrl+I

    ent = Entry(None, width=40)       #, width=40 (dflt 20 kars), geen padx/pady
    ent.pack(padx=5, pady=5)          #padx=5, pady=5
    print(ent['justify'], ent['width'], ent['state'])       #left 40 normal
    ent.insert(END, txt)
    ent.insert(6, "aaa")            #na de H, mag ook '6', kent geen -1 enz
    ent.delete(1, 2)
    #print(type(ent.index(END)))
    ent.delete(ent.index(END)-1)    #wis vanaf 1 na laatste
    print(ent.get())
    #ent['state'] = 'readonly'
    #print(ent['state'])
    
    ent.mainloop()



def tstButton1():
    #import functools as fun

    def onClick():
        print("onClick() begin")
        # vlg modal dlg houdt knop NIET ingedrukt
        messagebox.showinfo(title='Info', message='Het is niet okee')
        #time.sleep(3)          #houdt knop 3 sec ingedrukt + block
        #cmd.after(3000)        #idem, ook block
        print("onClick() einde")
        #print("thread:", th.get_ident())
        # events draaien op de main thread

    def onClick2(msg):
        # msg wordt gevuld via hetzij fun.partial, hetzij een lambda
        messagebox.showinfo(title='Info', message=msg)

    # let op: in IDLE blijft topwindow staan na sys.exit of root.quit
    # in dosbox niet
    # padx/y in ctor ->ruimte binnen knop wordt groter ->knop groter)
    # padx/y in .pack() ->ruimte rond knop wordt groter
    # ctor width/height in kars, .pack() width/height in px
    cmd = Button(None, text=' OK ', command=onClick)
    #cmd = Button(None, text='OK', padx=16, command=onClick)
    #cmd = Button(None, text=' OK ', font=(None,12), command=onClick)

    #cmd = Button(None, text=' OK ', command=fun.partial(onClick2,"Hoe gaat ie?"))
    #cmd = Button(None, text=' OK ', command=lambda : onClick2("Gaat ie goed?"))

    #command=quit ->hij komt met dlg: prog draait nog; kill it?
    # (=quit-fn vd Python shell, is Quitter class; zie help(quit))
    #command=root.destroy ->zou goed gaan als we root hadden...
    #command=destroy ->NameError: 'destroy' not defined
    
    #cmd = Button(None, text=' OK ')
    #cmd.config(command=cmd.destroy)     #haalt knop weg!
    #cmd.config(command=cmd.quit)        #in IDLE blijft venster staan
    #cmd.config(command=cmd.master.quit) #idem
    #cmd.config(command=cmd.master.destroy)  #in IDLE hfdvenster weg

    cmd.pack()      #side=TOP, anchor=CENTER; venster vert even groot als knop
    #cmd.pack(ipadx=10, ipady=6)     #ruimte in knop; vgl padx/y in ctor
    #cmd.pack(padx=10, pady=6)
    #cmd.pack(anchor=CENTER)    #idem
    #cmd.pack(anchor=W)      #knop links
    #cmd.pack(anchor=E)      #knop rechts
    #cmd.pack(anchor=EW)     #error; NE,SE,NW,SW mogen wel
    #cmd.pack(side=LEFT)     #side=LEFT,RIGHT,TOP,BOTTOM; dflt TOP
    #cmd.pack(expand=YES, fill=BOTH)    #fill=X,Y,BOTH
    #cmd.pack(expand=YES, fill=BOTH, padx=10, pady=10)   #ruimte rond knop
    # vor fill=X ->zonder expand: knop bovenaan, volle breedte, groeit hor
    # met expand ->vert gecentreerd, groeit NIET vert
    # vor fill=Y ->zonder expand: knop bovenaan, std br, groeit NIET vert
    # met expand ->std br, vert groei
    # vor fill=BOTH ->zonder expand: knop bovenaan, volle breedte, groeit hor
    # met expand ->hor+vert groei

    print(cmd['text'])        #'OK'
    print(cmd['padx'], cmd['pady'])         #dflt 1 1
    print(cmd['font'])          #->str: TkDefaultFont
    print(cmd.info())      #doet .pack_info() ->dict met pack(..) args
    # default:
    # {'ipadx': 0, 'fill': 'none', 'side': 'top', 'anchor': 'center',
    # 'ipady': 0, 'padx': 0, 'expand': 0, 'pady': 0,
    # 'in': <tkinter.Frame object at 0x0200F4F0>}
    print(cmd.info()['padx'])       #0
    print(cmd.info()['side'])       #top

    #print(cmd.config())             #enorme dict met alle instellingen
    #print(cmd.keys())               #list met alle keys, bv: fg,bg,font,relief
    # vlg 5-tuple: optname, optname db lookup, optclass, dflt val, curr val
    #print(cmd.config('relief'))    #('relief', 'relief', 'Relief', <index object: 'raised'>, 'raised')
    #print(cmd.config('background')) #('background', 'background', 'Background', <border object: 'SystemButtonFace'>, 'SystemButtonFace')
    #print(cmd.config('bg'))         #idem
    # doc zegt: 'bg' is alias, geeft 2-tuple: ('bg'.'background'); klopt niet
    #print(cmd.winfo_class())        #Button

    #print("thread:", threading.get_ident())     #thread: 5172

    cmd.mainloop()


def tstMultiTk():
    #NoDefaultRoot()    #bij deze MOET je bij iedere ctrl master opgeven
    #multi Tk() geeft via IDLE eig altijd gezeik. Je MOET eerst win2
    #sluiten via knop of sluitkruis, daarna win1, anders prb sluiten 2e venster
    #ook gezeik als je eerst win1 mkt en onderaan win2.mainloop() zet
    #moraal: NOOIT 2 Tk() vensters openen!
    #kan wel meerdere TopLevel vensters.
    win1 = Tk()
    win2 = Tk()
    #als ik bij vlg win1 weglaat, wordt master autom 1e Tk, dus win1,
    #tenzij NoDefaultRoot() aanstaat
    Button(win1, text='klik!', command=win1.destroy).pack()
    Button(win2, text='klak!', command=win2.destroy).pack()
    
    win1.mainloop()


def tstTk_properties():
    root = Tk()         #className='Oef' ->wnd titel
    # vor args:
    # screenName ->zet window op scherm met deze naam
    # baseName ->naam voor profile file, zie readprofile()
    # className='Tk' ->nm vd class, wordt window title

    #root['width'] = 200            # let op: deze + geom -> grootte client area
    #root['height'] = 200           # venster is vanwege titelbalk dus langwerpig
    #root.geometry('400x200')            #width,height
    #root.geometry('400x200+300+50')     #width,height,x,y (x,y kunnen neg zijn)
    root.geometry('+300+50')            #alleen x,y
    #root.geometry(200,200)         #error
    #root.title('tralala')

    root.update_idletasks()

    print('\ncontrol props:')
    #print(root['background'])   # SystemButtonFace, idem 'bg'
    #print(root['borderwidth'])  # 0, idem 'bd'; zie geen verschil met zetten
    #print(root['cursor'])      # std leeg; zetten: root['cursor'] = 'gumby'
    print(root['height'])       # 0, kan zetten: root['height'] = 60
    print(root['width'])            # 0, kan zetten, samen met 'height'
    # height + width beide zetten, anders raar venster
    #print(root['highlightbackground'])  # SystemButtonFace, zetten werkt niet
    #print(root['highlightcolor'])       # SystemWindowFrame, kan zetten
    #print(root['highlightthickness'])   # 0, kan zetten, gekoppeld aan vor
    #print(root['relief'])           # flat, kan zetten, eist 'bd' > 0
    #print(root['takefocus'])        # 0
    #print(root['padx'])             # 0
    #print(root['pady'])             # 0
    #print(root['class'])            # Tk
    #print(root['colormap'])         # leeg
    #print(root['container'])        # 0
    #print(root['visual'])           # leeg
    #print(root['use'])              # leeg

    print(root.title())              # tk
    
    # unknown properties/resources:
    # activebackground, activeforeground, anchor, bitmap, closeenough,
    # command, confine, disabledforeground, fg, font, foreground, image,
    # insertbackground, insertborderwidth, insertofftime, insertontime,
    # insertwidth, justify, offset, scrollregion, selectbackground,
    # selectborderwidth, selectcolor, selectforeground, state, text,
    # title, type, x, y,
    # xscrollcommand, xscrollincrement, yscrollcommand, yscrollincrement

    # zonder vlg mkt hij wel juiste grootte, maar toont niet in .winfo_xyz()
    # wsch doet mainloop() een update()
    #root.update()          #meestal niet in eventhandler ->kans recurs aanroep!
    #root.update_idletasks()

    print('\ncontrol:')
    print(root.winfo_width())           # 200 (default)
    print(root.winfo_height())          # 200
    print(root.winfo_rootx())           # x,y: 70,89 bij geometry 66,66
    print(root.winfo_rooty())           # ->libo client area (onder titelbalk) tov scherm
    print(root.winfo_geometry())        # 200x200+xxx+yyy (default)
    # als je geen x,y opgeeft ->venster verspringt bij iedere start
    print(root.winfo_x())               # hier gelijk aan x-deel geom
    print(root.winfo_y())               # idem y-deel geom
    print(root.bbox())                  #(0,0,0,0), voor grid layout
    print(root.winfo_reqwidth())        # 200 (requested width)
    print(root.winfo_reqheight())       # 200
    print(root.winfo_toplevel())        # . [want Tk() is al toplevel]
    print(root.winfo_id())              # hwnd, window handle
    print(root.winfo_class())           # Tk
    print(root.winfo_ismapped())        # 1
    print(root.winfo_name())            # tk
    print(root.winfo_parent())          # <leeg>

    print('\nscreen:')
    print(root.winfo_screen())          # :0.0
    print(root.winfo_screenwidth())     # 1024 (op Netbook)
    print(root.winfo_screenheight())    # 600 (op Netbook)
    print(root.winfo_screenmmwidth())   # 271 (op Netbook)
    print(root.winfo_screenmmheight())  # 159 (op Netbook)

    print('\ncolor:')
    print(root.winfo_depth())           # 32  [bits per pixel]
    print(root.winfo_screencells())     # 256
    print(root.winfo_screendepth())     # 32
    print(root.winfo_rgb('blue'))       # (0, 0, 65535)
    print(root.winfo_screenvisual())    # truecolor
    print(root.winfo_visual())          # truecolor
    print(root.winfo_colormapfull())    # False

    print('\nextra:')
    print(root.winfo_interps())         # ()    [in principe de Tcl-interpr namen]
    print(root.winfo_manager())         # wm
    print(root.protocol())              # ('WM_DELETE_WINDOW',)

    print(root.event_info())            #list v alle voorgedef virt event namen

    
    #root.attributes('-alpha',0.6)       #0.0 transparant, 1.0 opaque
    #root.attributes('-disabled',True)   #alles disabled, NIET doen voor topwnd!
    #root.attributes('-toolwindow',True) #wel resizable
    #root.resizable(width=False, height=False)      #goed ->vast venster
    #root.attributes('-topmost',True)
    #root.lift()                 #werkt niet tov ander prog
    #root.attributes('-transparentcolor','black')       #werkt
    #root.attributes('-fullscreen',True)     #metro-look, geen titel/randen/startmenu
    #root.overrideredirect(True)    #alleen client area, geen titel/randen; Alt+F4 werkt

    root.mainloop()


#grid ->tstTk_grid_Entry_Clipboard_validate(), tstTk_grid_Entry_saveinlist()

def tstTk_pack():
    # volgorde van packen doet er toe
    root = Tk()
    #fra1 = Frame(root)
    fra1 = Frame(root, bd=3, relief=RIDGE)
    fra1.pack(side=RIGHT)       #komt rechts, vert gecentreerd
    cmd = Button(fra1, text='Klik')
    cmd.pack()          #side=TOP ->knop bovenin fra1, maar fra1 vert centr
    print(cmd.info())   #of .pack_info(); moet .place_info()/.grid_info() volledig opgeven
    
    Label(root, text='Een label').pack()    #side=TOP
    Label(root, text='Tweede label').pack()
    
    root.mainloop()


def tstTk_place():
    # place: abs pos binnen frame; x,y (=pos v anchor),width,height;
    # relx/y, relwidth/height: 0.0-1.0 ->rel tov frame
    # anchor=N,E,S,W,CENTER (dflt NW)
    # pack binnen frame maakt zelf ruimte ->mkt frame en zonodig form groter
    # place binnen frame eist hetzij geometry + fill=BOTH + expand,
    # (zonder geometry start frm te klein, moet uitschuiven om frame te zien)
    # hetzij opgegeven frame width + height ->past frmgrootte aan
    # (dit zijn startgrootten; met fill+expand frame uitschuifbaar)
    
    root = Tk()
    #root.geometry('400x300')

    # hier buitenste lb + fra1 met .pack(), ctrls binnen fra1 met .place()
    Label(root, text='Top label').pack()
    Label(root, text='Nog een label').pack()
    fra1 = Frame(root, bd=2, relief=SOLID)
    fra1.config(width=360, height=260)
    #fra1.pack()
    fra1.pack(fill=BOTH, expand=YES)
    Label(fra1, text='Eerste label').place(x=10,y=10)
    Label(fra1, text='Tweede label').place(x=10,y=40)
    cmd1 = Button(fra1, text="knop1", width=10)     #kars
    cmd1.place(x=200,y=10)          #, anchor=CENTER
    Button(fra1, text="knop2").place(x=200,y=40, width=100)     #px
    # vlg kan ook, moet in_ = .., niet in = ..
    #Button(root, text="knop2").place(in_=fra1, x=200,y=40, width=100)
    #print(cmd1.info())      #error, wnd isn't packed
    print(cmd1.place_info())

    root.mainloop()

    
def tstTk_Label_Buttons():
    lst = ['ik slaap', 'ik eet', 'ik drink', 'ik niks', 'ik doe maar wat\nen waar niet']
    idx = 0

    def showText():
        nonlocal idx
        lbl['text'] = 'Ha, ' + lst[idx]
        #lbl.text = 'ohoo'      #werkt niet, wordt extra prop
        idx +=1
        if idx == len(lst): idx = 0

    def showTikTak(ev):
        #atts = [x for x in dir(ev) if x[:2] != '__']
        #print(atts)
        # vlg beide goed
        if str(ev.widget) == '.cmd1':
            lbl['text'] = 'Rikketikketik.'
        elif ev.widget is cmd2:
            lbl['text'] = 'Takketakketak!'
        else:
            lbl['text'] = str(ev.widget)

    def askQuestion(ev):
        print(ev.widget)
        if ev.widget is cmd1:
            vraag = 'Hoe heet u?'
        elif ev.widget is cmd2:
            vraag = 'Waar woont u?'
        else:
            vraag = 'Wat doet u?'
        antw = simpledialog.askstring(None, vraag)
        print('antw=', antw)    #bij Cancel -> None
        lbl['text'] = antw      #als None -> blijft oude text

    root = Tk()
    root.title('Label en Buttons')
    #root['title'] = 'Mijn venster'     #_tkinter.TclError: unknown option

    # vlg alle .pack() met default side=TOP ->alles onder elkaar
    
    # hij past grootte topvenster aan grootte label aan
    # lbl width/height aant chars; kapt tekst af; scrollt niet autom; \n mag
    # Message = meerregelig Label, doet wel auto wrap
    # bij 1-rgl tekst en height=2 wordt tekst vert gecentreerd
    # tekst normaal hor gecentreerd; met anchor=W li zetten
    # justify=LEFT,CENTER,RIGHT ->vervolgregels
    lbl = Label(root, text='Hehe, ik eet.', height=2)   #2 regels
    lbl.pack()      #doet std side=TOP
    lbl['fg'] = '#332299'       #of 'white' enz
    lbl['bg'] = '#BBE7AA'       #rrggbb, mag ook met kl lett
    # vlg width/height in kars
    Button(root, width=10, text='Klik!', command=showText).pack()
    # goed: command=lambda : lbl.config(text='aie aie')
    # fout: command=lambda : lbl['text']='aie aie' ->syntax error, ook met haakjes
    # (want je mag niet toekennen in lambda)
    
    cmd1 = Button(root, width=10, text=' Tik ', name='cmd1')  #wordt: .cmd1
    #zonder name krijgt cmd1 een getal als id, genre: .33318960
    cmd1.bind('<Button-1>', showTikTak)     #bind-> fn krijgt event-obj mee
    cmd1.bind('<Button-3>', askQuestion)    #Button-3 is rmuis
    cmd1.pack()
    cmd2 = Button(root, width=10, text=' Tak ', name='cmd2')
    cmd2.bind('<Button-1>', showTikTak)
    cmd2.bind('<Button-3>', askQuestion)
    cmd2.pack()
    
    root.mainloop()         #kan ook via lbl.mainloop()


def tstTk_Font_Labels():
    root = Tk()
    root.title('Font Labels')
    root.geometry('400x220+250+50')     #grootte + pos 300,50; -300,50 is 300 v rechts

    #print(font.families())     #mag pas na creatie root; alle fontnamen
    # vlg zijn font-configuraties: dit font met deze size en deze slant
    #print(font.names())    #klein rijtje voorgedefinieerd

    # vlg geeft echt Font-obj, voegt mijn fnt toe aan font.names()
    fnt = font.Font(family='comic sans ms', size=14, name='mycomic')
    # family, size, weight='bold'|'normal', slant='italic'|'roman',
    # underline=0|1, overstrike=0|1 (beide ook False|True)
    # , name='mycomic'
    # name: eigen naam voor deze specifieke font-configuratie
    # zonder eigen name='..' krijgt ie naam: 'font1'

    print(type(fnt))                #tkinter.font.Font
    #print(fnt)                     #mycomic
    #print(vars(fnt))
    #print(dir(fnt))
    #print(type(fnt.actual()))       #<class 'dict'>
    #print(fnt.actual())
    print(fnt.actual()['size'])     #14
    print(fnt['size'])             #14
    #fnt['size'] = 24               #goed
    #fnt.config(size=18)             #goed

    # vlg negeert slant, size enz. krijgt name='mycomic_italic'
    fnt2 = font.Font(font='mycomic', slant='italic', name='mycomic_italic')
    fnt2['slant'] = 'italic'        #zo wordt ie wel italic
    print("fnt2:\n", fnt2.actual())

    fnt3 = font.nametofont('mycomic')       #deze fn wel hfdlet gevoelig
    #fnt3 = font.nametofont('TkdefaultFont')
    print("fnt3\n", fnt3.actual())
    # {'family': 'Tahoma', 'slant': 'roman', 'underline': 0, 'overstrike': 0, 'weight': 'normal', 'size': 8}
    # rest idem, [Small]CaptionFont ->bold;
    # TkFixedFont: {'overstrike': 0, 'weight': 'normal', 'slant': 'roman', 'size': 9, 'underline': 0, 'family': 'Courier New'}

    print(fnt is fnt3, fnt == fnt3)     #False True
    
    # vlg geven tupel ipv echt Font-obj:
    #ftup = 'times'              #goed; fontfam namen hfdlett ongevoelig
    ftup = ('times', 14, 'bold italic')
    # 14 = punt, -14 = pixel
    #ftup = 'times 14 bold italic'            #ook goed
    #ftup = ('comic sans ms', 14)             #goed
    #ftup = ('comic sans ms', 14 , 'bold italic')
    #ftup = 'comic sans ms 14'            #error, spatie in fontnaam

    #print(type(ftup))            # tuple of str

    
    print(font.names())    #bevat nu ook mycomic, mycomic_italic

    lbl1 = Label(root, text='Dit is het eerste label')
    #lbl1 = Label(root, text='Dit is het eerste label', font=ftup)
    lbl1.pack()
    #lbl2 = Label(root, text='En nog een mooi label!', font=18)
    lbl2 = Label(root, text='En nog een mooi label!', font=('',18))
    #lbl2 = Label(root, text='En nog een mooi label!', font=fnt)
    lbl2.pack()

    print()
    #print(root["font"])        #error
    print("lbl1['font']:", lbl1["font"])    #TkDefaultFont
    print("lbl2['font']:", lbl2["font"])    #{} 18
    #print(lbl2.config("font"))      #('font', 'font', 'Font', <font object: 'TkDefaultFont'>, '{} 18')
    #print(lbl2.cget("font"))        #{} 18

    #fnt.config(size=28)         #lbl2 krijgt deze font-grootte

    root.mainloop()

    
def tstTk_Sound_Frame_optiondb():

    def doeOK():
        lbl['text'] = 'Dit was OK'
        #root.bell()         #werkt
        #winsound.Beep(freq, msecs)
        winsound.PlaySound('basil.wav', winsound.SND_FILENAME)
        #winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        # extra flags, bv: or winsound.SND_ASYNC or winsound.SND_LOOP
        # stoppen met: .PlaySound(None)

    def doeCancel():
        #lbl['text'] = 'Dit was Cancel'
        #lbl['text'] = font.nametofont(lbl['font']).size    #error
        lbl['text'] = lbl['font']       # '{comic sans ms} 14'
        # of: '{comic sans ms} 14 bold', of: '{comic sans ms} 14 {bold italic}'
        #print(lbl['fontsize'])
        cmd1.flash()

    root = Tk()

    #root.title('Font, Frame, Button, sound')
    root.geometry('240x140+300+50')     #grootte + pos 300,50; -300,50 is 300 v rechts
    #root.resizable(width=False, height=False)

    # option database gebruiken:
    # (geldt voor alle vervolg ctrls)
    # Button, Label etc case sensitive; font/Font case insensitive
    # vooraan altijd *
    # daarna . = prop v deze ctrl; * = prop voor deze ctrl + alle subctrls
    # helemaal vooraan mag appname; in Win willek naam ->beter weglaten

    #root.option_add('*font', 'times 12 bold')      #alle ctrls
    #root.option_add('*foreground', 'dark slate blue')
    #root.option_add('*Frame*foreground', 'dark slate blue') #alles met fg binnen Frames
    #root.option_add('*Frame.foreground', 'dark slate blue')
    root.option_add('*fra1*foreground', 'dark slate blue') #alles met fg binnen fra1
    # vor werkt alleen als je name='fra1' opgeeft, anders krijgt Frame nm .9876543
    #root.option_add('*fra1.foreground', 'dark slate blue')     #fg v fra1 zelf
    #root.option_add('*Button.font', 'times 12 bold')   #alleen voor buttons
    #root.option_add('*Button.font', 'times 12')   #ook goed, normal
    #root.option_add('*Button.font', ('times', 12, 'bold'))     #ook goed
    #root.option_add('*Button.foreground', 'blue')       # niet fg
    #root.option_add('*fra1*Button.foreground', 'blue')  #alleen buttons in fra1

    #print(root.option_get('*foreground', '*fra1'))       #allemaal niks

    fnt = ('comic sans ms', 14)             #goed
    
    lbl = Label(root, text='Probeer de knoppen!', font=fnt)
    lbl['fg'] = 'brown'
    
    lbl.pack(expand=YES, fill=BOTH)   #default side=TOP
    #padx/pady in widget mkt ctrl groter; in .pack() ->meer ruimte om ctrl
    fra1 = Frame(root, name='fra1')      #, pady=5; name nodig voor option_add()
    fra1['bd'] = 4          #zonder bd doet relief niks
    #fra1['relief'] = GROOVE
    #fra1['highlightcolor'] = 'black'       #niks
    fra1.pack(pady=5)     #dit frame zorgt ervoor dat de knoppen elkaar raken
    #het frame komt gecentreerd onder lbl, met flex+minimale grootte
    cmd1 = Button(fra1, text='OK', width=7, command=doeOK)
    cmd1['bg'] = 'cyan'
    cmd1.pack(side=LEFT)
    Button(fra1, text='Cancel', width=7, command=doeCancel).pack(side=LEFT)
    Button(fra1, text='Exit', width=7, fg='red', command=root.destroy).pack(side=RIGHT)

    root.mainloop()         #kan ook via lbl.mainloop()


def tstTk_RadioButtons():
    componisten = ['Bach', 'Purcell', 'Marais', 'Sting', 'Schnittke']
    betaalwijze = ['Creditcard', 'IDEAL','PayPal','Bitcoin','SuperTrust']
    #ivar_radio = IntVar()     #hier error, moet na creatie root, want eist master
    # std tk kent geen Combobox (ttk wel) ->gebr OptionMenu

    def toonKeuze():
        a = ivar_radio.get()
        if a < 0:
            lbl['text'] = 'U moet wel een keuze maken!'
        else:
            lbl['text'] = 'De keuze viel op: %s\nU betaalt met: %s' \
                % (componisten[a], svar_cbo.get())
    
    root = Tk()
    root.title('Radiobuttons + IntVar')
    #ivar_radio = IntVar()         #impliciet root als master
    ivar_radio = IntVar(root)      #IntVar(master=None,value=0) -> .get(), .set(x)
    #ivar_radio.set(None)          #niet doen, get() eist int ->error bij geen selectie
    ivar_radio.set(-1)             #werkt wel ->geen bolletje geselecteerd
    
    Label(root, text='Kies uw favoriete componist:', width=40).pack()
    lbl = Label(root, text='', height=2, font=('courier',9,'underline'))
    lbl.pack(pady=4)        #in lbl komt het antwoord te staan

    #fra1 = Frame(root)
    fra1 = LabelFrame(root, text='Opties', padx=20,pady=1)   #ruimte in frame
    #print(fra1['labelanchor'])              # nw, mag niet CENTER
    fra1['labelanchor'] = N                 #text boven midden
    for i,nm in enumerate(componisten):
        Radiobutton(fra1, text=nm, value=i, variable=ivar_radio).pack(anchor=W)
        # vanwege impliciete side=TOP komen ze onder elkaar
        # default takefocus=1 ->je kunt met tab naar vlg, niet met pijltjes
    #print(fra1.winfo_children())       #lijst met radio-obj
    fra1.pack()

    fra2 = Frame(root)              #, width=200, height=50
    fra2.pack(padx=2,pady=2,anchor=W)  #side=TOP,dus onder fra1, maar li ipv center
    # let op: place() binnen fra2 alleen goed als je fra2 eerst width,height geeft
    # anders blijft fra2 onzichtbaar
    Button(fra2, text=' Toon uw keuze ', command=toonKeuze).pack(side=BOTTOM,anchor=E,pady=2)
    Label(fra2, text='U betaalt met:').pack(side=LEFT)
    svar_cbo = StringVar(value=betaalwijze[0])     #init val
    #svar_cbo = StringVar()      #optieknop begint leeg
    opt = OptionMenu(fra2, svar_cbo, *betaalwijze)     #kan hier niet width opgeven
    # opt wil losse keuze-items ->moet mijn list uitpakken met *
    opt.config(width=len(max(betaalwijze, key=len)))    #hier wel, in aant chars
    #print(opt.keys())          #bevat inderdaad o.a. 'width'
    opt.pack(side=LEFT)
    
    #Button(root, text=' Toon uw keuze ', command=toonKeuze).pack(pady=2)
    # als je vor button in fra2 zet, krijg je 'm nooit onder de andere items

    root.mainloop()


def tstTk_Listbox_Scrollbar():

    def toonKeuze():
        sel = lbox.curselection()    #tupel met geselec rijen
        lbl['text'] = repr(sel)
        #print(lbox.get(ACTIVE))     #toont 1e bij multiselect
        #print(lbox.get(sel))        #get() wil idx of (idx,), error multiselect
        for i in sel:
            print(lbox.get(i))

    root = Tk()
    root.title('Listbox + Scrollbar')

    fra1 = Frame(root)
    fra1.pack(expand=YES, fill=BOTH, padx=3, pady=3)
    sbar = Scrollbar(fra1, orient=VERTICAL)
    sbar.pack(side=RIGHT,fill=Y)    #heeft geen expand=YES nodig
    # sbar eerst packen, anders verdwijnt ie bij kleiner maken wnd
    lbox = Listbox(fra1, selectmode=MULTIPLE)
    # selectmode=BROWSE (def), SINGLE, MULTIPLE, EXTENDED
    # EXTENDED=win manier met ctrl/shift+klik, MULT=alleen kliks
    lbox.pack(side=LEFT, expand=YES, fill=BOTH)
    for rg in range(1,81):
        lbox.insert(END, 'Dit is regel ' + str(rg))
    sbar['command'] = lbox.yview        #sbar roept lbox aan ->lbox beweegt mee
    lbox['yscrollcommand'] = sbar.set   #lbox roept sbar aan ->sbar loopt mee met up/down op lbox

    fra2 = Frame(root)
    fra2.pack(fill=X, padx=3, pady=3)
    lbl = Label(fra2, text='wat?')
    lbl.pack(side=LEFT, fill=X)
    cmd = Button(fra2, text='  Kijk  ', command=toonKeuze)
    cmd.pack(side=RIGHT)
    
    root.mainloop()


def tstTk_Text_Scrollbar():

    def toonKeuze():
        #get() voegt zelf \n toe, maar niet zichtbaar in tekstvenster
        txt = tbox.get('1.0', END)    #END+'-1c' (= 'end-1c') ->laat slot \n weg
        # vlg error als niets geselecteerd
        #txt = tbox.get(SEL_FIRST, SEL_LAST)  #of: 'sel.first','sel.last'
        #print(ord(txt[-1]))         #10, dwz \n
        print(txt + 'q')
        
        #lbl['text'] = repr(tbox['font'])    #'TkFixedFont'
        #lbl['text'] = tbox.edit_modified()
        #lbl['text'] = tbox.index('bingo.first')    #INSERT | END | 'bingo.first'
        lbl['text'] = tbox.index(INSERT)        #huid cursorpos, bij wrap zelfde rg
        #print(tbox.get('bingo.first','bingo.last'))    #'bingo' is tag met range
        #print(tbox.get('bingo.first'))      #geeft 1 char
        #print(tbox.get('1.0','3.0') + 'x')    #geeft 2 regels
        #print(tbox.get('1.0','1.0+3.0'))       #error, idem '1.0+3'
        print(tbox.get('1.0','1.0+3 lines'))     #+3 el ->beg + 3 regels
        # vor mag met 3l,3 l,3 li,3 lin, enz; ook: 3c,3 c,3 cha, enz
        # error met 3 lon,3 cho, enz
        #tbox.delete('1.0', END)

    def voegtoe():
        tbox.insert(END,'kiwi')

    def vulTbox():
        # index: 1e regel is rg 1; kol telt vanaf 0 ->vooraan is '1.0'
        #tbox.delete('1.0', END)
        tbox.insert(END, 'appel\npeer\nen een lekkere banaan\ncitroen\ndruif')
        #tbox.insert('3.0', 'Regel 3\n')

        # je markeert een punt met beg; tagt een substr met beg,eind
        #tbox.mark_set(INSERT, '3.10')    #zet cursor; of markeer pnt: 'bingopnt'
        #tbox.mark_set(INSERT, '3.10 wordstart')
        #tbox.mark_set(INSERT, '3.0 lineend')
        tbox.mark_set(INSERT, '3.10 linestart')
        #tbox.icursor('3.0')         #error bestaat niet, wel goed bij Entry
        #tbox.tag_add('bingo', '3.0','4.2')

        tbox.tag_add(SEL, '1.0','1.end')      #sel gebied, hier rg tot aan \n
        #tbox.tag_add(SEL, '1.0','1.0 lineend')     #idem
        #tbox.tag_add(SEL, '1.0','2.0-1c')    #idem, '-1c' moet vanwege \n
        # vor zonder -1c tot eind v regel in tekstvak
        #tbox.tag_remove(SEL, '1.0',END)     #sel weg (niet tekst) in deze regio
        tbox.edit_modified(False)

    root = Tk()
    root.title('Text + Scrollbar')

    # vlg kan ook met scrolledtext; die bevat Frame, Scrollbar, Text
    fra1 = Frame(root)
    fra1.pack(expand=YES, fill=BOTH, padx=3, pady=3)
    sbar = Scrollbar(fra1, orient=VERTICAL)
    sbar.pack(side=RIGHT,fill=Y)
    tbox = Text(fra1, wrap=WORD)           #geen textvariable=myStringVar
    # wrap=CHAR (dflt),WORD,NONE
    tbox.pack(side=LEFT, expand=YES, fill=BOTH)
    sbar['command'] = tbox.yview
    tbox['yscrollcommand'] = sbar.set
    tbox.focus()

    vulTbox()
    
    fra2 = Frame(root)
    fra2.pack(fill=X, padx=3, pady=3)
    lbl = Label(fra2, text='wat?')
    lbl.pack(side=LEFT, fill=X)
    # knop Kijk komt helemaal rechts
    Button(fra2, text='  Kijk  ', command=toonKeuze).pack(side=RIGHT)
    Button(fra2, text='  Add   ', command=voegtoe).pack(side=RIGHT)

    root.mainloop()


def tstTk_grid_Entry_Clipboard_validate():
    # pack en grid NIET compatibel (behalve in aparte Frames)
    # pack en place WEL compatibel
    entries = []

    def showClipboard():
        try:
            clip = root.clipboard_get()
        except TclError:        #bv bij geen txt op klembord
            clip = ''
        print('clipboard:', clip)
        print('entries[0]:', entries[0].get())

    def isOkee(act, idx, old, new):
        print('act:', act)
        print('idx:', idx)
        print('old:', old)
        print('new:', new)
        if new == 'klaas':
            print('dit is klaas')
            return False            #werkt alleen bij validate='key'
        else:
            return True

    def isOkee2():
        txt = entries[0].get()
        print(txt)
        if txt == 'klaas':
            print('dit is klaas')
            entries[0].focus()      #focus terugzetten bij validate='focusout' enz
        return True                 #moet
    
    root = Tk()
    root.title("Grid + Entry, simpel")

    # Label: anchor bep waar txt in lbl komt, default CENTER
    # geef het 1e lbl een vaste breedte ->bep kolbreedte in grid
    # vervolg lbls zijn even breed als hun tekstinhoud ->anchor niet nodig
    # je ziet niet dat ze kleiner zijn vanwege hun default bg kleur!
    # Label kan niet transparant zijn; default bg='SystemButtonFace'
    # sticky=W ->plaats lbl's li in gridcell
    # gridcol wordt even breed als breedste item -> 1e lbl width=12 kars gezet
    Label(root, text='Naam:', bg='cyan', width=12, anchor=W).grid(row=0,column=0, sticky=W)
    Label(root, text='Adres:').grid(row=1,column=0, sticky=W)
    Label(root, text='Plaats:').grid(row=2,column=0, sticky=W)
    for i in range(3):
        ent = Entry(root)           #textvariable=...
        ent.grid(row=i,column=1, sticky=EW)     #volle breedte cel
        entries.append(ent)

    ent = entries[0]
    # vlg valfn met args moet je eerst registreren
    #isok = ent.register(isOkee)         #type(isok)->str
    #ent.config(validate='focusout', validatecommand=(isok,'%d','%i','%s','%P'))

    # vlg valfn zonder args ->kan zonder .register(..)
    ent.config(validate='focusout', validatecommand=isOkee2)

    Button(root, text='ToonClip', command=showClipboard).grid(row=3,column=0,columnspan=2)
    # zonder vlg wordt kol niet breder bij resize -> sticky werkt niet
    # weight is int; kan ook weight > 1 ->ene kol groeit harder and andere
    #root.columnconfigure(0, weight=0)  #default weight=0 ->mag weg
    root.columnconfigure(1, weight=1)   #kol 1 breder maken bij resize
    #root.rowconfigure(0, weight=1)     #rij 0 hoger bij resize

    root.mainloop()


def tstTk_grid_Entry_saveinlist():
    isNew = True
    idx = -1
    lst = []                    #list v records; ieder rec is list v strings
    cmdsNav = []                #4 pijltjes knoppen
    entries = []                #3 Entry tekstvakken

    def navigate(ev):
        nonlocal idx
        if not lst:
            return
        if ev.widget is cmdsNav[0]:
            idx = 0
        elif ev.widget is cmdsNav[1]:
            idx -= 1
        elif ev.widget is cmdsNav[2]:
            idx += 1
        elif ev.widget is cmdsNav[3]:
            idx = len(lst) - 1
        show()

    def show():
        nonlocal idx
        if not lst:
            return
        if idx >= len(lst):
            idx = len(lst) - 1
        if idx < 0:
            idx = 0
        wis()
        d = lst[idx]                        #d is list v strings
        for i in range(len(d)):
            entries[i].insert(0, d[i])
        lblNav['text'] = '(%d)' % idx

    def wis():                          #alleen scherm wissen
        for ent in entries:
            ent.delete(0, END)

    def doDel():                        #rec wissen uit lijst
        nonlocal idx
        wis()
        if lst and 0 <= idx < len(lst):
            del lst[idx]
            show()
        
    def doSave():
        nonlocal idx, isNew
        for ent in entries:               #als niet alle tekstvakjes gevuld...
            if not ent.get(): return      # '' als leeg; geen .set(..)
        d = [e.get() for e in entries]    #list v strings
        if d:
            print(d)
        if lst and not isNew:
            lst[idx] = d
        else:
            lst.append(d)
            idx = len(lst) - 1
            lblNav['text'] = '(%d)' % idx
        isNew = False

    def doNew():
        nonlocal isNew
        wis()
        entries[0].focus()
        isNew = True
        
    root = Tk()
    root.title("Grid + Entry, met 'save'")

    fra1 = Frame(root)      #, bd=1, relief=SOLID
    fra1.pack(expand=YES, fill=X, padx=3, pady=3)
    # .grid() heeft veel opties ->je moet argnaam opgeven
    Label(fra1, text='Naam:', width=12, anchor=W).grid(row=0,column=0, sticky=W)
    Label(fra1, text='Adres:').grid(row=1,column=0, sticky=W)
    Label(fra1, text='Plaats:').grid(row=2,column=0, sticky=W)
    for i in range(3):
        ent = Entry(fra1)           #textvariable=...
        ent.grid(row=i,column=1, sticky=EW)     #volle breedte cel
        entries.append(ent)
    fra1.columnconfigure(1, weight=1)   #kol 1 breder maken bij resize

    fra2 = Frame(root)
    fra2.pack(fill=X, padx=3, pady=3)

    # vlg gebr .bind() ipv command=, zodat je met ev.widget op cmd kunt testen
    cmd = Button(fra2, text='<<', width=7, name='cmdFirst')
    cmd.bind('<Button-1>', navigate)
    cmd.pack(side=LEFT)
    cmdsNav.append(cmd)
    cmd = Button(fra2, text='<', width=7, name='cmdLeft')
    cmd.bind('<Button-1>', navigate)
    cmd.pack(side=LEFT)
    cmdsNav.append(cmd)
    cmd = Button(fra2, text='>', width=7, name='cmdRight')
    cmd.bind('<Button-1>', navigate)
    cmd.pack(side=LEFT)
    cmdsNav.append(cmd)
    cmd = Button(fra2, text='>>', width=7, name='cmdLast')
    cmd.bind('<Button-1>', navigate)
    cmd.pack(side=LEFT)
    cmdsNav.append(cmd)

    fra3 = Frame(root)
    fra3.pack(fill=X, padx=3, pady=3)
    
    cmd = Button(fra3, text='Del', width=6, name='cmdDel', command=doDel)
    cmd.pack(side=LEFT)
    cmd = Button(fra3, text='Save', width=6, name='cmdSave', command=doSave)
    cmd.pack(side=LEFT)
    cmd = Button(fra3, text='New', width=7, name='cmdNew', command=doNew)
    cmd.pack(side=LEFT)
    Button(fra3, text=' P ', command=lambda : print(lst)).pack(side=LEFT)
    lblNav = Label(fra3, text='( )', fg='blue')
    lblNav.pack(side=RIGHT)

    entries[0].focus()
    root.mainloop()


def tstTk_Canvas():
    ids =[]
    tags = []
    pos = False

    def onFigureClick(ev):          #na deze doet ie ook onCanvasClick
        nonlocal pos
        print('fig:',ev.x,ev.y)
        #print(ev.widget.widgetName)     # canvas
        pos = True
        #return "break"          #geen effect, want hierna ander event
        # "break" werkt alleen bij cascade v zelfde event

    def onCanvasClick(ev):
        nonlocal pos
        if not pos:          #dit event onderdrukken na onFigureClick
            print('can:',ev.x,ev.y)                         #int
            #print(can.canvasx(ev.x), can.canvasy(ev.y))     #float
        pos = False

    def onCanvasResize(ev):
        print('can resize=',ev.width,ev.height)   #alleen bij resize/repos (<Configure>)
        print("can.coords('kop')=", can.coords('kop'))
    
    def cmdMoveClick():
        s = ent.get()           # formaat: id/tag,dx,dy
        if not s:
            return
        id_dx_dy = s.split(',')
        can.move(*id_dx_dy)       #lst uitpakken ->losse args; relat verpl

    root = Tk()
    root.title("Een canvas venster")
    root.geometry('+300+50')            #alleen x,y pos op scherm

    can = Canvas(root, width=300, height=240)   #, bg='white'
    #can: default bg = SystemButtonFace
    #can: default size = 378, 265
    # scrollregion=(0,0,300,960)
    can['bg'] = 'white'     # canvas heeft geen fg,fill,outline,font
    #can.config(highlightthickness=0)   #default 2px grijze rand; kan je op klikken
    #can['highlightthickness'] = 0

    can.bind('<Button-1>', onCanvasClick)
    can.bind('<Configure>', onCanvasResize)
    can.pack(expand=YES, fill=BOTH)

    print('can: width/height:', can['width'], can['height'])    #str, niet int
    #print('can: width/height:', can.cget('width'), can.cget('height'))
    print('can: borderwidth:', can['borderwidth'])     # 0
    print('can: highlightthickness:', can['highlightthickness'])   # 2
    
    fra1 = Frame(root)
    fra1.pack()
    ent = Entry(fra1, width=20)
    ent.pack(side=LEFT)
    Button(fra1, text=' Move ', command=cmdMoveClick, fg='dark green').pack(side=RIGHT)
    #lbl = Label(fra1, text='', width=20)

    id = can.create_line(40,15,80,15,80,30,120,15,140,30, width=3, tag='kop')
    #of: tags='kop' | ('kop',) | ('kop','staart')
    # polygon voegt zelf afsluitend lijnstuk toe v eindpunt naar begpunt; line niet
    ids.append(id)
    tags.append('kop')
    fnt = ('comic sans ms', 14)

    id = can.create_text(40,25, text='Peer', fill='blue', font=fnt, anchor=NW, tag='kop')
    # default anchor=CENTER -> centreert rond x,y
    # vanaf tk 8.6 ook: angle=30 ->roteer tekst linksom
    #can.addtag_withtag('kop', id)   #geef item met id=2 ook de tag 'kop'
    ids.append(id)

    lblcan = Label(can, text='Banaan', font=fnt)    #, bg='white'
    # label niet transparant
    id = can.create_window(160,25, window=lblcan, anchor=NW, tags=('kop','staart'))
    ids.append(id)
    tags.append('staart')

    id = can.create_oval(20,100,140,180, outline='red', fill='brown')
    # bij oval geen angle=30
    can.tag_bind(id, '<Button-1>', onFigureClick)
    ids.append(id)

    id = can.create_arc(160,100,260,200, start=20, extent=250, activefill='blue')
    # hij zet mdp v arc in midden gereserveerde ruimte
    # default: start=0, extent=90, style=PIESLICE (CHORD,ARC)
    can.tag_bind(id, '<Button-1>', onFigureClick)
    ids.append(id)

    print('ids=', ids)
    print('tags=', tags)
    print('can.find_closest(30,25)=', can.find_closest(30,25))
    #print(can.tag_names())     #error, alleen bij Text, idem tag_config()

    root.mainloop()


class MenuDemo(Tk):

    def __init__(self):
        super().__init__()
        self.title("Frame met topmenu")
        self.geometry('+300+100')
        self.text = "Using Python menus"

        self.can = Canvas(self, width=440, height=240)
        self.can['bg'] = '#c8dce6'
        #self.curFnt = ('arial', 18, 'italic')
        self.curFnt = ('arial', 18)
        self.can.create_text(220,120, text=self.text, font=self.curFnt
            , tag='info', angle=0)     #angle vanaf tk 8.6, in graden
        self.can.bind('<Configure>', self.onCanvasResize)
        
        self.can.pack(expand=YES, fill=BOTH)
        self.createMenu()
        
    def createMenu(self):
        top = Menu(self)
        self.config(menu=top)

        file = Menu(top, tearoff=False)
        top.add_cascade(label='File', menu=file,underline=0)
        file.add_command(label='New...', command=lambda : self.chtxt('New'))
        file.add_command(label='Open...', command=self.chooseFilename)
        file.add_command(label='Save...', command=lambda : self.chtxt('Save'))
        file.add_command(label='Close...', command=lambda : self.chtxt('Close'))
        file.add_separator()        #kan niet met add_command(label='-')
        file.add_command(label='Exit', command=self.destroy)

        edit = Menu(top, tearoff=False)
        top.add_cascade(label='Format', menu=edit, underline=5)
        edit.add_command(label='Size...', command=lambda : self.chtxt('Size'))

        colors = Menu(edit, tearoff=False)
        edit.add_cascade(label='Colors', menu=colors)
        colors.add_command(label='Red', command=lambda : self.chtxt('Red'))
        colors.add_command(label='Green', command=lambda : self.chtxt('Green'))
        colors.add_command(label='Blue', command=lambda : self.chtxt('Blue'))
        colors.add_command(label='Grey', command=lambda : self.chtxt('Grey'))
        colors.add_command(label='Default', command=lambda : self.chtxt('Default'))
        colors.add_separator()
        colors.add_command(label='Choose...', command=self.chooseClr)
        
        edit.add_command(label='Font...', command=self.notimpl)

    def onCanvasResize(self, ev):
        #print(self.can.itemconfig('info')['text'])  # ('text', '', '', '', 'Using Python menus')
        #print(self.can.itemcget('info','text'))
        #print(self.can.coords('info'))      # [220.0, 120.0], anchor=CENTER
        # hij neemt 2 of meer coords v 1e item met deze tag ->bij line extra x2,y2, evt x3,y3 enz
        # Ik wil tekst centreren in venster
        # [1] can.move() ->dx,dy ->oude x,y nodig om dx,dy te berekenen
        #x,y = self.can.coords('info')       #text heeft alleen x,y
        #self.can.move('info', ev.width/2 - x, ev.height/2 - y)
        # [2] can.coords() ->x,y ->oude x,y niet nodig ->alleen mdp v canvas
        self.can.coords('info', ev.width/2, ev.height/2)

    def notimpl(self):
        print('not implemented yet')

    def chtxt(self, item):
        if item == 'Size':
            self.can.itemconfig('info', text="This is menu Size")
        elif item == 'New':
            self.can.itemconfig('info', text="Een nieuwe lente, een nieuw geluid")
        elif item == 'Save':
            self.can.itemconfig('info', text="This is menu Save")
        elif item == 'Close':
            self.can.itemconfig('info', text="Let's close down")
        elif item == 'Red':
            self.can.itemconfig('info', fill='red', text="The rednecks are coming!")
        elif item == 'Green':
            self.can.itemconfig('info', fill='dark green', text="The green pastures are gone forever")
        elif item == 'Blue':
            self.can.itemconfig('info', fill='blue', text="Blue is the sea")
        elif item == 'Grey':
            self.can.itemconfig('info', fill='grey', text="On a grey morning I went fishing")
        elif item == 'Default':
            self.can.itemconfig('info', fill='black', text="Black are the night\nand the days\nand almighty's future")

    def chooseClr(self):
        clr = colorchooser.askcolor()
        #clr = colorchooser.askcolor("yellow")  #zelt alvast kleur klaar
        #->tuple: ((234.9140625, 228.890625, 30.1171875), '#eae41e')
        #  bij Cancel: (None, None), wordt NIET als False gezien!
        # tkinter werkt verder nooit met (r,g,b) ->gebr altijd color str
        # (r,g,b) moet je converteren: "#%02x%02x%02x" % (33.102,147.887, 255.998)
        # ->'#2193ff'

        #print(clr, bool(clr))
        if clr[1]:
            self.can.itemconfig('info', fill=clr[1])

    def chooseFilename(self):
        fname = filedialog.askopenfilename(
            filetypes=[('Text files','*.txt'),('All files','*.*')])
        #of: tupel v tupels
        print(fname)        # D:/PythonData/Sandbox/dwarfs.txt
        
def tstTk_MenuDemo_class():
    root = MenuDemo()
    root.mainloop()


def tstTk_Photo_Button_Label():
    root = Tk()
    root.title("Een fotoknop")

    #img = PhotoImage(file="blueman.gif")
    #img = PhotoImage(file="Apollo11.png")
    img = PhotoImage(file="bld.jpg")            #eist PIL

    # Button krijgt grootte img, venster krijgt grootte button
    # bij expand + fill wordt knop groter + img gecentreerd op knop
    # vanwege default anchor=CENTER voor item binnen knop/lbl
    #Button(root, image=img).pack(expand=YES, fill=BOTH)

    # Label idem
    lbl = Label(root, image=img)
    #lbl = Label(root, fg='white', text="Hallo!", image=img, compound=CENTER
    #    , font=('times',24))
    # compound: LEFT=plaatje links, TOP=boven, CENTER=tekst op plaatje
    # zonder compound ->tekst onderdrukt
    lbl.pack(expand=YES, fill=BOTH)

    root.mainloop()


def tstTk_Photo_Canvas_pack():
    # prb bij resize is dat canvas wel meegroeit met form, maar dat
    # maar dat het plaatje z'n oorspr pos op canvas houdt
    # beter: canvas vaste grootte, plaatje eenmalig centreren en
    # daarna canvas centreren op form mbv place() ipv pack()
    root = Tk()
    root.title("Een fotocanvas, pack")

    img = PhotoImage(file="blueman.gif")
    #img = PhotoImage(file="bld.jpg")
    #print(dir(img))         # .width(), .height(), niet als props met [..]
    print('img:',img.width(),img.height())      #img: 150 150 (int)
    can = Canvas(root)
    print('can:',can['width'],can['height'])    #can: 378 265 (str)
    #can.create_image(5,5, image=img, anchor=NW)    # x,y wordt NW v plaatje
    # vlg zonder anchor centreert hor/vert rond x,y op canvas
    can.create_image(int(can['width'])/2,int(can['height'])/2, image=img)

    can.pack(expand=YES, fill=BOTH)
    
    root.mainloop()


def tstTk_Photo_Canvas_place():
    root = Tk()
    root.title("Een fotocanvas, place")

    root['bg'] = 'white'        #geen fg
    

    img = PhotoImage(file="blueman.gif")
    #img = PhotoImage(file="bld.jpg")
    w, h = img.width(), img.height()

    can = Canvas(root, width=w, height=h)
    # of: canvas op std grootte laten en bij place width/height opgeven
    print('can:',can['width'],can['height'])    #can: default 378 265 (str)
    #can['bg'] = 'red'
    #can['highlightthickness']=0                #geen rand
    print('can:',can['width'],can['height'])
    can.create_image(2,2, image=img, anchor=NW)
    # hij legt 2px rand libo over canvas heen, reon ernaast
    # zonder rand: w+4,h+4,(2,2) ->rondom 2px red bg canvas
    # met rand: idem ->rondom 2px grijze rand, reon 4 px red
    # zonder rand: w,h,(0,0) ->hele plaatje
    # met rand: idem ->libo 2px afgeknipt, reon 2px red
    # met rand: w,h,(2,2) ->hele plaatje, rondom 2px rand, geen red
    # KORTOM: met rand mkt hij canvas 2 px groter; je hoeft canvas niet
    # te vergroten, maar je moet plaatje wel op pos (2,2) neerzetten!

    root.geometry('%dx%d+200+50' % (w+120,h+80))

    can.place(relx=0.5,rely=0.5, anchor=CENTER)     #default NW
    # rel[x/y/width/height] 0.0 - 1.0 tov master, hier hele form; default 0.0
    # x,y komen na relx/rely; x=30, relx=0.5 ->ga 30px re van midden
    # width,height ->clip img of vergroot canvas
    # in/in_ = ctrl -> plaats in deze ctrl
    # bordermode = 'inside','outside' ->tel border width master wel/niet mee
    # ->geen effect bij master=Tk()
    
    #can.place(x=20,y=20)
    #can.place(x=0,y=0)          #img libo
    #can.place(x=0,y=0, bordermode='outside')
    #can.place(x=0,y=0, width=100, height=100)
    #can.place(x=-10,y=10)       #img te ver naar li, van rand form af
    #can.place(relx=1.0, anchor=NE)      #img rebo

    root.mainloop()


#--- script ---

#tstLabel1()
#tstLabel2()
#tstMessage1()
#tstEntry1()
#print("thread:", threading.get_ident())
#tstButton1()            #incl arg via fun.partial en via lambda

#tstMultiTk()
#tstTk_properties()

#tstTk_pack()
#tstTk_place()

tstTk_Label_Buttons()
#tstTk_Font_Labels()
#tstTk_Sound_Frame_optiondb()
#tstTk_RadioButtons()
#tstTk_Listbox_Scrollbar()
#tstTk_Text_Scrollbar()
#tstTk_grid_Entry_Clipboard_validate()
#tstTk_grid_Entry_saveinlist()

#tstTk_Canvas()
#tstTk_MenuDemo_class()

#tstTk_Photo_Button_Label()
#tstTk_Photo_Canvas_pack()
#tstTk_Photo_Canvas_place()

