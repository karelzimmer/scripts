# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-raspbian-8.0-desktop-pc09.sh
# Doel:     Installatiebestand voor Raspbian 8.0 desktop op pc09
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-raspbian-8.0-desktop-pc09.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-raspbian-8.0-desktop-pc09.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-raspbian-8.0-desktop-pc09.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=03.02.06
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen
# ------------------------------------------------------------------------------
#1 Systeemgebruiker toevoegen
## Voor toegang op afstand/systeembeheer
if ! id karel &> /dev/null; then sudo useradd --create-home --shell /bin/bash --comment 'Karel Zimmer (systeemgebruiker)' --groups sudo karel; fi
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo userdel --remove karel

#1 Computernaam wijzigen
:
#2 1. Via menu > Voorkeuren > Raspbery pi Configuratie programma > Systeem
#2   (tab).
#2 2. Vul in achter Hostname: pc09.
#2 3. Klik op OK.
#2 4. Herstart de Raspbery Pi.

# Einde installatiebestand
