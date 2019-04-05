#!/usr/bin/python3
"""
    GPIO handling
    
    handling GPIO's
"""
import RPi.GPIO as gpio
import names
import logging_

global logger
logger = logging_.create_logger(__name__)
logger.debug('logging initialised')

###########----------------------------------------###########
class gpio_handling():
    
    #---------------------------------------------------------
    def __init__():
        pass
    
    #---------------------------------------------------------
    # Function Setup GPIO
    def setupGPIO():
        """
        setting up GPIO's (boardmode, in/out)
        """
        global logger
        logstring = 'setupGPIO()'
        logger.debug(logstring)
        gpio.setwarnings(False)
        
        
        # Einstellen der GPIO PINS
        # Pinleiste vertikal Pin 1 oben links pin 2 oben rechts
        
        # linke Pinleiste:
        # 3,3 V
        # gpio.setup(names.gpio_i2c_sda, gpio. )                # I2C
        #gpio.setup(names.gpio_i2c_scl, gpio.)                  # I2C
        #gpio.setup(names.gpio_1wire, gpio.)                    # 1-Wire
        # Ground
        gpio.setup(names.gpio_sim808_powerbutton, gpio.OUT )    # powerbutton Sim808
        # gpio.setup(names.gpio_notinuse_27, gpio. )            # 
        #gpio.setup(names.gpio_notinuse_22, gpio. )             # 
        # 3,3 V
        #gpio.setup(names.gpio_mcp3208_din, gpio.)              # D-IN
        #gpio.setup(names.gpio_mcp3208_dout, gpio.)             # D-Out
        # gpio.setup(names.gpio_mcp3208_clk, gpio.)             # CLK
        # Ground
        # gpio.setup(names.gpio_notinuse_0, gpio. )             # 
        # gpio.setup(names.gpio_notinuse_5, gpio.)              # 
        # gpio.setup(names.gpio_notinuse_6, gpio.)              # 
        gpio.setup(names.gpio_anemometer, gpio.IN )             # Windmesser
        gpio.setup(names.gpio_piezzo, gpio.OUT )                # Piezzo
        #gpio.setup(names.gpio_notinuse_26, gpio.)              # 
        # Ground

        # rechte Pinleiste:
        # 5 V
        # 5 V
        # Ground
        # gpio.setup(names.gpio_TX, gpio. )                     # TX
        # gpio.setup(names.gpio_RX, gpio. )                     # RX
        gpio.setup(names.gpio_fridge_exhaust_fan, gpio.OUT)     # fridge exhaust fan setzen
        # Ground
        gpio.setup(names.gpio_relais2, gpio.OUT)                # Relais2 setzen
        gpio.setup(names.gpio_relais3, gpio.OUT)                # Relais3 setzen
        # Ground
        gpio.setup(names.gpio_relais4, gpio.OUT)                # Relais4 setzen
        #gpio.setup(names.gpio_mcp3208_cs_shdn, gpio.OUT)       # Data
        gpio.setup(names.gpio_relais5, gpio.OUT)                # Relais5 setzen
        # gpio.setup(names.gpio_notinuse_1, gpio. )             #
        # Ground
        gpio.setup(names.gpio_relais6, gpio.OUT)                # Relais6 setzen
        # Ground
        gpio.setup(names.gpio_relais7, gpio.OUT)                # Relais7 setzen
        gpio.setup(names.gpio_relais8, gpio.OUT )               # Relais8 setzen
        gpio.setup(names.gpio_gpio_si4703_rst, gpio.OUT)        # Si4703 (Radio)
    
    #---------------------------------------------------------
    def defaultGPIO():
        """
        setting up default gpio (1/0)
        """
        global logger
        logstring = 'defaultGPIO()'
        logger.debug(logstring)
        
        gpio.output(names.gpio_sim808_powerbutton, names.pin_without_voltage)   # powerbutton sim808 nur zum an und ausschalten 
        #gpio.output(names.gpio_anemometer, names.pin_without_voltage)          # Anemometer ist Eingang
        gpio.output(names.gpio_piezzo, names.pin_without_voltage)               # Piezzo standardmaessig aus
        gpio.output(names.gpio_fridge_exhaust_fan, names.relay_off)             # Abluft Kühlschrank standardmaessig aus
        gpio.output(names.gpio_relais2, names.relay_off)                        # Relais standardmaessig aus
        gpio.output(names.gpio_relais3, names.relay_off)                        # Relais standardmaessig aus
        gpio.output(names.gpio_relais4, names.relay_off)                        # Relais standardmaessig aus
        gpio.output(names.gpio_relais5, names.relay_off)                        # Relais standardmaessig aus
        gpio.output(names.gpio_relais6, names.relay_off)                        # Relais standardmaessig aus
        gpio.output(names.gpio_relais8, names.relay_off)                        # Relais standardmaessig aus
        # gpio.output(names.gpio_notinuse_27, names.pin_without_voltage)
        # gpio.output(names.gpio_notinuse_22, names.pin_without_voltage)
        # gpio.output(names.gpio_notinuse_0, names.pin_without_voltage)
        # gpio.output(names.gpio_notinuse_5, names.pin_without_voltage)
        # gpio.output(names.gpio_notinuse_6, names.pin_without_voltage)
        # gpio.output(names.gpio_notinuse_26, names.pin_without_voltage)
        # gpio.output(names.gpio_notinuse_1, names.pin_without_voltage)
    
    #---------------------------------------------------------
    def setGPIO_boardmode():
        """
        set GPIO boardmode
        """
        # Board mode wird gesetzt
        gpio.setmode(names.board_mode)
    
    #---------------------------------------------------------
    def setGPIO(gpio, state):
        """
        change gpio setting on/off
        """
        gpio.output(gpio, state)
    
    #---------------------------------------------------------
    def gpios_are_in_use(self):
        """
        setting up gpio_xxx_used variables
        """
        gpio_sim808_powerbutton_used = self.gpio_is_in_use(names.gpio_sim808_powerbutton)
        #gpio_anemometer_used = self.gpio_is_in_use(names.gpio_anemometer) # Ist Eingang
        gpio_piezzo_used = self.gpio_is_in_use(names.gpio_piezzo)
        gpio_fridge_exhaust_fan_used = self.gpio_is_in_use(names.gpio_fridge_exhaust_fan)
        gpio_relais2_used = self.gpio_is_in_use(names.gpio_relais2)
        gpio_relais3_used = self.gpio_is_in_use(names.gpio_relais3)
        gpio_relais4_used = self.gpio_is_in_use(names.gpio_relais4)
        gpio_relais5_used = self.gpio_is_in_use(names.gpio_relais5)
        gpio_relais6_used = self.gpio_is_in_use(names.gpio_relais6)
        gpio_relais8_used = self.gpio_is_in_use(names.gpio_relais7)
        gpio_notinuse_27_used = self.gpio_is_in_use(names.gpio_notinuse_27)
        gpio_notinuse_22_used = self.gpio_is_in_use(names.gpio_notinuse_22)
        gpio_notinuse_0_used = self.gpio_is_in_use(names.gpio_notinuse_0)
        gpio_notinuse_5_used = self.gpio_is_in_use(names.gpio_notinuse_5)
        gpio_notinuse_6_used = self.gpio_is_in_use(names.gpio_notinuse_6)
        gpio_notinuse_26_used = self.gpio_is_in_use(names.gpio_notinuse_26)
        gpio_notinuse_1_used = self.gpio_is_in_use(names.gpio_notinuse_1)
        
        if gpio_sim808_powerbutton_used or gpio_piezzo_used or gpio_fridge_exhaust_fan_used or gpio_relais2_used or gpio_relais3_used or gpio_relais4_used or gpio_relais5_used or gpio_relais6_used or gpio_relais8_used or gpio_notinuse_27_used or gpio_notinuse_22_used or gpio_notinuse_0_used or gpio_notinuse_5_used or gpio_notinuse_6_used or gpio_notinuse_26_used or gpio_notinuse_1_used:
            return True
        else:
            return False
    
    #---------------------------------------------------------
    def gpio_is_in_use(self, gpio):
        """
        check if GPIO is in use
        """
        gpio_used = gpio.gpio_function(gpio)
        
        if gpio_used == -1:
            return False
        else:
            return True
    
    #---------------------------------------------------------
    def gpio_cleanup():
        gpio.cleanup()