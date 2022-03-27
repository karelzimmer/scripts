#!/bin/bash
# Bestand: compiz-fix.sh
# Mocht na in/uitschakelen Bureaublad-effecten (Desktop Effects)
# e.e.a. niet werken: geef dit script een kans (Ubuntu 7.04).
gconftool-2 --type int --set /apps/compiz/general/screen0/options/hsize 4
gconftool-2 --type int --set /apps/compiz/general/screen0/options/number_of_desktops 1
