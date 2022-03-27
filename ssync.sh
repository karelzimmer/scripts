#!/bin/bash
#############################################################################
# Bestand:  ssync.sh                                                        #
# Doel:     Script voor het kopiëren van externe harde schijven naar een    #
#           NAS.                                                            #
# Gebruik:  ./ssync.sh [opties]                                             #
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
# Versies:  1.0.0   2011-05-18  Eerste versie.                              #
#############################################################################
readonly VERSION_NUMBER=1.11.0
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

readonly SMB=smb://mybooklive           # Server Message Block servernaam
                                        # (CIFS)
readonly NASSHR1="$SMB/backups"         # NAS share #1
readonly NASSHR2="$SMB/public"          # NAS share #2

declare GVFS="$HOME/.gvfs"              # Koppelpunt voor  Ubuntu 12.10
if [[ -d $GVFS ]]; then
    readonly NASMNT1="$GVFS/backups op mybooklive"
                                        # NAS koppelpunt #1
    readonly NASMNT2="$GVFS/public op mybooklive"
                                        # NAS koppelpunt #2
else
    GVFS="/run/user/$USER/gvfs"         # Koppelpunt vanaf Ubuntu 12.10
    readonly NASMNT1="$GVFS/smb-share:server=mybooklive,share=backups"
                                        # NAS koppelpunt #1
    readonly NASMNT2="$GVFS/smb-share:server=mybooklive,share=public"
                                        # NAS koppelpunt #2
fi
readonly GVFS                           # GNOME virtual filesystem koppelpunt

readonly HDDVOL1=LaCie_1TB              # HDD volumenamen
readonly HDDVOL2=ADATA_320GB
readonly HDDVOL3=LaCie_160GB

readonly HDDMNT1="$MOUNTDIR/$HDDVOL1"   # HDD koppelpunten
readonly HDDMNT2="$MOUNTDIR/$HDDVOL2"
readonly HDDMNT3="$MOUNTDIR/$HDDVOL3"

readonly -a FROM1=(
    [1]="$HDDMNT1/Backups"
        "$HDDMNT2/Backups"
        "$HDDMNT3/Backups"
    )                                   # Bronmappen #1

readonly TO1="$NASMNT1"                 # Doelmap #1

readonly -a FROM2=(
    [1]="$HDDMNT1/Afbeeldingen"
        "$HDDMNT1/Foto's"
        "$HDDMNT1/Muziek"
        "$HDDMNT1/Video's"
        "$HDDMNT2/Afbeeldingen"
        "$HDDMNT2/Foto's"
        "$HDDMNT2/Muziek"
        "$HDDMNT2/Video's"
        "$HDDMNT3/Afbeeldingen"
        "$HDDMNT3/Foto's"
        "$HDDMNT3/Muziek"
        "$HDDMNT3/Video's"
    )                                   # Bronmappen #2

readonly TO2="$NASMNT2"                 # Doelmap #2

readonly E_MOUNT_NAS_FAILED=64          # Foutcode

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
    Script voor het kopiëren van externe harde schijven naar een NAS.

    Dit script kopieert de inhoud van externe harde schijven naar een NAS.
    Bijvoorbeeld de inhoud gemaakt door script sync.
    De namen van de harde schijven staan "hard-coded" in dit script.

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
    local -i    fromnum
    local       msg

    clear
    log     "$DASHES"
    normal  "$HEADER"
    normal

    msg='Sync van:  '
    for (( fromnum=1; fromnum<=${#FROM1[*]}; fromnum++ )); do
        normal "${msg}1 <- ${FROM1[$fromnum]}"
        msg='           '
    done

    for (( fromnum=1; fromnum<=${#FROM2[*]}; fromnum++ )); do
        normal "${msg}2 <- ${FROM2[$fromnum]}"
        msg='           '
    done

    normal  "Sync naar: 1 -> $TO1"
    normal  "           2 -> $TO2"
    normal  "Logboek:   $LOG"
    log     "$DASHES"
    normal
}

#-Functie-------------------------------------------------------------------#
# Naam: koppel_schijven_aan                                                 #
# Doel: Koppel partities netwerkschijven aan.                               #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function koppel_schijven_aan {
    gvfs-mount  "$NASSHR1"  &>> "$LOG"
    cd          "$NASMNT1"  &>> "$LOG"  # "Activeer"
    if [[ ! -e $NASMNT1 ]]; then
        error "Aankoppelen NAS mislukt, $NASSHR1 -> $NASMNT1."
        exit $E_MOUNT_NAS_FAILED
    fi

    gvfs-mount  "$NASSHR2"  &>> "$LOG"
    cd          "$NASMNT2"  &>> "$LOG"  # "Activeer"
    if [[ ! -e $NASMNT2 ]]; then
        error "Aankoppelen NAS mislukt, $NASSHR2 -> $NASMNT2."
        exit $E_MOUNT_NAS_FAILED
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: kopieer_naar_doelmap_1                                              #
# Doel: Kopieer naar map 1.                                                 #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function kopieer_naar_doelmap_1 {
    local -i    fromnum
    local -i    rsync_rc=0
    local -i    rsync_totrc=0

    if [[ -d $TO1 ]]; then

        spinner 'aan'

        #-------------------------------------------------------------------#
        # Voor het kopiëren naar NAS wordt rsync gebruikt.                  #
        #-------------------------------------------------------------------#
        for (( fromnum=1; fromnum<=${#FROM1[*]}; fromnum++ )); do
            if [[ -d ${FROM1[$fromnum]} ]]; then
                normal "Sync van ${FROM1[$fromnum]} naar $TO1 ..."
                rsync   --archive               \
                        --verbose               \
                        "${FROM1[$fromnum]}"    \
                        "$TO1"                  \
                        &>> "$LOG"
                rsync_rc=$?
                rsync_totrc=$(( rsync_totrc + rsync_rc ))
            else
                warning "Sync van ${FROM1[$fromnum]} wordt overgeslagen, \
media is niet aangekoppeld."
            fi
        done

        spinner 'uit'

        verwerk_rc "$PROGNAME: $FUNCNAME[$LINENO]: sync naar doelmap1" \
                    $rsync_totrc 0 'noabend' MAXRC
    else
        error "Sync naar $TO1 wordt overgeslagen, want niet aangekoppeld."
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: kopieer_naar_doelmap_2                                              #
# Doel: Kopieer naar map 2.                                                 #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function kopieer_naar_doelmap_2 {
    local -i    fromnum
    local -i    rsync_rc=0
    local -i    rsync_totrc=0

    if [[ -d $TO2 ]]; then

        spinner 'aan'

        #-------------------------------------------------------------------#
        # Voor het kopiëren naar NAS wordt rsync gebruikt.                  #
        #-------------------------------------------------------------------#
        for (( fromnum=1; fromnum<=${#FROM2[*]}; fromnum++ )); do
            if [[ -d ${FROM2[$fromnum]} ]]; then
                normal "Sync van ${FROM2[$fromnum]} naar $TO2 ..."
                rsync   --archive               \
                        --verbose               \
                        "$TO2"                  \
                        &>> "$LOG"
                rsync_rc=$?
                rsync_totrc=$(( rsync_totrc + rsync_rc ))
            else
                warning "Sync van ${FROM2[$fromnum]} wordt overgeslagen, \
media is niet aangekoppeld."
                fi
        done

        spinner 'uit'

        verwerk_rc "$PROGNAME: $FUNCNAME[$LINENO]: sync naar doelmap2" \
                    $rsync_totrc 0 'noabend' MAXRC
    else
        error "Sync naar $TO2 wordt overgeslagen, want niet aangekoppeld."
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: koppel_schijven_af                                                  #
# Doel: Koppel partities netwerkschijven af.                                #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function koppel_schijven_af {
    normal 'Ontkoppel alle schijven en/of schakel deze uit...'

    gvfs-mount --unmount "$NASSHR1"
    gvfs-mount --unmount "$NASSHR2"

    if [[ -e $HDDMNT1 ]]; then
        umount "$HDDMNT1"
    fi

    if [[ -e $HDDMNT2 ]]; then
        umount "$HDDMNT2"
    fi

    success 'Alle schijven kunnen uitgeschakeld en/of verwijderd worden.'

}

#-Functie-------------------------------------------------------------------#
# Naam: toon_afsluiten                                                      #
# Doel: Afsluitende meldingen en/of acties.                                 #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function toon_afsluiten {
    : # no-op
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
    koppel_schijven_aan
    kopieer_naar_doelmap_1
    kopieer_naar_doelmap_2
    koppel_schijven_af
    toon_gestopt
}
# afsl_script
{
    toon_afsluiten
    toon_afsluiten_sc
    exit $MAXRC
}

# Einde script.
