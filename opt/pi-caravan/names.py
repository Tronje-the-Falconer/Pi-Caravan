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
id_anemometer_sensor = 'Froggit'

# GPIO
# Pinbelegung
# Pinleiste vertikal Pin 1 oben links pin 2 oben rechts
board_mode = gpio.BOARD           # GPIO board mode (BCM = Broadcom SOC channel number - numbers after GPIO Bsp. GPIO12=12 [GPIO.BOARD = Pin by number Bsp: GPIO12=32])

# linke Pinleiste:
# 3 V                           # Pin 1
gpio_i2c_scl = 3                # Pin 3 GPIO 2 fuer I2C SDA
gpio_i2c_scl = 5                # Pin 5 GPIO 3 fuer I2C SCL
gpio_notinuse_4 = 7             # Pin 7 GPIO 4 fuer OneWire
# Ground                        # Pin 9
gpio_notinuse_17 = 11           # Pin 11 GPIO 17 fuer
gpio_notinuse_27 = 13           # Pin 13 GPIO 27 fuer
gpio_notinuse_22 = 15           # Pin 15 GPIO 22 fuer
# 3 V                           # Pin 17
gpio_notinuse_10 = 19           # Pin 19 GPIO 10 fuer on/off SIM808
gpio_notinuse_9 = 21            # Pin 21 GPIO 9 fuer Windmesser
gpio_notinuse_11 = 23           # Pin 23 GPIO 11 fuer
# Ground                        # Pin 25
gpio_notinuse_0 = 27            # Pin 27 GPIO 0 fuer
gpio_notinuse_5 = 29            # Pin 29 GPIO 5 fuer
gpio_notinuse_6 = 31            # Pin 31 GPIO 6 fuer
gpio_notinuse_13 = 33           # Pin 33 GPIO 13 fuer
gpio_notinuse_19 = 35           # Pin 35 GPIO 19 fuer
gpio_notinuse_26 = 37           # Pin 37 GPIO 26 für
# Ground                        # Pin 39

# rechte Pinleiste:#
# 5 V                           # Pin 2
# 5 V                           # Pin 4
# Ground                        # Pin 6
gpio_TX = 8                     # Pin 8 GPIO 14 fuer UART TXD
gpio_RX = 10                    # Pin 10 GPIO 15 fuer UART RXD
gpio_notinuse_18 = 12           # Pin 12 GPIO 18 fuer
# Ground                        # Pin 14
gpio_notinuse_23 = 16           # Pin 16 GPIO 23 fuer
gpio_notinuse_24 = 18           # Pin 18 GPIO 24 fuer
# Ground                        # Pin 20
gpio_notinuse_25 = 22           # Pin 22 GPIO 25 fuer
gpio_notinuse_8 = 24            # Pin 24 GPIO 8 fuer
gpio_notinuse_7 = 26            # Pin 26 GPIO 7 fuer
gpio_notinuse_1 = 28            # Pin 28 GPIO 1 fuer
# Ground                        # Pin 30
gpio_notinuse_12 = 32           # Pin 32 GPIO 12 fuer
# Ground                        # Pin 34
gpio_notinuse_16 = 36           # Pin 36 GPIO 16 fuer
gpio_notinuse_20 = 38           # Pin 38 GPIO 20 fuer
gpio_notinuse_21 = 40           # Pin 40 GPIO 21 fuer

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

