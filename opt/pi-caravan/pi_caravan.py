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
import organization
import logging_
import loop
from class_gpio_handling import gpio_handling

class Loopcounter():
    def __init__(self):
        self.reset()
    def reset(self):
        self.loopcount = 0
    def increase(self):
        self.loopcount +=1
    def get_value(self):
        return self.loopcount
    


loopcounter = Loopcounter()
logger = logging_.create_logger('main')
logger.debug('logging initialised')

# initialise system

try:
    gpio_handling.setGPIO_boardmode()
    gpio_handling.setupGPIO()
    gpio_handling.defaultGPIO()
    loop.do_mainloop()
    
except KeyboardInterrupt:
    logger.warning('KeyboardInterrupt')
    pass

except Exception as e:
    logstring = 'exception occurred' + '!!!'
    logger.exception(logstring, exc_info = True)
    pass

finally:
    loopcounter.reset()
    organization.goodbye()
