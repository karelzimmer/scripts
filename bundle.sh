#!/bin/bash
###############################################################################
# Bestand:   bundle.sh                                                      
# Doel:      Script voor het bundelen van bestanden tot een shell-archief.  
# Gebruik:   ./bundle.sh [bestand]... > BESTAND                             
#            Bundelen:  $ ./bundle *.sh > scripts.shar                      
#            Uitpakken: $ bash scripts.shar                                 
# Gebruikt:  -                                                              
# Auteur:    Mark G. Sobell, A Practical Guide to Ubuntu Linux.             
#            Karel Zimmer (http://karelzimmer.nl, info@karelzimmer.nl)      
# ----------------------------------------------------------------------------- 
# Auteursrecht © 2011-2015 Karel Zimmer.                                    
# ----------------------------------------------------------------------------- 
# Versies:      1.0.0   2011-01-28  Eerste versie.                          
###############################################################################

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
