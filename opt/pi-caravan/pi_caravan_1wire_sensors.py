#!/usr/bin/python
# coding=utf-8
# 1wire_sensors.py
#------------------------------------------------------------
import os, sys
import pi_caravan_logging
import pi_caravan_path

global logger
logger = pi_caravan_logging.create_logger(__name__)
logger.debug('logging initialised')


# temperature sensors
def read_temperature_sensors():
    temperature_sensor_designation = []   # list of all single sensors identifiers
    temperature_senor_count = 0           # INT for the number of read sensors
    temperature_sensor_value = []         # list with the individual sensor values
    # read directory contents with all existing sensor designations 28-xxxx
    try:
        for x in os.listdir(pi_caravan_path.onewire_path):
            if (x.split("-")[0] == "28") or (x.split("-")[0] == "10"):
                temperature_sensor_designation.append(x)
                temperature_senor_count = temperature_senor_count + 1
    except:
        # reading error
        logger.warning('the directory "' . pi_caravan_path.onewirepath . '" content could not be read.')
    return temperature_sensor_designation, temperature_senor_count, temperature_sensor_value
