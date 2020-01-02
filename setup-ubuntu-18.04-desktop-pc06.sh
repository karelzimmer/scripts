# shellcheck shell=bash
# ##############################################################################
# Bestand:  setup-ubuntu-18.04-desktop-pc06.sh
# Doel:     Instellingsbestand voor Ubuntu 18.04 LST desktop op pc06
# Gebruik:  In het terminalvenster met script setup (aanbevolen):
#           setup /usr/local/bin/setup-ubuntu-18.04-desktop-pc06.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/setup-ubuntu-18.04-desktop-pc06.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           setup -s /usr/local/bin/setup-ubuntu-18.04-desktop-pc06.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.08.08
# REL_DAT=2019-12-19
# REL_MSG='Beschrijving icaclient gewijzigd'

# ------------------------------------------------------------------------------
# Gebruikersinstellingen wijzigen
# ------------------------------------------------------------------------------
#@schermbeveiliging
#1 Schermbeveiliging wijzigen
gsettings set org.gnome.desktop.screensaver lock-enabled true

#@backintime
#1 BackInTime back-upprogramma (snapshots)
:
#2 1. Start Back In Time.
#2 2. Klik op  Instellingen (schroevendraaier/sleutel-symbool).
#2 3. Klik op Algemeen (tab).
#2 4. Bij Waar wilt u de resvervekopie opslaan kies /home/karel en maak
#2    map snapshots aan,
#2    bij Planning kies Elke 10 minuten.
#2 5. Klik op Opnemen (tab) en voeg de volgende mappen toe:
#2    /home/karel/Documenten/Checklists
#2    /home/karel/scripts
#2 6. Klik op Uitsluiten (tab) en vervolgens op Standaardwaarde toevoegen.
#2 7. Klik op OK.
#2 8. Klik op Reservekopie maken (harde schijf-symbool).
#2 9. Wacht tot kopie gereed (zie voortgang onderin) en sluit Back In Time af.

#@bluefish
#1 Bluefish web en programmeurs-editor
:
#2 1. Start Bluefish.
#2 2. Zet via Bewerken > Voorkeuren > Initiele document instellingen de
#2    Tab breedte op 4 en vink aan
#2    Gebruik spaties voor inspringen, geen tabs.

#@gedit
#1 Gedit teksteditor
gsettings set org.gnome.gedit.plugins active-plugins "['sort','spell','smartspaces','changecase','zeitgeistplugin','filebrowser','docinfo','time','codecomment','modelines']"
gsettings set org.gnome.gedit.preferences.editor bracket-matching true
gsettings set org.gnome.gedit.preferences.editor display-line-numbers true
gsettings set org.gnome.gedit.preferences.editor display-right-margin true
gsettings set org.gnome.gedit.preferences.editor highlight-current-line true
gsettings set org.gnome.gedit.preferences.editor insert-spaces true
gsettings set org.gnome.gedit.preferences.editor right-margin-position 80
gsettings set org.gnome.gedit.preferences.editor tabs-size 4
gsettings set org.gnome.gedit.preferences.editor wrap-last-split-mode 'char'
gsettings set org.gnome.gedit.preferences.editor wrap-mode 'char'
gsettings set org.gnome.gedit.preferences.print print-font-body-pango 'Monospace 8.5'
gsettings set org.gnome.gedit.preferences.print print-header true
gsettings set org.gnome.gedit.preferences.print print-line-numbers 1
gsettings set org.gnome.gedit.preferences.print print-syntax-highlighting true
gsettings set org.gnome.gedit.preferences.print print-wrap-mode 'char'
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='org.gnome.gedit.desktop'; then gsettings set org.gnome.shell favorite-apps "['org.gnome.gedit.desktop', ""$(gsettings get org.gnome.shell favorite-apps | awk -F[ '{print $2}')"; fi
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.gedit.plugins active-plugins
#3    gsettings reset org.gnome.gedit.preferences.editor bracket-matching
#3    gsettings reset org.gnome.gedit.preferences.editor display-line-numbers
#3    gsettings reset org.gnome.gedit.preferences.editor display-right-margin
#3    gsettings reset org.gnome.gedit.preferences.editor highlight-current-line
#3    gsettings reset org.gnome.gedit.preferences.editor insert-spaces
#3    gsettings reset org.gnome.gedit.preferences.editor right-margin-position
#3    gsettings reset org.gnome.gedit.preferences.editor tabs-size
#3    gsettings reset org.gnome.gedit.preferences.editor wrap-last-split-mode
#3    gsettings reset org.gnome.gedit.preferences.editor wrap-mode
#3    gsettings reset org.gnome.gedit.preferences.print print-font-body-pango
#3    gsettings reset org.gnome.gedit.preferences.print print-header
#3    gsettings reset org.gnome.gedit.preferences.print print-line-numbers
#3    gsettings reset org.gnome.gedit.preferences.print print-syntax-highlighting
#3    gsettings reset org.gnome.gedit.preferences.print print-wrap-mode

#@icaclient
#1 Citrix Workspace app telewerken (v/h Citrix Receiver, aka ICA Client)
xdg-mime default wfica.desktop application/x-ica
#2 1. Start Firefox webbrowser.
#2 2. Ga naar menu > Voorkeuren > Bestanden en Toepassingen.
#2 3. Zoek ica en zorg dat bij Citrix ICA-instellingen is geselecteerd
#2    Citrix Receiver Engine gebruiken.
#2 4. Ga naar https://telewerkportaal.rabobank.nl, log in, en stel vast dat
#2    het inloggen op het Telewerkportaal werkt.

#@keepass
#1 KeePassXC wachtwoordkluis
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='keepassxc_keepassxc.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'keepassxc_keepassxc.desktop']"; fi

#@kvm
#1 KVM virtualisatieprogramma
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='virt-manager.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'virt-manager.desktop']"; fi

#@spotify
#1 Spotify online muziekservice
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='spotify_spotify.desktop'; then gsettings set org.gnome.shell favorite-apps "['spotify_spotify.desktop', ""$(gsettings get org.gnome.shell favorite-apps | awk -F[ '{print $2}')"; fi
#2 1. Start Spotify.
#2 2. Ga naar Edit (Bewerken) en vervolgens naar Preferences (Voorkeuren).
#2 3. Zet Language (Taal) op Nederlands (Dutch).
#2 4. Herstart Spotify.

#@terminal
#1 GNOME Terminal
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='org.gnome.Terminal.desktop'; then gsettings set org.gnome.shell favorite-apps "['org.gnome.Terminal.desktop', ""$(gsettings get org.gnome.shell favorite-apps | awk -F[ '{print $2}')"; fi
#2 1. Start Terminalvenster.
#2 2. Ga naar Bewerken > Voorkeuren.
#2 3. Onder Profielen klik op Naamloos.
#2 4. Vul in achter Oorspronkelijke afmeting van de terminal:
#2    206 kolommen en 62 rijen, en klik op Sluiten.

#@thunderbird-google-calendar
#1 Provider for Google Calendar (Thunderbird add-on)
:
#2 1. Start Thunderbird.
#2 2. Ga naar menu > Add-ons > Add-ons.
#2 3. Zoek naar agenda.
#2 4. Achter 'Provider for Google Calendar' klik op + Toevoegen aan Thunderbird.
#2 5. Klik op Nu installeren.
#2 6. Klik op Nu herstarten.
#2 7. Ga naar menu > Add-ons > Provider for Google Agenda.
#2 8. Voer het Google e-mailadres en wachtwoord in, en geef toestemming.
#3 1. Start Thunderbird.
#3 2. Ga naar menu > Add-ons > Add-ons.
#3 3. Bij Provider for Google Agenda klik op Uitschakelen of Verwijderen.

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

#@virtualbox
#1 VirtualBox virtualisatieprogramma
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='virtualbox.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'virtualbox.desktop']"; fi
#2 1. Ga naar Apparaten > Installeren Guest Additions en volg de aanwijzingen
#2    op het scherm.
#2 2. Voor optimale netwerksnelheid kies bij Netwerk voor Gekoppeld aan:
#2    Netwerk bridge adapter.
#3 Verwijder map VirtualBox VMs in de Persoonlijke map.

#@vscodium
#1 VSCodium 100% open source Visual Studio Code
:
#2 1. Toon rechter kantlijn via Manage > Settings > zoek naar ruler.
#2 2. Klik op Edit in settings.json.
#2 3. Voeg de volgende regel toe na '{':
#2    "editor.rulers": [80],

#@webmin
#1 Webmin web-gebaseerd admin tool
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='webmin.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'webmin.desktop']"; fi
#2 1. Log aan Webmin (http://<IP-nummer>:10000).
#2 2. Ga naar Webmin > Change Language and Theme (Wijzigen van Taal en
#2    Thema).
#2 3. Klik op Personal choice (Persoonlijke keuze) en selecteer
#2    Dutch (NL.UTF-8).
#2 4. Log af en weer aan Webmin.

#1 Bureaubladachtergrond wijzigen
gsettings set org.gnome.desktop.background picture-uri 'file:///usr/share/backgrounds/scripts/gnome.png'
gsettings set org.gnome.desktop.screensaver picture-uri 'file:///usr/share/backgrounds/scripts/gnome.png'
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.desktop.background picture-uri
#3    gsettings reset org.gnome.desktop.screensaver picture-uri

# Einde instellingsbestand
