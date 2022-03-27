#!/bin/bash
#############################################################################
# Bestand:  sync.sh                                                         #
# Doel:     Script voor het kopiëren van lokale mappen naar externe harde   #
#           schijven.                                                       #
# Gebruik:  ./sync.sh [opties]                                              #
# Gebruikt: script-common.sh    (algemene variabelen en functies)           #
# Auteur:   Karel Zimmer (http://karelzimmer.nl, info@karelzimmer.nl)       #
# ------------------------------------------------------------------------- #
# Auteursrecht © 2011-2014 Karel Zimmer.                                    #
#                                                                           #
# Dit programma is vrije software: u mag het herdistribueren en/of wijzigen #
# onder de voorwaarden van de GNU Algemene Publieke Licentie zoals          #
# gepubliceerd door de Free Software Foundation, onder versie 3 van de      #
# Licentie of (naar Uw keuze) elke latere versie.                           #
#                                                                           #
# Dit programma is gedistribueerd in de hoop dat het nuttig zal zijn maar   #
# ZONDER ENIGE GARANTIE; zelfs zonder de impliciete garanties die           #
# GEBRUIKELIJK ZIJN IN DE HANDEL of voor BRUIKBAARHEID VOOR EEN SPECIFIEK   #
# DOEL.  Zie de GNU Algemene Publieke Licentie voor meer details.           #
#                                                                           #
# U hoort een kopie van de GNU Algemene Publieke Licentie te hebben         #
# ontvangen samen met dit programma. Als dat niet het geval is, zie         #
# http://www.gnu.org/licenses/.                                             #
# ------------------------------------------------------------------------- #
# Versies:  1.0.0   2011-02-20  Eerste versie.                              #
#############################################################################
readonly VERSION_NUMBER=1.19.0
readonly RELEASE_DATE=2014-10-02

#############################################################################
# Instellingen                                                              #
#############################################################################

#---------------------------------------------------------------------------#
# Algemene instellingen                                                     #
# ------------------------------------------------------------------------- #
# Lees de algemene variabelen en functies in.                               #
#---------------------------------------------------------------------------#
source script-common.sh 2> /dev/null || {
    echo "Het algemeen scriptbestand 'script-common.sh'"    >&2
    echo 'is niet gevonden of bevat fouten.'                >&2
    echo 'Dit algemeen scriptbestand wordt gewoonlijk door'
    echo "script getscripts (gs) gedownload en in '/tmp' geplaatst."
    echo "Is 'cd /tmp; wget karelzimmer.nl/gs; bash gs' uitgevoerd?"
    echo 'Voor scripts zie http:/karelzimmer.nl, klik op Linux.'
    exit 1
    }

#---------------------------------------------------------------------------#
# Globale constanten                                                        #
#---------------------------------------------------------------------------#
readonly SCRIPT_NEEDS_SUDO=false        # Uitvoeren als standaardgebruiker
readonly FIRST_COPYRIGHT_YEAR=2011      # Eerste auteursrechtjaar

declare MOUNTDIR="/media/$USER"         # Koppelpunt vanaf Ubuntu 12.10
if [[ ! -d $MOUNTDIR ]]; then
    MOUNTDIR=/media                     # Koppelpunt voor  Ubuntu 12.10
fi
readonly MOUNTDIR                       # Koppelpunt verwisselbare media

readonly -A FROM=(
    [AFB]="/home/$USER/Afbeeldingen"
    [FOTO]="/home/$USER/Foto's"
    [MUZIEK]="/home/$USER/Muziek"
    [VIDEO]="/home/$USER/Video's"
    )                                   # Bronmappen

readonly -A TO=(
    [ADATA]="$MOUNTDIR/LaCie_1TB"
    [LACIE]="$MOUNTDIR/ADATA_320GB"
    [VERBATIM]="$MOUNTDIR/LaCie_160GB"
    )                                   # Doelmappen

#---------------------------------------------------------------------------#
# Globale variabelen                                                        #
#---------------------------------------------------------------------------#

#############################################################################
# Functies (op volgorde van uitvoering)                                     #
#############################################################################

#-Functie-------------------------------------------------------------------#
# Naam: toon_hulp                                                           #
# Doel: Uitleg werking script.                                              #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function toon_hulp {
    toon_gebruik "$SCRIPT_NEEDS_SUDO" "$OPTION_USAGE"
    cat << HULP

Beschrijving:
    Script voor het kopiëren van lokale mappen naar externe harde schijven.

    Dit script kopieert mappen naar externe harde schijven.
    De namen van mappen en harde schijven staan "hard-coded" in dit script.

    Gebruik eventueel script ssync om de inhoud van externe harde schijven
    te kopiëren naar een netwerk harde schijf, NAS.

$OPTIONS_HELP_SC
HULP
}

#-Functie-------------------------------------------------------------------#
# Naam: controleer_invoer                                                   #
# Doel: Initiële controles en/of acties.                                    #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function controleer_invoer {
    : # no-op
}

#-Functie-------------------------------------------------------------------#
# Naam: toon_invoer                                                         #
# Doel: Toon wat het script gaat doen.                                      #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function toon_invoer {
    local from
    local msg
    local to

    clear
    log     "$DASHES"
    normal  "$HEADER"
    normal
    msg='Sync van:  '
    for from in "${!FROM[@]}"; do
        normal "$msg${FROM[$from]}"
        msg='           '
    done
    msg='Sync naar: '
    for to in "${!TO[@]}"; do
        normal "$msg${TO[$to]}"
        msg='           '
    done
    normal  "Logboek:   $LOG"
    log     "$DASHES"
    normal
}

#-Functie-------------------------------------------------------------------#
# Naam: kopieer_naar_aangekoppelde_schijven                                 #
# Doel: Kopieer naar aangekoppelde harde schijven.                          #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function kopieer_naar_aangekoppelde_schijven {
    local       from
    local -i    rsync_rc
    local -i    rsync_totrc
    local       to

    for to in "${!TO[@]}"; do
        if [[ -d ${TO[$to]} ]]; then
            normal  "Sync naar ${TO[$to]} ..."
            rsync_rc=0
            rsync_totrc=0

            spinner 'aan'

            #---------------------------------------------------------------#
            # Voor het kopiëren naar externe HDD wordt rsync gebruikt.      #
            #---------------------------------------------------------------#
            for from in "${!FROM[@]}"; do
                if [[ -d ${FROM[$from]} ]]; then
                    normal  "  Sync van ${FROM[$from]} ..."
                    rsync   --archive           \
                            --verbose           \
                            "${FROM[$from]}"    \
                            "${TO[$to]}"        \
                            &>> "$LOG"
                    rsync_rc=$?
                    rsync_totrc=$(( rsync_totrc + rsync_rc ))
                else
                    warning "  Sync van ${FROM[$from]} sla ik over, want \
niet aanwezig."
                fi
            done

            spinner 'uit'

            verwerk_rc "$PROGNAME: $FUNCNAME[$LINENO]: syncronisatie" \
                        $rsync_totrc 0 'noabend' MAXRC
        else
            warning "Sync naar ${TO[$to]} overgeslagen, want niet \
aangekoppeld."
        fi
    done
}

#-Functie-------------------------------------------------------------------#
# Naam: toon_afsluiten                                                      #
# Doel: Afsluitende meldingen en/of acties.                                 #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function toon_afsluiten {
    normal
    warning "Koppel zelf de schijven af en schakel deze uit en/of verwijder \
deze."
    normal
    normal 'Bewaar de gesynchroniseerde gegevens ook op een andere'
    normal 'veilige plek, zoals een externe (netwerk)schijf.'
    normal 'Gebruik eventueel script ssync hiervoor.'
}

#############################################################################
# Hoofdlijn                                                                 #
#############################################################################
# init_script
{
    verwerk_invoer "$@"
    controleer_gebruiker "$SCRIPT_NEEDS_SUDO"
    controleer_invoer
}
# verwerk
{
    bepaal_log "$SCRIPT_NEEDS_SUDO" LOGDIR "$LOGFILE" LOG
    toon_invoer
    toon_gestart
    kopieer_naar_aangekoppelde_schijven
    toon_gestopt
}
# afsl_script
{
    toon_afsluiten
    toon_afsluiten_sc
    exit $MAXRC
}

# Einde script.
