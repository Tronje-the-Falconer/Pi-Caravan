"""
    basic functions
    
    
"""
import RPi.GPIO as gpio
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
    logstring = _('goodbye') + '!'
    logger.info(logstring)
