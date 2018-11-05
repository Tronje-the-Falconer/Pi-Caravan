#!/usr/bin/python
# coding=utf-8
# pi_caravan_init.py
#------------------------------------------------------------
"""
    inital settings for pi-caravan
    
    setting up inital settings
"""

import os
import pi_caravan_logging
import pi_caravan_paths

global logger
global temperature_sensor_designation, temperature_sensor_count, temperature_sensor_value

def init():
    logger = pi_caravan_logging.create_logger(__name__)
    logger.debug('logging initialised')

    temperature_sensor_designation = []   # list of all single sensors identifiers
    temperature_sensor_count = 0           # INT for the number of read sensors
    temperature_sensor_value = []         # list with the individual sensor values
    print('init')

    # read directory contents with all existing sensor designations 28-xxxx
    try:
        for x in os.listdir(pi_caravan_paths.get_path_onewire()):
            if (x.split("-")[0] == "28") or (x.split("-")[0] == "10"):
                temperature_sensor_designation.append(x)
                temperature_sensor_count = temperature_sensor_count + 1
    except:
        # reading error
        logger.warning('the directory "' + pi_caravan_paths.get_path_onewire() + '" content could not be read.')



loopcounter = 0                      #  Zaehlt die Durchlaeufe des Mainloops