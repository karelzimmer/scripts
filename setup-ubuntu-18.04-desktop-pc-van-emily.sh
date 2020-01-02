# shellcheck shell=bash
# ##############################################################################
# Bestand:  setup-ubuntu-18.04-desktop-pc-van-emily.sh
# Doel:     Instellingsbestand voor Ubuntu 18.04 LTS desktop op pc-van-emily
# Gebruik:  In het terminalvenster met script setup (aanbevolen):
#           setup ~/bin/setup-ubuntu-18.04-desktop-pc-van-emily.sh
#      of:  Direct in het terminalvenster:
#           bash ~/bin/setup-ubuntu-18.04-desktop-pc-van-emily.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           setup -s ~/bin/setup-ubuntu-18.04-desktop-pc-van-emily.sh
# Auteur:   Karel Zimmer (http://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=01.03.07
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# ------------------------------------------------------------------------------
# Gebruikersinstellingen wijzigen
# ------------------------------------------------------------------------------
#@firefox-adblock-plus
#1 Adblock Plus (Firefox add-on)
:
#2 1. Start Firefox webbrowser.
#2 2. Ga naar https://addons.mozilla.org/nl/firefox/addon/adblock-plus
#2 3. Klik op Toevoegen aan Firefox.
#2 4. Klik op Toevoegen.
#2 5. Klik op Oké, begrepen.
#3 1. Start Firefox webbrowser.
#3 2. Ga naar menu > Add-ons (Ctrl+Shift+A).
#3 3. Klik links op Extensies.
#3 4. Bij Adblock Plus klik op Uitschakelen of Verwijderen.

#@firefox-video-downloadhelper
#1 Video DownloadHelper (Firefox add-on)
:
#2  1. Start Firefox webbrowser.
#2  2. Ga naar https://addons.mozilla.org/nl/firefox/addon/video-downloadhelper
#2  3. Klik op Toevoegen aan Firefox.
#2  4. Klik op Toevoegen.
#2  5. Klik op Oké, begrepen.
#2  6. Klik op Video DownloadHelper (symbool bovenin de balk).
#2  7. Klik op Instellingen (tandwielsymbool).
#2  8. Klik op Mede-app niet geinstalleerd.
#2  9. Klik op Mede-app installeren.
#2 10. Klik op Download (onder Linux - 64 bits - deb).
#2 11. Kies Openen met Software-installatie (standaard)
#2 12. Klik op Installeren.
#3 1. Start Firefox webbrowser.
#3 2. Ga naar menu > Add-ons (Ctrl+Shift+A).
#3 3. Klik links op Extensies.
#3 4. Bij Video DownloadHelper klik op Uitschakelen of Verwijderen.
#3 5. Start Terminalvenster en typ, of kopieer en plak:
#3    sudo apt remove net.downloadhelper.coapp

# Einde instellingsbestand
