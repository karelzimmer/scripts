#!/bin/python
###############################################################################
# Oefening voor gettext, vertaling naar NL. 
#
# Geschreven door Karel Zimmer <info@karelzimmer.nl>.
###############################################################################

import gettext

gettext.bindtextdomain('helloworld', '/home/karel/scripts')
# gettext.bindtextdomain('helloworld', '/usr/share/locale')
gettext.textdomain('helloworld')
_ = gettext.gettext

program_name = 'helloworld.py'

# Werkt niet met gettext om dezelfde reden als bij .sh:
# print(_(f"Program name: {program_name}"))
print(_('Program name: {}').format(program_name))
print('')
# Meerdere {}:
# print(_('The awesomeness level of {} is {}.').format(country, level))

print(_('Hello world!'))

# Informatie
# ----------
# https://www.gnu.org/software/gettext/manual/gettext.html
# # https://docs.python.org/3/library/gettext.html
# https://github.com/QubesOS/qubes-issues/issues/7824
# https://phrase.com/blog/posts/translate-python-gnu-gettext/
 
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
