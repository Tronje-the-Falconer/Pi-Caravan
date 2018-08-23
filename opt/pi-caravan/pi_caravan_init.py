#!/usr/bin/python
# coding=utf-8
# pi_caravan_init.py
#------------------------------------------------------------
"""
    inital settings for pi-caravan
    
    setting up inital settings
"""

import pi_caravan_1wire_sensors

def get_sensors():
    temperature_sensor_designation, temperature_senor_count, temperature_sensor_value = pi_caravan_1wire_sensors.import_temperature_sensors()

loopcounter = 0                      #  Zaehlt die Durchlaeufe des Mainloops
