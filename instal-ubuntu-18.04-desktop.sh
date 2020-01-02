# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-ubuntu-18.04-desktop.sh
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
# REL_NUM=02.18.04
# REL_DAT=2019-12-15
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen - init
# ------------------------------------------------------------------------------
#1 Foutrapportage uitzetten
sudo sed --in-place --expression='s/enabled=1/enabled=0/' /etc/default/apport
sudo systemctl disable --now apport.service
sudo rm --force /var/crash/*

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

#@gnome-shell-integratie
#1 GNOME Shell integratie voor Firefox en Chrome
## Integratie met GNOME Shell extensies repository voor Chrome en Firefox;
## platform-eigen connector voor https://extensions.gnome.org
sudo apt-get install --yes chrome-gnome-shell git make
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove chrome-gnome-shell

#@libreoffice
#1 LibreOffice kantoorpakket
sudo apt-get install --yes libreoffice libreoffice-help-nl libreoffice-l10n-nl
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove libreoffice libreoffice-help-nl libreoffice-l10n-nl

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

#@skype
#1 Skype beeldbellen over internet
sudo snap install --classic skype
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo snap remove skype

#@thunderbird
#1 Mozilla Thunderbird e-mail/nieuws
sudo rm --force /home/*/.config/evolution/sources/*

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

#@luks
#1 LUKS encryptie wachtwoorden
:
#2 Om een LUKS-wachtwoord toe te voegen, start Terminalvenster en typ, of
#2 kopieer en plak:
#2    sudo cryptsetup luksAddKey $(blkid -t TYPE=crypto_LUKS -o device)
#2
#2 Om een LUKS-wachtwoord te wijzigen, start Terminalvenster en typ, of
#2 kopieer en plak:
#2    sudo cryptsetup luksChangeKey $(blkid -t TYPE=crypto_LUKS -o device)
#2
#2 Voor het aantal LUKS-wachtwoorden, start Terminalvenster en typ, of
#2 kopieer en plak:
#2    sudo cryptsetup luksDump $(blkid -t TYPE=crypto_LUKS -o device)
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo cryptsetup luksRemoveKey $(blkid -t TYPE=crypto_LUKS -o device)

#1 Wijzig opstartwachttijd
sudo sed --in-place --expression='s/GRUB_TIMEOUT=10/GRUB_TIMEOUT=1/' /etc/default/grub
sudo sed --in-place --expression='s/GRUB_TIMEOUT=0/GRUB_TIMEOUT=1/' /etc/default/grub
sudo update-grub

# Einde installatiebestand
