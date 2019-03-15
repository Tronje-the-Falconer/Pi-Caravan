#!/usr/bin/python
# coding=utf-8
# pi_caravan_organization.py
#------------------------------------------------------------
"""
    basic functions
    
    
"""
import logging_
import RPi.GPIO as gpio

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
    logstring = 'goodbye!'
    logger.info(logstring)
