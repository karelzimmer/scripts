#!/bin/bash
# shellcheck disable=SC2034 # I.v.m. eacaped $PROGNAME t.b.v. eval_gettext.
###############################################################################
# Oefening voor gettext, vertaling naar NL. 
#
# Geschreven door Karel Zimmer <info@karelzimmer.nl>.
###############################################################################

export TEXTDOMAIN=helloworld
# export TEXTDOMAINDIR=/usr/share/locale
export TEXTDOMAINDIR=/home/karel/scripts

source /usr/bin/gettext.sh

PROGNAME=$0
msg=$(eval_gettext "Program name: \$PROGNAME")
echo "$msg"; echo

msg="$(gettext 'Hello world!')"
echo "$msg"

exit

# Werkwijze
# ---------
# sudo apt install gettext

cd ~/scripts

# Maak helloworld.pot (Portable Object Template) aan:
xgettext --language=Shell --output=helloworld.pot helloworld.sh
mkdir --parents nl/LC_MESSAGES
# Opnieuw genereren voegt '#, fuzzy' toe?? Wat betekent fuzzy??

# Maak helloworld.nl.po (Portable Object) aan:
msginit --locale=nl --input=helloworld.pot
# Herhalen is mogelijk:
xgettext --language=Shell --join-existing --output=helloworld.pot helloworld.sh
msgmerge --update helloworld.nl.po helloworld.pot

# Wijzig 1-malig de helloworld.nl.po:
# Content-Type: text/plain; charset=UTF-8\n" <== UTF-8
# PACKAGE -> helloworld
# VERSION -> 0.1

# Wijzig als vertaler de helloworld.nl.po:
# msgid "Hello world!"
# msgstr "" --> "Hallo wereld!"

# Maak nl.mo (Machine Object) aan:
msgfmt --output-file=./nl/LC_MESSAGES/helloworld.mo helloworld.nl.po
# Wordt gedistribueerd en geinstalleerd met "kz.deb".


# Testen
# ------
echo $LANGUAGE
# nl:en
# LANGUAGE=nl

./helloworld.sh 
# Programmanaam: ./helloworld.sh
#
# Hallo wereld!

LANGUAGE=en
./helloworld.sh 
# Program name: ./helloworld.sh
#
# Hello world!


# Informatie
# ----------

# cd /bin; grep gettext 2> /dev/null
# locate .po|grep '.po$'
# locate .mo|grep '.mo$'
# download src-versie van een pakket die .po/.mo heeft
# Hoe werkt gettext met meerdere te vertalen regels?

# Bash:
# https://wiki.ubuntu-nl.org/community/Vertaalteam/Startersgids-Vertaaltips
# https://wiki.ubuntu.com/UbuntuDevelopment/Internationalisation/InternationalizationPrimer/Gettext
# https://stackoverflow.com/questions/2221562/using-gettext-in-bash
# http://eyesfreelinux.ninja/posts/internationalising-shell-scripts-with-gettext.html
# https://www.tutorialspoint.com/unix_commands/gettext.htm

# Python:
# https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/
# https://phrase.com/blog/posts/translate-python-gnu-gettext/
# https://phrase.com/blog/posts/learn-gettext-tools-internationalization/

# Voorbeeld grub-kbdcomp:
# #!/bin/sh
# ...
# datarootdir="/usr/share"
# ...
# export TEXTDOMAIN=grub
# export TEXTDOMAINDIR="${datarootdir}/
# ...
# print_option_help "-h, --help" "$(gettext "print this message and exit")"
# print_option_help "-v, --version" "$(gettext "print the version information and exit")"
# print_option_help "-o, --output=$(gettext FILE)" "$(gettext "save output in FILE [required]")"
# ...
# /usr/share/locale/nl/LC_
# ...