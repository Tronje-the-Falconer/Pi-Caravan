#!/usr/bin/python
# coding=utf-8
# pi_caravan_loop.py
#------------------------------------------------------------
import pi_caravan_logging
import pi_caravan_read_onewire_sensors


global logger
logger = pi_caravan_logging.create_logger(__name__)
logger.debug('logging initialised')

def do_mainloop():
    global temperature_sensor_designation, temperature_senor_count, temperature_sensor_value 
    # temperature output in loop
    try:
        while True:
            x = 0
            pi_caravan_read_onewire_sensors.read_temperature_sensors()
            print ("Sensorbezeichnung und Temperaturwert:")
            while x < temperature_senor_count:
                print temperature_sensor_designation[x] , " " , temperature_sensor_value[x] , " °C"
                x = x + 1
            time.sleep(.5)
            print ("\n")
    except:
        # error 
        logger.warning('reading temperature sensors was not possible.')
