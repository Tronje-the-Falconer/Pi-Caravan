#!/usr/bin/python
# coding=utf-8
# pi_caravan_loop.py
#------------------------------------------------------------
import traceback
import json
import logging_
#import init
import names
import paths
from class_anemometer import cl_fact_anemometer
from class_mcp3208 import cl_fact_mcp3208
from class_sim808 import cl_fact_sim808
from class_mpu6050 import cl_fact_mpu6050
from class_onewire import cl_fact_1wire_temperature
from class_sht31 import cl_fact_sht31
from class_gpio_handling import gpio_handling


_logger = logging_.create_logger(__name__)
_logger.debug('logging initialised')

def do_mainloop():
    print('mainloop')
    # temperature output in loop
    try:
        while True:
            
            json_dict = {}
            
            print ('temperature onewire')
            temperature_truma_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_truma).get_temperature()
            temperature_trumavent_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_trumavent).get_temperature()
            temperature_fridge_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_fridge).get_temperature()
            temperature_fridge_exhaust_dict = cl_fact_1wire_temperature().get_instance(names.id_temperature_sensor_fridge_exhaust).get_temperature()
            
            if temperature_truma_dict is not None:
                temperature_truma = temperature_truma_dict.get('temperature')
                time_truma = temperature_truma_dict.get('timestamp')
                id_truma = temperature_truma_dict.get('sensor')
            else:
                temperature_truma = None
                time_truma = None
                id_truma = None
            if temperature_trumavent_dict is not None:
                temperature_trumavent = temperature_trumavent_dict.get('temperature')
                time_trumavent = temperature_trumavent_dict.get('timestamp')
                id_trumavent = temperature_trumavent_dict.get('sensor')
            else:
                temperature_trumavent = None
                time_trumavent = None
                id_trumavent = None
            if temperature_fridge_dict is not None:
                temperature_fridge = temperature_fridge_dict.get('temperature')
                time_fridge = temperature_fridge_dict.get('timestamp')
                id_fridge = temperature_fridge_dict.get('sensor')
            else:
                temperature_fridge = None
                time_fridge = None
                id_fridge = None
            if temperature_fridge_exhaust_dict is not None:
                temperature_fridge_exhaust = temperature_fridge_exhaust_dict.get('temperature')
                time_fridge_exhaust = temperature_fridge_exhaust_dict.get('timestamp')
                id_fridge_exhaust = temperature_fridge_exhaust_dict.get('sensor')
            else:
                temperature_fridge_exhaust = None
                time_fridge_exhaust = None
                id_fridge_exhaust = None
                
            
            #print ('Outside: ' + str(temperature_outside) + ' time: ' + str(time_outside) + ' id: ' + str(id_outside))
            #print ('Inside: ' + str(temperature_inside)+ ' time: ' + str(time_inside) + ' id: ' + str(id_inside))
            #print ('Fridge: ' + str(temperature_fridge)+ ' time: ' + str(time_fridge) + ' id: ' + str(id_fridge))
            #print ('Fridge Exhaust: ' + str(temperature_fridge_exhaust)+ ' time: ' + str(time_fridge_exhaust) + ' id: ' + str(id_fridge_exhaust))
            
            json_dict['temperature_truma'] = temperature_truma
            json_dict['temperature_trumavent'] = temperature_trumavent
            json_dict['temperature_fridge'] = temperature_fridge
            json_dict['temperature_fridge_exhaust'] = temperature_fridge_exhaust
            print ('temperature onewire done')
            
            print('sht31')
            sht31_indoor_dict = cl_fact_sht31().get_instance(names.id_sht31_indoor).get_sht31_dict()
            sht31_outdoor_dict = cl_fact_sht31().get_instance(names.id_sht31_outdoor).get_sht31_dict()
            
            #print(sht31_indoor_dict)
            #print(sht31_outdoor_dict)
            if sht31_indoor_dict is not None:
                temperature_inside = sht31_indoor_dict.get('temperature_c')
                humidity_inside = sht31_indoor_dict.get('humidity')
            else:
                temperature_inside = None
                humidity_inside = None
            
            if sht31_outdoor_dict is not None:
                temperature_outside = sht31_outdoor_dict.get('temperature_c')
                humidity_outside = sht31_outdoor_dict.get('humidity')
            else:
                temperature_outside = None
                humidity_outside = None
            
            json_dict['temperature_outside'] = temperature_outside
            json_dict['temperature_inside'] = temperature_inside
            json_dict['humidity_outside'] = humidity_outside
            json_dict['humidity_inside'] = humidity_inside
            
            print('sht31 done')
            
            print ('gyro')
            gyro_dict = cl_fact_mpu6050().get_instance().get_mpu6050_dict()
            if gyro_dict is not None:
                gyro_x = gyro_dict.get('gyroskop_xout')
                gyro_y = gyro_dict.get('gyroskop_yout')
                gyro_z = gyro_dict.get('gyroskop_zout')
                gyro_temp = gyro_dict.get('temperatur')
                gyro_time = gyro_dict.get('time')
            else:
                gyro_x = None
                gyro_y = None
                gyro_z = None
                gyro_temp = None
                gyro_time = None
            #print('X: ' + str(gyro_x) + ' Y: ' + str(gyro_y) + ' Z: ' + str(gyro_z) + ' temp: ' + str(gyro_temp) + ' time: ' + str(gyro_time))
            json_dict['gyroskop_x'] = gyro_x
            json_dict['gyroskop_y'] = gyro_y
            json_dict['gyroskop_z'] = gyro_z
            json_dict['gyroskop_temp'] = gyro_temp
            print ('gyro done')
            
            print('Sim808')
            cl_fact_sim808().get_instance().write_sim808('AT+CGNSINF'+ '\r\n')
            gps_dict = cl_fact_sim808().get_instance().get_gps_dict()
            lat = gps_dict.get('lat')
            lon = gps_dict.get('lon')
            date = gps_dict.get('date')
            #print('lat: ' + str(lat) + ' lon: ' + str(lon) + ' date: ' + str(date))
            
            json_dict['lat'] = lat
            json_dict['lon'] = lon
            json_dict['date'] = date
            print('Sim808_done')
            
            print('Windmesser')
            anemometer_windspeed = cl_fact_anemometer().get_instance(names.gpio_anemometer).get_windspeed()
            anemometer_windaverage = cl_fact_anemometer().get_instance(names.gpio_anemometer).get_windaverage()
            if anemometer_windaverage is not None and temperature_outside is not None:
                anemometer_windaverage_kmh = anemometer_windaverage * 3.6
                windchill = 13.12 + 0.6215 * temperature_outside - 11.37 * (anemometer_windaverage_kmh)**0.16 + 0.3965 * temperature_outside * (anemometer_windaverage_kmh)**0.16
            elif anemometer_windspeed is not None and temperature_outside is not None:
                anemometer_windspeed_kmh = anemometer_windspeed * 3.6
                windchill = 13.12 + 0.6215 * temperature_outside - 11.37 * (anemometer_windspeed_kmh)**0.16 + 0.3965 * temperature_outside * (anemometer_windspeed_kmh)**0.16
            else:
                windchill = None
                
            #print('windspeed: ' + str(anemometer_windspeed))
            #print('windaverage: ' + str(anemometer_windaverage))
            
            json_dict['windspeed'] = anemometer_windspeed
            json_dict['windaverage'] = anemometer_windaverage
            json_dict['windchill'] = windchill
            print('Windmesser done')
            
            print('AD-Wandler')
            mcp3208 = cl_fact_mcp3208().get_instance()
            raw_frischwasser = mcp3208.get_value(names.channel_frischwasser)
            raw_abwasser = mcp3208.get_value(names.channel_abwasser)
            raw_toilette = mcp3208.get_value(names.channel_toilette)
            raw_batteriespannung = mcp3208.get_value(names.channel_batteriespannung)
            raw_systemverbrauch = mcp3208.get_value(names.channel_systemverbrauch)
            raw_solarerzeugung = mcp3208.get_value(names.channel_solarerzeugung)
            raw_netzbezug = mcp3208.get_value(names.channel_netzbezug)
            raw_unused_2 = mcp3208.get_value(names.channel_unused_2)
            
            frischwasserstand = None
            abwasserstand = None
            toilettenstand = None
            batteriespannung = None
            systemverbrauch = None
            solarerzeugung = None
            netzbezug = None
            undefined_2 = None
            
            ############# Fuellstaende
            if raw_frischwasser is not None:
                if raw_frischwasser >= 840:
                    frischwasserstand = 100
                elif raw_frischwasser < 840 and raw_frischwasser >= 735:
                    frischwasserstand = 86
                elif raw_frischwasser < 735 and raw_frischwasser >= 620:
                    frischwasserstand = 71
                elif raw_frischwasser < 620 and raw_frischwasser >= 540:
                    frischwasserstand = 57
                elif raw_frischwasser < 540 and raw_frischwasser >= 454:
                    frischwasserstand = 43
                elif raw_frischwasser < 454 and raw_frischwasser >= 366:
                    frischwasserstand = 28
                elif raw_frischwasser < 366 and raw_frischwasser >= 269:
                    frischwasserstand = 14
                elif raw_frischwasser < 269:
                    frischwasserstand = 0
            else:
                frischwasserstand = None
            
            if raw_abwasser is not None:
                if raw_abwasser >= 840:
                    abwasserstand = 100
                elif raw_abwasser < 840 and raw_abwasser >= 451:
                    abwasserstand = 66
                elif raw_abwasser < 451 and raw_abwasser >= 269:
                    abwasserstand = 33
                elif raw_abwasser < 269:
                    abwasserstand = 0
            else:
                abwasserstand = None
            
            if raw_toilette is not None:
                if raw_toilette >= 840:
                    toilettenstand = 100
                elif raw_toilette < 840 and raw_toilette >= 612:
                    toilettenstand = 75
                elif raw_toilette < 612 and raw_toilette >= 448:
                    toilettenstand = 50
                elif raw_toilette < 448 and raw_toilette >= 268:
                    toilettenstand = 25
                elif raw_toilette < 268:
                    toilettenstand = 0
            else:
                toilettenstand = None
                
            #Batterie
            if raw_batteriespannung is not None: # 12v 2870 8v 1800 1,2v 270
                if (names.battery_digits2-names.battery_digits1) != 0:
                    batteriespannung = (names.battery_volt2-names.battery_volt1)/(names.battery_digits2-names.battery_digits1) * raw_batteriespannung + names.battery_offset
                else:
                    batteriespannung = 0
                        
                batteriefuellstand = batteriespannung / (names.battery_maxvolt/100)
            else:
                batteriespannung = None
                batteriefuellstand = None
            
            #Systemverbrauch
            if raw_systemverbrauch is not None:
                systemverbrauch = raw_systemverbrauch
            else:
                systemverbrauch = None
                
            #solarerzeugung
            if raw_solarerzeugung is not None:
                solarerzeugung = raw_solarerzeugung
            else:
                solarerzeugung = None
                
            #Netzbezug
            if raw_netzbezug is not None:
                netzbezug = raw_netzbezug
            else:
                netzbezug = None
                
            #print ('Kanal 1 Frischwasser    : ' + str(raw_frischwasser) + ' ' + str(frischwasserstand))
            #print ('Kanal 2 Abwasser        : ' + str(raw_abwasser) + ' ' + str(abwasserstand))
            #print ('Kanal 3 Toilette        : ' + str(raw_toilette) + ' ' + str(toilettenstand))
            #print ('Kanal 4 Batterie        : ' + str(raw_batteriespannung) + ' '  + str(batteriespannung))
            #print ('Kanal 5 Systemverbrauch : ' + str(raw_systemverbrauch) + ' '  + str(systemverbrauch))
            #print ('Kanal 6 Solarerzeugung  : ' + str(raw_solarerzeugung) + ' '  + str(solarerzeugung))
            #print ('Kanal 7 Netzbezug       : ' + str(raw_netzbezug) + ' '  + str(netzbezug))
            #print ('Kanal 8 Undefinded 2    : ' + str(raw_unused_2) + ' ' )#+ str(undefined_2)
            
            
            
            json_dict['batteriespannung'] =  batteriespannung
            json_dict['batteriefuellstand'] = batteriefuellstand
            json_dict['systemverbrauch'] = systemverbrauch
            json_dict['solarerzeugung'] = solarerzeugung
            json_dict['netzbezug'] = netzbezug
            json_dict['frischwasserstand'] = frischwasserstand
            json_dict['abwasserstand'] = abwasserstand
            json_dict['toilettenstand'] = toilettenstand
            print('AD-Wandler done')
            
            
            print('relais')
            if temperature_fridge_exhaust is not None and temperature_outside is not None and names.fridge_fan_mode == 'automatic':
                if temperature_fridge_exhaust >= names.fridge_exhaust_on and fridge_exhaust_fan is not True:
                    gpio_handling.setGPIO(pi_ager_names.gpio_fridge_exhaust_fan, pi_ager_names.relay_on)
                    fridge_exhaust_fan = True
                elif temperature_fridge_exhaust < names.fridge_exhaust_off and fridge_exhaust_fan is not False:
                    gpio_handling.setGPIO(pi_ager_names.gpio_fridge_exhaust_fan, pi_ager_names.relay_off)
                    fridge_exhaust_fan = False
            elif names.fridge_fan_mode == 'on':
                fridge_exhaust_fan = True
            else:
                fridge_exhaust_fan = False
            json_dict['fridge_exhaust_fan'] = fridge_exhaust_fan
            print('relais done')

            json_values = json.dumps(json_dict)
            with open(paths.get_path('values_json_file'), 'w') as file:
                file.write(json_values)

            
            print ('loop done')
            
            print ("\n")

                
            
    except KeyboardInterrupt:
        raise
    except Exception as e:
        _logger.warning('main loop failed')
        _logger.warning(e)
        traceback.print_exc()