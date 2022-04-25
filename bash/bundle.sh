#!/bin/bash
#############################################################################
# Bestand:   bundle.sh                                                      #
# Doel:      Script voor het bundelen van bestanden tot een shell-archief.  #
# Gebruik:   ./bundle.sh [bestand]... > BESTAND                             #
#            Bundelen:  $ ./bundle *.sh > scripts.shar                      #
#            Uitpakken: $ bash scripts.shar                                 #
# Gebruikt:  -                                                              #
# Auteur:    Mark G. Sobell, A Practical Guide to Ubuntu Linux.             #
#            Karel Zimmer (http://karelzimmer.nl, info@karelzimmer.nl)      #
# ------------------------------------------------------------------------- #
# Auteursrecht © 2011-2015 Karel Zimmer.                                    #
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
# Versies:      1.0.0   2011-01-28  Eerste versie.                          #
#############################################################################
readonly VERSION_NUMBER=1.3.1
readonly RELEASE_DATE=2015-02-14

# init_script
echo '# Pak dit bestand uit met bash. Voorbeeld: $ bash bestand.shar'

# verwerk
for file; do

    # Verwerk alleen reguliere bestanden.
    if [[ ! -f $file ]]; then
        continue
    fi

    file_base=$(basename $file)

    echo "cat > $file_base << 'Einde van $file_base'"
    cat $file
    echo "Einde van $file_base"
    echo "echo $file_base uitgepakt 1>&2"
done

# afsl_script
echo '# Einde bestand.'
exit 0

# Einde shell-archief.
