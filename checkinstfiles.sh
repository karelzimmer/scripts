#!/bin/bash

# Terminalattributen ('man terminfo'). Gebruik ${<variabele_naam>}.
readonly BOLD=$(tput bold)
readonly NORMAL=$(tput sgr0)
readonly RED=${BOLD}$(tput setaf 1)

error=false

# cd /home/karel/kzscripts || exit 1

#XXX NB. #@, #1, en OPD is verplicht.
#XXX NB. #2 en #3 is niet verplicht.
#XXX NB. Volgorde is
#XXX     #@     VERPLICHT
#XXX     #1     VERPLICHT
#XXX     OPD-1  VERPLICHT
#XXX     ...    VERPLICHT
#XXX     OPD-n  VERPLICHT
#XXX     #2     OPTIONEEL
#XXX     #3     OPTIONEEL

#for file in ./{kzinstall,kzsetup}*; do
#for file in ./{kzinstall,kzsetup}*20.04-desktop.sh; do
#for file in ./kzsetup*20.04-desktop.sh; do
for file in ./kzinstall*20.04-desktop.sh; do
    appline=false
    dscline=false
    cmdline=false
    lineno=0
    while read -r record; do
        ((++lineno))
        recordtype=${record:0:2}
        case $recordtype in
            '')
                continue
                ;;
            '#@')
                appline=true
                ;;
            '#1')
                if ! $appline; then
                    echo "${RED}In bestand $file ontbreekt een app-tag (#@):
    regelnummer $lineno: $record."
                    error=true
                fi
                dscline=true
                ;;
            '#'*)
                # Commentaarregel.
                continue
                ;;
            *)
                if ! $dscline; then
                    echo "${RED}In bestand $file ontbreekt een beschrijving (#1):
    regelnummer $lineno: $record."
                    error=true
                fi
                appline=false
                cmdline=true
                ;;
        esac
        if $error; then
            echo "
${RED}Fouten geconstateerd${NORMAL}
Controle afgebroken."
            exit 1
        fi

    done < "$file"        
done


# EOF
