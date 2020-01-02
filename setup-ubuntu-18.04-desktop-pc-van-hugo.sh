# shellcheck shell=bash
# ##############################################################################
# Bestand:  setup-ubuntu-18.04-desktop-pc-van-hugo.sh
# Doel:     Instellingsbestand voor Ubuntu 18.04 LST desktop op pc-van-hugo
# Gebruik:  In het terminalvenster met script setup (aanbevolen):
#           setup /usr/local/bin/setup-ubuntu-18.04-desktop-pc-van-hugo.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/setup-ubuntu-18.04-desktop-pc-van-hugo.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           setup -s /usr/local/bin/setup-ubuntu-18.04-desktop-pc-van-hugo.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.03.07
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Gebruikersinstellingen wijzigen
# ------------------------------------------------------------------------------
#@kvm
#1 KVM virtualisatieprogramma
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='virt-manager.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'virt-manager.desktop']"; fi

#@virtualbox
#1 VirtualBox virtualisatieprogramma
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='virtualbox.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'virtualbox.desktop']"; fi
if [[ $USER = hugo ]]; then wget --output-document="$HOME/.local/share/applications/virtualbox-hugowin732.desktop" 'https://karelzimmer.nl/apps/virtualbox/virtualbox-hugowin732.desktop'; fi
if [[ $USER = hugo ]]; then if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='virtualbox-hugowin732.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'virtualbox-hugowin732.desktop']"; fi; fi
#2 1. Ga naar Apparaten > Installeren Guest Additions en volg de aanwijzingen
#2    op het scherm.
#2 2. Voor optimale netwerksnelheid kies bij Netwerk voor Gekoppeld aan:
#2    Netwerk bridge adapter.
#3 Verwijder map VirtualBox VMs in de Persoonlijke map.

#1 Actie sluiten laptopklep wijzigen
gsettings set org.gnome.settings-daemon.plugins.power power-button-action 'suspend'
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.settings-daemon.plugins.power power-button-action

#1 Bureaubladachtergrond wijzigen
gsettings set org.gnome.desktop.background picture-uri 'file:///usr/share/backgrounds/scripts/bol.jpg'
gsettings set org.gnome.desktop.screensaver picture-uri 'file:///usr/share/backgrounds/scripts/bol.jpg'
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.desktop.background picture-uri
#3    gsettings reset org.gnome.desktop.screensaver picture-uri

# Einde instellingsbestand
