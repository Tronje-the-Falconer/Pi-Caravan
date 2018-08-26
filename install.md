
HotSpot Projekt von Github
https://github.com/damiencaselli/rpi3-hotspot
Dank an damiencaselli
Funktionsumfang
Der Pi wird per Netzwerkkabel an einem vorhanden Router mit Zugang zum Internet angeschlossen. 
Der Pi erzeugt mit Hilfe des integrierten WLAN-Moduls ein weiteres Funk-Netzwerk, welches eigene 
IP-Adressen an die Klienten vergibt (eigener DHCP-Server). Das Gerät verbindet die über WLAN 
angemeldeten Geräte mit dem Internet des externen Routers. Somit haben die Geräte, welche am 
WLAN-Modul / HotSpot des Pis angemeldet sind auch Zugriff auf das Internet.
Erweiterung
Durch die Erweiterung mit einem USB-WLAN-Modul und der weiter unten angegebenen 
Routingeinträge, muss nicht zwingend der Internetzugriff durch ein Kabel erfolgen, sondern kann 
auch durch das zweite WLAN-Modul erfolgen.
Ggf. Zusätzliches WLAN-Modul
tinxi® 150M Raspberry Pi USB WiFi Wireless LAN IEEE802.11 N / G / B Adapter WiFi Network Dongle
Chipsatz: REALTEK RTL8188CUS
Schnittstelle: USB 2.0 High Speed
Geschwindigkeit: 150Mbps
Hinweis
Was in Kursiv geschrieben ist sind Befehle, die direkt über SSH in die Konsole eingetragen werden 
können oder in einem Terminalfenster. Wenn der Zugriff über SSH mit z.B. Putty erfolgt, kann man 
diese Befehle markieren und kopieren und durch einen Klick mit der rechten Maustaste in Putty 
direkt eingefügt werden.
Zuvor muss natürlich Raspbian installiert werden!
1. Installation Git (Meist schon vorhanden)
sudo apt-get install git
2. Herunterladen HotSpot-Skipt von Github

Wechseln in das Home Verzeichnis
cd /home/pi/
git clone https://github.com/damiencaselli/rpi3-hotspot.git
3. Bearbeitung der Beispieldatei, um den HotSpot zu benennen und ein Passwort zu vergeben.
Das geht am besten auf dem Desktop des Pis. 
Einfach ins Home-Verzeichnis, dann den Ordner /rpi3-hotspot/ und den folgenden Ordner /boot/
öffnen und darin die Datei /hotspot.txt.example öffnen.
Nach „ssid=“ können wir jeden Namen verwenden. Nach “passphase=” gibt man das gewünschte
Passwort für das WLAN-Netzwerk ein.
Also z.B.
ssid=jukebox
passphrase=12345678
Jetzt die Datei Speichern mit folgendem Namen:
hotspot.txt
Diese Datei muss in das /boot/- Verzeichnis auf dem Pi kopiert werden. Dies über Putty oder im 
Terminal machen.
In das Verzeichnis der gerade erstellten Datei wechseln.
cd /home/pi/rpi3-hotspot/boot/
Kopieren nach /boot/
sudo cp -u hotspot.txt /boot/hotspot.txt
4. Erweiterung durch zusätzlichen USB-WLAN-Stick (Rot nur mit zusätzlichem Wlan-Stick)
Ich habe mit dem Hotspot vor, dass dieser das Internet, was er an dem Ethernet Anschluss und an 
einem zusätzlichen USB-WLAN-Stick bekommt zu nutzen. 
Meine Intension war, dass ich immer Zugriff auf dem Pi erhalte z.B. mit dem Handy und diesem, 
wenn ich unterwegs bin einen Internetzugriff über ein fremdes WLAN-Netzwerk gebe kann. Der Pi 
macht nun seinen HotSpot auf und ich kann mich über VNC auf den Desktop einwählen und dort am 
zweiten WLAN-USB-Stick ein neues Wlan-Netzwerk wählen, damit dieses genutzt wird für die 
Internetverbindung.
Dafür in der Datei im Ordner rpi3-hotspot/etc/network/interfaces folgendes hinzufügen
Iface wlan1 inet manuel

Wie es zuvor für eth0 schon enthalten ist.
5. Weitere Anpassung in der Datei „rpi-access-point“ im Verzeichnis rpi3-hotspot/usr/bin/
Hier muss IPTABLES erweitert werden. Damit wird das Internet an wlan1 auch zu wlan0 
weitergegeben. In Zeile 72-82 steht folgendes (grün):
if ! iptables -t nat -C POSTROUTING -o eth0 -j MASQUERADE > /dev/null 2>&1; then
 iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
 fi
 if ! iptables -C FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT > 
/dev/null 2>&1; then
 iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
 fi
 if ! iptables -C FORWARD -i wlan0 -o eth0 -j ACCEPT > /dev/null 2>&1; then
 iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
 fi
Einfach die Zeilen kopieren und überall dort wo in den kopierten Zeilen eth0 steht wlan1 eintragen.
Hier das fertige Beispiel:
if ! iptables -t nat -C POSTROUTING -o eth0 -j MASQUERADE > /dev/null 2>&1; then
 iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
 fi
 if ! iptables -C FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT > 
/dev/null 2>&1; then
 iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
 fi
 if ! iptables -C FORWARD -i wlan0 -o eth0 -j ACCEPT > /dev/null 2>&1; then
 iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
 fi
 if ! iptables -t nat -C POSTROUTING -o wlan1 -j MASQUERADE > /dev/null 2>&1; then
 iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
 fi
 if ! iptables -C FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT > 
/dev/null 2>&1; then
 iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
 fi
 if ! iptables -C FORWARD -i wlan0 -o wlan1 -j ACCEPT > /dev/null 2>&1; then
 iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT
 fi
 
 6. Installationsskript ausführen
Wechsel zum Verzeichnis
cd rpi3-hotspot
sudo ./install.sh
7. Neustart.
8. Jetzt kann man den HotSpot testen.
9. Jetzt kann man, wenn man einen zusätzlichen Wlan-Stick am Pi hat, sich auch zusätzlich mit 
einem anderen WLAN-Netzwerk verbinden, welches in der Umgebung ist. Über z.B. VNC oder 
SSH kann man die Netzwerke in seiner Umgebung suchen und mit dem entsprechenden 
verbinden.
Weitere Einstellungen
In der Datei “rpi3-hotspot/etc/dnsmasq.d/rpi-access-point.conf“ kann die IP-Adresse des HotSpot,
sowie der IP-Adressenbereich der verbundenen Klienten eingestellt werden.
Standard ist
10.99.99.1
DHCP-Range 10.99.99.2 – 10.99.99.51
Auch muss die Datei „rpi-access-point“ angepasst werden, wo die IP enthalten ist.
Nach diesen Einstellungen muss aber alles gelöscht werden und das Skript neu ausgeführt werden.
sudo systemctl stop rpi-access-point
sudo systemctl disable rpi-access-point
sudo rm /etc/systemd/system/rpi-access-point.service /usr/bin/rpi-access-point
sudo systemctl daemon-reload
