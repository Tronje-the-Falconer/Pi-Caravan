#!/usr/bin/python
# coding=utf-8
# pi_caravan_init.py
#------------------------------------------------------------
"""
    inital settings for pi-caravan
    
    setting up inital settings
"""

import os
import logging_
import names
import class_temperature


_logger = logging_.create_logger(__name__)
_logger.debug('logging initialised')

_temperature_sensor_outside = None
_temperature_sensor_inside = None
_temperature_sensor_fridge = None
_temperature_sensor_fridge_exhaust = None

def get_instance(sensorid):
    global _temperature_sensor_outside
    global _temperature_sensor_inside
    global _temperature_sensor_fridge
    global _temperature_sensor_fridge_exhaust
    
    if sensorid == names.id_temperature_sensor_outside:
        if _temperature_sensor_outside == None:
            _temperature_sensor_outside = class_temperature.TemperatureSensor(sensorid=names.id_temperature_sensor_outside)
        return _temperature_sensor_outside
    elif sensorid == names.id_temperature_sensor_inside:
        if _temperature_sensor_inside == None:
            _temperature_sensor_inside = class_temperature.TemperatureSensor(sensorid=names.id_temperature_sensor_inside)
        return _temperature_sensor_inside
    elif sensorid == names.id_temperature_sensor_fridge:
        if _temperature_sensor_fridge == None:
            _temperature_sensor_fridge = class_temperature.TemperatureSensor(sensorid=names.id_temperature_sensor_fridge)
        return _temperature_sensor_fridge
    elif sensorid == names.id_temperature_sensor_fridge_exhaust:
        if _temperature_sensor_fridge_exhaust == None:
            _temperature_sensor_fridge_exhaust = class_temperature.TemperatureSensor(sensorid=names.id_temperature_sensor_fridge_exhaust)
        return _temperature_sensor_fridge_exhaust