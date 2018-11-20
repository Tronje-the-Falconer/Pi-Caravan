import glob, os, sys, time
import threading

import numpy as np
 
class TemperatureSensor(threading.Thread):
    def __init__(self, base_path= '/sys/bus/w1/devices/', 
                     file_name='/w1_slave', sensorid='28*', default=25.0):
        threading.Thread.__init__(self)
        self.default = default #private
        self.sensorid = sensorid #private
 
        try:
            self.sensor_path = glob.glob(base_path + self.sensorid)[0] + file_name 
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
        except KeyboardInterrupt:
            raise
        except:
            print("Can't read temperature sensor!")
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
 
 
 
# if __name__ == "__main__":
    # temp_sensor_1 = TemperatureSensor(pi_caravan_names.tempsensor1)
    # temp_sensor_2 = TemperatureSensor(pi_caravan_names.tempsensor2)
    # temp_sensor_3 = TemperatureSensor(pi_caravan_names.tempsensor3)
    # temp_sensor_4 = TemperatureSensor(pi_caravan_names.tempsensor4)
 
    # if sys.argv[-1] == "log":
        # temp_sensor_1.log_temperature()
        # temp_sensor_2.log_temperature()
        # temp_sensor_3.log_temperature()
        # temp_sensor_4.log_temperature()
    # else:
        # print(temp_sensor_1.get_temperature())
        # print(temp_sensor_2.get_temperature())
        # print(temp_sensor_3.get_temperature())
        # print(temp_sensor_4.get_temperature())