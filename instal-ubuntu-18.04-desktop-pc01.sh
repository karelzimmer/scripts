# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-ubuntu-18.04-desktop-pc01.sh
# Doel:     Installatiebestand voor Ubuntu 18.04 LTS desktop op pc01
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-ubuntu-18.04-desktop-pc01.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-ubuntu-18.04-desktop-pc01.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-ubuntu-18.04-desktop-pc01.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=03.04.11
# REL_DAT=2019-12-19
# REL_MSG='Beschrijving icaclient gewijzigd'

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------
#@clamav
#1 ClamAV/ClamTK antivirus
sudo apt-get install --yes clamtk
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove clamtk

#@gradio
#1 Gradio desktop internetradio-speler
## Flatpak setup
sudo add-apt-repository --yes 'ppa:alexlarsson/flatpak'
sudo apt-get install --yes flatpak gnome-software-plugin-flatpak
sudo flatpak remote-add --if-not-exists flathub 'https://flathub.org/repo/flathub.flatpakrepo'
## Gradio instal
sudo flatpak install --assumeyes flathub de.haeckerfelix.gradio
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo flatpak uninstall de.haeckerfelix.gradio
#3    sudo apt update

#@icaclient
#1 Citrix Workspace app telewerken (v/h Citrix Receiver, aka ICA Client)
wget --output-document=/tmp/LATEST 'https://karelzimmer.nl/apps/icaclient/LATEST'
wget --output-document=/tmp/icaclient.deb "https://karelzimmer.nl/apps/icaclient/icaclient_$(cat /tmp/LATEST)_amd64.deb"
echo 'icaclient icaclient/accepteula select true' | sudo debconf-set-selections
sudo apt-get install --yes /tmp/icaclient.deb
sudo ln --symbolic --force /usr/share/ca-certificates/mozilla/* /opt/Citrix/ICAClient/keystore/cacerts
sudo c_rehash /opt/Citrix/ICAClient/keystore/cacerts
sudo rm /tmp/LATEST /tmp/icaclient.deb
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove icaclient

#@gparted
#1 GParted partitiebewerker
sudo apt-get install --yes gparted
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove gparted

#@openssh
#1 OpenSSH secure shell-connectiviteitsprogramma
sudo apt-get install --yes ssh
sudo sed --in-place --expression='s/PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
grep --quiet --regexp='PermitRootLogin no' /etc/ssh/sshd_config
sudo systemctl restart ssh.service
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove ssh

#@spotify
#1 Spotify online muziekservice
sudo snap install spotify
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo snap remove spotify

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen
# ------------------------------------------------------------------------------
#@gastgebruiker
#1 Gastgebruiker toevoegen
if ! id gast &> /dev/null; then sudo useradd --create-home --shell /bin/bash --comment 'Gast' gast; sudo passwd --delete gast; fi
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo userdel --remove gast

#1 Systeemgebruiker toevoegen
## Voor toegang op afstand/systeembeheer
if ! id karel &> /dev/null; then sudo useradd --create-home --shell /bin/bash --comment 'Karel Zimmer (systeemgebruiker)' --groups sudo karel; fi
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo userdel --remove karel

# Einde installatiebestand
