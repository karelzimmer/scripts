# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-ubuntu-18.04-desktop-pc-van-emily.sh
# Doel:     Installatiebestand voor Ubuntu 18.04 LTS desktop op pc-van-emily
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-ubuntu-18.04-desktop-pc-van-emily.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-ubuntu-18.04-desktop-pc-van-emily.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-ubuntu-18.04-desktop-pc-van-emily.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.05.08
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------
#@teamviewer
#1 TeamViewer computer op afstand bedienen
wget --output-document=/tmp/teamviewer.deb 'https://download.teamviewer.com/download/linux/teamviewer_amd64.deb'
echo 'ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true' | sudo debconf-set-selections
sudo apt-get install --yes /tmp/teamviewer.deb
sudo rm /tmp/teamviewer.deb
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove teamviewer
#3    sudo rm /etc/apt/sources.list.d/teamviewer.list*
#3    sudo apt update

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen
# ------------------------------------------------------------------------------
# Einde installatiebestand
