#!/usr/bin/python
# coding=utf-8
# pi_caravan_loop.py
#------------------------------------------------------------
import traceback
import json
import logging_
import init
import names
import paths

_logger = logging_.create_logger(__name__)
_logger.debug('logging initialised')

def do_mainloop():
    print('mainloop')
    # temperature output in loop
    try:
        while True:
            temperature_outside = init.get_onewire_sensor_instance(names.id_temperature_sensor_outside).get_temperature()
            temperature_inside = init.get_onewire_sensor_instance(names.id_temperature_sensor_inside).get_temperature()
            temperature_fridge = init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge).get_temperature()
            temperature_fridge_exhaust = init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge_exhaust).get_temperature()
            print ('Outside: ' + str(temperature_outside))
            print ('Inside: ' + str(temperature_inside))
            print ('Fridge: ' + str(temperature_fridge))
            print ('Fridge Exhaust: ' + str(temperature_fridge_exhaust))
            
            json_values = json.dumps({"temperature_outside":temperature_outside, "temperature_inside":temperature_inside, "temperature_fridge":temperature_fridge, "temperature_fridge_exhaust":temperature_fridge_exhaust})
            with open(paths.get_path_web_json_file(), 'w') as file:
                file.write(json_values)
                
            print ('Done')
            print ("\n")
    except KeyboardInterrupt:
        raise
    except Exception as e:
        _logger.warning('main loop failed')
        _logger.warning(e)
        traceback.print_exc()