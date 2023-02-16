#!/bin/bash
# shellcheck disable=SC2034
###############################################################################
# Oefening voor gettext, vertaling naar NL. 
#
# Geschreven door Karel Zimmer <info@karelzimmer.nl>.
###############################################################################

export TEXTDOMAIN=helloworld
# export TEXTDOMAINDIR=/usr/share/locale
export TEXTDOMAINDIR=/home/karel/scripts

source /usr/bin/gettext.sh

program_name=$0

printf '%s\n\n' "$(eval_gettext "Program name: \$program_name")"

printf '%s\n\n' "$(gettext 'Use'): $program_name"

printf '%s\n\n' "$(gettext 'Hello world!')"

printf '%b\n\n' "$(gettext 'Sentence

with

spaces

between the

lines.')"

printf '%b\n\n' "$(gettext 'Sentence\nover\nfour\nlines.')"

exit

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
