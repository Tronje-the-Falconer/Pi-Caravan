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
            print ('temperature')
            temperature_outside = init.get_onewire_sensor_instance(names.id_temperature_sensor_outside).get_temperature()
            temperature_inside = init.get_onewire_sensor_instance(names.id_temperature_sensor_inside).get_temperature()
            temperature_fridge = init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge).get_temperature()
            temperature_fridge_exhaust = init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge_exhaust).get_temperature()
            print ('Outside: ' + str(temperature_outside))
            print ('Inside: ' + str(temperature_inside))
            print ('Fridge: ' + str(temperature_fridge))
            print ('Fridge Exhaust: ' + str(temperature_fridge_exhaust))
            
            # json_values = json.dumps({"temperature_outside":temperature_outside, "temperature_inside":temperature_inside, "temperature_fridge":temperature_fridge, "temperature_fridge_exhaust":temperature_fridge_exhaust})
            # with open(paths.get_path_web_json_file(), 'w') as file:
                # file.write(json_values)
            print ('temperature done')
            
            print ('gyro')
            gyro_dict = init.get_gyro_sensor_instance(names.id_gyro_sensor).get_mpu6050_dict()
            gyro_x = gyro_dict.get('gyroskop_xout')
            gyro_y = gyro_dict.get('gyroskop_yout')
            gyro_z = gyro_dict.get('gyroskop_zout')
            gyro_temp = gyro_dict.get('temperatur')
            print(gyro_x)
            print(gyro_y)
            print(gyro_z)
            print(gyro_temp)
            print ('gyro done')
            
            print('Sim808')
            init.get_sim808_sensor_instance(names.id_sim808_sensor).write_sim808('AT+CGNSINF'+ '\r\n')
            gps_dict = init.get_sim808_sensor_instance(names.id_sim808_sensor).get_gps_dict()
            print('Sim808_done')
            
            print ('loop done')
            print ("\n")
            
            json_values = json.dumps(gps_dict)
            with open(paths.get_path_gps_json_file(), 'w') as file:
                file.write(json_values)
                
            json_values = json.dumps({"temperature_outside":temperature_outside, "temperature_inside":temperature_inside, "temperature_fridge":temperature_fridge, "temperature_fridge_exhaust":temperature_fridge_exhaust, "gyroskop_x":gyro_x, "gyroskop_y":gyro_y, "gyroskop_z":gyro_z,"gyroskop_temp":gyro_temp})
            with open(paths.get_path_web_json_file(), 'w') as file:
                file.write(json_values)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        _logger.warning('main loop failed')
        _logger.warning(e)
        traceback.print_exc()