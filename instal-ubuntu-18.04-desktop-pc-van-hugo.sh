# shellcheck shell=bash
# ##############################################################################
# Bestand:  instal-ubuntu-18.04-desktop-pc-van-hugo.sh
# Doel:     Installatiebestand voor Ubuntu 18.04 LTS desktop op pc-van-hugo
# Gebruik:  In het terminalvenster met script instal (aanbevolen):
#           instal /usr/local/bin/instal-ubuntu-18.04-desktop-pc-van-hugo.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/instal-ubuntu-18.04-desktop-pc-van-hugo.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           instal -s /usr/local/bin/instal-ubuntu-18.04-desktop-pc-van-hugo.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=03.04.08
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Software installeren
# ------------------------------------------------------------------------------
#@pinta
#1 Pinta afbeeldingen bewerken
sudo apt-get install --yes pinta
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove pinta

#@kvm
#1 KVM virtualisatieprogramma
## Images staan in /var/lib/libvirt/images/
sudo apt-get install --yes cpu-checker qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils virt-manager
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove cpu-checker qemu-kvm libvirt-bin
#3    sudo apt remove ubuntu-vm-builder bridge-utils virt-manager
#3    sudo delgroup libvirtd-dnsmasq
#3    sudo deluser $USER libvirtd
#3    sudo delgroup libvirtd

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

#@telegram
#1 Telegram berichtendienst
sudo snap install telegram-desktop
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    sudo snap remove telegram-desktop

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

# ------------------------------------------------------------------------------
# Systeeminstellingen wijzigen
# ------------------------------------------------------------------------------
# Einde installatiebestand
