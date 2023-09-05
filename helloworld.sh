#!/usr/bin/bash
###############################################################################
# Oefening voor gettext, vertaling naar NL. 
#
# Geschreven door Karel Zimmer <info@karelzimmer.nl>.
###############################################################################

export TEXTDOMAIN=helloworld
# export TEXTDOMAINDIR=/usr/share/locale
export TEXTDOMAINDIR=/home/karel/scripts

source /usr/bin/gettext.sh

# shellcheck disable=SC2034
program_name=helloworld.sh

printf '%s\n' "$(eval_gettext "Program name: \$program_name")"
printf '\n'

printf '%s\n' "$(gettext 'Hello world!')"

# Informatie
# ----------
# https://www.gnu.org/software/gettext/manual/gettext.html
# https://wiki.ubuntu-nl.org/community/Vertaalteam/Startersgids-Vertaaltips
# https://wiki.ubuntu.com/UbuntuDevelopment/Internationalisation/InternationalizationPrimer/Gettext
# http://eyesfreelinux.ninja/posts/internationalising-shell-scripts-with-gettext.html

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
