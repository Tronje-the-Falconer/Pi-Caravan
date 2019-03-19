from abc import ABC
import inspect

import glob, os, sys, time
import threading

import numpy as np
 
class cl_1wire_temperature(threading.Thread):
    def __init__(self, base_path= '/sys/bus/w1/devices/', 
                     file_name='/w1_slave', sensorid='28*', default=99.9):
        threading.Thread.__init__(self)
        self.default = default #private
        self.sensorid = sensorid #private
        self.sensortemperature_dict = None
        self.thread_status = True
 
        try:
            self.sensor_path = glob.glob(base_path + self.sensorid)[0] + file_name
            self.temperaturesensor_startthread()
        except:
            print("Bad sensor path " + self.sensorid)
            
    def temperaturesensor_startthread(self):
        self.thread_temperaturesensor = threading.Thread(target = self.handle_temperature_recieve)
        #thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_temperaturesensor.setDaemon(True)
        self.thread_temperaturesensor.start()
        
        
    def handle_temperature_recieve(self):
        while self.thread_status:
            sensortemperature = self.read_temperature()
            timestamp = time.time()
            self.sensortemperature_dict = {"temperature":sensortemperature, "timestamp":timestamp,"sensor":self.sensorid}
    
    def get_temperature(self):
        if self.sensortemperature_dict == None:
            fake = {"temperature":99.9, "timestamp":0,"sensor":"None"}
            return fake
        else:
            return self.sensortemperature_dict
    
    def read_temperature(self):
        temperature = self.default
 
        try:           
            with open(self.sensor_path, 'r') as f:
                data = f.read()
 
                if 'YES\n' not in data:
                    raise Exception()
                temperature = round(float(data.rsplit('t=',1)[1])/1000, 1)    
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print("Can't read temperature sensor!")
            print(e)
        return float(temperature) 
 
    def log_temperature(self, interval=5.0):
        temperatures = []
        temperatures.append(self.get_temperature())
        print(self.sensorid, 'Temperature: ' + str(temperatures[-1]))

        # while True:
            # time.sleep(interval)
            # temperatures.append(self.get_temperature())
            # print(self.sensorid, 'Temperature: ' + str(temperatures[-1]))
            #np.save('temperatures', np.array(temperatures))
            
        # load stored temperatures with
        # np.load('temperatures.npy')

    def cleanup(self):
        self.thread_status = False
        
class th_1wire_temperature(cl_1wire_temperature):   

    
    def __init__(self):
        pass


class cl_fact_1wire_temperature(ABC):
    __o_instance = None
    
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_1wire_temperature.__o_instance = i_instance
        
    @classmethod        
    def get_instance(self, id):
        if cl_fact_1wire_temperature.__o_instance is not None:
            return(cl_fact_1wire_temperature.__o_instance)
        cl_fact_1wire_temperature.__o_instance = cl_1wire_temperature(sensorid=id)
        return(cl_fact_1wire_temperature.__o_instance)

    def __init__(self):
        pass 