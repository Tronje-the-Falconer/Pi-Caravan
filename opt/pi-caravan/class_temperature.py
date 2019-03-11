import glob, os, sys, time
import threading

import numpy as np
 
class TemperatureSensor(threading.Thread):
    def __init__(self, base_path= '/sys/bus/w1/devices/', 
                     file_name='/w1_slave', sensorid='28*', default=99.9):
        threading.Thread.__init__(self)
        self.default = default #private
        self.sensorid = sensorid #private
        self.sensortemperature = None
 
        try:
            self.sensor_path = glob.glob(base_path + self.sensorid)[0] + file_name
            self.temperaturesensor_startthread()
        except:
            print("Bad sensor path")
    def temperaturesensor_startthread(self):
        self.thread_temperaturesensor = threading.Thread(target = self.handle_temperature_recieve)
        #thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_temperaturesensor.setDaemon(False)
        self.thread_temperaturesensor.start()
        
        
    def handle_temperature_recieve(self):
        while 1:
            self.sensortemperature = self.read_temperature()
    
    def get_temperature(self):
        return self.sensortemperature
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
 