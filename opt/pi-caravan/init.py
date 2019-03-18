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
import class_mpu6050
import class_sim808
import class_anemometer
import class_mcp3208


_logger = logging_.create_logger(__name__)
_logger.debug('logging initialised')

dict_onewire_sensors = {}
dict_gyro_sensors = {}
dict_sim808_sensors = {}
dict_aneometer_sensors = {}
dict_mcp3208_ad = {}

def get_onewire_sensor_instance(id_sensor):
    global dict_onewire_sensors
    if id_sensor not in dict_onewire_sensors:
        dict_onewire_sensors[id_sensor] = class_temperature.TemperatureSensor(sensorid=id_sensor)
    return dict_onewire_sensors[id_sensor]
    
def get_gyro_sensor_instance(id_sensor):
    global dict_gyro_sensors
    if id_sensor not in dict_gyro_sensors:
        dict_gyro_sensors[id_sensor] = class_mpu6050.MPU6050()
    return dict_gyro_sensors[id_sensor]
    
def get_sim808_sensor_instance(id_sensor):
    global dict_sim808_sensors
    if id_sensor not in dict_sim808_sensors:
        dict_sim808_sensors[id_sensor] = class_sim808.Sim808()
    return dict_sim808_sensors[id_sensor]
    
def get_aneometer_sensor_instance(id_sensor):
    global dict_aneometer_sensors
    if id_sensor not in dict_aneometer_sensors:
        dict_aneometer_sensors[id_sensor] = class_anemometer.AnemometerSensor(names.gpio_notinuse_17)
    return dict_aneometer_sensors[id_sensor]
    
def get_mcp3208_sensor_instance(id_ad):
    global dict_mcp3208_ad
    if id_ad not in dict_mcp3208_ad:
        dict_mcp3208_ad[id_ad] = class_mcp3208.MCP3208()
    return dict_mcp3208_ad[id_ad]