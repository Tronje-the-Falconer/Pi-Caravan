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
import pi_caravan_names
import class_temperature

global logger

def init():
    logger = pi_caravan_logging.create_logger(__name__)
    logger.debug('logging initialised')
    
    temperature_sensor_outside = class_temperature.TemperatureSensor(sensorname=pi_caravan_names.temperature_sensor_outside)
    temperature_sensor_inside = class_temperature.TemperatureSensor(sensorname=pi_caravan_names.temperature_sensor_inside)
    temperature_sensor_fridge = class_temperature.TemperatureSensor(sensorname=pi_caravan_names.temperature_sensor_fridge)
    temperature_sensor_fridge_exhaust_air = class_temperature.TemperatureSensor(sensorname=pi_caravan_names.temperature_sensor_fridge_exhaust_air)
    return temperature_sensor_outside,temperature_sensor_inside,temperature_sensor_fridge,temperature_sensor_fridge_exhaust_air
    
loopcounter = 0                      #  Zaehlt die Durchlaeufe des Mainloops