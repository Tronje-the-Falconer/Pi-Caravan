#!/usr/bin/python
# coding=utf-8
# pi_caravan_names.py
#------------------------------------------------------------#
"""
    pi-ager variables
    
    setting up variables
"""
import RPi.GPIO as gpio

#########################################
######### CONFIG BEGIN ##################
#########################################

fridge_exhaust_on = 40 # Einschalten des Lüfters
fridge_exhaust_off = 35 # Ausschalten des Lüfters
fridge_fan_mode = 'automatic' # 'auto' oder 'on' or 'off'

battery_maxvolt = 12.85
battery_volt1 = 0
battery_digits1 = 0
battery_volt2 = 12.4
battery_digits2 = 2870
battery_offset = 0


# 1wire sensorids
id_temperature_sensor_truma = '28-02131dc6e4aa'
id_temperature_sensor_fridge = '28-0213139dc0aa'
id_temperature_sensor_freezer = '28-021313977aaa'
id_temperature_sensor_trumavent = '28-00ff98430494'
id_temperature_sensor_fridge_exhaust = '28-000c98430a7b'

testsensor = '28-01143291af56'
test = False

#########################################
######### CONFIG ENDE ###################
#########################################



# SHT31
id_sht31_outdoor = 1 #
id_sht31_indoor = 2 # bridge vcc -> AD
# MCP3208

channel_frischwasser = 0
channel_abwasser = 1
channel_toilette = 2
channel_batteriespannung = 3
channel_systemverbrauch = 4
channel_solarerzeugung = 5
channel_netzbezug = 6
channel_unused_2 = 7
# GPIO
# Pinbelegung
# Pinleiste vertikal Pin 1 oben links pin 2 oben rechts
board_mode = gpio.BOARD           # GPIO board mode (BCM = Broadcom SOC channel number - numbers after GPIO Bsp. GPIO12=12 [GPIO.BOARD = Pin by number Bsp: GPIO12=32])

# linke Pinleiste:
# 3 V                           # Pin 1
gpio_i2c_sda = 3                # Pin 3 GPIO 2 fuer I2C SDA - Si4703(Radio), MPU6050(Gyroskop), SHT31
gpio_i2c_scl = 5                # Pin 5 GPIO 3 fuer I2C SCL
gpio_1wire = 7                  # Pin 7 GPIO 4 fuer OneWire - Temperatursensoren
# Ground                        # Pin 9
gpio_sim808_powerbutton = 11    # Pin 11 GPIO 17 fuer Powerbutton Sim808
gpio_notinuse_27 = 13           # Pin 13 GPIO 27 fuer 
gpio_notinuse_22 = 15           # Pin 15 GPIO 22 fuer 
# 3 V                           # Pin 17
gpio_mcp3208_din = 19           # Pin 19 GPIO 10 fuer MCP3208 D-IN
gpio_mcp3208_dout = 21          # Pin 21 GPIO 9 fuer MCP3208 D-OUT
gpio_mcp3208_clk = 23           # Pin 23 GPIO 11 fuer MCP3208 CLK
# Ground                        # Pin 25
gpio_notinuse_0 = 27            # Pin 27 GPIO 0 fuer
gpio_notinuse_5 = 29            # Pin 29 GPIO 5 fuer 
gpio_notinuse_6 = 31            # Pin 31 GPIO 6 fuer 
gpio_anemometer = 33            # Pin 33 GPIO 13 fuer Windmesser
gpio_piezzo = 35                # Pin 35 GPIO 19 fuer Piezzo
gpio_notinuse_26 = 37           # Pin 37 GPIO 26 fuer 
# Ground                        # Pin 39

# rechte Pinleiste:#
# 5 V                           # Pin 2
# 5 V                           # Pin 4
# Ground                        # Pin 6
gpio_TX = 8                     # Pin 8 GPIO 14 fuer UART TXD - SIM808(GPS)
gpio_RX = 10                    # Pin 10 GPIO 15 fuer UART RXD - SIM808(GPS)
gpio_fridge_exhaust_fan = 12    # Pin 12 GPIO 18 fuer Relais 1 (Abluft)
# Ground                        # Pin 14
gpio_relais2 = 16               # Pin 16 GPIO 23 fuer Relais 2
gpio_relais3 = 18               # Pin 18 GPIO 24 fuer Relais 3
# Ground                        # Pin 20
gpio_relais4 = 22               # Pin 22 GPIO 25 fuer Relais 4
gpio_mcp3208_cs_shdn = 24       # Pin 24 GPIO 8 fuer MCP3208 CS/SHDN
gpio_relais5 = 26               # Pin 26 GPIO 7 fuer Relais 5
gpio_notinuse_1 = 28            # Pin 28 GPIO 1 fuer
# Ground                        # Pin 30
gpio_relais6 = 32               # Pin 32 GPIO 12 fuer Relais 6
# Ground                        # Pin 34
gpio_relais7 = 36               # Pin 36 GPIO 16 fuer Relais 7
gpio_relais8 = 38               # Pin 38 GPIO 20 fuer Relais 8
gpio_gpio_si4703_rst = 40       # Pin 40 GPIO 21 fuer Si4703 RST (Radio)

pin_with_voltage = True                      # 3,3V = 1 | GPIO.HIGH  | TRUE
pin_without_voltage = (not pin_with_voltage) #   0V = 0 | GPIO.LOW   | FALSE
# Sainsmart Relais Vereinfachung 0 aktiv
relay_on = pin_without_voltage   # negative Logik!!! des Relay's, Schaltet bei 0 | GPIO.LOW  | False  ein
relay_off = (not relay_on)       # negative Logik!!! des Relay's, Schaltet bei 1 | GPIO.High | True aus

# fields
key_field = 'key'
value_field = 'value'
loglevel_file_field = 'loglevel_file'
loglevel_console_field = 'loglevel_console'


# tables
debug_table = 'debug'

def get_sensorid(sensor):
    # reset sensors for testcase
    global testsensor,  id_temperature_sensor_truma, id_temperature_sensor_trumavent, id_temperature_sensor_fridge, id_temperature_sensor_freezer, id_temperature_sensor_fridge_exhaust, id_sht31_outdoor, id_sht31_indoor
    if test:
        
        if sensor == 'sensor_truma':
            return testsensor
        if sensor == 'sensor_trumavent':
            return testsensor
        if sensor == 'sensor_fridge':
            return testsensor
        if sensor == 'sensor_freezer':
            return testsensor
        if sensor == 'sensor_fridge_exhaust':
            return testsensor
        if sensor == 'sht31_outdoor':
            return 1
        if sensor == 'sht31_indoor':
            return 1
    else:
        if sensor == 'sensor_truma':
            return id_temperature_sensor_truma
        if sensor == 'sensor_trumavent':
            return id_temperature_sensor_trumavent
        if sensor == 'sensor_fridge':
            return id_temperature_sensor_fridge
        if sensor == 'sensor_freezer':
            return id_temperature_sensor_freezer
        if sensor == 'sensor_fridge_exhaust':
            return id_temperature_sensor_fridge_exhaust
        if sensor == 'sht31_outdoor':
            return id_sht31_outdoor
        if sensor == 'sht31_indoor':
            return id_sht31_indoor