# shellcheck shell=bash
# ##############################################################################
# Bestand:  setup-ubuntu-18.04-desktop-pc04.sh
# Doel:     Instellingsbestand voor Ubuntu 18.04 LTS desktop op pc04
# Gebruik:  In het terminalvenster met script setup (aanbevolen):
#           setup /usr/local/bin/setup-ubuntu-18.04-desktop-pc04.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/setup-ubuntu-18.04-desktop-pc04.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           setup -s /usr/local/bin/setup-ubuntu-18.04-desktop-pc04.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.03.08
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Gebruikersinstellingen wijzigen
# ------------------------------------------------------------------------------
#1 Script accu automatisch starten
:
#2 1. druk kort op de Windows/Apple-toets, typ 'ops' en klik op
#2    Opstarttoepassingen.
#2 2. Klik op Toevoegen.
#2 3. Vul in Naam Accu, Opdracht /usr/local/bin/_accu,
#2    Commentaar Bewaak en meld status accu, en klik op Sluiten.

#1 Schermbeveiliging wijzigen
gsettings set org.gnome.desktop.screensaver lock-enabled true
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings set org.gnome.desktop.screensaver lock-enabled false

#@google-earth
#1 Google Earth verken de planeet
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='google-earth.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'google-earth.desktop']"; fi

#1 Bureaubladachtergrond wijzigen
gsettings set org.gnome.desktop.background picture-uri 'file:///usr/share/backgrounds/scripts/prunus.jpg'
gsettings set org.gnome.desktop.screensaver picture-uri 'file:///usr/share/backgrounds/scripts/prunus.jpg'
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.desktop.background picture-uri
#3    gsettings reset org.gnome.desktop.screensaver picture-uri

# Einde instellingsbestand
