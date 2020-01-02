# shellcheck shell=bash
# ##############################################################################
# Bestand:  setup-ubuntu-18.04-desktop-pc01.sh
# Doel:     Instellingsbestand voor Ubuntu 18.04 LTS desktop op pc01
# Gebruik:  In het terminalvenster met script setup (aanbevolen):
#           setup /usr/local/bin/setup-ubuntu-18.04-desktop-pc01.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/setup-ubuntu-18.04-desktop-pc01.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           setup -s /usr/local/bin/setup-ubuntu-18.04-desktop-pc01.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.07.03
# REL_DAT=2019-12-19
# REL_MSG='Beschrijving icaclient gewijzigd'

# ------------------------------------------------------------------------------
# Gebruikersinstellingen wijzigen
# ------------------------------------------------------------------------------
#@dash-to-panel
#1 Dash to Panel pictogram taakbalk
## GNOME extensie, met name voor ex-Windows 7+ gebruikers.
git clone https://github.com/home-sweet-gnome/dash-to-panel.git /tmp/dash-to-panel
make install --directory=/tmp/dash-to-panel
if ! gsettings get org.gnome.shell enabled-extensions | grep --quiet --regexp='workspace-indicator@gnome-shell-extensions.gcampax.github.com'; then gnome-shell-extension-tool --enable-extension=dash-to-panel@jderose9.github.com; fi
rm --force --recursive /tmp/dash-to-panel
## ** Handmatige setup **
## 0. Voer uit als nog niet gedaan: setup gnome-shell-integratie.
## 1. Start een browser.
## 2. Ga naar https://extensions.gnome.org/extension/1160/dash-to-panel
## 3. Zet schuifje op ON.
## 4. Klik op Installeren.
## 5. Instellen via blauw vierkantje achter schuif op deze site, of via
##    Afstellingen > Uitbreidingen > Dash to panel > klik op tandwielsymbool.
#3 1. Start Afstellingen > Uitbreidingen > Dash to panel > zet schuifje uit.
#3 OF
#3 1. Start een browser.
#3 2. Ga naar https://extensions.gnome.org/local
#3 3. Bij Dash to Panel zet schuifje op OFF of klik op kruisje.

#@icaclient
#1 Citrix Workspace app telewerken (v/h Citrix Receiver, aka ICA Client)
xdg-mime default wfica.desktop application/x-ica
#2 1. Start Firefox webbrowser.
#2 2. Ga naar menu > Voorkeuren > Bestanden en Toepassingen.
#2 3. Zoek ica en zorg dat bij Citrix ICA-instellingen is geselecteerd
#2    Citrix Receiver Engine gebruiken.
#2 4. Ga naar https://telewerkportaal.rabobank.nl, log in, en stel vast dat
#2    het inloggen op het Telewerkportaal werkt.

#@spotify
#1 Spotify online muziekservice
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='spotify_spotify.desktop'; then gsettings set org.gnome.shell favorite-apps "['spotify_spotify.desktop', ""$(gsettings get org.gnome.shell favorite-apps | awk -F[ '{print $2}')"; fi
#2 1. Start Spotify.
#2 2. Ga naar Edit (Bewerken) en vervolgens naar Preferences (Voorkeuren).
#2 3. Zet Language (Taal) op Nederlands (Dutch).
#2 4. Herstart Spotify.

#@thunderbird-manually-sort-folders
#1 Manually sort folders (Thunderbird add-on)
:
#2 1. Start Thunderbird.
#2 2. Ga naar menu > Add-ons > Add-ons.
#2 3. Zoek naar sort.
#2 4. Achter 'Manually sort folders' klik op + Toevoegen aan Thunderbird.
#2 5. Klik op Nu installeren.
#2 6. Klik op Nu herstarten.
#2 7. Ga naar menu > Add-ons > Manually Sort Folders.
#3 1. Start Thunderbird.
#3 2. Ga naar menu > Add-ons > Add-ons.
#3 3. Bij Manually sort folders klik op Uitschakelen of Verwijderen.

#1 Bureaubladachtergrond wijzigen
gsettings set org.gnome.desktop.background picture-uri 'file:///usr/share/backgrounds/scripts/marmer.jpg'
gsettings set org.gnome.desktop.screensaver picture-uri 'file:///usr/share/backgrounds/scripts/marmer.jpg'
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.desktop.background picture-uri
#3    gsettings reset org.gnome.desktop.screensaver picture-uri

# Einde instellingsbestand
