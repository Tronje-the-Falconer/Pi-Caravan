#!/usr/bin/python
# coding=utf-8
# pi_caravan_organization.py
#------------------------------------------------------------
"""
    basic functions
    
    
"""
import logging_

global logger
logger = logging_.create_logger(__name__)
logger.debug('logging initialised')

# Function goodbye
def goodbye():
    """
    last function for clean up system
    """
    global logger
    logstring = 'goodbye!'
    logger.info(logstring)
