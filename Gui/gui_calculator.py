# https://python-forum.io/Thread-Tkinter-VS-PyQt
# zat in een van de antwoorden; door mij aangepast
# Pmw is een oude externe lib voor megawidgets, combinatie v bestaande widgets
# in tkinter zit al tkinter.scrolledtext.ScrolledText ->Frame + Text + vert Scrollbar

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from math import *      #ook zichtbaar binnen eval(..)

KWIDTH = 6              #knop breedte; 5 knoppen/regel; std br=5 ->evt 6
DWIDTH = 16             #display breedte; niet belangrijk; wordt fill=BOTH
 
class SLabel(Frame):
    """ SLabel defines a 2-sided label within a Frame. The
        left hand label has blue letters the right has white letters
    """
 
    def __init__(self, master, leftl, rightl):
        #Frame.__init__(self, master, bg='gray40')
        super().__init__(master, bg='gray40')
        self.pack(side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=leftl, fg='steelblue1',
              font=("arial", 6, "bold"), width=KWIDTH, bg='gray40').pack(
            side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=rightl, fg='white',
              font=("arial", 6, "bold"), width=1, bg='gray40').pack(
            side=RIGHT, expand=YES, fill=BOTH)
 
class Key(Button):
    def __init__(self, master, font=('arial', 8, 'bold'),
            fg='white', width=KWIDTH, borderwidth=5, **kw):
        # je kan kw wel rechtstreeks doorgeven aan hogere init, maar
        # dan kun je geen default args meegeven.
        kw['font'] = font
        kw['fg'] = fg
        kw['width'] = width
        kw['borderwidth'] = borderwidth
        super().__init__(master, **kw)        #**kw werkt niet
        self.pack(side=LEFT, expand=NO, fill=NONE)
"""
class Key(Button):
    def __init__(self, master, **kw):
        # alternatief:
        kw.setdefault('font',('arial', 8, 'bold'))
        kw.setdefault('fg','white')
        kw.setdefault('width',KWIDTH)
        kw.setdefault('borderwidth',5)
        super().__init__(master, **kw)        #**kw werkt niet
        self.pack(side=LEFT, expand=NO, fill=NONE)
""" 

class Calculator(Frame):
    def __init__(self, parent=None):
        #Frame.__init__(self, bg='gray40')
        super().__init__(bg='gray40')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Tkinter Toolkit TT-42')
        #self.master.iconname('Tk-42')  #naam bij minimize ->niet in Win
        #self.calc = Evaluator()  # This is our evaluator, doet eval(..)

        self.build_calculator()  # Build the widgets

        # call table bij FUN knop
        self.actionDict = {'second': self.do_this, 'mode': self.do_this,
           'delete': self.do_this, 'alpha': self.do_this,
           'stat': self.do_this, 'math': self.do_this,
           'matrix': self.do_this, 'program': self.do_this,
           'vars': self.do_this, 'clear': self.clearall,
           'sin': self.gonio, 'cos': self.gonio,
           'tan': self.gonio, 'up': self.do_this,
           'X1': self.do_this, 'X2': self.do_this,
           'log': self.do_this, 'ln': self.do_this,
           'store': self.do_this, 'off': self.turnoff,
           'neg': self.neg, 'enter': self.do_enter,
        }
        self.current = ""

    # vlg actionDict
    def do_this(self, action):
        print('"{}" has not been implemented'.format(action))

    def turnoff(self, *args):
        #self.quit()
        self.master.destroy()
 
    def clearall(self, *args):
        self.current = ""
        self.display.delete(1.0, END)

    def gonio(self, action):
        # action bevat 'sin','cos','tan'
        txt = action + '(radians('
        self.display.insert(END, txt)
        self.current += txt

    def neg(self, action):
        pos = self.display.index(INSERT) + ' linestart'
        self.display.insert(pos, '-')
        self.current = '-' + self.current
        
        
    # actionDict + bind aan Text [=self.display]
    def do_enter(self, *args):
        #result = self.calc.runpython(self.current)
        try:
            result = eval(self.current)
        except Exception as ex:
            result = "## ERROR ##"
            print(ex)
        if result:
            self.display.insert(END, '\n')
            self.display.insert(END, '{}\n'.format(result), 'ans')
        self.current = ""
        self.display.see(END)       #toon onderste regel

    # bind aan Text [=self.display]
    def do_keypress(self, event):
        key = event.char
        if not key in ['\b']:
            self.current = self.current + event.char
        if key == '\b':
            self.current = self.current[:-1]
 
    # bij een KEY knop (zie hieronder bij knop-definities)
    def key_action(self, key):
        self.display.insert(END, key)
        self.current = self.current + key

     # bij een FUN knop ->call fn uit actionDict met key action
    def eval_action(self, action):
        try:
            self.actionDict[action](action)
        except KeyError:
            pass
 
    def build_calculator(self):
        FUN = 1  # Designates a Function
        KEY = 0  # Designates a Key
        KC1 = 'gray30'  # Dark Keys
        KC2 = 'gray50'  # Light Keys
        KC3 = 'steelblue1'  # Light Blue Key
        KC4 = 'steelblue'  # Dark Blue Key
        keys = [
            [('2nd', '', '', KC3, FUN, 'second'),  # Row 1
             ('Mode', 'Quit', '', KC1, FUN, 'mode'),
             ('Del', 'Ins', '', KC1, FUN, 'delete'),
             ('Alpha', 'Lock', '', KC2, FUN, 'alpha'),
             ('Stat', 'List', '', KC1, FUN, 'stat')],
            [('Math', 'Test', 'A', KC1, FUN, 'math'),  # Row 2
             ('Mtrx', 'Angle', 'B', KC1, FUN, 'matrix'),
             ('Prgm', 'Draw', 'C', KC1, FUN, 'program'),
             ('Vars', 'YVars', '', KC1, FUN, 'vars'),
             ('Clr', '', '', KC1, FUN, 'clear')],
            [('X-1', 'Abs', 'D', KC1, FUN, 'X1'),  # Row 3
             ('Sin', 'Sin-1', 'E', KC1, FUN, 'sin'),
             ('Cos', 'Cos-1', 'F', KC1, FUN, 'cos'),
             ('Tan', 'Tan-1', 'G', KC1, FUN, 'tan'),
             ('^', 'PI', 'H', KC1, FUN, 'up')],
            [('X2', 'Root', 'I', KC1, FUN, 'X2'),  # Row 4
             (',', 'EE', 'J', KC1, KEY, ','),
             ('(', '{', 'K', KC1, KEY, '('),
             (')', '}', 'L', KC1, KEY, ')'),
             ('/', '', 'M', KC4, KEY, '/')],
            [('Log', '10x', 'N', KC1, FUN, 'log'),  # Row 5
             ('7', 'Un-1', 'O', KC2, KEY, '7'),
             ('8', 'Vn-1', 'P', KC2, KEY, '8'),
             ('9', 'n', 'Q', KC2, KEY, '9'),
             ('X', '[', 'R', KC4, KEY, '*')],
            [('Ln', 'ex', 'S', KC1, FUN, 'ln'),  # Row 6
             ('4', 'L4', 'T', KC2, KEY, '4'),
             ('5', 'L5', 'U', KC2, KEY, '5'),
             ('6', 'L6', 'V', KC2, KEY, '6'),
             ('-', ']', 'W', KC4, KEY, '-')],
            [('STO', 'RCL', 'X', KC1, FUN, 'store'),  # Row 7
             ('1', 'L1', 'Y', KC2, KEY, '1'),
             ('2', 'L2', 'Z', KC2, KEY, '2'),
             ('3', 'L3', '', KC2, KEY, '3'),
             ('+', 'MEM', '"', KC4, KEY, '+')],
            [('Off', '', '', KC1, FUN, 'off'),  # Row 8
             ('0', '', '', KC2, KEY, '0'),
             ('.', ':', '', KC2, KEY, '.'),
             ('(-)', 'ANS', '?', KC2, FUN, 'neg'),
             ('Enter', 'Entry', '', KC4, FUN, 'enter')]]
 
        fra1 = Frame(self, bd=8, relief=SUNKEN, bg='gray40')
        fra1.pack(side=TOP, expand=YES, fill=BOTH)
        self.display = ScrolledText(fra1, 
            background='honeydew4', width=DWIDTH,
            foreground='black', height=6,
            bd=3, relief=GROOVE,
            font=('arial', 12, 'bold'))
        self.display.pack(expand=YES, fill=BOTH, padx=0, pady=0)
        self.display.tag_config('ans', foreground='white')
        self.display.bind('<Key>', self.do_keypress)
        self.display.bind('<Return>', self.do_enter)
        #print(self.display['padx'])
        
        for row in keys:
            rowa = Frame(self, bg='gray40')
            rowb = Frame(self, bg='gray40')
            for p1, p2, p3, color, ktype, sfunc in row:
                if ktype == FUN:
                    a = lambda s=self, a=sfunc: s.eval_action(a)
                else:
                    a = lambda s=self, k=sfunc: s.key_action(k)
                SLabel(rowa, p2, p3)
                Key(rowb, text=p1, bg=color, command=a)
            rowa.pack(side=TOP, expand=YES, fill=BOTH)
            rowb.pack(side=TOP, expand=YES, fill=BOTH)
 

#--- script ---

if __name__ == '__main__':
    Calculator().mainloop()

