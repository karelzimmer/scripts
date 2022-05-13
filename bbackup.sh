#!/bin/bash
#############################################################################
# Bestand:  bbackup.sh                                                      #
# Doel:     Script voor het maken van een back-up van een back-up.          #
# Gebruik:  [sudo] ./bbackup.sh [opties]                                    #
# Gebruikt: script-common.sh    (algemene variabelen en functies)           #
# Auteur:   Karel Zimmer (http://karelzimmer.nl, info@karelzimmer.nl)       #
# ------------------------------------------------------------------------- #
# Auteursrecht © 2010-2014 Karel Zimmer.                                    #
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
# Versies:  1.0.0   2010-08-02  Eerste versie.                              #
#           2.0.0   2010-08-27  Meer berichten naar de gebruiker.           #
#           3.0.0   2010-09-22  Meerdere back-uplocaties mogelijk.          #
#           4.0.0   2010-10-15  Meer generaties en betere toelichting.      #
#           5.0.0   2012-02-18  Schijven afkoppelen wanneer klaar.          #
#           6.0.0   2013-11-28  Controle op schijfruimte toegevoegd.        #
#           7.0.0   2014-10-05  Configuratiebestand en optie reset          #
#                               toegevoegd.                                 #
#           8.0.0   2014-10-23  Configuratiebestand en optie reset          #
#                               verwijderd, harddisks opzoeken en verwerken.#
#############################################################################
readonly VERSION_NUMBER=8.1.0
readonly RELEASE_DATE=2014-11-05

#############################################################################
# Instellingen.                                                             #
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
#------- ALGEMEEN -----------------------------------------------------------
readonly SCRIPT_NEEDS_SUDO=true         # Uitvoeren als beheerder
readonly FIRST_COPYRIGHT_YEAR=2010      # Eerste auteursrechtjaar

#------- FROM ---------------------------------------------------------------
readonly STORAGEDIR=/var/scripts/backup # Back-upbmap, bron. STORAGEDIR ivm
                                        # gebruik in backup en script-common.
readonly BACKUPFILE=backup*             # Back-upbestand
readonly LOGFILE_TO_COPY=$(ls $STORAGEDIR/$BACKUPFILE.log 2>> "$LOG")
readonly LOGFILE_TO_COPY_BASE=$(basename "$LOGFILE_TO_COPY")
                                        # Te kopiëren logboek
readonly TARFILE_TO_COPY=$(ls $STORAGEDIR/$BACKUPFILE.tar 2>> "$LOG")
readonly TARFILE_TO_COPY_BASE=$(basename "$TARFILE_TO_COPY")
                                        # Te kopiëren backup
readonly FILES_TO_COPY="$LOGFILE_TO_COPY $TARFILE_TO_COPY"
                                        # Te kopiëren bestanden
readonly NEED_BYTES=$(du    $FILES_TO_COPY  \
                            --summarize     \
                            --total         \
                            --apparent-size \
                            --block-size=1  \
                            2>> "$LOG"      |
                            tail --lines=1  |
                            awk '{print $1}')
                                        # Back-upgrootte in bytes
readonly NEED_HUMAN=$(du    $FILES_TO_COPY      \
                            --summarize         \
                            --total             \
                            --apparent-size     \
                            --human-readable    \
                            2>> "$LOG"          |
                            tail --lines=1      |
                            awk '{print $1}')
                                        # Back-upgrootte in leesbare vorm

#------- TO -----------------------------------------------------------------
readonly NUM_TO_FILES_OKE='0, 2, 4, 6, of 8'
                                        # Correct aantal BACKUPDIR bestanden
readonly NUM_TO_FILES_MAX=${NUM_TO_FILES_OKE:${#NUM_TO_FILES_OKE} - 1:1}
                                        # Maximum aantal BACKUPDIR bestanden
readonly NUM_GEN=$(( NUM_TO_FILES_MAX / 2 ))
                                        # Aantal bewaarde generaties
readonly -A HARDDISK_STATUS_TXT=(
    [PRESENT]='- aanwezig'
    [NO-BACKUPS-FOLDER]="- map 'Backups' niet aanwezig"
    [NO-COMPNAME-FOLDER]="- map '$COMPNAME' niet aanwezig"
    )                                   # Harddisk status-teksten

#------- FOUTCODES ----------------------------------------------------------
readonly E_STORAGEDIR_NOT_FOUND=64      # Foutcodes
readonly E_STORAGEDIR_NUMBER_OF_FILES_ERROR=65
readonly E_BACKUPDIR_NUMBER_OF_FILES_ERROR=66
readonly E_SIZES_ARE_DIFFERENT=67

#---------------------------------------------------------------------------#
# Globale variabelen                                                        #
#---------------------------------------------------------------------------#
declare BUPFILES_COPIED=0               # Aantal gekopieerde BUPFILEs
declare BUPFILES_DELETED=0              # Aantal verwijderde BUPFILEs
declare MAX_BACKUPDIR_LEN=0             # Maximale lengte string BACKUPDIR

declare DISKSPACE_OK=true               # Voldoende back-up ruimte
declare NO_HARDDISK_FOUND=true          # Geen enkele harddisk aangekoppeld
declare SOME_BACKUPDIR_NOT_FOUND=false  # Enkele BACKUPDIRs niet gevonden

#------ TO ------------------------------------------------------------------
declare -A HARDDISK                     # Harddisk koppelpunt/namen
declare -A HARDDISK_STATUS              # Harddisk status
declare -A BACKUPDIR                    # Back-upmappen, doel

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
    Script voor het maken van een back-up van een back-up.

    Dit script maakt een extra back-up van een eerder gemaakt back-up als
    deze lokaal is opgeslagen (standaard op $STORAGEDIR).
    Met andere woorden: kopieer een back-up, bijvoorbeeld gemaakt met script
    backup, naar een andere plek zoals een (externe) (netwerk)schijf.
    Er wordt gezocht naar aangekoppelde schijven op /media/ en /mnt/.
    Voorwaarden:
        - Bron dient 2 bestanden te bevatten, back-up en back-uplogboek.
        - Doel dient $NUM_TO_FILES_OKE bestanden te bevatten.
          Als het doel $NUM_TO_FILES_MAX bestanden bevat en er zijn bestanden
          te kopiëren, worden de oudste 2 bestanden verwijderd.
          Dit correspondeert met \
overgrootvader/grootvader/vader/zoon-strategie; $NUM_GEN generaties.

    Als de back-up van een back-up is uitgevoerd, worden de lokale back-up en
    logboek verwijderd.

    Indien nodig wordt het beheerderswachtwoord gevraagd.

$OPTIONS_HELP_SC
$PART_OF_INSTALL_HELPTEXT
HULP
}


#-Functie-------------------------------------------------------------------#
# Naam: controleer_invoer                                                   #
# Doel: Initiële controles en/of acties.                                    #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function controleer_invoer {
    local       harddisk
    local -i    num_from_files
    local -i    to_dir_len

    #-----------------------------------------------------------------------#
    # Controleer opslagmap.                                                 #
    #-----------------------------------------------------------------------#
    if [[ ! -d $STORAGEDIR ]]; then
        error   "Opslagmap $STORAGEDIR bestaat niet"
        normal  'Is script backup uitgevoerd?'
        warning "Voer dit script niet uit als de back-up extern is \
opgeslagen."
        exit $E_STORAGEDIR_NOT_FOUND
    fi

    #-----------------------------------------------------------------------#
    # Controleer aantal bestanden in opslagmap.                             #
    #-----------------------------------------------------------------------#
    num_from_files=$(ls "$STORAGEDIR"/$BACKUPFILE 2>> "$LOG" | wc --lines)
    if [[ $num_from_files -ne 2 ]]; then
        error   'Het aantal gevonden bestanden is niet 2.'
        warning 'Verwacht 2 bestanden, namelijk backup en logboek.'
        normal  "Het aantal gevonden bestanden is $num_from_files."
        normal  "Controleer de $BACKUPFILE bestanden in $STORAGEDIR."
        normal  'Is script backup (teveel) uitgevoerd?'
        exit $E_STORAGEDIR_NUMBER_OF_FILES_ERROR
    fi

    #-----------------------------------------------------------------------#
    # Vul associatief array met harddisknamen.                              #
    #-----------------------------------------------------------------------#
    while read record; do
        HARDDISK[$record]="$record"
    done < <(mount |
            grep    --regexp='/media/' \
                    --regexp='/mnt/'   |
            awk '{print $3}')
    readonly HARDDISK

    #-----------------------------------------------------------------------#
    # Verwerk aangekoppelde harddisks.                                      #
    #-----------------------------------------------------------------------#
    for harddisk in "${!HARDDISK[@]}"; do

        NO_HARDDISK_FOUND=false

        #-------------------------------------------------------------------#
        # Vul overig associatief array.                                     #
        #-------------------------------------------------------------------#
        BACKUPDIR[$harddisk]="${HARDDISK[$harddisk]}/Backups/$COMPNAME"

        #-------------------------------------------------------------------#
        # Bepaal grootste breedte voor melding.                             #
        #-------------------------------------------------------------------#
        to_dir_len=${#BACKUPDIR[$harddisk]}
        if [[ $to_dir_len -gt $MAX_BACKUPDIR_LEN ]]; then
            MAX_BACKUPDIR_LEN=$to_dir_len
        fi

        #-------------------------------------------------------------------#
        # Controleer of map 'Backups' aanwezig is.                          #
        #-------------------------------------------------------------------#
        if [[ ! -d ${HARDDISK[$harddisk]}/Backups ]]; then
            SOME_BACKUPDIR_NOT_FOUND=true
            HARDDISK_STATUS[$harddisk]=\
"${HARDDISK_STATUS_TXT[NO-BACKUPS-FOLDER]}"
            continue
        fi

        #-------------------------------------------------------------------#
        # Controleer of map '<computernaam>' aanwezig is.                   #
        #-------------------------------------------------------------------#
        if [[ ! -d ${BACKUPDIR[$harddisk]} ]]; then
            SOME_BACKUPDIR_NOT_FOUND=true
            HARDDISK_STATUS[$harddisk]=\
"${HARDDISK_STATUS_TXT[NO-COMPNAME-FOLDER]}"
            continue
        else
            HARDDISK_STATUS[$harddisk]="${HARDDISK_STATUS_TXT[PRESENT]}"
        fi

        #-------------------------------------------------------------------#
        # Controleer het aantal bestanden.                                  #
        #-------------------------------------------------------------------#
        controleer_aantal_bestanden
    done
}

#-Functie-------------------------------------------------------------------#
# Naam: controleer_aantal_bestanden                                         #
# Doel: Controles aantal back-up/logbestanden.                              #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function controleer_aantal_bestanden {
#   local harddisk is gedefinieerd in aanroepende functie
    local num_to_files=$(ls "${BACKUPDIR[$harddisk]}"/$BACKUPFILE   \
                            2>> "$LOG"                              |
                            wc --lines)

    if ! echo "$NUM_TO_FILES_OKE" | grep --quiet $num_to_files; then
        error   "Het aantal gevonden bestanden is niet $NUM_TO_FILES_OKE."
        normal  "Het aantal gevonden bestanden is $num_to_files."
        normal  "Controleer de $BACKUPFILE bestanden in"
        normal  "${BACKUPDIR[$harddisk]}."
        exit $E_BACKUPDIR_NUMBER_OF_FILES_ERROR
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: toon_invoer                                                         #
# Doel: Toon wat het script gaat doen.                                      #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function toon_invoer {
    local       filler
    local       msg
    local       harddisk
    local -i    to_dir_len

    clear
    log     "$DASHES"
    normal  "$HEADER"
    normal
    normal  'Back-up:     '$BACKUPFILE
    normal  "Van:         $STORAGEDIR"
    msg='Naar:        '
    for harddisk in "${!HARDDISK[@]}"; do

        #-------------------------------------------------------------------#
        # Filler voor uitlijnen back-upmap en doel aanwezig tekst.          #
        #-------------------------------------------------------------------#
        to_dir_len=${#BACKUPDIR[$harddisk]}
        filler=${SPACES:0:$MAX_BACKUPDIR_LEN-$to_dir_len+1}

        normal "$msg${BACKUPDIR[$harddisk]}$filler\
${HARDDISK_STATUS[$harddisk]}"
        msg='             '
    done
    normal  "Generaties:  $NUM_GEN"
    normal  'Snelheid:    ≈ 2,0 GB/min'
    normal  "Logboek:     $LOG"
    log     "$DASHES"
    normal
}

#-Functie-------------------------------------------------------------------#
# Naam: verwerk_backup_backup                                               #
# Doel: Bepaal wat er gekopieerd/verwijderd moet worden.                    #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function verwerk_backup_backup {
    local       bupfilecopy
    local       bupfiledelete
    local       filler
    local       harddisk
    local -i    to_dir_len

    for harddisk in "${!HARDDISK[@]}"; do

        #-------------------------------------------------------------------#
        # Filler voor uitlijnen back-upmap en doel aanwezig tekst.          #
        #-------------------------------------------------------------------#
        to_dir_len=${#BACKUPDIR[$harddisk]}
        filler=${SPACES:0:$MAX_BACKUPDIR_LEN-$to_dir_len+1}

        if [[ ${HARDDISK_STATUS[$harddisk]} = \
${HARDDISK_STATUS_TXT[PRESENT]} ]]; then
            normal "Verwerk..... \
${BACKUPDIR[$harddisk]}$filler${HARDDISK_STATUS[$harddisk]}"
            bupfilecopy=false
            controleer_kopieren_nodig
            if ! $bupfilecopy; then
                controleer_gekopieerde_bestanden
            fi

            bupfiledelete=false
            if $bupfilecopy; then
                controleer_verwijderen_nodig
            fi

            if $bupfilecopy && $bupfiledelete; then
                verwijder_bestanden
            fi

            if $bupfilecopy; then
                controleer_schijfruimte
                if $DISKSPACE_OK; then
                    kopieer_bestanden
                    controleer_gekopieerde_bestanden
                fi
            fi
        else
            normal "Sla over.... \
${BACKUPDIR[$harddisk]}$filler${HARDDISK_STATUS[$harddisk]}"
            normal ' Kan geen bestanden verwijderen.'
            normal ' Kan geen bestanden kopiëren.'
        fi
    done
}

#-Functie-------------------------------------------------------------------#
# Naam: controleer_kopieren_nodig                                           #
# Doel: Bepaal of er gekopieerd moet worden.                                #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function controleer_kopieren_nodig {
#   local bupfilecopy is gedefinieerd in aanroepende functie
#   local harddisk is gedefinieerd in aanroepende functie
    local first_fromfilename=$(ls "$STORAGEDIR"   \
                                2>> "$LOG"      |
                                head --lines=1)

    if [[ -f ${BACKUPDIR[$harddisk]}/$first_fromfilename ]]; then
        normal ' Geen bestanden te verwijderen.'
        normal " Bestanden zijn al gekopieerd ($(basename \
$first_fromfilename .log))."
    else
        bupfilecopy=true
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: controleer_gekopieerde_bestanden                                    #
# Doel: Controleer de gekopieerde bestanden op grootte.                     #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function controleer_gekopieerde_bestanden {
    local -i copied_bytes=\
$(du    ${BACKUPDIR[$harddisk]}/$TARFILE_TO_COPY_BASE   \
        ${BACKUPDIR[$harddisk]}/$LOGFILE_TO_COPY_BASE   \
        --summarize                                     \
        --total                                         \
        --apparent-size                                 \
        --block-size=1                                  \
        2>> "$LOG"                                      |
        tail --lines=1                                  |
        awk '{print $1}')

    if [[ copied_bytes -ne NEED_BYTES ]]; then
        error 'De gekopieerde backup is niet even groot als de back-up.'
        error 'Verwijder de gekopieerde back-up van de externe harddisk,'
        error "zie hierboven, en start $PROGNAME opnieuw."
        exit  $E_SIZES_ARE_DIFFERENT
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: controleer_verwijderen_nodig                                        #
# Doel: Bepaal of er verwijderd moet worden.                                #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function controleer_verwijderen_nodig {
#   local bupfiledelete is gedefinieerd in aanroepende functie
#   local harddisk is gedefinieerd in aanroepende functie
    local num_to_files=$(ls "${BACKUPDIR[$harddisk]}"/$BACKUPFILE  \
                        2>> "$LOG"                              |
                        wc --lines)

    if [[ $num_to_files -eq $NUM_TO_FILES_MAX ]]; then
        bupfiledelete=true
    else
        normal ' Geen bestanden te verwijderen.'
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: verwijder_bestanden                                                 #
# Doel: Verwijder oudste back-up en logboek.                                #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function verwijder_bestanden {
#   local harddisk is gedefinieerd in aanroepende functie
    local       file_to_delete
    local       file_to_delete_base
    local -i    rm_rc
    local       msg
    local       files_to_delete=$(ls "${BACKUPDIR[$harddisk]}"/$BACKUPFILE  \
                                    2>> "$LOG"                              |
                                    head --lines=2)

    normal ' Twee oudste bestanden worden nu verwijderd...'
    msg='  Verwijder. '
    for file_to_delete in $files_to_delete; do
        bepaal_bestandsgrootte "$file_to_delete" filesize
        file_to_delete_base="$(basename $file_to_delete)"

        #-------------------------------------------------------------------#
        # Filler voor uitlijnen te verwijderen back-up en grootte.          #
        #-------------------------------------------------------------------#
        file_to_delete_base_len=${#file_to_delete_base}
        filler=${SPACES:0:$file_to_delete_base_len-109}

        normal "$msg$file_to_delete_base$filler - ${filesize}B"
        msg='         en. '
    done

    spinner 'aan'

    TO_DELETE="$files_to_delete"    # Voor eventueel afbreken van het script
    rm  --verbose           \
        $files_to_delete    \
        &>> "$LOG"
    rm_rc=$?
    TO_DELETE=''
    verwerk_rc "$PROGNAME: $FUNCNAME[$LINENO]: verwijder bestanden" \
                $rm_rc 0 'abend' MAXRC

    spinner 'uit'

    (( BUPFILES_DELETED = BUPFILES_DELETED + 2 ))
}

#-Functie-------------------------------------------------------------------#
# Naam: controleer_schijfruimte                                             #
# Doel: Controleer of er voldoende schijfruimte beschikbaar is om een       #
#       back-up van een back-up op te slaan.                                #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function controleer_schijfruimte {
#   local harddisk is gedefinieerd in aanroepende functie

    spinner 'aan'

    local free_bytes=$(df "${BACKUPDIR[$harddisk]}" \
                        --block-size=1              |
                        tail --lines=1              |
                        awk '{print $4}')
    local free_human=$(df "${BACKUPDIR[$harddisk]}" \
                        --human-readable            |
                        tail --lines=1              |
                        awk '{print $4}')

    spinner 'uit'

    if [[ $NEED_BYTES -gt $free_bytes ]]
    then
        local filesys=$(df ${BACKUPDIR[$harddisk]}  |
                        tail --lines=1              |
                        awk '{print $1}')
        local mounted=$(df ${BACKUPDIR[$harddisk]}  |
                        tail --lines=1              |
                        awk '{print $6}')
        warning "  Te weinig schijfruimte op $mounted (bestandssysteem \
$filesys)"
        warning '  voor het kopiëren van de backup:'
        warning "  $TARFILE_TO_COPY_BASE en $LOGFILE_TO_COPY_BASE."
        normal  "  Benodigd is ${NEED_HUMAN}B, beschikbaar is ${free_human}B."
        normal  "  Maak ruimte vrij op $mounted (bestandssysteem $filesys),"
        normal  "  of gebruik een ander opslagmedium met minimaal \
${NEED_HUMAN}B beschikbaar,"
        normal  "  zoals een andere (externe) (netwerk)schijf, USB-stick, \
CD, of DVD."
        DISKSPACE_OK=false
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: kopieer_bestanden                                                   #
# Doel: Kopieer nieuwste back-up en logboek.                                #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function kopieer_bestanden {
#   local bupfiledelete is gedefinieerd in aanroepende functie
#   local harddisk is gedefinieerd in aanroepende functie
    local -i    cp_rc
    local       filesize
    local       file_to_copy
    local       file_to_copy_base
    local       msg

    if $bupfiledelete; then
        normal ' Twee nieuwe bestanden worden nu gekopieerd...'
    else
        normal ' Twee bestanden worden nu gekopieerd...'
    fi
    msg='  Kopieer... '
    for file_to_copy in $FILES_TO_COPY; do
        bepaal_bestandsgrootte "$file_to_copy" filesize
        file_to_copy_base="$(basename $file_to_copy)"

        #-------------------------------------------------------------------#
        # Filler voor uitlijnen te kopiëren back-up en grootte.             #
        #-------------------------------------------------------------------#
        file_to_copy_base_len=${#file_to_copy_base}
        filler=${SPACES:0:$file_to_copy_base_len-109}

        normal "$msg$file_to_copy_base$filler - ${filesize}B"
        msg='       en... '
        # Voor het evtueel afbreken van het script
        TO_DELETE="$TO_DELETE${BACKUPDIR[$harddisk]}/$file_to_copy_base "
    done

    spinner 'aan'

    cp  --preserve              \
        --verbose               \
        $FILES_TO_COPY          \
        "${BACKUPDIR[$harddisk]}"  \
        &>> "$LOG"
    cp_rc=$?
    TO_DELETE=''
    verwerk_rc "$PROGNAME: $FUNCNAME[$LINENO]: kopieer bestanden" \
                $cp_rc 0 'abend' MAXRC

    spinner 'uit'

    (( BUPFILES_COPIED = BUPFILES_COPIED + 2 ))
}

#-Functie-------------------------------------------------------------------#
# Naam: bepaal_bestandsgrootte                                              #
# Doel: Bepaal de grootte van een bestand.                                  #
# Arg.: Twee verplichte argumenten:                                         #
#       1. bestandsnaam     string, invoer                                  #
#       2. variabelenaam    string, uitvoer, krijgt als inhoud de bepaalde  #
#                           bestandsgrootte                                 #
# Vb. : bepaal_bestandsgrootte "$file" filesize                             #
#---------------------------------------------------------------------------#
function bepaal_bestandsgrootte {
    local file=${1:-/dev/null}
    local _filesize_variable=${2:-filesize}
    local _filesize_value=$(du  --apparent-size     \
                                --human-readable    \
                                "$file"             |
                            cut --fields=1)

    eval $_filesize_variable="'$_filesize_value'"
}

#-Functie-------------------------------------------------------------------#
# Naam: toon_afsluiten                                                      #
# Doel: Afsluitende meldingen en/of acties.                                 #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function toon_afsluiten {
    if $NO_HARDDISK_FOUND; then
        normal
        warning 'Geen enkele harddisk is aanwezig:'
        normal  '- koppel een harddisk aan,'
        normal  '- start daarna dit script opnieuw.'
        normal
        warning 'De back-up van de back-up is NIET gemaakt.'
        warning 'De back-up is NIET verwijderd.'
    elif $SOME_BACKUPDIR_NOT_FOUND; then
        normal
        normal  "Voor de harddisk met de melding 'map ... niet aanwezig' \
(zie hierboven):"
        normal  '- maak op de harddisk de ontbrekende map aan,'
        normal  '- start daarna dit script opnieuw.'
        normal
        warning 'De back-up van de back-up is NIET gemaakt.'
        warning 'De back-up is NIET verwijderd.'
    else
        if [[ $BUPFILES_COPIED -eq 0 ]]; then
            normal  'De back-up van de back-up is al gemaakt.'
        else
            success 'De back-up van de back-up is gemaakt.'
        fi

        if $DISKSPACE_OK; then

            koppel_schijven_af

            #---------------------------------------------------------------#
            # Verwijder backup, maar niet als deze op externe media staat.  #
            #---------------------------------------------------------------#
            if $DISKSPACE_OK && [[ ${STORAGEDIR:0:6} != /media ]]; then
                verwijder_backup_en_logboek
            fi
        else
            normal
            warning 'De back-up van de back-up is NIET gemaakt.'
            warning 'De back-up is NIET verwijderd.'
        fi
    fi
}

#-Functie-------------------------------------------------------------------#
# Naam: koppel_schijven_af                                                  #
# Doel: Koppel de aangekoppelde schijven af.                                #
# Arg.: Geen argumenten.                                                    #
#---------------------------------------------------------------------------#
function koppel_schijven_af {
    normal 'Ontkoppel gebruikte schijven...'

    spinner 'aan'

    for harddisk in "${!HARDDISK[@]}"; do
        if [[ -e ${HARDDISK[$harddisk]} ]]; then
            umount "${HARDDISK[$harddisk]}" &>> "$LOG"
            success "Schijf ${HARDDISK[$harddisk]} kan uitgeschakeld en/of \
verwijderd worden."
        fi
    done

    spinner 'uit'

    success 'Alle schijven kunnen uitgeschakeld en/of verwijderd worden.'
}

#############################################################################
# Hoofdlijn                                                                 #
#############################################################################
# init_script
{
    verwerk_invoer "$@"
    controleer_gebruiker "$SCRIPT_NEEDS_SUDO"
}
# verwerk
{
    bepaal_log "$SCRIPT_NEEDS_SUDO" LOGDIR "$LOGFILE" LOG
    controleer_invoer
    toon_invoer
    toon_gestart
    verwerk_backup_backup
    toon_gestopt
}
# afsl_script
{
    toon_afsluiten
    toon_afsluiten_sc
    exit $MAXRC
}

# Einde script.
