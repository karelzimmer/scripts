#!/bin/bash

# Hostname (computernaam) wijzigen

#==========================================================================#
# Instellingen.                                                            #
#==========================================================================#
hostnameold=$(hostname)
hostnamenew='gg-'$(mktemp --dry-run XXXXXXX)
parmerr=0

GPL=$(cat << GPL

Licentie GPLv3+: GNU GPL versie 3 of later.
Zie <http://gnu.org/licenses/gpl.html> voor de volledige (Engelse) tekst.
Dit is vrije software: je bent vrij om het te veranderen
en te herdistriburen volgens hiervoor genoemde licentie.
Deze software kent geen GARANTIE, voor zover de wet dit toestaat.

Geschreven door Karel Zimmer, <http://karelzimmer.nl>, \
<info@karelzimmer.nl>.
GPL
)

HELP=$(cat << HELP
Geldige opties zijn:
    -h, --help      deze hulptekst tonen en stoppen
    -u, --usage     een korte gebruikssamenvatting tonen en stoppen
    -v, --verbose   elke invoerregel en opdracht tonen
                    (kan ook met '(sudo) bash -vx $0')
    -V, --version   scriptversie tonen en stoppen
HELP
)

#  Voorbeeld gebruik: echo "${RED}Foutje${NORMAL}"
#  Mogelijke tput's : $ man terminfo 
BLACK=$(tput bold;tput setaf 9)
GREEN=$(tput bold;tput setaf 2)
YELLOW=$(tput smul;tput setaf 3)
RED=$(tput bold;tput setaf 1)
UNDERLINE=$(tput smul)
NORMAL=$(tput sgr0)

#==========================================================================#
# Functies.                                                                #
#==========================================================================#

#-Functie------------------------------------------------------------------#
# Naam:   init                                                             #
# Doel:   Initiele acties van dit script                                   #
# Parm 1: Opties en argumenten van aanroep script                          #
#--------------------------------------------------------------------------#
init ()
{

    #----------------------------------------------------------------------#
    # Evalueer de opties en argumenten meegegeven bij de aanroep.          #
    #----------------------------------------------------------------------#
    while [ "$1" != "" ]
        do

        #------------------------------------------------------------------#
        # Verwerk algemene opties en argumenten.                           #
        #------------------------------------------------------------------#
        case $1 in
            --help|-h)
                hulp
                exit 0
                ;;
            --usage|-u)
                gebruik
                exit 0
                ;;
            --verbose|-v)
                set -o verbose
                set -o xtrace
                ;;
            --version|-V)
                versie
                exit 0
                ;;
            --new|-N)
                shift
                if [ "$1" = '' ]
                then
                    parmerr=1
                    echo "${RED}Ongeldige computernaam '$1'.${NORMAL}"
                else
                    hostnamenew=$1
                fi
                shift
                continue
                ;;
            --)
                shift
                break
                ;;
            *)
                parmerr=1

                #----------------------------------------------------------#
                # Afhankelijk eerste positie een optie of een argument.    #
                #----------------------------------------------------------#
                if [ "${1:0:1}" = '-' ]
                then
                    echo "${RED}Ongeldige optie '$1'.${NORMAL}"
                else
                    echo "${RED}Ongeldig argument '$1'.${NORMAL}"
                fi
                ;;
        esac
        shift
    done

    #----------------------------------------------------------------------#
    # Controleer op argumenten na --.                                      #
    # De -- geeft het einde van de opties aan,                             #
    # de rest wordt beschouwd als argumenten.                              #
    # Bijvoorbeeld handig als een bestandsnaam begint met -.               #
    #----------------------------------------------------------------------#
    if [ ! -z "$*" ]
    then
        parmerr=1
        echo "${RED}Ongeldig argument '$*'.${NORMAL}"
    fi

    #----------------------------------------------------------------------#
    # Geef optie help aan als er fouten zijn geconstateerd.                #
    #----------------------------------------------------------------------#
    if [ $parmerr -eq 1 ]
    then
        echo "Typ '$0 --help' of '$0 --usage' voor meer informatie."
        exit 1
    fi

    #----------------------------------------------------------------------#
    # Controleer of we root zijn.                                          #
    #----------------------------------------------------------------------#
    check_root

    echo "${GREEN}Computernaam $hostnameold wordt gewijzigd naar" \
         "$hostnamenew.${NORMAL}"
}

#-Functie------------------------------------------------------------------#
# Naam:   gebruik                                                          #
# Doel:   Uitleg aanroep script                                            #
# Parm 1: ---                                                              #
#--------------------------------------------------------------------------#
gebruik ()
{
    echo "Gebruik: sudo $0 [-N hostname|-h|-u|-V] [-v]"
}

#-Functie------------------------------------------------------------------#
# Naam:   hulp                                                             #
# Doel:   Uitleg werking script                                            #
# Parm 1: ---                                                              #
#--------------------------------------------------------------------------#
hulp ()
{
    gebruik
cat << HULP
Script $0 wijzigt de hostname (computernaam).
Als bij de aanroep geen nieuwe hostname wordt opgegeven
wordt een computernaam bepaald lijkend op 'gg-XXXXXXX'.
Hierin wordt 'XXXXXXX' vervangen door willekeurige letters en cijfers.
$HELP
    -N H, --new=H   wijzig hostname (computernaam) naar H
HULP
}
                                                                            
#-Functie------------------------------------------------------------------#
# Naam:   versie                                                           #
# Doel:   Toon versie-informatie                                           #
# Parm 1: ---                                                              #
#--------------------------------------------------------------------------#
versie ()
{
    echo "$HEADER"
    echo 'Copyright (C) 2010 Karel Zimmer.'
    echo "$GPL"
}

#-Functie------------------------------------------------------------------#
# Naam:  check_root                                                        #
# Doel:  Controleer of we root zijn                                        #
# Parm 1: ---                                                              #
#--------------------------------------------------------------------------#
check_root ()
{

    #----------------------------------------------------------------------#
    # Controleren of we root zijn.                                         #
    #----------------------------------------------------------------------#
    if [ $(whoami) != 'root' ]
    then
        echo "${RED}Dit script moet worden uitgevoerd als superuser" \
             "(root).${NORMAL}"
        gebruik
        exit 1
    fi
}

#-Functie------------------------------------------------------------------#
# Naam:   wijzig                                                           #
# Doel:   Wijzig hostname                                                  #
# Parm 1: Bestandsnaam waarin de hostname gewijzigd moet worden            #
#--------------------------------------------------------------------------#
wijzig ()
{
    cp  $1 $1.old
    cat $1 | sed --expression="s/$hostnameold/$hostnamenew/g" > $1 
}

#-Functie------------------------------------------------------------------#
# Naam:   afsl                                                             #
# Doel:   Afsluitende acties van dit script                                #
# Parm 1: ---                                                              #
#--------------------------------------------------------------------------#
afsl ()
{
    echo "${GREEN}Computernaam $hostnameold is gewijzigd" \
         "naar $hostnamenew.${NORMAL}"
    echo
    echo "Typ 'exit' om Terminalvenster af te sluiten."
    exit 0
}

#==========================================================================#
# Procedure.                                                               #
#==========================================================================#
# Vervang in invoer '-c=' door '-c ' en '--computer=' door '--computer '.
init $(echo $* | sed --expression='s/-N=/-N /g'      \
                     --expression='s/--new=/--new /g')
wijzig /etc/hostname
wijzig /etc/hosts
afsl
#EOF
