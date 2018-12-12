#!/usr/bin/python

import smbus, time
import math
import threading

class Gyro(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
        self.address = 0x68       # via i2cdetect
        self.power_mgmt_1 = 0x6b
        # Aktivieren, um das Modul ansprechen zu koennen
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
        try:
            self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
            self.bus.write_byte_data(self.address, 0x1A, 6) #Tiefpasfilter ein
            self.running = True # setting the thread running to true
        except:
            print("Keine Verbindung zum Gyroskop")
            self.running = False
    def read_byte(self,reg):
        return self.bus.read_byte_data(self.address, reg)
    def read_word(self,reg):
        h = self.bus.read_byte_data(self.address, reg)
        l = self.bus.read_byte_data(self.address, reg+1)
        value = (h << 8) + l
        return value 
    def read_word_2c(self,reg):
        val = self.read_word(reg)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
    def dist(self,a,b):
        return math.sqrt((a*a)+(b*b))
    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)
    def get_x_rotation(self,x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)
def read_gyro():
    global bus, address
    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect
    power_mgmt_1 = 0x6b
    # Aktivieren, um das Modul ansprechen zu koennen
    bus.write_byte_data(address, power_mgmt_1, 0)
     
    print ("Gyroskop")
    print ("--------")
     
    gyroskop_xout = gyro.read_word_2c(0x43)
    gyroskop_yout = gyro.read_word_2c(0x45)
    gyroskop_zout = gyro.read_word_2c(0x47)
     
    print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131))
    print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131))
    print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131))
     
    print
    print("Beschleunigungssensor")
    print("---------------------")
     
    beschleunigung_xout = gyro.read_word_2c(0x3b)
    beschleunigung_yout = gyro.read_word_2c(0x3d)
    beschleunigung_zout = gyro.read_word_2c(0x3f)
     
    beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
    beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
    beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
     
    print("beschleunigung_xout: ", ("%6d" % beschleunigung_xout), " skaliert: ", beschleunigung_xout_skaliert)
    print("beschleunigung_yout: ", ("%6d" % beschleunigung_yout), " skaliert: ", beschleunigung_yout_skaliert)
    print("beschleunigung_zout: ", ("%6d" % beschleunigung_zout), " skaliert: ", beschleunigung_zout_skaliert)
     
    print("X Rotation: " , gyro.get_x_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
    print("Y Rotation: " , gyro.get_y_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
    
    
# global gyro, programmStatus
# programmStatus = 1
# gyro = Gyro()

# while programmStatus == 1:
##    read_temp()
    # read_gyro()
    # time.sleep(5)
   
##Programmende durch Veränderung des programmStatus
# print("Programm wurde beendet.")