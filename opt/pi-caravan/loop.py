#!/usr/bin/python
# coding=utf-8
# pi_caravan_loop.py
#------------------------------------------------------------
import logging_


global logger, temperature_sensor_outside, temperature_sensor_inside, temperature_sensor_fridge, temperature_sensor_fridge_exhaust_air


logger = logging_.create_logger(__name__)
logger.debug('logging initialised')

def do_mainloop(temperature_sensor_outside,temperature_sensor_inside,temperature_sensor_fridge,temperature_sensor_fridge_exhaust_air):
    print('mainloop')
    temperature_sensor_outside = temperature_sensor_fridge_exhaust_air
    temperature_sensor_inside = temperature_sensor_inside
    temperature_sensor_fridge = temperature_sensor_fridge
    temperature_sensor_fridge_exhaust_air = temperature_sensor_fridge_exhaust_air
    # temperature output in loop
    try:
        while True:
            print(temperature_sensor_outside.get_temperature())
            print(temperature_sensor_inside.get_temperature())
            print(temperature_sensor_fridge.get_temperature())
            print(temperature_sensor_fridge_exhaust_air.get_temperature())
            print ('Done')
            print ("\n")
    except KeyboardInterrupt:
        logger.warning('KeyboardInterrupt')
        pass
    except:
        # error 
        logger.warning('main loop failed')
