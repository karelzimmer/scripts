#!/usr/bin/python3
import called

print('caller __file__=', __file__)
# _file__= /home/karel/python_work/called.py
# vanuit script NIET altijd volledig pad + bestandnaam,
# karel@pc06:~/python_work$ ./caller.py 
# caller __file__= ./caller.py

called.init()

print('Filename:', called.filename)
#/home/karel/python_work/called.py
# dus niet dit progfile (/home/karel/python_work/caller.py)

print('Progname:', called.progname)

#called.py
# dus niet dit progname (caller.py)

##Zie ook in Python shell na import statement:
##>>> import called

##>>> help(called)
##Help on module called:
##
##NAME
##    called
##
##FUNCTIONS
##    init()
##
##DATA
##    filename = '/home/karel/python_work/called.py'
##    progname = 'called.py'
##
##FILE
##    /home/karel/python_work/called.py
##
##

##>>> dir(called)
##['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
## '__package__', '__spec__', 'filename', 'init', 'progname']

##>>> repr(called)
##"<module 'called' from '/home/karel/python_work/called.py'>"

##>>> repr(called.progname)
##"'called.py'"

##>>> repr(called.filename)
##"'/home/karel/python_work/called.py'"

##>>> type(called.progname)
##<class 'str'>

##>>> type(called.filename)
##<class 'str'>
##>>>
