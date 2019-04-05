from abc import ABC
import inspect

import smbus, time
import math
import threading

###########----------------------------------------###########
class cl_mpu6050(threading.Thread):
    
    #---------------------------------------------------------
    def __init__(self):
        threading.Thread.__init__(self)
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
        self.address = 0x68       # via i2cdetect
        self.power_mgmt_1 = 0x6b
        
        self.mpu6050_dict = None
        self.mpu6050_raw_dict = None
        self.thread_status = True

        try:
            self.bus.write_byte_data(self.address, self.power_mgmt_1, 0) # activate to call module
            self.bus.write_byte_data(self.address, 0x1A, 6) #deeppassfilter on
            self.mpu6050_startthread()
            self.running = True # setting the thread running to true
        except Exception as e:
            print("No connection to gyroscope")
            print(e)
            self.running = False
    
    #---------------------------------------------------------
    def mpu6050_startthread(self):
        self.thread_mpu6050 = threading.Thread(target = self.handle_mpu6050_recieve)
        #thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_mpu6050.setDaemon(True)
        self.thread_mpu6050.start()
    
    #---------------------------------------------------------
    def handle_mpu6050_recieve(self):
        while self.thread_status:
                       
            # print ("gyroscope")
            # print ("---------------------")
             
            gyroskop_xout = self.read_word_2c(0x43)
            gyroskop_yout = self.read_word_2c(0x45)
            gyroskop_zout = self.read_word_2c(0x47)
            
            gyroskop_xout_skaliert = gyroskop_xout / 131
            gyroskop_yout_skaliert = gyroskop_yout / 131
            gyroskop_zout_skaliert = gyroskop_zout / 131
            
            # print("gyroscope_xout: ", ("%5d" % gyroskop_xout), " scaled: ", gyroskop_xout_skaliert)
            # print("gyroscope_yout: ", ("%5d" % gyroskop_yout), " scaled: ", gyroskop_yout_skaliert)
            # print("gyroscope_zout: ", ("%5d" % gyroskop_zout), " scaled: ", gyroskop_zout_skaliert)
             
            # print
            # print("accelerometer")
            # print("---------------------")
             
            beschleunigung_xout = self.read_word_2c(0x3b)
            beschleunigung_yout = self.read_word_2c(0x3d)
            beschleunigung_zout = self.read_word_2c(0x3f)
             
            beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
            beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
            beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
             
            # print("accelerometer_xout: ", ("%6d" % beschleunigung_xout), " scaled: ", beschleunigung_xout_skaliert)
            # print("accelerometer_yout: ", ("%6d" % beschleunigung_yout), " scaled: ", beschleunigung_yout_skaliert)
            # print("accelerometer_zout: ", ("%6d" % beschleunigung_zout), " scaled: ", beschleunigung_zout_skaliert)
             
            # print("x rotation: " , self.get_x_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
            # print("y rotation: " , self.get_y_rotation(beschleunigung_xout_skaliert, beschleunigung_yout_skaliert, beschleunigung_zout_skaliert))
            
            temperatur = self.read_word_2c(0x41)
            temperatur_skaliert = (temperatur / 340.0) + 36.53
            
            timestamp = time.time()
            
            self.mpu6050_raw_dict = {"gyroskop_xout":gyroskop_xout, "gyroskop_yout":gyroskop_yout, "gyroskop_zout":gyroskop_zout, "beschleunigung_xout":beschleunigung_xout, "beschleunigung_yout":beschleunigung_yout, "beschleunigung_zout":beschleunigung_zout, "temperatur":temperatur, "time":timestamp }
            self.mpu6050_dict = {"gyroskop_xout":gyroskop_xout_skaliert, "gyroskop_yout":gyroskop_yout_skaliert, "gyroskop_zout":gyroskop_zout_skaliert, "beschleunigung_xout":beschleunigung_xout_skaliert, "beschleunigung_yout":beschleunigung_yout_skaliert, "beschleunigung_zout":beschleunigung_zout_skaliert, "temperatur":temperatur_skaliert, "time":timestamp }
            #print(self.mpu6050_dict)
            time.sleep(1)
    
    #---------------------------------------------------------
    def get_mpu6050_raw_dict(self):
        return self.mpu6050_raw_dict
    
    #---------------------------------------------------------
    def get_mpu6050_dict(self):
        return self.mpu6050_dict
    
    #---------------------------------------------------------
    def read_byte(self,reg):
        return self.bus.read_byte_data(self.address, reg)
    
    #---------------------------------------------------------
    def read_word(self,reg):
        h = self.bus.read_byte_data(self.address, reg)
        l = self.bus.read_byte_data(self.address, reg+1)
        value = (h << 8) + l
        return value
        
    #---------------------------------------------------------
    def read_word_2c(self,reg):
        val = self.read_word(reg)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
    
    #---------------------------------------------------------
    def dist(self,a,b):
        return math.sqrt((a*a)+(b*b))
    
    #---------------------------------------------------------
    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)
    
    #---------------------------------------------------------
    def get_x_rotation(self,x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)
    
    #---------------------------------------------------------
    def cleanup(self):
        self.thread_status = False

###########----------------------------------------###########
class th_mpu6050(cl_mpu6050):   
    
    #---------------------------------------------------------
    def __init__(self):
        pass

###########----------------------------------------###########
class cl_fact_mpu6050(ABC):
    __o_instance = None
    
    #---------------------------------------------------------
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_mpu6050.__o_instance = i_instance
    
    #---------------------------------------------------------
    @classmethod        
    def get_instance(self):
        if cl_fact_mpu6050.__o_instance is not None:
            return(cl_fact_mpu6050.__o_instance)
        cl_fact_mpu6050.__o_instance = cl_mpu6050()
        return(cl_fact_mpu6050.__o_instance)
    
    #---------------------------------------------------------
    def __init__(self):
        pass