#!/usr/bin/python
# coding=utf-8
# pi_caravan_read_onewire_sensors.py
#------------------------------------------------------------
"""
    getting temperatures
"""

import os, sys, time
import pi_caravan_names
import pi_caravan_logging

global logger
logger = pi_caravan_logging.create_logger(__name__)
logger.debug('logging initialised')

def read_temperature_sensors():
    global temperature_sensor_designation, temperature_senor_count, temperature_sensor_value
    x = 0
    try:
        # 1-wire slave files acc. read the number determined
        while x < temperature_senor_count:
            filename = pi_caravan_names.onewire_path + temperature_sensor_designation[x] + "/w1_slave"
            file = open(filename)
            filecontent = file.read()
            file.close()
            # read and convert temperature values
            stringvalue = filecontent.split("\n")[1].split(" ")[9]
            sensorvalue = float(stringvalue[2:]) / 1000
            temperature = '%6.2f' % sensorvalue # sensor or temperature value formatted to 2 decimal places
            temperature_sensor_value.insert(x,temperature) # update value in list
            x = x + 1
