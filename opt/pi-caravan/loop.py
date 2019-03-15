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
            temperature_outside_dict = init.get_onewire_sensor_instance(names.id_temperature_sensor_outside).get_temperature()
            temperature_inside_dict = init.get_onewire_sensor_instance(names.id_temperature_sensor_inside).get_temperature()
            temperature_fridge_dict = init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge).get_temperature()
            temperature_fridge_exhaust_dict = init.get_onewire_sensor_instance(names.id_temperature_sensor_fridge_exhaust).get_temperature()
            
            temperature_outside = temperature_outside_dict.get('temperature')
            time_outside = temperature_outside_dict.get('timestamp')
            id_outside = temperature_outside_dict.get('sensor')
            temperature_inside = temperature_inside_dict.get('temperature')
            time_inside = temperature_inside_dict.get('timestamp')
            id_inside = temperature_inside_dict.get('sensor')
            temperature_fridge = temperature_fridge_dict.get('temperature')
            time_fridge = temperature_fridge_dict.get('timestamp')
            id_fridge = temperature_fridge_dict.get('sensor')
            temperature_fridge_exhaust = temperature_fridge_exhaust_dict.get('temperature')
            time_fridge_exhaust = temperature_fridge_exhaust_dict.get('timestamp')
            id_fridge_exhaust = temperature_fridge_exhaust_dict.get('sensor')
            
            print ('Outside: ' + str(temperature_outside) + ' time: ' + str(time_outside) + ' id: ' + str(id_outside))
            print ('Inside: ' + str(temperature_inside)+ ' time: ' + str(time_inside) + ' id: ' + str(id_inside))
            print ('Fridge: ' + str(temperature_fridge)+ ' time: ' + str(time_fridge) + ' id: ' + str(id_fridge))
            print ('Fridge Exhaust: ' + str(temperature_fridge_exhaust)+ ' time: ' + str(time_fridge_exhaust) + ' id: ' + str(id_fridge_exhaust))
            
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
            gyro_time = gyro_dict.get('time')
            print('X: ' + str(gyro_x) + ' Y: ' + str(gyro_y) + ' Z: ' + str(gyro_z) + ' temp: ' + str(gyro_temp) + ' time: ' + str(gyro_time))
            print ('gyro done')
            
            print('Sim808')
            init.get_sim808_sensor_instance(names.id_sim808_sensor).write_sim808('AT+CGNSINF'+ '\r\n')
            gps_dict = init.get_sim808_sensor_instance(names.id_sim808_sensor).get_gps_dict()
            lat = gps_dict.get('lat')
            lon = gps_dict.get('lon')
            date = gps_dict.get('date')
            print('lat: ' + str(lat) + ' lon: ' + str(lon) + ' date: ' + str(date))
            print('Sim808_done')
            
            print('Windmesser')
            anemometer_windspeed = init.get_aneometer_sensor_instance(names.id_anemometer_sensor).get_windspeed()
            anemometer_windaverage = init.get_aneometer_sensor_instance(names.id_anemometer_sensor).get_windaverage()
            print('windspeed: ' + str(anemometer_windspeed))
            print('windaverage: ' + str(anemometer_windaverage))
            print('Windmesser done')
            
            print ('loop done')
            
            print ("\n")
            
                            
            json_values = json.dumps({"windspeed":anemometer_windspeed, "windaverage":anemometer_windaverage, "gyroskop_x":gyro_x, "gyroskop_y":gyro_y, "gyroskop_z":gyro_z,"gyroskop_temp":gyro_temp, "lat":lat, "lon":lon, "date":date, "temperature_outside":temperature_outside, "temperature_inside":temperature_inside, "temperature_fridge":temperature_fridge, "temperature_fridge_exhaust":temperature_fridge_exhaust})
            with open(paths.get_path_values_json_file(), 'w') as file:
                file.write(json_values)
                
            
    except KeyboardInterrupt:
        raise
    except Exception as e:
        _logger.warning('main loop failed')
        _logger.warning(e)
        traceback.print_exc()