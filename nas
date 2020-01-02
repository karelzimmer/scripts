#!/bin/bash
# shellcheck source=common.sh
# ##############################################################################
# Bestand:  nas
# Doel:     Koppel een NAS aan tijdens het opstarten
# Gebruik:  Met starter 'Start Hier', kies 'Menu Opdrachten' (aanbevolen)
#      of:  In het terminalvenster:
#           nas
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Auteursrecht (c) 2014-2020 Karel Zimmer.
#
# Dit programma is vrije software: u mag het herdistribueren en/of wijzigen
# onder de voorwaarden van de GNU Algemene Publieke Licentie zoals gepubliceerd
# door de Free Software Foundation, onder versie 3 van de Licentie of (naar uw
# keuze) elke latere versie.
#
# Dit programma is gedistribueerd in de hoop dat het nuttig zal zijn maar ZONDER
# ENIGE GARANTIE; zelfs zonder de impliciete garanties die GEBRUIKELIJK ZIJN IN
# DE HANDEL of voor BRUIKBAARHEID VOOR EEN SPECIFIEK DOEL.
# Zie de GNU Algemene Publieke Licentie voor meer details.
#
# U hoort een kopie van de GNU Algemene Publieke Licentie te hebben ontvangen
# samen met dit programma. Als dat niet het geval is, zie
# http://www.gnu.org/licenses/.
# ##############################################################################
readonly REL_NUM=11.01.13
readonly REL_DAT=2019-12-11
readonly REL_MSG='Beschrijving opties aangepast'

# ##############################################################################
# Instellingen
# ##############################################################################
source "$(dirname "$0")"/common.sh

# ------------------------------------------------------------------------------
# Globale constanten
# ------------------------------------------------------------------------------
readonly NAS_LOGIN=/root/.${PROGNAME}login
readonly NAS_MOUNT_POINT=/mnt/$PROGNAME
readonly NAS_FIXED_IP_ADDRESS="Zorg dat de NAS een vast IP-adres heeft.  \
Hiervoor is nodig:

 -  het MAC-adres van de NAS (zoals $(
     ip -oneline link | awk '/ UP /{print $17}'
     ))
 -  toegang tot de NAS via een webbrowser
 -  toegang tot de router via een webbrowser

 1. Kies in de router met het MAC-adres van de NAS een
    IP-adres buiten het bereik van DHCP die automatisch
    de IP-adressen uitdeelt (vaak 192.168.0.200).
 2. Kies in de NAS het vaste IP-adres en zet DHCP uit."
readonly RUN_AS_SUPERUSER=true
readonly SYSTEMD_MOUNT_DIR=/etc/systemd/system
readonly SYSTEMD_MOUNT_FILE=mnt-$PROGNAME.mount
readonly SYSTEMD_MOUNT=$SYSTEMD_MOUNT_DIR/$SYSTEMD_MOUNT_FILE

readonly OPTIONS_SHORT=$OPTIONS_SHORT_COMMON
readonly OPTIONS_LONG=$OPTIONS_LONG_COMMON
readonly OPTIONS_TAB_COMPLETION=$OPTIONS_TAB_COMPLETION_COMMON
readonly USAGE="Gebruik: $PROGNAME
             $OPTIONS_USAGE_COMMON

$OPTIONS_LONG_SHORT"
readonly HELP="Gebruik: $PROGNAME [OPTIE...]

Koppel een NAS aan tijdens het opstarten.

Opties:
  $OPTIONS_LONG_SHORT

$OPTIONS_HELP_COMMON"

# ------------------------------------------------------------------------------
# Globale variabelen
# ------------------------------------------------------------------------------
declare NAS_GEBRUIKERSNAAM=${SUDO_USER:-$USER}
declare NAS_IP_ADRES=192.168.0.200
declare NAS_SHARENAAM=${SUDO_USER:-$USER}
declare NAS_WACHTWOORD='geheim'

# ##############################################################################
# Functies
# ##############################################################################
controleer_invoer() {
    local -i getopt_rc=0
    local parsed=''

    set +o errexit
    parsed=$(getopt --alternative                       \
                    --options       "$OPTIONS_SHORT"    \
                    --longoptions   "$OPTIONS_LONG"     \
                    --name          "$PROGNAME"         \
                    -- "$@")
    getopt_rc=$?
    set -o errexit
    if [[ $getopt_rc -ne 0 ]]; then
        printf '%s\n' "$HELPLINE" >&2
        quiet; exit $ERROR
    fi
    eval set -- "$parsed"
    verwerk_algemene_opties "$@"

    while true; do
        case $1 in
            --)
                shift
                break
                ;;
            *)
                shift
                ;;
        esac
    done

    if [[ "$*" ]]; then
        printf '%s\n%s\n' "Geen argumenten opgeven." "$HELPLINE" >&2
        quiet; exit $ERROR
    fi

    controleer_gebruiker
    vraag_invoer
}

vraag_invoer() {
    local fstab=''
    local quest1='Deze regels verwijderen?'
    local quest2="Heeft de NAS een vast IP-adres zoals $NAS_IP_ADRES?"
    local quest3='IP-adres van de NAS'
    local quest4='Gebruikersnaam op de NAS'
    local quest5='Wachtwoord van deze gebruiker op de NAS'
    local quest6='Share-naam van deze gebruiker op de NAS'
    local -i quest_rc=0
    local text='Beantwoord alstublieft de volgende vragen'
    local warning=''

    fstab=$(
        if !    grep    --regexp="$PROGNAME" \
                        /etc/fstab; then
            echo
        fi
        )
    if [[ $fstab ]]; then
        warning="Onderstaande regels zijn al aanwezig in de koppeltabel:
$fstab"
        if $OPTION_GUI; then
            set +o errexit
            zenity  --question                      \
                    --width=400                     \
                    --height=100                    \
                    --title="$PROGNAME"             \
                    --text="$warning\n\n$quest1"    \
                    2> /dev/null
            quest_rc=$?
            set -o errexit
            if [[ $quest_rc -eq 0 ]]; then
                verwijder_regels
            fi
        else
            printf '%s\n' "$warning"
            read -rp "$quest1 (j/N) " </dev/tty
            while true; do
                case $REPLY in
                    j*|J*)
                        verwijder_regels
                        break
                        ;;
                    n*|N*|'')
                        toon_tekst 'Ok, we gaan verder.'
                        break
                        ;;
                    *)
                        echo -e "${UP_ONE_LINE}${ERASE_LINE}"
                        continue
                        ;;
                esac
            done
        fi
    fi

    if $OPTION_GUI; then
        set +o errexit
        if ! zenity --question          \
                    --width=400         \
                    --height=100        \
                    --title="$PROGNAME" \
                    --text="$quest2"    \
                    2> /dev/null; then
            zenity  --info                          \
                    --width=500                     \
                    --height=100                    \
                    --title="$PROGNAME"             \
                    --text="$NAS_FIXED_IP_ADDRESS"  \
                    2> /dev/null
            quiet; exit $SUCCESS
        fi
        set -o errexit
    else
        while true; do
            read -rp "$quest2 (j/N) " </dev/tty
            case $REPLY in
                j*|J*)
                    toon_tekst 'Ok, we gaan verder.'
                    break
                    ;;
                n*|N*|'')
                    echo "$NAS_FIXED_IP_ADDRESS"
                    toon_tekst 'Gestopt.'
                    quiet; exit $SUCCESS
                    ;;
                *)
                    echo -e "${UP_ONE_LINE}${ERASE_LINE}"
                    continue
                    ;;
            esac
        done
    fi

    if $OPTION_GUI; then
        set +o errexit
        REPLY=$(
            zenity  --forms                     \
                    --title="$PROGNAME"         \
                    --text="$text"              \
                    --separator=","             \
                    --add-entry="$quest3"       \
                    --add-entry="$quest4"       \
                    --add-password="$quest5"    \
                    --add-entry="$quest6"       \
                    2> /dev/null
	        )
        # shellcheck disable=SC2181
        if [[ $? -ne 0 ]]; then
            quiet; exit $SUCCESS
        fi
        set -o errexit
        NAS_IP_ADRES=$(echo "$REPLY"        | awk -F, '{print $1}')
        NAS_GEBRUIKERSNAAM=$(echo "$REPLY"  | awk -F, '{print $2}')
        NAS_WACHTWOORD=$(echo "$REPLY"      | awk -F, '{print $3}')
        NAS_SHARENAAM=$(echo "$REPLY"       | awk -F, '{print $4}')
    else
        printf '%s\n%s\n' "$text." \
"Als u niets opgeeft, wordt de waarde tussen [] gebruikt als antwoord."
        read -rp "
$quest3? [$NAS_IP_ADRES]: " </dev/tty
        if [[ $REPLY ]]; then
            NAS_IP_ADRES=$REPLY
        fi
        read -rp "
$quest4? [$NAS_GEBRUIKERSNAAM]: " </dev/tty
        if [[ $REPLY ]]; then
            NAS_GEBRUIKERSNAAM=$REPLY
        fi
        read -rsp "
$quest5? [$NAS_WACHTWOORD]: " </dev/tty
        if [[ $REPLY ]]; then
            NAS_WACHTWOORD=$REPLY
        fi
        printf '\n'
        read -rp "
$quest6? [$NAS_SHARENAAM]: " </dev/tty
        if [[ $REPLY ]]; then
            NAS_SHARENAAM=$REPLY
        fi
    fi
}

verwerk_invoer() {
    local text0='Opdrachten worden verwerkt...'
    local text1='Controleer afhankelijkheden...'
    local text2='Maak koppelpunt...'
    local text3='Maak NAS login...'
    local text4='Maak systemd...'
    local text5='Koppel NAS aan...'
    local wait_for_zenity_progress=1s

    if $OPTION_GUI; then
        (
        printf '%s\n' "#$text1"; sleep $wait_for_zenity_progress
        controleer_afhankelijkheden
        printf '%s\n' "#$text2"; sleep $wait_for_zenity_progress
        maak_koppelpunt
        printf '%s\n' "#$text3"; sleep $wait_for_zenity_progress
        maak_naslogin
        printf '%s\n' "#$text4"; sleep $wait_for_zenity_progress
        maak_systemd_mount_bestand
        printf '%s\n' "#$text5"; sleep $wait_for_zenity_progress
        koppel_nas_aan
        ) |&
        zenity  --progress          \
                --pulsate           \
                --auto-close        \
                --no-cancel         \
                --width=600         \
                --height=50         \
                --title="$PROGNAME" \
                --text="$text0"     \
                2> /dev/null
    else
        maak_koppelpunt
        maak_naslogin
        maak_systemd_mount_bestand
        koppel_nas_aan
    fi
}

maak_koppelpunt() {
    if [[ -d $NAS_MOUNT_POINT ]]; then
        return 0
    fi

    printf '%s\n' 'Maak NAS koppelpunt...'

    mkdir   "$NAS_MOUNT_POINT"  |& $LOGCMD
    chmod   '777'               \
            "$NAS_MOUNT_POINT"  |& $LOGCMD
}

maak_naslogin() {
    printf '%s\n' 'Maak NAS login...'

    echo "username=$NAS_GEBRUIKERSNAAM" > "$NAS_LOGIN"
    echo "password=$NAS_WACHTWOORD"     >> "$NAS_LOGIN"
    chmod   '600'           \
            "$NAS_LOGIN"    |& $LOGCMD
}

maak_systemd_mount_bestand() {
    printf '%s\n' 'Maak systemd mount-bestand...'

    echo "[Unit]
Description=Mount NAS Directory

[Mount]
What=//$NAS_IP_ADRES/$NAS_SHARENAAM
Where=/mnt/nas
Type=cifs
Options=credentials=$NAS_LOGIN,sec=ntlm,vers=1.0,rw,noperm,iocharset=utf8,\
dir_mode=0777,file_mode=0777

[Install]
WantedBy=multi-user.target" > "$SYSTEMD_MOUNT"
}

koppel_nas_aan() {
    printf '%s\n' 'Koppel NAS aan...'

    systemctl enable mnt-nas.mount      |& $LOGCMD
    if ! systemctl start mnt-nas.mount  |& $LOGCMD; then
        true
    fi
    systemctl daemon-reload             |& $LOGCMD
}

term_script() {
    if ! systemctl status mnt-nas.mount; then
        true
    fi
    toon_tekst "Het systemd mount-bestand is geactiveerd.
De NAS zou beschikbaar moetn zijn op '$NAS_MOUNT_POINT'.

De-activeer het systemd mount-besta2nd met de opdracht:
${BLUE}sudo systemctl disable mnt-nas.mount${NORMAL}"
    quiet; exit $SUCCESS
}

verwerk_script() {
    controleer_invoer "$@"
    verwerk_invoer
}

# ##############################################################################
# Hoofdlijn
# ##############################################################################
main() {
    init_script
    verwerk_script "$@"
    term_script
}


main "$@"

# Einde script
