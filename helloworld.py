#!/bin/python
###############################################################################
# Oefening voor gettext, vertaling naar NL. 
#
# Geschreven door Karel Zimmer <info@karelzimmer.nl>.
###############################################################################

import gettext
import sys

_ = gettext.gettext
# nl = gettext.translation('helloworld', localedir='/home/karel/scripts', languages=['nl'])
# nl.install()
# _ = nl.gettext

# export TEXTDOMAIN=helloworld
# # export TEXTDOMAINDIR=/usr/share/locale
# export TEXTDOMAINDIR=/home/karel/scripts

# source /usr/bin/gettext.sh

message = "Hello world!"
print(_("Hello world!"))

sys.exit(0)

# Informatie
# ----------
# https://phrase.com/blog/posts/translate-python-gnu-gettext/
# https://phrase.com/blog/posts/learn-gettext-tools-internationalization/

# [zimmerce@lsrv0100 bin]$ grep gettext * 2> /dev/null|grep 'import gettext'
# abrt-action-analyze-core:
# abrt-action-analyze-vmcore:
# abrt-action-check-oops-for-hw-
# abrt-action-install-debuginfo:
# abrt-action-perform-ccpp-
# abrt-handle-upload:import gettext <== zie hieronder, complex
# chcat:import gettext
# sandbox:import gettext <== zie hieronder, eenvoudig


# Voorbeeld abrt-handle-upload:

#!/usr/bin/python -u
# Called by abrtd when a new file is noticed in upload directory.
# The task of this script is to unpack the file and move
# problem data found in it to abrtd spool directory.

# import sys
# import stat
# import os
# import getopt
# import tempfile
# import shutil
# import datetime
# import grp

# from reportclient import set_verbosity, error_msg_and_die, error_msg, log

# GETTEXT_PROGNAME = "abrt"
# import locale
# import gettext

# _= lambda x: gettext.lgettext(x)

# def init_gettext():
#  try:
#  locale.setlocale(locale.LC_
#  except locale.Error:
#  os.environ['LC_ALL'] = 'C'
#  locale.setlocale(locale.LC_
#  # Defeat "AttributeError: 'module' object has no attribute 'nl_langinfo'"
#  try:
#  gettext.bind_textdomain_
#  except AttributeError:
#  pass
#  gettext.bindtextdomain(
#  gettext.textdomain(GETTEXT_

# …
#  init_gettext()

# …

#  help_text =_(
#  "Usage: %s [-vd] ABRT_SPOOL_DIR UPLOAD_DIR FILENAME"
#  "\n"
#  "\n -v - Verbose"
#  "\n -d - Delete uploaded archive"
#  "\n ABRT_SPOOL_DIR - Directory where valid uploaded archives are unpacked to"
#  "\n UPLOAD_DIR - Directory where uploaded archives are stored"
#  "\n FILENAME - Uploaded archive file name"
#  "\n"
#  ) % progname


# Uit sandbox:
# #! /usr/bin/python -Es

# PROGNAME = "policycoreutils"
# import gettext
# gettext.bindtextdomain(
# gettext.textdomain(PROGNAME)

# try:
#  gettext.install(PROGNAME,
#  localedir="/usr/share/locale",
#  codeset='utf-8')
# except IOError:
#  try:
#  import builtins
#  builtins.__dict__['_'] = str
#  except ImportError:
#  import __builtin__
#  __builtin__.__dict__['_'] = unicode

# …

# ans = input(_("Do you want to save changes to '%s' (y/N): ") % orig)
