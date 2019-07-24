import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT )
print('start')
gpio.output(11, gpio.HIGH)
print('sleep')
time.sleep(2)               # wait for 1 second
print('Low')
gpio.output(11, gpio.LOW)

gpio.cleanup()