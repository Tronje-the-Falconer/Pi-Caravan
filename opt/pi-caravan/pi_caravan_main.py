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
import pi_caravan_init
import pi_caravan_organization
import pi_caravan_logging
import pi_caravan_loop


logger = pi_caravan_logging.create_logger('main')
logger.debug('logging initialised')

pi_caravan_init.init()
# initialise system
#pi_caravan_init.get_sensors()

try:
    pi_caravan_loop.do_mainloop()
    
except KeyboardInterrupt:
    logger.warning('KeyboardInterrupt')
    pass

except Exception as e:
    logstring = 'exception occurred' + '!!!'
    logger.exception(logstring, exc_info = True)
    pass

finally:
    pi_caravan_init.loopcounter = 0
    pi_caravan_organization.goodbye()
