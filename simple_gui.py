#!/usr/bin/python3

"""
Simpe GUI using PySimpleGUI module.
"""

# Vooraf:
#   pip3 install PySimpleGUI
# Verwijderen:
#   pip3 uninstall PySimpleGUI

import PySimpleGUI as sg

# Very basic form.  Return values as a list
form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
          [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
          [sg.Submit(), sg.Cancel()]
         ]

# Oorspronkelijk:
# button, values = form.LayoutAndRead(layout)
# Geeft:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/karel/.local/lib/python3.8/site-packages/PySimpleGUI/PySimpl...
#     raise DeprecationWarning(
# DeprecationWarning: LayoutAndRead is no longer supported... change your ca...
# or window(title, layout).Read()
button, values = form.Layout(layout).Read()

print(button, values[0], values[1], values[2])

# EOF
