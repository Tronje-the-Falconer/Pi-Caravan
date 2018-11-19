#!/usr/bin/python
# coding=utf-8
# main.py
#------------------------------------------------------------
"""
pi-caravan - boardcomputer for a caravan
pi-carvan should:
monitor temperatures
monitor the battery status
monitor the levels of fresh and waste water
provide a DAB radio
provide a Wifi access point
provide GPS tracking
provide a weather station
Forward WiFi from the campsite
"""

# import modules
import os
import init
import organization
import logging_
import loop

class Loopcounter():
    def __init__(self):
        self.reset()
    def reset():
        self.__loopcounter__ = 0
    def increase():
        self.__loopcounter__ +=1
    def get_value():
        return self.__loopcounter__
    

def __init__():
    Loopcounter.__init__()
    
logger = logging_.create_logger('main')
logger.debug('logging initialised')

temperature_sensor_outside,temperature_sensor_inside,temperature_sensor_fridge,temperature_sensor_fridge_exhaust_air = pi_caravan_init.get_sensors()
# initialise system

try:
    loop.do_mainloop(temperature_sensor_outside,temperature_sensor_inside,temperature_sensor_fridge,temperature_sensor_fridge_exhaust_air)
    
except KeyboardInterrupt:
    logger.warning('KeyboardInterrupt')
    pass

except Exception as e:
    logstring = 'exception occurred' + '!!!'
    logger.exception(logstring, exc_info = True)
    pass

finally:
    Loopcounter.reset()
    organization.goodbye()
