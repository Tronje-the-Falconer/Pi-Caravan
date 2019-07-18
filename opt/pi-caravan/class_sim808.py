from abc import ABC
import inspect


import serial   
import RPi.GPIO as gpio
import os, time, sys
import threading
import re
import json
import paths

gpio.setmode(gpio.BOARD)    

class cl_sim808(threading.Thread):
    
    #---------------------------------------------------------
    def __init__(self, pin=11):
        threading.Thread.__init__(self)
        
        self.pin = pin
        self.sim808 = 0
        self.thread_sim808 = 0
        
        self.sim808 = serial.Serial()
        self.sim808.port = "/dev/ttyS0"
        self.sim808.baudrate = 9600
        self.sim808.timeout = 1
        self.gps_dict = None
        self.thread_status = True
        self.sim808_is_ready = False
        
####################   Reihenfolge prüfen!
        
        try:
            self.sim808.open() # try to open port, if possible print message and proceed with 'while True:'
            #print ("sim808 port is opened!")

        except IOError: # if port is already opened, close it and open it again and print message
            self.sim808.close()
            self.sim808.open()
            #print ("sim808 port was already open, was closed and opened again!")
        
        self.sim808_is_ready = self.check_sim808()
        if self.sim808_is_ready:
            self.sim808_startthread()
    
    #---------------------------------------------------------
    def sim808_startthread(self):
        self.thread_sim808 = threading.Thread(target = self.handle_sim808_recieve) #saves the raw GPS data over serial while the main program runs
        #thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_sim808.setDaemon(True)
        self.thread_sim808.start()
    
    #---------------------------------------------------------
    def handle_sim808_recieve(self):
        #this fxn creates a txt file and saves only GPGGA sentences
        while self.thread_status:
            line = self.sim808.readline()
            line_str = str(line.decode('utf8'))
            try:
                #if(line_str[2] == 'G'): # $GPGGA
                if(line_str[2:8] == 'GNSINF'):
                    #print('sim808:  GPS Treffer: ' + line_str)
                    gps_list = re.sub(r'.*:', '', line_str)
                    #gps_list = re.sub(r', \r\n', '', gps_list)
                    gps_list = gps_list.strip()
                    ##  GNSS run status,Fix status,UTC date & Time,Latitude,Longitude,MSL Altitude,Speed Over Ground,Course Over Ground,Fix Mode,Reserved1,HDOP,PDOP,VDOP,Reserved2,GNSS Satellites in View,GNSS Satellites Used,GLONASS SatellitesUsed,Reserved3,C/N0 max,HPA,VPA
                    sim808_list = gps_list.split(",")
                    gps_runs_status = int(sim808_list[0])
                    gps_fix_status = int(sim808_list[1])
                    gps_datum = float(sim808_list[2]) #utc date & time
                    gps_lat = float(sim808_list[3])
                    gps_lon = float(sim808_list[4])
                    gps_msl_altitude = float(sim808_list[5])
                    gps_speed_over_ground = float(sim808_list[6])
                    gps_course_over_ground = float(sim808_list[7])
                    #gps_fix_mode = int(sim808_list[8])
                    #gps_reserved1 = sim808_list[9]
                    #gps_hdop = float(sim808_list[10])
                    #gps_pdop = float(sim808_list[11])
                    #gps_vdop = float(sim808_list[12])
                    #gps_reserved2 = sim808_list[13]
                    gps_gps_satellites_in_view = int(sim808_list[14])
                    gps_gnss_satellites_used = int(sim808_list[15])
                    #gps_glonass_satellites_used = int(sim808_list[16])
                    #gps_reserved3 = sim808_list[17]
                    #gps_c_n0_max = int(sim808_list[18])
                    #gps_hpa = sim808_list[19]
                    #gps_vpa = sim808_list[20]
                    
                    self.gps_dict = {"runs_status":gps_runs_status, "fix_status":gps_fix_status, "date":gps_datum, "lat":gps_lat, "lon":gps_lon, "msl_altitude":gps_msl_altitude, "speed_over_ground":gps_speed_over_ground, "course_over_ground":gps_course_over_ground, "gps_satellites_in_view":gps_gps_satellites_in_view,"gnss_satellites_used":gps_gnss_satellites_used}
                    # print('sim808: dict_written')
                    # print(self.gps_dict)
                    # return gps_return_list
                    
                # if(line_str[0] == 'O'): 
                    # print('Treffer: ' + line_str)
                # else:
                    # self.stream_serial()
            except Exception as e:
                print(e)
    
    #---------------------------------------------------------
    def stream_serial(self):
        #stream data directly from the serial port
        line = self.sim808.readline()
        line_str = 'sim808: ' + str(line)    
        #print (line_str)
    
    #---------------------------------------------------------
    def get_gps_dict(self):
        return self.gps_dict
    
    #---------------------------------------------------------
    def get_sim808_ready(self):
        return self.sim808_is_ready
    #---------------------------------------------------------
    def check_sim808(self):
        if self.check_module_is_on():
            #if self.check_GNSS_power_supply():
            if self.check_GPS_status():
                if self.check_GPS_fix():
                    return True
    
    #---------------------------------------------------------
    def check_module_is_on(self):
        self.sim808.write(str.encode('AT'+'\r\n')) # check module
        time.sleep(0.5)
        at_command = self.sim808.read(self.sim808.inWaiting())
        #print ('sim808_check')
        #print(at_command)
        if 'OK' in at_command.decode('utf8'):
            #print('sim808: Module is on')
            return True
        else:
            self.sim808_is_ready = False
            #print('sim808: Module must be set on, power with pin')
            self.power_on_off_module()
            self.check_module_is_on()
    #---------------------------------------------------------
    def check_GNSS_power_supply(self):
        self.sim808.write(str.encode('AT+CGNSPWR?'+'\r\n'))
        time.sleep(0.5)
        at_command = self.sim808.read(self.sim808.inWaiting())
        #print ('sim808_check')
        #print(at_command)
        if '+CGNSPWR: 1' in at_command.decode('utf8'):
            #print('sim808: GNSSpowersuply is on')
            return True
        else:
            self.sim808_is_ready = False
            #print('sim808: GNSSpowersuply is 0, setting it on')
            self.sim808.write(str.encode('AT+CGNSPWR=1'+'\r\n'))
            time.sleep(0.5)
    #---------------------------------------------------------
    def check_GPS_status(self):
        self.sim808.write(str.encode('AT+CGPSPWR?'+'\r\n'))
        time.sleep(0.5)
        at_command = self.sim808.read(self.sim808.inWaiting())
        at_command = at_command.decode('utf8')
        #print(at_command)
        if 'CGPSPWR: 1' in at_command:            
            print('sim808: GPS runs')
            return True
        else:
            self.sim808_is_ready = False
            #print('sim808: GPS is not running, turning on')
            self.sim808.write(str.encode('AT+CGPSPWR=1'+'\r\n'))
            time.sleep(1)
            self.check_GPS_status()
                
    #---------------------------------------------------------
    def check_GPS_fix(self):
        self.sim808.write(str.encode('AT+CGPSSTATUS?'+'\r\n'))
        time.sleep(0.5)
        at_command = self.sim808.read(self.sim808.inWaiting())
        at_command = at_command.decode('utf8')
        if 'D Fix' in at_command:
            #print('sim808: GPS has fix')
            return True
        else:
            self.sim808_is_ready = False
            #print('sim808: GPS has no fix, trying again')
            time.sleep(1)
            self.check_GPS_fix()
    #---------------------------------------------------------
    def write_sim808(self, command):
        # print('sim808 command ' + command)
        self.sim808.write(str.encode(command)) 
        # self.sim808.write(str.encode('AT'+'\r\n'))
        #reply = receiving()
        time.sleep(0.5)
        #reply = self.sim808.read(self.sim808.inWaiting())
        #reply = self.sim808.read(20)
        #reply = self.sim808.readline()
        #time.sleep(1.0)
        #print (reply)
        #return reply
            
    #---------------------------------------------------------
    def power_on_off_module(self):
        gpio.output(self.pin, gpio.HIGH)
        time.sleep(2)               # wait for 1 second
        gpio.output(self.pin, gpio.LOW)
        time.sleep(2)
       
    #---------------------------------------------------------
    def cleanup(self):
        self.thread_status = False
        
class th_sim808(cl_sim808):   
    
    #---------------------------------------------------------
    def __init__(self):
        pass

class cl_fact_sim808(ABC):
    __o_instance = None
    
    #---------------------------------------------------------
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_sim808.__o_instance = i_instance
    
    #---------------------------------------------------------
    @classmethod        
    def get_instance(self, pin=11):
        if cl_fact_sim808.__o_instance is not None:
            return(cl_fact_sim808.__o_instance)
        cl_fact_sim808.__o_instance = cl_sim808(pin)
        return(cl_fact_sim808.__o_instance)
    
    #---------------------------------------------------------
    def __init__(self):
        pass
        
def user_input():
    global sim808
    global thread_sim808
    #runs in main loop looking for user commands
    tester = input()
    if tester == 'g':
        sim808.write_sim808('AT+CGNSPWR?'+'\r\n')
    if tester == 'p':
        sim808.write_sim808('AT+CGNSINF'+ '\r\n')
    if tester == 'a':
        sim808.write_sim808('AT'+ '\r\n')
    if tester == 'e':
        sim808.sim808.close()
        
# sim808 = Sim808()
# while 1:
    # user_input() # the main program waits for user input the entire time