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

dict_onewire_sensors = {}
dict_loggers = {}

def get_onewire_sensor_instance(id_sensor):
    if id_sensor not in dict_onewire_sensors:
        dict_onewire_sensors[id_sensor] = class_temperature.TemperatureSensor(sensorid=id_sensor)
    return dict_onewire_sensors[id_sensor]

def get_logger_instance(pythonfile):
    if pythonfile not in dict_loggers:
        dict_loggers[pythonfile] = class_logger.Logger(pythonfile)
    return dict_loggers[pythonfile]