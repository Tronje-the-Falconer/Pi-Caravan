#!/usr/bin/python
# coding=utf-8
# pi_caravan_organization.py
#------------------------------------------------------------
"""
    basic functions
    
    
"""
import pi_caravan_logging
import pi_caravan_names

global logger
logger = pi_caravan_logging.create_logger(__name__)
logger.debug('logging initialised')

# Function goodbye
def goodbye():
    """
    last function for clean up system
    """
    global logger
    logstring = 'goodbye!'
    logger.info(logstring)
