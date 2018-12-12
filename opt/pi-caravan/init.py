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
import paths
import class_temperature
import class_gyro


_logger = logging_.create_logger(__name__)
_logger.debug('logging initialised')

dict_onewire_sensors = {}
dict_gyro_sensors = {}

def get_onewire_sensor_instance(id_sensor):
    if id_sensor not in dict_onewire_sensors:
        dict_onewire_sensors[id_sensor] = class_temperature.TemperatureSensor(sensorid=id_sensor)
    return dict_onewire_sensors[id_sensor]
    
def get_gyro_sensor_instance(id_sensor):
    if id_sensor not in dict_gyro_sensors:
        dict_gyro_sensors[id_sensor] = class_gyro.Gyro()
    return dict_gyro_sensors[id_sensor]