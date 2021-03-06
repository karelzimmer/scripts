# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-ubuntu-18.04-desktop-pc04.sh
# Doel:     Installatiebestand voor Ubuntu 18.04 LTS desktop op pc04
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-ubuntu-18.04-desktop-pc04.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-ubuntu-18.04-desktop-pc04.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-ubuntu-18.04-desktop-pc04.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=03.02.05
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------
#@calibre
#1 Calibre e-boek bibliotheekbeheer
sudo apt-get install --yes calibre
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove calibre

#@dropbox
#1 Dropbox bestanden synchroniseren via het web
sudo apt-get install --yes nautilus-dropbox
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove nautilus-dropbox

#@google-earth
#1 Google Earth verken de planeet
echo 'deb [arch=amd64] http://dl.google.com/linux/earth/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-earth.list
wget --output-document=- 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | sudo apt-key add -
sudo apt-get update
## google-earth-ec-stable is de Google Earth Enterprise Client (EC)
sudo apt-get install --yes google-earth-pro-stable
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove google-earth-pro-stable
#3    sudo rm /etc/apt/sources.list.d/google-earth.list
#3    sudo apt update

#@wine
#1 Wine Windows-apps op Linux
sudo dpkg --add-architecture i386
sudo add-apt-repository --yes 'ppa:cybolic/vineyard-testing'
wget --output-document=- 'https://dl.winehq.org/wine-builds/winehq.key' | sudo apt-key add -
sudo add-apt-repository --yes 'https://dl.winehq.org/wine-builds/ubuntu/'
echo 'ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true' | sudo debconf-set-selections
sudo apt-get install --yes --install-recommends winehq-stable winetricks playonlinux vineyard
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove wine winetricks playonlinux vineyard
#3    sudo add-apt-repository --yes --remove 'ppa:cybolic/vineyard-testing'
#3    sudo add-apt-repository --yes --remove 'https://dl.winehq.org/wine-builds/ubuntu/'
#3    sudo apt update

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen
# ------------------------------------------------------------------------------
# Einde installatiebestand
