# testmet ttk

r"""
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

help:
The Python Standard Library/Graphical User Interfaces with Tk/tkinter.ttk
->vrij goede doc over Notebook, Treeview, Style, enz

tk stijl:
l1 = tkinter.Label(text="Test", fg="black", bg="white")
l2 = tkinter.Label(text="Test", fg="black", bg="white")

ttk stijl:
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

vlg voor alle ttk-buttons [classname via cmd.winfo_class()]:
ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
btn = ttk.Button(text="Sample")


https://www.programcreek.com/python/example/104114/tkinter.ttk.Treeview
->33 voorbeelden

https://stackoverflow.com/questions/18562123/how-to-make-ttk=treeviews-rows-editable

tree.bind('<<TreeviewSelect>>',self.onSelect,'+')   '+' voeg event toe ipv vervang
tree.bind('<Double-Button-1>',self.onDblClick)
tree.bind('<<TreeviewOpen>>',self.onOpen)
tree.bind('<<TreeviewClose>>',self.onClose)

style = Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd-0, font=('Calibi',11))
style.configure("mystyle.Treeview.Heading", font=('Calibi',13,'bold'))
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea',{'sticky': 'nswe'})]
  vor remove borders?
tree = Treeview(root, style="mystyle.Treeview")

om en om andere kleur per regel, zonder stijl:
tree.insert(..., tag='odd')
tree.insert(..., tag='even')
tree.tag_configure('odd', background="#E8E8E8")
tree.tag_configure('even', background="#C2C2C2")
mag instellen: background, foreground, font, image

"""

from tkinter import *
from tkinter.ttk import Treeview


def tstTreeview1():

    def onOpen(ev):
        print("open")

    def onClose(ev):
        print("close")

    def onSelect(ev):
        #print("select")
        print(tree.focus())
        #print(tree.selection())        #alle gesel rijen (bij selmode 'extended')
        rowid = tree.selection()[0]      #tupel, kan meerdere rijen selecteren

        #print(rowid, tree.item(rowid))          #dict met alle props
        # {'tags': '', 'text': 'klant03', 'image': '', 'values': ['Koos', 'Den Haag'], 'open': 0}

        #print(rowid, tree.item(rowid, option='text'))       #klant03
        #print(rowid, tree.item(rowid, 'text'))      #kan zonder option=
        #print(rowid, tree.item(rowid)['text'])

        #print(rowid, tree.item(rowid, option='values'))     #['Koos','Den Haag']
        #print(rowid, tree.item(rowid, option='values')[1])  #Den Haag
        #print(rowid, tree.item(rowid, column='plaats'))     #error

        print(rowid, tree.set(rowid))       #{'plaats': 'Den Haag', 'naam': 'Koos'}
        print(rowid, tree.set(rowid, 'plaats'))     #of: column='plaats' ->Den Haag
        #print(rowid, tree.set(rowid)['plaats'])     #goed
        print(rowid, tree.set(rowid, '#2'))         #goed, geeft plaats
        print(rowid, tree.set(rowid, 1))            #goed, geeft plaats

        #tree.set(rowid)['plaats']='Voorburg'    #doet niks
        #tree.set(rowid, column='plaats', value='Voorburg')  #goed

    def onRClick(ev):           #<Button-3>
        print("rclick: x=%d, y=%d" % (ev.x,ev.y))
        #elem = tree.identify_element(ev.x, ev.y)
        # vor str: text (kols), padding (tree), Treeitem.indicator ([+]), '' (bij header)
        #elem = tree.identify_region(ev.x, ev.y)
        # vor str: cell (kols), tree (bij tree en [+]), heading, separator, nothing
        # vlg component: region, element, column, row, item (=row ->rowid) 
        #elem = tree.identify('column', ev.x, ev.y)      #goed: #0,#1,#2
        #elem = tree.identify('row', ev.x, ev.y)     #goed, rowid I001, enz
        #elem = tree.identify('item', ev.x, ev.y)    #goed, rowid I001, enz
        #print(elem)

        if 'cell' == tree.identify_region(ev.x, ev.y):
            rowid = tree.identify_row(ev.y)
            col = tree.identify_column(ev.x)
            bbox = tree.bbox(rowid,col)         #tuple libo,wh
            print(rowid, col, bbox)
        
        

    root = Tk()
    root.title("Treeview - als list")
    root.geometry('500x300+160+80')     #wh, libo

    tree = Treeview(root)
    tree['columns']=("naam","plaats")   #data-cols, komen na tree-col
    # zonder vor hebben data-cols alleen #nr naam (vanaf #1) en idx (vanaf 0)
    # cols krijgen ook interne naam: "#1","#2", enz
    # data-cols ook met idx-nr te vinden: 0, 1 (1 lager dan #nr, wegens tree-col)

    #print(tree['columns'])
    #print(tree['show'])             #(<index object: 'tree'>, <index object: 'headings'>)
    #print(tree['displaycolumns'])   #('#all',) default toon alle cols
    # kan vor instellen, zodat alleen bep cols in bep volgorde getoond worden
    #print(tree['height'])           #10
    #print(tree['padding'])         #leeg
    #print(tree['selectmode'])       #extended

    # bovenaan in tree staat altijd de onzichtbare root-node met naam "{}"
    # vlg "#0" is voorgedef naam van tree-kol
    # heading kw: text, image, anchor, command
    tree.heading("#0", text="Klant code")
    tree.heading("naam", text="Naam")
    tree.heading("plaats", text="Plaats")
    tree.column("#0", width=100)
    tree.column("naam", width=100)
    tree.column("plaats", width=140)
    #tree.column("plaats")['width']=140     #doet niks

    #print(tree.heading("#0"))   #{'text': 'Klant code', 'image': '', 'anchor': 'center', 'command': '', 'state': ''}
    #print(tree.column("#0"))    #{'id': '', 'anchor': 'w', 'minwidth': 20, 'width': 200, 'stretch': 1}
    #print(tree.column("#0")['width'])       #default 200
    #tree['show'] = "headings"   #toont niet de tree-kol
    #tree['show'] = "tree"       #toont geen kopregels, wel hele inhoud
    #tree['show'] = ("tree","headings")      #toont alles (default)
    #tree['show'] = "tree headings"         #idem, ook goed

    # vlg 1e arg is parent: ""=toplevel, id=sublevel tov id
    # hij genereert autom EN gebruikt intern 'I001', 'I002' enz, vanaf 1,
    # tenzij je zelf unieke iid=".." opgeeft
    # nodig voor selecties
    tree.insert("",0,text="klant01", values=('Piet','Amsterdam'), tag="first")
    tree.insert("",END,text="klant02", values=('Jan','Rotterdam'))
    rowid = tree.insert("",2,text="klant03", values=('Koos','Den Haag'))
    # vor ,open=True ->toon children
    #print(rowid)       #I003, gegeneerde unieke id
    tree.insert(rowid,0,text="contact", values=('Wil','Utrecht'))
    # vor: positie = 0|END|'end'
    # vlg zelf unieke rowid (=item id, iid) opgegeven:
    tree.insert("",3,text="klant04", iid="id-klant04", values=('Jet','Delft'))
    tree.insert("id-klant04",'end',text="contact", values=('Maaike','Nootdorp'))

    # vlg als rij zonder children ->geen [+], wel open/close events
    # ->bij 1e klik op regel zonder [+] doet ie open, bij 2e klik close
    tree.bind('<<TreeviewOpen>>', onOpen)       #bij klik op (plek v) [+]
    tree.bind('<<TreeviewClose>>', onClose)
    tree.bind('<<TreeviewSelect>>', onSelect)   #komt na vor twee
    tree.bind('<Button-3>', onRClick)

    tree.pack()

    #print(tree.info())              #doet .pack_info()
    #print(tree.winfo_class())       #Treeview
    
    #print(tree.get_children('I003'))        #directe subnodes/rijen
    #tree.selection_set("I002")      #goed, selecteer 2e regel

    root.mainloop()


#--- script ---

tstTreeview1()

