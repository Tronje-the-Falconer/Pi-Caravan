## Raspian

install Raspbian on Pi

than configure it

set Wifi

set i2c

set 1wire

set serial no and yes

     sudo apt-get update && sudo apt-get upgrade

## Git

     sudo apt-get install git git-core

## Hotspotscript

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

    sudo depmod -a
    sudo update-initramfs -u
    sudo nano /etc/modules
    
    
 insert at end of file
 
    snd-bcm2835
    RT5372
    
reboot and wifi should be there

----

## Wiring Pi

    cd /home/pi/
    git clone git://git.drogon.net/wiringPi
    cd wiringPi

install:

    ./build

## Webserver

    sudo apt-get install lighttpd
    sudo groupadd www-data
    sudo usermod -G www-data -a pi
    sudo chown -R www-data:www-data /var/www
    sudo chmod -R 775 /var/www
    sudo lighty-enable-mod auth

    
## PHP

    sudo apt-get install php7.0-common php7.0-cgi php7.0 php7.0-sqlite3
    sudo lighty-enable-mod fastcgi
    sudo lighty-enable-mod fastcgi-php
    sudo service lighttpd force-reload
    sudo apt-get install php7.0-apcu
    sudo nano /etc/php/7.0/mods-available/apcu_bc.ini
    
    extension=apc.so
    apc.enabled=1
    apc.file_update_protection=2
    apc.optimization=0
    apc.shm_size=32M
    apc.include_once_override=0
    apc.shm_segments=1
    apc.gc_ttl=7200
    apc.ttl=7200
    apc.num_files_hint=1024
    apc.enable_cli=0
    
    sudo nano /etc/lighttpd/conf-enabled/15-fastcgi-php.conf
    
    "allow-x-send-file" => "enable"
    
    sudo reboot

## Radio (https://tutorials-raspberrypi.de/raspberry-pi-als-radioempfaenger-benutzen-autoradio-car-pc/)

    sudo nano /etc/modules

insert

    i2c-bcm2708
    i2c-dev

    sudo apt-get install i2c-tools
    
    git clone https://github.com/achilikin/RdSpi && cd RdSpi

Zeile 93 auskommentieren mit /*  */

    sudo nano main.c
    
    /* rpi_pin_export(SI_RESET, RPI_INPUT); */

    make

    sudo nano i2c-init.c

    /* i2c-init.c */
    #include <wiringPi.h>
    
    int main() {
    int resetPin = 23; // GPIO23
    int sdaPin = 0; // GPIO0
    
    /* Setup GPIO access in BCM mode */
    wiringPiSetupGpio();
    
    /* Set pins as output */
    pinMode(resetPin, OUTPUT);
    pinMode(sdaPin, OUTPUT);
    
    /* A low SDA indicates a 2-wire interface */
    digitalWrite(sdaPin, LOW);
    /* Put chip into reset */
    digitalWrite(resetPin, LOW); 
    /* 1ms delay to allow pins to settle */ 
    delay(1);
    /* Bring chip out of reset with SDIO set low
    and SEN pulled high (with pull-up resistor) */
    digitalWrite(resetPin, HIGH); 
    
    return 0;
    }

    gcc -o i2c-init i2c-init.c -lwiringPi

    sudo ./i2c-init

prüfen

    i2cdetect -y 1
    
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: 10 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

testen:

    sudo ./rdspi reset
    sudo ./rdspi tune 95.00
    sudo ./rdspi volume 10

    chmod +x i2c-init
    chmod +x rdspi


    export PATH=$PATH:/home/pi/RdiSpi
    cd /usr/bin
    sudo ln -s /home/pi/RdSpi/i2c-init i2c-init
    sudo ln -s /home/pi/RdSpi/rdspi rdspi

aufruf dann ohne ./ und von überall aus möglich

In Autostart 

    sudo nano /etc/init.d/pi-caravan-radio.sh
    
    #! /bin/sh
    ### BEGIN INIT INFO
    # Provides: pi-caravan-radio.sh
    # Required-Start: $syslog
    # Required-Stop: $syslog
    # Default-Start: 2 3 4 5
    # Default-Stop: 0 1 6
    # Short-Description: pi-caravan-radio init
    # Description:
    ### END INIT INFO

    case "$1" in
        start)
            echo "pi-caravan Radio startet"
            # Starting Programm
            cd /home/pi/RdSpi/
            gcc -o i2c-init i2c-init.c -lwiringPi
            ./i2c-init
            echo "start done"
            ;;
        stop)
            echo "pi-caravan Radio will now shutdown"
            # Ending Programm
            ;;
        *)
            echo "Using: /etc/init.d/pi-ager-radio.sh {start|stop}"
            exit 1
            ;;
    esac

    exit 0  


    sudo chmod 755 /etc/init.d/pi-caravan-radio.sh

test

    sudo /etc/init.d/pi-caravan-radio.sh start
    sudo /etc/init.d/pi-caravan-radio.sh stop

    sudo update-rc.d pi-caravan-radio.sh defaults
