# shellcheck shell=bash
# ##############################################################################
# Bestand:  common.sh
# Doel:     Algemene variabelen en functies voor bash scripts
# Gebruik:  source common.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Kopieer dit bestand ("library file") in een script ("include").
# Dit om te voldoen aan de zogenaamde "SPOT rule" (Single Point of Truth regel):
# alle scripts gebruiken dezelfde gemeenschappelijke variabelen en functies.
# ------------------------------------------------------------------------------
# Auteursrecht (c) 2009-2020 Karel Zimmer.
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
# ------------------------------------------------------------------------------
# Toelichting versienummering:
#         VV.RR.MM  Versie.Release.Modificatie
#         ==.==.==  Alleen commentaar of spatiering gewijzigd
#         ==.==.+1  Kleine niet-functionele wijziging (patch)
#         ==.+1.00  Kleine (zichtbare) functionele wijziging (minor)
#         +1.00.00  Nieuwe functionaliteit (major)
# ##############################################################################
# REL_NUM=25.09.02
# REL_DAT=2020-01-01
# REL_MSG='Terminalattributen aangepast'

# ##############################################################################
# Instellingen
# ##############################################################################

# ------------------------------------------------------------------------------
# Algemene globale constanten
# ------------------------------------------------------------------------------
declare -ir SUCCESS=0
declare -ir ERROR=1
declare -ir WARNING=2
readonly CALLED="$0 $*"
readonly DASHES=$(printf '%.0s-' {1..80})
readonly PROGDIR=$(dirname "$0")
readonly PROGNAME=$(basename "$0")

# Terminalattributen ('man terminfo'). Gebruik ${<variabele_naam>}.
readonly BLINK=$(tput blink)
readonly BOLD=$(tput bold)
readonly BLUE=${BOLD}$(tput setaf 4)
readonly CLEAR_SCREEN="$(tput clear)"
readonly CURSOR_INVISABLE="$(tput civis)"
readonly CURSOR_VISABLE="$(tput cvvis)"
readonly ERASE_LINE="$(tput el)\c"
readonly GREEN=${BOLD}$(tput setaf 2)
readonly NORMAL=$(tput sgr0)
readonly RED=${BOLD}$(tput setaf 1)
readonly UP_ONE_LINE=$(tput cuu1)
readonly YELLOW=${BOLD}$(tput setaf 3)

readonly OPTIONS_SHORT_COMMON='dghuv'
readonly OPTIONS_LONG_COMMON='debug,gui,help,usage,version,zz-tab-compl'
readonly OPTIONS_TAB_COMPLETION_COMMON='--debug --gui --help --usage --version'
readonly OPTIONS_USAGE_COMMON="[-d|--debug] [-g|--gui] [-h|--help] \
[-u|--usage] [-v|--version] [--]"
readonly OPTIONS_HELP_COMMON="  -d --debug          Geef \
foutopsporingsinformatie weer in het logboek
  -g --gui            Start indien mogelijk in grafische modus
  -h --help           Deze hulptekst tonen en stoppen
  -u --usage          Een korte gebruikssamenvatting tonen en stoppen
  -v --version        De versie tonen en stoppen
  --                  Stop verwerken opdrachtregelopties"
readonly OPTIONS_LONG_SHORT="Lange opties kunnen worden afgekort, zolang de \
afkorting uniek blijft."
readonly ARGUMENT_LONG_SHORT="Een argument dat verplicht of optioneel is voor \
een lange optie, is dat ook voor de overeenkomstige korte optie."

# ------------------------------------------------------------------------------
# Algemene globale variabelen
# ------------------------------------------------------------------------------
declare CHKLOGCMD=''
declare CHKLOGRPT=''
declare HELPLINE=''
declare LESS_OPTIONS=''
declare LOGCMD=''
declare MANLINE=''
declare OPTION_DEBUG=false
declare OPTION_GUI=false
declare QUIET=false
declare RUN_AS_SUPERUSER=false
declare TO_DELETE=''

# ##############################################################################
# Algemene functies
# ##############################################################################
controleer_gebruiker() {
    if $RUN_AS_SUPERUSER; then
        if [[ $UID -ne 0 ]]; then
            toon_tekst "Uitvoeren met 'sudo' of als root."
            quiet; exit $ERROR
        fi
    else
        if [[ $UID -eq 0 ]]; then
            toon_tekst "Niet uitvoeren met 'sudo' of als root."
            quiet; exit $ERROR
        fi
    fi
}

init_script() {
    if command -v systemd &> /dev/null; then
        LOGCMD="systemd-cat --identifier=$PROGNAME --priority=info"
        CHKLOGCMD="journalctl -ab -t$PROGNAME \
-S'$(date '+%Y-%m-%d %H:%M:%S')'"
    else
        LOGCMD="logger --tag $PROGNAME --priority info"
        CHKLOGCMD="grep $PROGNAME /var/log/syslog"
    fi

    log_tekst ">>>>> started as $CALLED from $PWD"

    # Script-hardening
    set -o errexit
    set -o errtrace
    set -o nounset
    set -o pipefail
    # bash 5.0: trap exit: ${FUNCNAME[0]}: ongebonden variabele
    trap 'signal ${FUNCNAME:--} $LINENO "$BASH_COMMAND" $? ERR'     ERR
    trap 'signal ${FUNCNAME:--} $LINENO "$BASH_COMMAND" $? EXIT'    EXIT
    trap 'signal ${FUNCNAME:--} $LINENO "$BASH_COMMAND" $? INT'     SIGINT
    trap 'signal ${FUNCNAME:--} $LINENO "$BASH_COMMAND" $? TERM'    SIGTERM
    trap 'signal ${FUNCNAME:--} $LINENO "$BASH_COMMAND" $? HUP'     SIGHUP

    # Less-opties, overgenomen (en aangepast, zie 'man less', zoek PROMPTS) van:
    # 1. systemctl en journalctl, zie bijv. 'man systemctl', zoek LESS, en
    # 2. man, zie 'mam man', zoek LESS
    LESS_OPTIONS="--LONG-PROMPT --no-init --quit-if-one-screen --quit-on-intr \
--RAW-CONTROL-CHARS --prompt=M Tekst uitvoer $PROGNAME ?ltregel %lt?L/%L.:byte \
%bB?s/%s..? .?e (EINDE) :?pB %pB\%. .(druk h voor hulp of q voor stoppen)"
    HELPLINE="Typ '$PROGNAME --help' voor meer informatie."
    MANLINE="Typ 'man $PROGNAME' voor meer informatie."
}

log_tekst() {
    echo -e "$@" |& $LOGCMD
}

quiet() {
    # Geen exit-meldingen. Gebruik: quiet; exit ...
    QUIET=true
}

signal() {
    local funcname=${1:-funcname?}
    local -i lineno=${2:-0}
    local cmd=${3:-cmd?}
    local -i rc=${4:-1}
    local signal=${5:-signal?}
    local logtxt=''

    printf -v logtxt "##### functie[20] %-20.20s: regel %4d: foutcode %3d \
(%s/%-4.4s): opdracht %-s" \
"$funcname" "$lineno" "$rc" "${FUNCNAME[0]}" "$signal" "$cmd"

    case $signal in
        ERR)
            verwerk_error
            ;;
        EXIT)
            verwerk_exit
            ;;
        SIG*)
            verwerk_signal
            ;;
    esac
}

start_debugsessie() {
    toon_waarschuwingstekst '###### START DEBUG-SESSIE ######'
    log_tekst "====> START DEBUG-SESSIE"
    log_tekst "***** Start Huidige Omgeving Tonen *****"
    log_tekst "uname --all:\n$(uname --all)"
    log_tekst "lsb_release --all:\n$(lsb_release --all)"
    log_tekst "cat /etc/os-release:\n$(cat /etc/os-release)"
    log_tekst "***** Einde Huidige Omgeving Tonen *****"

    log_tekst '##### route bash xtrace to FD4...'
    exec 4> >($LOGCMD)
    BASH_XTRACEFD=4
    log_tekst '##### set bash options...'
    set -o verbose xtrace

    log_tekst '##### let the fun begin:'
    # shellcheck disable=SC2016
    ps4='+(${BASH_SOURCE}:${LINENO}): ${FUNCNAME[0]:+${FUNCNAME[0]}(): }'
    export PS4=$ps4
    unset ps4

    OPTION_DEBUG=true
}

stop_debugsessie() {
    set +o verbose
    set +o xtrace

    BASH_XTRACEFD=''
    exec 4>&-

    toon_waarschuwingstekst '###### EINDE DEBUG-SESSIE ######'
    log_tekst "<==== EINDE DEBUG-SESSIE"
    toon_tekst "Controleer de log met opdracht: ${BLUE}$CHKLOGCMD${NORMAL}"
}

toon_fouttekst() {
    local text=${1:-tekst?}

    if $OPTION_GUI; then
        local temp_text_file=''
        temp_text_file=$(mktemp -t "$PROGNAME-XXXXXXXXXX.txt")
        echo -e "$text" > "$temp_text_file"
        verwijder_stuurtekens "$temp_text_file"
        if ! zenity --error                             \
                    --width=400                         \
                    --height=100                        \
                    --title="$PROGNAME"                 \
                    --text="$(cat "$temp_text_file")"   \
                    2> /dev/null; then
            true
        fi
        rm "$temp_text_file"
    else
        printf "${RED}%b${NORMAL}\n" "$text"
    fi
}

toon_gebruik() {
    if $OPTION_GUI; then
        local title="$PROGNAME usage"
        local temp_text_file=''
        temp_text_file=$(mktemp -t "$PROGNAME-XXXXXXXXXX.txt")
        echo -e "$USAGE" > "$temp_text_file"
        if ! zenity --text-info                     \
                    --width=700                     \
                    --height=240                    \
                    --title="$title"                \
                    --filename="$temp_text_file"    \
                    --font='Ubuntu Mono 12'         \
                    2> /dev/null; then
            true
        fi
        rm "$temp_text_file"
    else
        if [[ $PROGNAME = 's' ]]; then
            echo -e "$USAGE" | less "$LESS_OPTIONS"
        else
            echo -e "$USAGE\n\n$HELPLINE" | less "$LESS_OPTIONS"
        fi
    fi

    quiet; exit $SUCCESS
}

toon_hulp() {
    if $OPTION_GUI; then
        local title="$PROGNAME help"
        local temp_text_file=''
        temp_text_file=$(mktemp -t "$PROGNAME-XXXXXXXXXX.txt")
        echo -e "$HELP" > "$temp_text_file"
        if ! zenity --text-info                     \
                    --width=660                     \
                    --height=400                    \
                    --title="$title"                \
                    --filename="$temp_text_file"    \
                    --font='Ubuntu Mono 12'         \
                    2> /dev/null; then
            true
        fi
        rm "$temp_text_file"
    else
        if [[ $PROGNAME = 's' ]]; then
            echo -e "$HELP" | less "$LESS_OPTIONS"
        else
            echo -e "$HELP" "\n\n$MANLINE" | less "$LESS_OPTIONS"
        fi
    fi

    quiet; exit $SUCCESS
}

toon_succestekst() {
    local text=${1:-tekst?}

    if $OPTION_GUI; then
        local temp_text_file=''
        temp_text_file=$(mktemp -t "$PROGNAME-XXXXXXXXXX.txt")
        local timeout=5
        text="$text\n\n\nTimeout $timeout seconden..."
        echo -e "$text" > "$temp_text_file"
        verwijder_stuurtekens "$temp_text_file"
        if ! zenity --info                              \
                    --width=400                         \
                    --height=100                        \
                    --timeout=$timeout                  \
                    --title="$PROGNAME"                 \
                    --text="$(cat "$temp_text_file")"   \
                    2> /dev/null; then
            true
        fi
        rm "$temp_text_file"
    else
        printf "${GREEN}%b${NORMAL}\n" "$text"
    fi
}

toon_tekst() {
    local text=${1-tekst?}

    if $OPTION_GUI; then
        local temp_text_file=''
        temp_text_file=$(mktemp -t "$PROGNAME-XXXXXXXXXX.txt")
        local timeout=5
        text="$text\n\n\nTimeout $timeout seconden..."
        echo -e "$text" > "$temp_text_file"
        verwijder_stuurtekens "$temp_text_file"
        if ! zenity --info                              \
                    --width=400                         \
                    --height=100                        \
                    --timeout="$timeout"                \
                    --title="$PROGNAME"                 \
                    --text="$(cat "$temp_text_file")"   \
                    2> /dev/null; then
            true
        fi
        rm "$temp_text_file"
    else
        printf '%b\n' "$text"
    fi
}

toon_versie() {
    local author="Geschreven door Karel Zimmer, https://karelzimmer.nl, \
info@karelzimmer.nl."
    local copyright_years=1971

    if ! copyright_years=$(grep --regexp='^# Auteursrecht ' \
"$PROGDIR/$PROGNAME" | awk '{print $4;exit}'); then
        copyright_years=$(date +%Y)
    fi
    local copyright="Auteursrecht © $copyright_years Karel Zimmer.
Dit is vrije software: u mag het vrijelijk wijzigen en verder verspreiden.
De precieze licentie is GPL-3+: GNU General Public License versie 3 of later.
Zie http://gnu.org/licenses/gpl.html voor de volledige (Engelse) tekst.
Deze software kent GEEN GARANTIE, voor zover de wet dit toestaat."

    if $OPTION_GUI; then
        local title="$PROGNAME version"
        local temp_text_file=''
        temp_text_file=$(mktemp -t "$PROGNAME-XXXXXXXXXX.txt")
        echo "$PROGNAME $REL_NUM ($REL_DAT)
$copyright

$author"  > "$temp_text_file"
        if ! zenity --text-info                     \
                    --width=650                     \
                    --height=250                    \
                    --title="$title"                \
                    --filename="$temp_text_file"    \
                    --font='Ubuntu Mono 12'         \
                    2> /dev/null; then
            true
        fi
        rm "$temp_text_file"
    else
        echo "$PROGNAME $REL_NUM
$copyright

$author" | less "$LESS_OPTIONS"
    fi

    quiet; exit $SUCCESS
}

toon_waarschuwingstekst() {
    local text=${1:-tekst?}

    if $OPTION_GUI; then
        local temp_text_file=''
        temp_text_file=$(mktemp -t "$PROGNAME-XXXXXXXXXX.txt")
        echo -e "$text" > "$temp_text_file"
        verwijder_stuurtekens "$temp_text_file"
        if ! zenity --warning                           \
                    --width=400                         \
                    --height=100                        \
                    --title="$PROGNAME"                 \
                    --text="$(cat "$temp_text_file")"   \
                    2> /dev/null; then
            true
        fi
        rm "$temp_text_file"
    else
        printf "${YELLOW}%b${NORMAL}\n" "$text" >&2
    fi
}

verwerk_algemene_opties() {
    while true; do
        case $1 in
            -d|--debug)
                start_debugsessie
                shift
                ;;
            -g|--gui)
                if ! command -v zenity &> /dev/null; then
                    log_tekst 'Programma zenity ontbreekt; optie gui genegeerd.'
                else
                    OPTION_GUI=true
                fi
                shift
                ;;
            -h|--help)
                toon_hulp
                ;;
            -u|--usage)
                toon_gebruik
                ;;
            -v|--version)
                toon_versie
                ;;
            --zz-tab-compl)
                # Verborgen optie.
                printf '%s' "$OPTIONS_TAB_COMPLETION"
                quiet; exit $SUCCESS
                ;;
            --)
                return 0
                ;;
            *)
                shift
                ;;
        esac
    done
}

verwerk_error() {
    log_tekst "$logtxt"
    # Systeemvariabele $- bevat alle huidige shell-opties.
    # Shell-optie errexit (exit onmiddelijk als een opdracht eindigt met een
    # niet-nul afsluitwaarde) wordt aangezet met 'set -e' of 'set -o errexit'.
    # Als shell-optie errexit is aangezet, bevat $- een e, en in dat geval
    # gelijk exit.  Als shell-optie errexit, met reden want standaard aan, is
    # uitgezet, geef dan alleen de afsluitwaarde terug.
    if [[ $- == *e* ]]; then
        exit "$rc"
    else
        return "$rc"
    fi
}

verwerk_exit() {
    verwerk_exit_meldingen

    if $OPTION_DEBUG; then
        stop_debugsessie
    fi

    if [[ $rc -ne 0 ]]; then
        log_tekst "$logtxt"
    fi

    log_tekst "<<<<< ended with rc=$rc"
    trap - ERR EXIT SIGINT SIGTERM SIGHUP
    exit "$rc"
}

verwerk_exit_meldingen() {
    if $QUIET; then
        return 0
    fi

    if [[ $rc -ne 0 ]]; then
        printf "${BOLD}%s\n${NORMAL}%s${BLUE}%s${NORMAL}\n%s\n" \
"Controleer de meldingen hierboven en hieronder." \
"Controleer de log met opdracht: " "$CHKLOGCMD" \
"Start indien gewenst $PROGNAME opnieuw met 'bash -vx $CALLED'."
        if $OPTION_GUI; then
            CHKLOGRPT=$(mktemp -t "$PROGNAME-XXXXXXXXXX.log")
            {
                echo "$DASHES"
                eval "$CHKLOGCMD"
                echo "$DASHES"
            }   >> "$CHKLOGRPT"
            if [[ $PROGNAME = 'instal' ]]; then
                echo "$APT_REPAIR" >> "$CHKLOGRPT"
            fi
            verwijder_stuurtekens "$CHKLOGRPT"
            if ! zenity --text-info                     \
                        --width=1300                    \
                        --height=600                    \
                        --title="$PROGNAME lograpport"  \
                        --filename="$CHKLOGRPT"         \
                        --font='Ubuntu Mono 12'         \
                        2> /dev/null; then
                true
            fi
            rm "$CHKLOGRPT"
        else
            printf '%s\n' "$DASHES"
            eval "$CHKLOGCMD --no-pager"
            printf '%s\n' "$DASHES"
            if [[ $PROGNAME = 'instal' ]]; then
                printf '%s\n' "$APT_REPAIR"
            fi
        fi

        case $rc in
            $SUCCESS)
                toon_succestekst "Opdracht $PROGNAME is succesvol uitgevoerd."
                ;;
            $WARNING)
                toon_waarschuwingstekst "Opdracht $PROGNAME is gestopt met een \
waarschuwing."
                ;;
            *)
                toon_fouttekst "Opdracht $PROGNAME is afgebroken."
                ;;
        esac
    fi
}

verwerk_signal() {
    case $PROGNAME in
        backup)
            if [[ $TO_DELETE ]]; then
                toon_tekst 'Opgeslagen back-up verwijderen...'
                rm "$TO_DELETE" |& $LOGCMD
                toon_tekst 'Opgeslagen back-up is verwijderd.'
            fi
            ;;
    esac
    log_tekst "$logtxt"
    exit $ERROR
}

verwijder_stuurtekens() {
    local file=${1:-file?}

    sed --in-place --expression='s/[^[:print:]]//g' "$file" # Non-printables
    sed --in-place --expression='s/\[1m//g'         "$file" # Bold
    sed --in-place --expression='s/(B\[m//g'        "$file" # Normal
    sed --in-place --expression='s/\[31m//g'        "$file" # Red
    sed --in-place --expression='s/\[32m//g'        "$file" # Green
    sed --in-place --expression='s/\[33m//g'        "$file" # Yellow
    sed --in-place --expression='s/\[34m//g'        "$file" # Blue
    sed --in-place --expression='s/\[4m//g'         "$file" # Underlined
}

# Einde script
