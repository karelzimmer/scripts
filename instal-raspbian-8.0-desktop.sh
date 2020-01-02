# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-raspbian-8.0-desktop.sh
# Doel:     Installatiebestand voor Raspbian 8.0 desktop
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-raspbian-8.0-desktop.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-raspbian-8.0-desktop.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-raspbian-8.0-desktop.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=03.01.06
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------
#@openssh
#1 OpenSSH secure shell-connectiviteitsprogramma
:
#2 1. Via menu > Voorkeuren > Raspbery pi Configuratie programma > Interfaces
#2    (tab).
#2 2. Bij SSH selecteer Aan.
#2 3. Klik op OK.
#2 4. Herstart de Raspbery Pi.

#@vnc-connect
#1 VNC Connect computer op afstand bedienen
:
#2 1. Via menu > Voorkeuren > Raspbery pi Configuratie programma > Interfaces
#2    (tab).
#2 2. Bij VNC selecteer Aan.
#2 3. Klik op OK.
#2 4. Herstart de Raspbery Pi.

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen
# ------------------------------------------------------------------------------
#1 Localisatie wijzigen
:
#2  1. Via menu > Voorkeuren > Raspbery pi Configuratie programma >
#2     Localizatie (tab).
#2  2. Klik achter Landinstellingen op Stel Landinstellingen in.
#2  3. Achter Taal selecteer nl (Dutch), achter Land: NL (Netherlands).
#2  4. Klik op OK.
#2  5. Klik achter Tijdzone op Stel Tijdzone in.
#2  6. Achter Regio selecteer Europe, achter locatie: Amsterdam.
#2  7. Klik op OK.
#2  8. Klik achter Toetsendbord op Stel Toetsendbord in.
#2  9. Achter Country selecteer Verenigde Staten, achter Variant: Engels (VS,
#2     internationaal, met dode toetsen).
#2 10. Klik op OK.
#2 11. Klik achter WiFi Land op Stel WiFi Land in.
#2 12. Achter Land selecteer NL  Netherlands.
#2 13. Klik op OK.
#2 14. Herstart de Raspbery Pi.

# Einde installatiebestand
