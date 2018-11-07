#!/usr/bin/python
# coding=utf-8
# messprogramm.py
#------------------------------------------------------------

import os, sys, time
import smbus
import math

# Global für vorhandene Temperatursensoren
tempSensorBezeichnung = [] #Liste mit den einzelnen Sensoren-Kennungen
tempSensorAnzahl = 0 #INT für die Anzahl der gelesenen Sensoren
tempSensorWert = [] #Liste mit den einzelnen Sensor-Werten

# Global für Programmstatus / 
programmStatus = 1 

def ds1820einlesen():
    global tempSensorBezeichnung, tempSensorAnzahl, programmStatus
    #Verzeichnisinhalt auslesen mit allen vorhandenen Sensorbezeichnungen 28-xxxx
    try:
        for x in os.listdir("/sys/bus/w1/devices"):
            if (x.split("-")[0] == "28") or (x.split("-")[0] == "10"):
                tempSensorBezeichnung.append(x)
                tempSensorAnzahl = tempSensorAnzahl + 1
    except:
        # Auslesefehler
        print("Der Verzeichnisinhalt konnte nicht ausgelesen werden.")
        programmStatus = 0

def ds1820auslesen():
    global tempSensorBezeichnung, tempSensorAnzahl, tempSensorWert, programmStatus
    x = 0
    try:
        # 1-wire Slave Dateien gem. der ermittelten Anzahl auslesen 
        while x < tempSensorAnzahl:
            dateiName = "/sys/bus/w1/devices/" + tempSensorBezeichnung[x] + "/w1_slave"
            file = open(dateiName)
            filecontent = file.read()
            file.close()
            # Temperaturwerte auslesen und konvertieren
            stringvalue = filecontent.split("\n")[1].split(" ")[9]
            sensorwert = float(stringvalue[2:]) / 1000
            temperatur = '%6.2f' % sensorwert #Sensor- bzw. Temperaturwert auf 2 Dezimalstellen formatiert
            tempSensorWert.insert(x,temperatur) #Wert in Liste aktualisieren
            x = x + 1
    except:
        # Fehler bei Auslesung der Sensoren
        print("Die Auslesung der DS1820 Sensoren war nicht möglich.")
        programmStatus = 0

################################################### Gyro
def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)#############################################
def initialize():
    ##### temp
    #Programminitialisierung
    ds1820einlesen() #Anzahl und Bezeichnungen der vorhandenen Temperatursensoren einlesen
    
    ##### gyro
    global power_mgmt_1
    global power_mgmt_2
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

def read_temp():
    x = 0
    ds1820auslesen()
    print("Sensorbezeichnung und Temperaturwert:")
    while x < tempSensorAnzahl:
        print (tempSensorBezeichnung[x] , " " , tempSensorWert[x] , " °C")
        x = x + 1
    time.sleep(.5)
    print("\n")
    
def read_gyro():
    global bus
    global address
    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect
     
    # Aktivieren, um das Modul ansprechen zu koennen
    bus.write_byte_data(address, power_mgmt_1, 0)
     
    print("Gyroskop")
    print("--------")
     
    gyroskop_xout = read_word_2c(0x43)
    gyroskop_yout = read_word_2c(0x45)
    gyroskop_zout = read_word_2c(0x47)
     
    print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131))
    print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131))
    print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131))
     
    print()
    print("Beschleunigungssensor")
    print("---------------------")
     
    beschleunigung_xout = read_word_2c(0x3b)
    beschleunigung_yout = read_word_2c(0x3d)
    beschleunigung_zout = read_word_2c(0x3f)
     
    beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
    beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
    beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
     
    print("beschleunigung_xout: ", ("%6d" % beschleunigung_xout), " skaliert: ", beschleunigung_xout_skaliert)
    print("beschleunigung_yout: ", ("%6d" % beschleunigung_yout), " skaliert: ", beschleunigung_yout_skaliert)
    print("beschleunigung_zout: ", ("%6d" % beschleunigung_zout), " skaliert: ", beschleunigung_zout_skaliert)
     
    print("X Rotation: " , get_x_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
    print("Y Rotation: " , get_y_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))

initialize()

# Temperaturausgabe in Schleife
while programmStatus == 1:
    read_temp()
    read_gyro()
   
# Programmende durch Veränderung des programmStatus
print("Programm wurde beendet.")
