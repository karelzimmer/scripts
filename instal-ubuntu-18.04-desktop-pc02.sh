# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-ubuntu-18.04-desktop-pc02.sh
# Doel:     Installatiebestand voor Ubuntu 18.04 LTS desktop op pc02
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-ubuntu-18.04-desktop-pc02.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-ubuntu-18.04-desktop-pc02.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-ubuntu-18.04-desktop-pc02.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=03.03.06
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------
#@openshot
#1 OpenShot video's maken en bewerken
sudo apt-get install --yes openshot
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove openshot

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
#1 Helderheid wijzigen
## Helderheid RADEON varieert van 0 tot 255 (max_brightness).  Ingestelde helderheid wordt vergeten na een herstart.
## systemd & rc.local: if rc.local exists and is executable, it gets pulled automatically into multi-user.target
sudo touch /etc/rc.local
sudo chmod 'u+x' /etc/rc.local
if ! grep --quiet --regexp='backlight' /etc/rc.local; then echo 'echo 145 > /sys/class/backlight/radeon_bl0/brightness' | sudo tee --append /etc/rc.local; fi

# Einde installatiebestand
