#!/usr/bin/python
# coding=utf-8
# pi_caravan_loop.py
#------------------------------------------------------------
import pi_caravan_temperature

def do_mainloop():
    global temperature_sensor_designation, temperature_senor_count, temperature_sensor_value 
    # temperature output in loop
    try:
        while True:
            x = 0
            pi_caravan_temperature.read_temperature_sensors()
            print ("Sensorbezeichnung und Temperaturwert:")
            while x < temperature_senor_count:
                print temperature_sensor_designation[x] , " " , temperature_sensor_value[x] , " °C"
                x = x + 1
            time.sleep(.5)
            print ("\n")
    except:
        # error 
        logger.warning('reading DS1820 sensors was not possible.')
