# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-ubuntu-18.04-desktop-pc06.sh
# Doel:     Installatiebestand voor Ubuntu 18.04 LTS desktop
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-ubuntu-18.04-desktop.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-ubuntu-18.04-desktop.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-ubuntu-18.04-desktop.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.25.00
# REL_DAT=2019-12-28
# REL_MSG='Webmin (weer) toegevoegd'

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen - init
# ------------------------------------------------------------------------------
#1 Foutrapportage uitzetten
sudo sed --in-place --expression='s/enabled=1/enabled=0/' /etc/default/apport
sudo systemctl disable --now apport.service

#1 Repository aanzetten
## T.b.v. Ubuntu Live
sudo add-apt-repository --yes universe

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------
#@afstellingen
#1 Afstellingen uitgebreide instellingen voor Gnome
sudo apt-get install --yes gnome-tweak-tool
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove gnome-tweak-tool

#@chkrootkit
#1 Check RootKit bepaal of een systeem is geïnfecteerd met een rootkit
sudo apt-get install --yes chkrootkit
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove chkrootkit

#@communitheme
#1 Communitheme/Yaru uiterlijk aanpassen voor Gnome
sudo snap install communitheme
#2 Met snap (standaard):
#2 ~~~~~~~~~~~~~~~~~~~~~
#2 Geen aktie vereist.
#2
#2 Met PPA:
#2 ~~~~~~~~
#2 Start Terminalvenster en typ, of kopieer en plak:
#2    sudo add-apt-repository ppa:communitheme/ppa
#2    sudo apt install ubuntu-communitheme-session
#3 Met snap (standaard):
#3 ~~~~~~~~~~~~~~~~~~~~~
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo snap remove communitheme
#3
#3 Met PPA:
#3 ~~~~~~~~
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove ubuntu-communitheme-session
#3    sudo add-apt-repository --yes --remove ppa:communitheme/ppa

#@flatpak
#1 Flatpak bouw, installeer, en draai apps en runtimes
sudo add-apt-repository --yes 'ppa:alexlarsson/flatpak'
sudo apt-get install --yes flatpak gnome-software-plugin-flatpak
sudo flatpak remote-add --if-not-exists flathub 'https://flathub.org/repo/flathub.flatpakrepo'
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove flatpak gnome-software-plugin-flatpak
#3    sudo flatpak-remote-delete flathub 'https://flathub.org/repo/flathub.flatpakrepo'
#3    sudo add-apt-repository --yes --remove ppa:alexlarsson/flatpak

#@git
#1 git revisie controle systeem (SCM = source code management)
sudo apt-get install --yes git git-gui
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove git git-gui

#@google-chrome
#1 Google Chrome webbrowser
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
wget --output-document=- 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | sudo apt-key add -
sudo apt-get update
sudo apt-get install --yes google-chrome-stable
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove google-chrome-stable
#3    sudo rm /etc/apt/sources.list.d/google-chrome.list*
#3    sudo apt update

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
rm /tmp/LATEST /tmp/icaclient.deb
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove icaclient

#@imcompressor
#1 ImCompressor verliesloos afbeeldingen comprimeren voor PNG en JPEG bestanden.
## Flatpak setup
sudo add-apt-repository --yes 'ppa:alexlarsson/flatpak'
sudo apt-get install --yes flatpak gnome-software-plugin-flatpak
sudo flatpak remote-add --if-not-exists flathub 'https://flathub.org/repo/flathub.flatpakrepo'
## ImCompressor instal
flatpak install flathub com.github.huluti.ImCompressor
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo flatpak uninstall com.github.huluti.ImCompressor
#3    sudo apt update

#@libreoffice
#1 LibreOffice kantoorpakket
sudo apt-get install --yes libreoffice libreoffice-help-nl libreoffice-l10n-nl
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove libreoffice libreoffice-help-nl libreoffice-l10n-nl

#@odio
#1 Odio desktop internetradio-speler
sudo snap install odio
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo snap remove odio

#@password-safe
#1 Password Safe wachtwoordkluis
## Flatpak setup
sudo add-apt-repository --yes 'ppa:alexlarsson/flatpak'
sudo apt-get install --yes flatpak gnome-software-plugin-flatpak
sudo flatpak remote-add --if-not-exists flathub 'https://flathub.org/repo/flathub.flatpakrepo'
## Password Safe instal
sudo flatpak install --assumeyes flathub org.gnome.PasswordSafe
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo flatpak uninstall org.gnome.PasswordSafe
#3    sudo apt update

#@rkhunter
#1 RootKit Hunter detecteer bekende rootkits en mqalware
sudo apt-get install --yes rkhunter
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove rkhunter

#@shortwave
#1 Shortwave desktop internetradio-speler
## Flatpak setup
sudo add-apt-repository --yes 'ppa:alexlarsson/flatpak'
sudo apt-get install --yes flatpak gnome-software-plugin-flatpak
sudo flatpak remote-add --if-not-exists flathub 'https://flathub.org/repo/flathub.flatpakrepo'
## Shortwave instal
sudo flatpak install --assumeyes https://haeckerfelix.de/~repo/shortwave.flatpakref
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo flatpak uninstall de.haeckerfelix.Shortwave.Devel
#3    sudo apt update

#@skype
#1 Skype beeldbellen over internet
sudo snap install --classic skype
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo snap remove skype

#@virtualbox
#1 VirtualBox virtualisatieprogramma
## Images staan in ~/VirtualBox VMs/
echo 'virtualbox-ext-pack virtualbox-ext-pack/license select true' | sudo debconf-set-selections
echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release --codename --short) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
wget --output-document=- 'https://www.virtualbox.org/download/oracle_vbox_2016.asc' | sudo apt-key add -
sudo apt-get update
wget --output-document=/tmp/LATEST.TXT 'http://download.virtualbox.org/virtualbox/LATEST.TXT'
## VirtualBox Guest Additions ISO staat in /usr/share/virtualbox
sudo apt-get install --yes virtualbox-"$(awk -F. '{print $1"."$2}' < /tmp/LATEST.TXT)"
wget --output-document="/tmp/Oracle_VM_VirtualBox_Extension_Pack-$(cat /tmp/LATEST.TXT).vbox-extpack" "http://download.virtualbox.org/virtualbox/$(cat /tmp/LATEST.TXT)/Oracle_VM_VirtualBox_Extension_Pack-$(cat /tmp/LATEST.TXT).vbox-extpack"
echo 'y' | sudo VBoxManage extpack install --replace "/tmp/Oracle_VM_VirtualBox_Extension_Pack-$(cat /tmp/LATEST.TXT).vbox-extpack"
sudo adduser "${SUDO_USER:-$USER}" vboxusers
sudo rm --force "/tmp/Oracle_VM_VirtualBox_Extension_Pack-$(cat /tmp/LATEST.TXT).vbox-extpack" /tmp/LATEST.TXT
#2 Met een AMD-processor zal AMD-V wel aanstaan, maar bij Intel moet vaak VT-x
#2 aangezet worden in het BIOS of UEFI-firmware!
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove virtualbox-*
#3    sudo deluser $USER vboxusers
#3    sudo delgroup vboxusers
#3    sudo apt update

#@vlc
#1 VLC mediaspeler en multimedia-ondersteuning
## Voor libdvdcss, onderdeel van het VideoLAN-project
echo 'deb http://download.videolan.org/pub/debian/stable/ /' | sudo tee /etc/apt/sources.list.d/vlc.list
wget --output-document=- 'http://download.videolan.org/pub/debian/videolan-apt.asc' | sudo apt-key add -
sudo apt-get update
echo 'ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true' | sudo debconf-set-selections
sudo apt-get install --yes ubuntu-restricted-extras libavcodec-extra libdvdread4 libdvdcss2 vlc winff
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove libavcodec-extra libdvdread4 libdvdcss2 vlc winff
#3    sudo rm /etc/apt/sources.list.d/vlc.list*
#3    sudo apt update

#@wallpapers
#1 Bureaubladachtergronden
sudo apt-get install --yes ubuntu-wallpapers-*
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove ubuntu-wallpapers-*

#@webmin
#1 Webmin web-gebaseerd admin tool
## ===============================
sudo echo 'deb http://download.webmin.com/download/repository sarge contrib' | sudo tee /etc/apt/sources.list.d/webmin.list
sudo wget --output-document=- 'http://www.webmin.com/jcameron-key.asc' | sudo apt-key add -
sudo apt-get update
sudo apt-get install --yes webmin
sudo sed --in-place=.save --expression='s/ssl=1/ssl=0/' /etc/webmin/miniserv.conf
sudo systemctl restart webmin.service

#3 1. Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove webmin
#3    sudo rm /etc/apt/sources.list.d/webmin.list
#3    sudo apt update

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen - term
# ------------------------------------------------------------------------------
#@drivers
#1 Extra stuurprogramma's
:
#2 1. Zoek Software & Updates.
#2 2. Ga naar Extra stuurprogramma's.
#2 3. Selecteer de aanwezige niet-vrije stuurprogramma's en klik op
#2    Wijzigingen doorvoeren.
#2 Als de installatie begonnen is met Ubuntu 18.04 of 18.04.1, overweeg dan het
#2 uitvoeren van (check uname -r, kernel release < 5.0):
#2 sudo apt install --install-recommends linux-generic-hwe-18.04 xserver-xorg-hwe-18.04

#1 Wijzig opstartwachttijd
sudo sed --in-place --expression='s/GRUB_TIMEOUT=10/GRUB_TIMEOUT=1/' /etc/default/grub
sudo sed --in-place --expression='s/GRUB_TIMEOUT=0/GRUB_TIMEOUT=1/' /etc/default/grub
sudo update-grub

# Einde installatiebestand
