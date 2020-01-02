# shellcheck shell=bash
# ##############################################################################
# Bestand:  setup-raspbian-8.0-desktop.sh
# Doel:     Instellingsbestand voor Raspbian 8.0 desktop
# Gebruik:  In het terminalvenster met script setup (aanbevolen):
#           setup /usr/local/bin/setup-raspbian-8.0-desktop.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/setup-raspbian-8.0-desktop.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           setup -s /usr/local/bin/setup-raspbian-8.0-desktop.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.03.06
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# Voor het opzoeken van gebruikersinstellingen zie: Linux-info.txt
# ------------------------------------------------------------------------------
# Gebruikersinstellingen wijzigen
# ------------------------------------------------------------------------------
#@vnc-connect
#1 VNC Connect computer op afstand bedienen
:
#2 1. Klik op VNC Sever - Servermode (rechtsboven)
#2 2. Klik op sign in.
#2 3. Vul in Email en Password, klik op Next.
#2 4. Selecteer Direct and cloud connectivity, klik op Next.
#2 5. Klik op Done.
#2 6. Herstart de Raspbery Pi.

#@wachtwoord
#1 Wachtwoord wijzigen
:
#2 1. Via menu > Voorkeuren > Raspbery pi Configuratie programma > Systeem
#2    (tab).
#2 2. Vul in achter Wachtwoord: **** (Standaard Wachtwoord: raspberry)
#2 3. Klik op OK.
#2 4. Herstart de Raspbery Pi.

# Einde instellingsbestand
