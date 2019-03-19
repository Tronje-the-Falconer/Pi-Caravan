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
from class_anemometer import cl_fact_anemometer
from class_mcp3208 import cl_fact_mcp3208
from class_sim808 import cl_fact_sim808
from class_mpu6050 import cl_fact_mpu6050
from class_temperature import cl_fact_1wire_temperature


_logger = logging_.create_logger(__name__)
_logger.debug('logging initialised')

def do_mainloop():
    print('mainloop')
    # temperature output in loop
    try:
        while True:
            print ('temperature')
            temperature_outside_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_outside).get_temperature()
            temperature_inside_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_inside).get_temperature()
            temperature_fridge_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_fridge).get_temperature()
            temperature_fridge_exhaust_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_fridge_exhaust).get_temperature()
            
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
            gyro_dict = cl_fact_mpu6050().get_instance().get_mpu6050_dict()
            gyro_x = gyro_dict.get('gyroskop_xout')
            gyro_y = gyro_dict.get('gyroskop_yout')
            gyro_z = gyro_dict.get('gyroskop_zout')
            gyro_temp = gyro_dict.get('temperatur')
            gyro_time = gyro_dict.get('time')
            print('X: ' + str(gyro_x) + ' Y: ' + str(gyro_y) + ' Z: ' + str(gyro_z) + ' temp: ' + str(gyro_temp) + ' time: ' + str(gyro_time))
            print ('gyro done')
            
            print('Sim808')
            cl_fact_sim808().get_instance().write_sim808('AT+CGNSINF'+ '\r\n')
            gps_dict = cl_fact_sim808().get_instance().get_gps_dict()
            lat = gps_dict.get('lat')
            lon = gps_dict.get('lon')
            date = gps_dict.get('date')
            print('lat: ' + str(lat) + ' lon: ' + str(lon) + ' date: ' + str(date))
            print('Sim808_done')
            
            print('Windmesser')
            anemometer_windspeed = cl_fact_anemometer().get_instance(names.gpio_anemometer).get_windspeed()
            anemometer_windaverage = cl_fact_anemometer().get_instance(names.gpio_anemometer).get_windaverage()
            print('windspeed: ' + str(anemometer_windspeed))
            print('windaverage: ' + str(anemometer_windaverage))
            print('Windmesser done')
            
            print('AD-Wandler')
            raw_frischwasser = cl_fact_mcp3208().get_instance().get_value(names.channel_frischwasser)
            raw_abwasser = cl_fact_mcp3208().get_instance().get_value(names.channel_abwasser)
            raw_toilette = cl_fact_mcp3208().get_instance().get_value(names.channel_toilette)
            raw_batteriespannung = cl_fact_mcp3208().get_instance().get_value(names.channel_batteriespannung)
            raw_entnahmestrom = cl_fact_mcp3208().get_instance().get_value(names.channel_entnahmestrom)
            raw_ladestrom = cl_fact_mcp3208().get_instance().get_value(names.channel_ladestrom)
            raw_unused_1 = cl_fact_mcp3208().get_instance().get_value(names.channel_unused_1)
            raw_unused_2 = cl_fact_mcp3208().get_instance().get_value(names.channel_unused_2)
            
            
            ##### Füllstandssensoren digits bei 750 ohm
            ### 10cm
            # 847   100%
            # 451   66%
            # 269   33%
            # 1     0%

            ### 15 cmd
            # 845   100%
            # 612   75%    
            # 448   50%
            # 268   25%
            # 1     0%

            ### 20cm
            # 845   100%
            # 735   86%
            # 620   71%
            # 540   57%
            # 454   43%
            # 366   28%
            # 269   14%
            # 1     0%
            
            
            frischwasserstand = None
            abwasserstand = None
            toilettenstand = None
            batteriespannung = None
            entnahmestrom = None
            ladestrom = None
            undefined_1 = None
            undefined_2 = None
            
            if raw_frischwasser >= 840:
                frischwasserstand = '100%'
            elif raw_frischwasser < 840 and raw_frischwasser >= 735:
                frischwasserstand = '86%'
            elif raw_frischwasser < 735 and raw_frischwasser >= 620:
                frischwasserstand = '71%'
            elif raw_frischwasser < 620 and raw_frischwasser >= 540:
                frischwasserstand = '57%'
            elif raw_frischwasser < 540 and raw_frischwasser >= 454:
                frischwasserstand = '43%'
            elif raw_frischwasser < 454 and raw_frischwasser >= 366:
                frischwasserstand = '28%'
            elif raw_frischwasser < 366 and raw_frischwasser >= 269:
                frischwasserstand = '14%'
            elif raw_frischwasser < 269:
                frischwasserstand = '0%'
                
            if raw_abwasser >= 840:
                abwasserstand = '100%'
            elif raw_abwasser < 840 and raw_abwasser >= 451:
                abwasserstand = '66%'
            elif raw_abwasser < 451 and raw_abwasser >= 269:
                abwasserstand = '33%'
            elif raw_abwasser < 269:
                abwasserstand = '0%'
                
            if raw_toilette >= 840:
                toilettenstand = '100%'
            elif raw_toilette < 840 and raw_toilette >= 612:
                toilettenstand = '75%'
            elif raw_toilette < 612 and raw_toilette >= 448:
                toilettenstand = '50%'
            elif raw_toilette < 448 and raw_toilette >= 268:
                toilettenstand = '25%'
            elif raw_toilette < 268:
                toilettenstand = '0%'
            
            
            print ('Kanal 1 Frischwasser: ' + str(raw_frischwasser) + ' ' + frischwasserstand)
            print ('Kanal 2 Abwasser    : ' + str(raw_abwasser) + ' ' + abwasserstand)
            print ('Kanal 3 Toilette    : ' + str(raw_toilette) + ' ' + toilettenstand)
            print ('Kanal 4 Batterie    : ' + str(raw_batteriespannung) + ' ' )#+ batteriespannung)
            print ('Kanal 5 Entnahme    : ' + str(raw_entnahmestrom) + ' ' )#+ entnahmestrom)
            print ('Kanal 6 Ladung      : ' + str(raw_ladestrom) + ' ' )#+ ladestrom)
            print ('Kanal 7 Undefinded 1: ' + str(raw_unused_1) + ' ' )#+ undefined_1)
            print ('Kanal 8 Undefinded 2: ' + str(raw_unused_2) + ' ' )#+ undefined_2)
            
            print('AD-Wandler done')
            
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