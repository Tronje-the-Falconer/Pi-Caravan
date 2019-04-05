from abc import ABC
import inspect

import smbus, time
import math
import threading

###########----------------------------------------###########
class cl_sht31(threading.Thread):
    
    #---------------------------------------------------------
    def __init__(self, sensor=1):
        threading.Thread.__init__(self)
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
        if sensor == 1:
            self.adress = 0x44      # via i2cdetect
        elif sensor == 2:
            self.adress = 0x45
        else:
            print('Wrong sensor!')
        
        self.sht31_dict = None
        self.sht31_raw_dict = None
        self.thread_status = True
        
        self.sensor_dict = None
        self.cTemp = 0.0
        self.fTemp = 0.0
        self.humidity = 0.0

        try:
            self.sht31_startthread()
            self.running = True # setting the thread running to true
        except Exception as e:
            print("No connection to sht31")
            print(e)
            self.running = False
    
    #---------------------------------------------------------
    def sht31_startthread(self):
        self.thread_sht31 = threading.Thread(target = self.handle_sht31_recieve)
        #thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_sht31.setDaemon(True)
        self.thread_sht31.start()
    
    #---------------------------------------------------------
    def handle_sht31_recieve(self):
        while self.thread_status:
            
            # print ("sht31")
            # print ("---------------------")
            
            self.write_block()
            data = self.read_block()
            
            # Convert the data
            temp = data[0] * 256 + data[1]
            self.cTemp = -45 + (175 * temp / 65535.0)
            self.fTemp = -49 + (315 * temp / 65535.0)
            self.humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
            
            
            timestamp = time.time()
            self.sensor_dict = {"temperature_c":self.cTemp, "temperature_f":self.fTemp, "humidity":self.humidity, "timestamp":timestamp}
            # Output data to screen
            # print("Temperature in Celsius is : %.2f C" %self.cTemp)
            # print("Temperature in Fahrenheit is : %.2f F" %self.fTemp)
            # print("Relative Humidity is : %.2f %%RH" %self.humidity)
    
    #---------------------------------------------------------
    def get_sht31_dict(self):
        return self.sensor_dict
    
    #---------------------------------------------------------
    def read_block(self):
        # Read data back from 0x00(00), 6 bytes
        # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
        return self.bus.read_i2c_block_data(self.adress, 0x00, 6)
    
    #---------------------------------------------------------
    def write_block(self):
        self.bus.write_i2c_block_data(self.adress, 0x2C, [0x06])
        time.sleep(0.5)
    
    #---------------------------------------------------------
    def cleanup(self):
        self.thread_status = False

###########----------------------------------------###########
class th_sht31(cl_sht31):   
    
    #---------------------------------------------------------
    def __init__(self):
        pass

###########----------------------------------------###########
class cl_fact_sht31(ABC):
    __o_instance = None
    
    #---------------------------------------------------------
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_sht31.__o_instance = i_instance
    
    #---------------------------------------------------------
    @classmethod        
    def get_instance(self, sensor):
        if cl_fact_sht31.__o_instance is not None:
            return(cl_fact_sht31.__o_instance)
        cl_fact_sht31.__o_instance = cl_sht31(sensor=1)
        return(cl_fact_sht31.__o_instance)
    
    #---------------------------------------------------------
    def __init__(self):
        pass
    
# test = cl_fact_sht31.get_instance(2)    
# while 1:
    # a=1