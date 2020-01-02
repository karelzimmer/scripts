# shellcheck shell=bash
# ##############################################################################
# Bestand:  setup-ubuntu-18.04-desktop.sh
# Doel:     Instellingsbestand voor Ubuntu 18.04 LTS desktop
# Gebruik:  In het terminalvenster met script setup (aanbevolen):
#           setup /usr/local/bin/setup-ubuntu-18.04-desktop.sh
#      of:  Direct in het terminalvenster:
#           bash /usr/local/bin/setup-ubuntu-18.04-desktop.sh
#      of:  Kopieer een opdrachtregel en plak deze in het terminalvenster,
#           bijvoorbeeld via opdracht:
#           setup -s /usr/local/bin/setup-ubuntu-18.04-desktop.sh
# Auteur:   Karel Zimmer (https://karelzimmer.nl, info@karelzimmer.nl)
# ------------------------------------------------------------------------------
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0
# Internationaal licentie (CC BY-SA 4.0).
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie te
# zien van de licentie of stuur een brief naar Creative Commons, PO Box 1866,
# Mountain View, CA 94042, USA.
# ##############################################################################
# REL_NUM=02.17.05
# REL_DAT=2019-12-07
# REL_MSG='Invoering changelog in pakket scripts'

# Voor het opzoeken van gebruikersinstellingen zie Linux-info.txt
# ------------------------------------------------------------------------------
# Gebruikersinstellingen wijzigen
# ------------------------------------------------------------------------------
#@communitheme
#1 Communitheme/Yaru uiterlijk aanpassen voor Gnome
:
#2 Met snap (standaard):
#2 ~~~~~~~~~~~~~~~~~~~~~
#2 Klik voor het aanloggen op het Tandwielsymbool en kies
#2 'Ubuntu met communitheme snap'.
#2
#2 Met PPA:
#2 ~~~~~~~~
#2 1. Start Terminalvenster en typ, of kopieer en plak:
#2    gsettings set org.gnome.desktop.interface gtk-theme 'Communitheme'
#2    gsettings set org.gnome.desktop.interface cursor-theme 'Suru'
#2    gsettings set org.gnome.desktop.interface icon-theme 'Suru'
#2 2. Klik voor het aanloggen op het Tandwielsymbool en kies
#2    'Ubuntu Communitheme on Xorg'.
#3 Met snap (standaard):
#3 ~~~~~~~~~~~~~~~~~~~~~
#3 Klik voor het aanloggen op het Tandwielsymbool en kies 'Ubuntu'.
#3
#3 Met PPA:
#3 ~~~~~~~~
#3 1. Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.desktop.interface gtk-theme
#3    gsettings reset org.gnome.desktop.interface cursor-theme
#3    gsettings reset org.gnome.desktop.interface icon-theme
#3 2. Klik voor het aanloggen op het Tandwielsymbool en kies 'Ubuntu'.

#@gnome
#1 Gnome aanpassen
gsettings set org.gnome.desktop.calendar show-weekdate true
gsettings set org.gnome.desktop.interface clock-show-date true
gsettings set org.gnome.desktop.interface show-battery-percentage true
gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true
gsettings set org.gnome.desktop.screensaver lock-enabled false
gsettings set org.gnome.desktop.wm.keybindings switch-applications []
gsettings set org.gnome.desktop.wm.keybindings switch-applications-backward []
gsettings set org.gnome.desktop.wm.keybindings switch-windows "['<Alt>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-windows-backward "['<Shift><Alt>Tab']"
gsettings set org.gnome.nautilus.desktop trash-icon-visible false
gsettings set org.gnome.nautilus.preferences click-policy 'single'
gsettings set org.gnome.settings-daemon.peripherals.touchscreen orientation-lock true
gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true
gsettings set org.gnome.settings-daemon.plugins.power idle-dim false
gsettings set org.gnome.settings-daemon.plugins.power power-button-action 'interactive'
if [[ $(gsettings get org.gnome.shell favorite-apps) == *[ ]]; then gsettings set org.gnome.shell favorite-apps "['yelp.desktop']"; fi
gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed --expression="s/, 'evolution.desktop'//")"
gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed --expression="s/, 'org.gnome.Photos.desktop'//")"
gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed --expression="s/, 'rhythmbox.desktop'//")"
gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed --expression="s/, 'ubuntu-amazon-default.desktop'//")"
gsettings set org.gnome.Terminal.Legacy.Settings new-terminal-mode 'tab'
touch "$HOME/Sjablonen/Platte_tekst"
#2 1. Pas de aanmeldfoto van <gebruiker> aan via het Activiteitenoverzicht,
#2    zoek use en klik op Users.
#2 2. Aan de rechterkant, klik links naast <gebruiker> en selecteer een
#2    aanmeldfoto (of neem een foto indien mogelijk).
#2 3. Sluit Gebruikers af.
#3 Start Terminalvenster en typ, of kopieer en plak:
#3    gsettings reset org.gnome.desktop.calendar show-weekdate
#3    gsettings reset org.gnome.desktop.interface clock-show-date
#3    gsettings reset org.gnome.desktop.interface show-battery-percentage
#3    gsettings reset org.gnome.desktop.peripherals.touchpad tap-to-click
#3    gsettings reset org.gnome.desktop.screensaver lock-enabled
#3    gsettings reset org.gnome.desktop.wm.keybindings switch-applications
#3    gsettings reset org.gnome.desktop.wm.keybindings switch-applications-backward
#3    gsettings reset org.gnome.desktop.wm.keybindings switch-windows
#3    gsettings reset org.gnome.desktop.wm.keybindings switch-windows-backward
#3    gsettings reset org.gnome.nautilus.desktop trash-icon-visible
#3    gsettings reset org.gnome.nautilus.preferences click-policy
#3    gsettings reset org.gnome.settings-daemon.peripherals.touchscreen orientation-lock
#3    gsettings reset org.gnome.settings-daemon.plugins.color night-light-enabled
#3    gsettings reset org.gnome.settings-daemon.plugins.power idle-dim
#3    gsettings reset org.gnome.settings-daemon.plugins.power power-button-action
#3    gsettings reset org.gnome.shell favorite-apps
#3    gsettings reset org.gnome.Terminal.Legacy.Settings new-terminal-mode
#3    rm --force "$HOME/Sjablonen/Platte_tekst"

#@firefox
#1 Firefox webbrowser
:
#2 1. Start Firefox webbrowser.
#2 2. Activeer enkelklik om het internetadres te selecteren via adres
#2    about:config en typ achter Zoeken click.
#2    Dubbelklik op de regel browser.urlbar.clickSelectsAll (waarde wordt true).
#2 3. Stel de startpagina in via menu > Voorkeuren > Algemeen.
#2 4. Wijzig PDF-lezer via menu > Voorkeuren > Bestanden en Toepassingen.
#2    Zoek pdf en achter Portable Document Format (PDF) selecteer
#2    Documentweergave gebruiken (Standaard).
#2 5. Om Netflix te kijken, ga naar menu > Opties > Inhoud.
#2    Schakel het vakje naast DRM-inhoud afspelen uit en weer in.
#2    Als het vakje naast DRM-inhoud afspelen niet is ingeschakeld, schakel deze
#2    in.
#2 6. Herstart Firefox.

#@google-chrome
#1 Google Chrome webbrowser
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='google-chrome.desktop'; then gsettings set org.gnome.shell favorite-apps "['google-chrome.desktop', ""$(gsettings get org.gnome.shell favorite-apps | awk -F[ '{print $2}')"; fi

#@gnome-shell-integratie
#1 GNOME Shell integratie voor Firefox en Chrome
:
#2 Firefox (add-on):
#2 ~~~~~~~~~~~~~~~~~
#2 1. Start Firefox browser.
#2 2. Ga naar https://addons.mozilla.org/nl/firefox/addon/gnome-shell-integration
#2 3. Klik op + Toevoegen aan Firefox.
#2 4. Klik op Toevoegen.
#2 5. Klik op Oké, begrepen.
#2
#2 Chrome (extensie):
#2 ~~~~~~~~~~~~~~~~~~
#2 6. Start Google Chrome.
#2 7. Ga naar https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep
#2 8. Klik op Toev. aan Chrome.
#2 9. Klik op Extensie toevoegen.
#3 Firefox (add-on):
#3 ~~~~~~~~~~~~~~~~~
#3 1. Start Firefox webbrowser.
#3 2. Ga naar about:addons
#3 3. Bij Gnome-shell-integratie klik op ... en kies Uitschakelen of Verwijderen.
#3
#3 Chrome (extensie):
#3 ~~~~~~~~~~~~~~~~~~
#3 4. Start Google Chrome
#3 5. Ga naar chrome://extensions/
#3 6. Bij Gnome-shell-integratie zet schuifje op uit of klik op Verwijderen.

#@libreoffice
#1 LibreOffice kantoorpakket
:
#2 1. Start een LibreOffice-app of open een LibreOffice-document.
#2 2. Ga naar Extra > Opties > Laden/Opslaan > Algemeen.
#2 3. Selecteer onder Standaard bestandsindeling en ODF-instellingen:
#2
#2    Documenttype    Altijd opslaan als
#2    -------------   ----------------------------------
#2    Tekstdocument   Microsoft Word 2007-2013 XML
#2    Werkblad        Microsoft Excel 2007-2013 XML
#2    Presentatie     Microsoft PowerPoint 2007-2013 XML
#2
#2 4. Klik op OK en sluit LibreOffice af.

#@password-safe
#1 Password Safe wachtwoordkluis
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='org.gnome.PasswordSafe.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'org.gnome.PasswordSafe.desktop']"; fi

#@skype
#1 Skype beeldbellen over internet
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='skype_skypeforlinux.desktop'; then gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | awk -F] '{print $1}')"", 'skype_skypeforlinux.desktop']"; fi

#@thunderbird
#1 Mozilla Thunderbird e-mail/nieuws
if ! gsettings get org.gnome.shell favorite-apps | grep --quiet --regexp='thunderbird.desktop'; then gsettings set org.gnome.shell favorite-apps "['thunderbird.desktop', ""$(gsettings get org.gnome.shell favorite-apps | awk -F[ '{print $2}')"; fi
#2 ** Voor het instellen van een Gmail-account **
#2 1. Start Mozilla Thunderbird e-mail/nieuws.
#2 2. Ga naar menu > Voorkeuren > Voorkeuren > Geavanceerd > Algemeen (tab).
##    https://support.google.com/mail/thread/4528103?msgid=18212232:
#2 3. Klik op Configuratie-editor en zoek naar:
#2    general.useragent.compatMode.firefox
#2 4. Dubbelklik op deze regel zodat Waarde wijzigt naar true.
#2 5. Klik op OK.
#2 6. Sluit scherm about:config.
#2 7. Klik op Sluiten.
#2 8. Sluit Thunderbird e-mail/nieuws.

# Einde instellingsbestand
