#!/bin/python
###############################################################################
# Oefening voor gettext, vertaling naar NL. 
#
# Geschreven door Karel Zimmer <info@karelzimmer.nl>.
###############################################################################

import gettext
import sys

gettext.bindtextdomain('helloworld', '/home/karel/scripts')
# gettext.bindtextdomain('helloworld', '/usr/share/locale')
gettext.textdomain('helloworld')
_ = gettext.gettext
# nl = gettext.translation('helloworld', localedir='/home/karel/scripts', languages=['nl'])
# nl.install()
# _ = nl.gettext

program_name = 'helloworld.py'

print(_("Hello world!"))

print(f"Program name: {program_name}")

sys.exit(0)

# Informatie
# ----------
# https://docs.python.org/3/library/gettext.html
# https://phrase.com/blog/posts/translate-python-gnu-gettext/
# https://phrase.com/blog/posts/learn-gettext-tools-internationalization/
 
# Uit gettext — Multilingual internationalization services:
# It supports both the GNU gettext message catalog API and
# # a higher level, class-based API that may be more appropriate for Python files. 

# GNU gettext message catalog API:
# import gettext
# gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
# gettext.textdomain('myapplication')
# _ = gettext.gettext
# ...
# print(_('This is a translatable string.'))

# class-based API:
# import gettext
# t = gettext.translation('mymodule', ...)
# _ = t.gettext
# ...
# print(_('This is a translatable string.'))
