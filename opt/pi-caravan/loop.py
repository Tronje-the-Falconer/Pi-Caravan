#!/usr/bin/python
# coding=utf-8
# pi_caravan_loop.py
#------------------------------------------------------------
import logging_
from init import _get_temperature_from_sensor_outside

global logger, temperature_sensor_outside, temperature_sensor_inside, temperature_sensor_fridge, temperature_sensor_fridge_exhaust_air

def __init__():
    __logger__ = logging_.create_logger(__name__)
    __logger__.debug('logging initialised')

def do_mainloop():
    __init__()
    print('mainloop')
    # temperature output in loop
    try:
        while True:
            print(_get_temperature_from_sensor_outside())
            print ('Done')
            print ("\n")
    except KeyboardInterrupt:
        __logger__.warning('KeyboardInterrupt')
        pass
    except:
        # error 
        __logger__.warning('main loop failed')

__init__()