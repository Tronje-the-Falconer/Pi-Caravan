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

    sudo depmod -a
    sudo update-initramfs -u
    sudo nano /etc/modules
    
    
 insert at end of file
 
    snd-bcm2835
    RT5372
    
reboot and wifi should be there

----

Wiring Pi

sudo apt-get update && sudo apt-get upgrade

GIT
    sudo apt-get install git git-core


    git clone git://git.drogon.net/wiringPi
    cd wiringPi

install:

    ./build

Webserver
[FEHLT]

Radio (https://tutorials-raspberrypi.de/raspberry-pi-als-radioempfaenger-benutzen-autoradio-car-pc/)

    sudo raspi-config

activate “I2C"

    sudo nano /etc/modules

insert

    i2c-bcm2708
    i2c-dev


    sudo apt-get update
    sudo apt-get install i2c-tools
    
Software

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

In Autostart [FEHLT]

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
