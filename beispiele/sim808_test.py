import serial   
import RPi.GPIO as GPIO
import os, time, sys
import threading
import re
import json
import paths

GPIO.setmode(GPIO.BOARD)    
 
# Enable Serial Communication
#sim808 = serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

sim808 = 0
thread_sim808 = 0

def init_serial_sim808():
    global sim808
    sim808 = serial.Serial()
    sim808.port = "/dev/ttyS0"
    sim808.baudrate = 9600
    sim808.timeout = 1
    
    try:
        sim808.open() # try to open port, if possible print message and proceed with 'while True:'
        print ("port is opened!")

    except IOError: # if port is already opened, close it and open it again and print message
        sim808.close()
        sim808.open()
        print ("port was already open, was closed and opened again!")
    
    sim808_is_on = check_sim808()
    if sim808_is_on:
        sim808_startthread()
    
def check_sim808():
    at_command = write_sim808('AT'+'\r\n') # check module
    print (at_command)
    if 'OK' in at_command.decode('utf8'):
        print ('Module is on')
        time.sleep(0.5)
        return True
    else:
        print('Module must be set on')
        ## es muss der Pin angesprochen werden der das Modul anschaltet

def sim808_startthread():
    global thread_sim808
    thread_sim808 = threading.Thread(target = handle_sim808_recieve) #saves the raw GPS data over serial while the main program runs
    #thread2 = threading.Thread(target = user_input) #optional second thread
    thread_sim808.setDaemon(False)
    thread_sim808.start()
    
def write_sim808(command):
    global sim808
    #print(command)
    sim808.write(str.encode(command)) 
    # sim808.write(str.encode('AT'+'\r\n'))
    #reply = receiving()
    time.sleep(0.5)
    reply = sim808.read(sim808.inWaiting())
    #reply = sim808.read(20)
    #reply = sim808.readline()
    #time.sleep(1.0)
    #print (reply)
    return reply

def handle_sim808_recieve():
    global sim808
    #this fxn creates a txt file and saves only GPGGA sentences
    while 1:
        line = sim808.readline()
        line_str = str(line.decode('utf8'))
        try:
            #if(line_str[2] == 'G'): # $GPGGA
            if(line_str[2:8] == 'GNSINF'):
                #print('GPS Treffer: ' + line_str)
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
                
                json_values = json.dumps({"runs_status":gps_runs_status, "fix_status":gps_fix_status, "datum":gps_datum, "lat":gps_lat, "lon":gps_lon, "msl_altitude":gps_msl_altitude, "speed_over_ground":gps_speed_over_ground, "course_over_ground":gps_course_over_ground, "gps_satellites_in_view":gps_gps_satellites_in_view,"gnss_satellites_used":gps_gnss_satellites_used})
                with open(paths.get_path_gps_json_file(), 'w') as file:
                    file.write(json_values)
                #print('Done')
            # if(line_str[0] == 'O'): 
                # print('Treffer: ' + line_str)
        except:
            stream_serial()

                
def stream_serial():
    global sim808
    #stream data directly from the serial port
    line = sim808.readline()
    line_str = 'thread: ' + str(line)    
    print (line_str)
    
def user_input():
    global sim808
    global thread_sim808
    #runs in main loop looking for user commands
    tester = input()
    if tester == 'g':
        write_sim808('AT+CGNSPWR?'+'\r\n')
    if tester == 'p':
        write_sim808('AT+CGNSINF'+ '\r\n')
    if tester == 'a':
        write_sim808('AT'+ '\r\n')
    if tester == 'e':
        sim808.close()
        time.sleep(2)
        thread_sim808.isDaemon()
        sys.exit()

init_serial_sim808()  

while 1:
    user_input() # the main program waits for user input the entire time