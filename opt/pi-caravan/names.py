#!/usr/bin/python
# coding=utf-8
# pi_caravan_names.py
#------------------------------------------------------------#
"""
    pi-ager variables
    
    setting up variables
"""
import RPi.GPIO as gpio

# 1wire sensorids
id_temperature_sensor_outside='28-0213139dc0aa'
id_temperature_sensor_inside='28-021313977aaa'
id_temperature_sensor_fridge='28-00ff98430494'
id_temperature_sensor_fridge_exhaust='28-000c98430a7b'

# classnames
id_gyro_sensor='MPU6050_knaus'
id_sim808_sensor = 'sim808_knaus'

# GPIO
# Pinbelegung
# Pinleiste vertikal Pin 1 oben links pin 2 oben rechts
board_mode = gpio.BCM           # GPIO board mode (BCM = Broadcom SOC channel number - numbers after GPIO Bsp. GPIO12=12 [GPIO.BOARD = Pin by number Bsp: GPIO12=32])

# linke Pinleiste:
# 3 V
gpio_i2c_scl = 2                # GPIO fuer I2C SDA
gpio_i2c_scl = 3                # GPIO fuer I2C SCL
gpio_notinuse_4 = 4             # GPIO fuer
# Ground
gpio_dht22_data = 17            # GPIO fuer Data Temperatur/Humidity Sensor
gpio_dht22_sync = 27            # GPIO fuer Sync Temperatur/Humidity Sensor
gpio_notinuse_22 = 22           # GPIO fuer
# 3 V
gpio_notinuse_10 = 10           # GPIO fuer on/off SIM808
gpio_notinuse_9 = 9             # GPIO fuer Windmesser
gpio_notinuse_11 = 11           # GPIO fuer
# Ground
gpio_notinuse_0 = 0
gpio_notinuse_5 = 5             # GPIO fuer
gpio_notinuse_6 = 6             # GPIO fuer
gpio_notinuse_13 = 13           # GPIO fuer
gpio_notinuse_19 = 19           # GPIO fuer
gpio_notinuse_26 = 26           # GPIO für
# Ground

# rechte Pinleiste:#
# 5 V
# 5 V
# Ground
gpio_TX = 14                    # GPIO fuer UART TXD
gpio_RX = 15                    # GPIO fuer UART RXD
gpio_notinuse_18 = 18           # GPIO fuer
# Ground
gpio_notinuse_23 = 23           # GPIO fuer
gpio_notinuse_24 = 24           # GPIO fuer
# Ground
gpio_notinuse_25 = 25           # GPIO fuer
gpio_notinuse_8 = 8             # GPIO fuer
gpio_notinuse_7 = 7             # GPIO fuer
gpio_notinuse_1 = 1
# Ground
gpio_notinuse_12 = 12
# Ground
gpio_notinuse_16 = 16     # GPIO fuer
gpio_notinuse_20 = 20    # GPIO fuer
gpio_notinuse_21 = 21    # GPIO fuer

pin_with_voltage = True                      # 3,3V = 1 | GPIO.HIGH  | TRUE
pin_without_voltage = (not pin_with_voltage) #   0V = 0 | GPIO.LOW   | FALSE
# Sainsmart Relais Vereinfachung 0 aktiv
relay_on = pin_without_voltage   # negative Logik!!! des Relay's, Schaltet bei 0 | GPIO.LOW  | False  ein
relay_off = (not relay_on)       # negative Logik!!! des Relay's, Schaltet bei 1 | GPIO.High | True aus

# fields
key_field = 'key'
value_field = 'value'
loglevel_file_field='loglevel_file'
loglevel_console_field='loglevel_console'


# tables
debug_table = 'debug'

