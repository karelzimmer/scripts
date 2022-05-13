#############################################################################
# Bestand:  install-vnc-server.sh                                           #
# Doel:     Installatiebestand voor VNC Server.                             #
# Gebruik:  Opdrachtregel in een installatiebestand (aanbevolen).           #
#           In het terminalvenster met script install (aanbevolen):         #
#           install ~/bin/install-vnc-server.sh                             #
#           Direct in het terminalvenster:                                  #
#           bash ~/bin/install-vnc-server.sh                                #
#           Een opdrachtregel kan ook uitgevoerd worden door deze eerst     #
#           te kopiëren, en daarna te plakken in het terminalvenster,       #
#           bijvoorbeeld via opdracht 'install -s install-vnc-server.sh'.   #
# Auteur:   Karel Zimmer (http://karelzimmer.nl, info@karelzimmer.nl)       #
# ------------------------------------------------------------------------- #
# Dit werk valt onder een Creative Commons Naamsvermelding-GelijkDelen 4.0  #
# Internationaal licentie (CC BY-SA 4.0).                                   #
# Bezoek http://creativecommons.org/licenses/by-sa/4.0/deed.nl om een kopie #
# te zien van de licentie of stuur een brief naar Creative Commons,         #
# PO Box 1866, Mountain View, CA 94042, USA.                                #
# ------------------------------------------------------------------------- #
# Versies:  1.0.0   2017-02-18  Eerste versie.                              #
#############################################################################
# VERSION_NUMBER=1.2.5
# RELEASE_DATE=2017-06-08

#---------------------------------------------------------------------------#
# VNC Server installeren                                                    #
#---------------------------------------------------------------------------#

#1 [ 1/1 ] Installeer VNC Server - Computer op afstand bedienen
## Versienummerbestand downloaden. Inhoud bijvoorbeeld: 6.0.2
wget --output-document=/tmp/latest \
http://karelzimmer.nl/downloads/apps/vnc-connect/latest

## Architectuurbestand downloaden. Inhoud amd64: x64, i386: x86
wget --output-document=/tmp/arch \
http://karelzimmer.nl/downloads/apps/vnc-connect/$(dpkg --print-architecture)

## Pakket downloaden.
wget --output-document=/tmp/\
VNC-Server-$(cat /tmp/latest)-Linux-$(cat /tmp/arch).deb \
http://karelzimmer.nl/downloads/apps/vnc-connect/vnc-server/\
$(cat /tmp/latest)/\
VNC-Server-$(cat /tmp/latest)-Linux-$(cat /tmp/arch).deb

## Pakket installeren.
sudo dpkg --install /tmp/\
VNC-Server-$(cat /tmp/latest)-Linux-$(cat /tmp/arch).deb

## Opruimen.
rm /tmp/\
VNC-Server-$(cat /tmp/latest)-Linux-$(cat /tmp/arch).deb
#2
#2 Installeer VNC Server - Computer op afstand bedienen
## ----------------------------------------------------
#2 Start Terminalvenster en typ, of kopieer en plak:
#2   sudo systemctl start vncserver-x11-serviced.service
#3
#3 Verwijder VNC Server - Computer op afstand bedienen
## ---------------------------------------------------
#3 Start Terminalvenster en typ, of kopieer en plak:
#3   sudo apt purge realvnc-vnc-server
#3   sudo apt update

# Einde installatiebestand.
