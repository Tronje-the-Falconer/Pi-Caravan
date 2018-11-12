import glob, os, sys, time
import threading

import numpy as np
 
class TemperatureSensor(threading.Thread):
    def __init__(self, base_path= '/sys/bus/w1/devices/', 
                     file_name='/w1_slave', sensorname='28*', default=25.0):
        threading.Thread.__init__(self)
        self.default = default
        self.sensorname = sensorname
 
        try:
            self.sensor_path = glob.glob(base_path + self.sensorname)[0] + file_name 
        except:
            print("Bad sensor path")
 
    def get_temperature(self):
        temperature = self.default
 
        try:           
            with open(self.sensor_path, 'r') as f:
                data = f.read()
 
                if 'YES\n' not in data:
                    raise Exception()
                temperature = round(float(data.rsplit('t=',1)[1])/1000, 1)    
        except:          
            print("Can't read temperature sensor!")   
 
        return float(temperature) 
 
    def log_temperature(self, interval=5.0):
        temperatures = []
        temperatures.append(self.get_temperature())
        print(self.sensorname, 'Temperature: ' + str(temperatures[-1]))

        # while True:
            # time.sleep(interval)
            # temperatures.append(self.get_temperature())
            # print(self.sensorname, 'Temperature: ' + str(temperatures[-1]))
            #np.save('temperatures', np.array(temperatures))
            
        # load stored temperatures with
        # np.load('temperatures.npy')
 
if __name__ == "__main__":
    temp_sensor_1 = TemperatureSensor(sensorname='28-0213139dc0aa')
    temp_sensor_2 = TemperatureSensor(sensorname='28-021313977aaa')
    temp_sensor_3 = TemperatureSensor(sensorname='28-00ff98430494')
    temp_sensor_4 = TemperatureSensor(sensorname='28-000c98430a7b')
 
    if sys.argv[-1] == "log":
        temp_sensor_1.log_temperature()
        temp_sensor_2.log_temperature()
        temp_sensor_3.log_temperature()
        temp_sensor_4.log_temperature()
    else:
        print(temp_sensor_1.get_temperature())
        print(temp_sensor_2.get_temperature())
        print(temp_sensor_3.get_temperature())
        print(temp_sensor_4.get_temperature())