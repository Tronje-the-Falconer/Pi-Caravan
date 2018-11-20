#!/usr/bin/python
# coding=utf-8
# pi_caravan_loop.py
#------------------------------------------------------------
import traceback
import logging_
import init
import names

_logger = logging_.create_logger(__name__)
_logger.debug('logging initialised')

def do_mainloop():
    print('mainloop')
    # temperature output in loop
    try:
        while True:
            print(init.get_onewire_sensor_instance(names.id_temperature_sensor_outside).get_temperature())
            print(init.get_onewire_sensor_instance(names.id_temperature_sensor_inside).get_temperature())
            print(init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge).get_temperature())
            print(init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge_exhaust).get_temperature())
            print ('Done')
            print ("\n")
    except KeyboardInterrupt:
        raise
    except Exception as e:
        _logger.warning('main loop failed')
        _logger.warning(e)
        traceback.print_exc()