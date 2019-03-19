#!/usr/bin/python
# coding=utf-8
# pi_caravan_organization.py
#------------------------------------------------------------
"""
    basic functions
    
    
"""
import logging_
import RPi.GPIO as gpio

import names
from class_anemometer import cl_fact_anemometer
from class_mcp3208 import cl_fact_mcp3208
from class_sim808 import cl_fact_sim808
from class_mpu6050 import cl_fact_mpu6050
from class_temperature import cl_fact_1wire_temperature

global logger
logger = logging_.create_logger(__name__)
logger.debug('logging initialised')

# Function goodbye
def goodbye():
    """
    last function for clean up system
    """
    global logger
    gpio.cleanup()
    cleanup_threads()
    logstring = 'goodbye!'
    logger.info(logstring)
    
def cleanup_threads():
    cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_outside).cleanup()
    cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_inside).cleanup()
    cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_fridge).cleanup()
    cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_fridge_exhaust).cleanup()
    cl_fact_mpu6050().get_instance().cleanup()
    cl_fact_sim808().get_instance().cleanup()
    cl_fact_anemometer().get_instance(names.gpio_anemometer).cleanup()
    cl_fact_mcp3208().get_instance().cleanup()
    
