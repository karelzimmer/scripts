def init():
    import os

    global filename
    filename = os.path.realpath(__file__)
    global progname
    progname = os.path.basename(__file__)

    print('called __file__=', __file__)
    # _file__= /home/karel/python_work/called.py
    # vanuit module altijd volledig pad + bestandnaam

    print('replaced called=', __file__.replace('called.py', 'caller.py'))
    # replaced= /home/karel/python_work/caller.py
