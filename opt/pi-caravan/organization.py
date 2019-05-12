#!/usr/bin/python
# coding=utf-8
# pi_caravan_organization.py
#------------------------------------------------------------
"""
    basic functions
    
    
"""
import logging_


import names
from class_anemometer import cl_fact_anemometer
from class_mcp3208 import cl_fact_mcp3208
from class_sim808 import cl_fact_sim808
from class_mpu6050 import cl_fact_mpu6050
from class_onewire import cl_fact_1wire_temperature
from class_gpio_handling import gpio_handling

global logger
logger = logging_.create_logger(__name__)
logger.debug('logging initialised')

# Function goodbye
def goodbye():
    """
    last function for clean up system
    """
    global logger
    cleanup_threads()
    gpio_handling.gpio_cleanup()
    logstring = 'goodbye!'
    logger.info(logstring)
    
def cleanup_threads():
    cl_fact_1wire_temperature().get_instance(names.get_sensorid('temperature_sensor_outside')).cleanup()
    cl_fact_1wire_temperature().get_instance(names.get_sensorid('names.temperature_sensor_inside')).cleanup()
    cl_fact_1wire_temperature().get_instance(names.get_sensorid('names.temperature_sensor_fridge')).cleanup()
    cl_fact_1wire_temperature().get_instance(names.get_sensorid('names.temperature_sensor_fridge_exhaust')).cleanup()
    cl_fact_mpu6050().get_instance().cleanup()
    cl_fact_sim808().get_instance().cleanup()
    cl_fact_anemometer().get_instance(names.gpio_anemometer).cleanup()
    cl_fact_mcp3208().get_instance().cleanup()
    
