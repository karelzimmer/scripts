#!/bin/bash
# shellcheck disable=SC2034,SC2317
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

printf '%s\n' "$(gettext 'Use'): $PROGNAME"

printf '%b\n' "$(gettext 'Sentence\nover\nfour\nlines.')"

exit

# Werkwijze
# ---------
# sudo apt install gettext

cd ~/scripts || exit

# Maak POT bestand (Portable Object Template) aan:
xgettext --language=Shell --output=helloworld.pot helloworld.sh
mkdir --parents nl/LC_MESSAGES
# Opnieuw genereren voegt '#, fuzzy' toe?? Wat betekent fuzzy??

# Maak PO bestand (Portable Object) aan:
msginit --locale=nl --input=helloworld.pot --output-file=nl/LC_MESSAGES/helloworld.po
# Herhalen is mogelijk:
xgettext --language=Shell --join-existing --output=helloworld.pot helloworld.sh
msgmerge --update nl/LC_MESSAGES/helloworld.po helloworld.pot

# Wijzig 1-malig het PO bestand:
# Content-Type: text/plain; charset=UTF-8\n" <== UTF-8
# PACKAGE -> helloworld
# VERSION -> 0.1

# Wijzig als vertaler het PO bestand:
# msgid "Hello world!"
# msgstr "" --> "Hallo wereld!"
# Etc.

# Vind duplicates in PO bestand:
msguniq --repeated nl/LC_MESSAGES/helloworld.po

# Combineer PO bestanden:
msgcat --repeated File1.po File2.po --output-file=File3.po

# Maak MO bestand (Machine Object) aan:
msgfmt --output-file=nl/LC_MESSAGES/helloworld.mo nl/LC_MESSAGES/helloworld.po
# Wordt gedistribueerd en geinstalleerd met "kz.deb", zonder helloword.po.
# ── helloworld.pot
# ├── helloworld.sh
# ├── nl
# │   └── LC_MESSAGES
# │       ├── helloworld.mo
# │       ├── helloworld.po
# Voor systeem:
sudo cp nl/LC_MESSAGES/helloworld.mo /usr/share/locale/nl/LC_MESSAGES
sudo rm /usr/share/locale/nl/LC_MESSAGES/helloworld.mo 


# Testen
# ------
echo "$LANGUAGE"
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
# https://wiki.ubuntu-nl.org/community/Vertaalteam/Startersgids-Vertaaltips
# https://wiki.ubuntu.com/UbuntuDevelopment/Internationalisation/InternationalizationPrimer/Gettext
# https://stackoverflow.com/questions/2221562/using-gettext-in-bash
# http://eyesfreelinux.ninja/posts/internationalising-shell-scripts-with-gettext.html
# https://www.tutorialspoint.com/unix_commands/gettext.htm

# cd /bin; grep gettext 2> /dev/null
# locate .po|grep '.po$'
# locate .mo|grep '.mo$'
# download src-versie van een pakket die .po/.mo heeft
# Hoe werkt gettext met meerdere te vertalen regels?

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
