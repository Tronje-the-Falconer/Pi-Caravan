First install raspbian on Pi

than configure it

set Wifi

then

installing git

    sudo apt-get install git

install HotSpot-Skipt from Github (https://github.com/damiencaselli/rpi3-hotspot)

    cd /home/pi/
    git clone https://github.com/damiencaselli/rpi3-hotspot.git

use templatefile to create configurationfile

    sudo nano /home/rpi3-hotspot/boot/hotspot.txt.example
    
set ssid and passphrase

Example:

    ssid=jukebox
    passphrase=12345678

save file as hotspot.txt 

copy file into boot-folder

    sudo cp -u /home/pi/rpi3-hotspot/boot/hotspot.txt /boot/hotspot.txt

edit file interfaces

    sudo nano /home/rpi3-hotspot/etc/network/interfaces
    
insert (like for eth0)

    iface wlan1 inet manual

edit file rpi-access-point

    sudo nano /home/rpi3-hotspot/usr/bin/rpi-access-point

copy and reinsert line 72-82 (section IPTABLES) and set eth0 to wlan1

    if ! iptables -t nat -C POSTROUTING -o wlan1 -j MASQUERADE > /dev/null 2>&1; then
        iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
    fi
    if ! iptables -C FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT > /dev/null 2>&1; then
        iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
    fi
    if ! iptables -C FORWARD -i wlan0 -o wlan1 -j ACCEPT > /dev/null 2>&1; then
        iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT
    fi

edit IP-Adress

    sudo nano /home/rpi3-hotspot/etc/dnsmasq.d/rpi-access-point.conf

change every 10.99.99 to your IP-Choice

    sudo nano /home/rpi3-hotspot/usr/bin/rpi-access-point

change 10.99.99 to your IP-Choice

run installation

    cd /home/rpi3-hotspot
    sudo ./install.sh
    
then reboot

if hotspot doesn't connect on reboot check chipset of usb-wifi (mine is RT5372)

make Blacklist

    sudo nano /etc/modprobe.d/wlan-blacklist.conf
    
insert

    blacklist RT5372
    
then

    sudo depmod -ae
    sudo update-initramfs -u
    sudo nano /etc/modules
    
    
 insert at end of file
 
    snd-bcm2835
    RT5372
    
reboot and wifi should be there
