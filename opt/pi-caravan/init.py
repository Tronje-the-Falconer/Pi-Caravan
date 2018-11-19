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

global logger

def __init__():
    logger = logging_.create_logger(__name__)
    logger.debug('logging initialised')
    _get_temperature_from_sensor_outside()
    _get_temperature_from_sensor_inside()
    _get_temperature_from_sensor_fridge()
    _get_temperature_from_sensor_fridge_exhaust_air()


def _get_temperature_from_sensor_outside():
    try:
        _temperature_sensor_outside
    except UnboundLocalError as error:
        _temperature_sensor_outside = class_temperature.TemperatureSensor(sensorname=names.temperature_sensor_outside)
        return temperature_sensor_outside.get_temperature()
    else:
        return temperature_sensor_outside.get_temperature()

def _get_temperature_from_sensor_inside():
    if _temperature_sensor_inside == NULL:
        _temperature_sensor_inside = class_temperature.TemperatureSensor(sensorname=names.temperature_sensor_inside)
        
    return _temperature_sensor_inside.get_temperature()

def _get_temperature_from_sensor_fridge():
    if _temperature_sensor_fridge == NULL:
        _temperature_sensor_fridge = class_temperature.TemperatureSensor(sensorname=names.temperature_sensor_fridge)
        
    return _temperature_sensor_fridge.get_temperature()

def _get_temperature_from_sensor_fridge_exhaust_air():
    if _temperature_sensor_fridge_exhaust_air == NULL:
        _temperature_sensor_fridge_exhaust_air = class_temperature.TemperatureSensor(sensorname=names.temperature_sensor_fridge)
        
    return _temperature_sensor_fridge_exhaust_air.get_temperature()