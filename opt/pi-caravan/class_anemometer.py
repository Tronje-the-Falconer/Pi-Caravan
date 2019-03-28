from abc import ABC
import inspect

import smbus, time, sys
import math
import threading
import RPi.GPIO as gpio

#from cx_exception import *

        
class cl_anemometer:
    #---------------------------------------------------------
    def __init__(self, gpio_pin = 33, boardmode = 'BOARD'):
   
        if "get_instance" not in inspect.stack()[1][3]:
            print('use factoryclass')
            raise
            #raise cx_direct_call("Please use factory class")
      
        threading.Thread.__init__(self)
        self.boardmode = boardmode
        self.sensor_pin = gpio_pin
        self.anemometer_dict = None
        self.windspeed = None
        self.windspeedlist = []
        self.windaverage = None
        self.listcount = 0
        self.count = 0
        self.starttime = time.time()
        self.averagestarttime = time.time()
        self.thread_status = True
        
        if (gpio.getmode() == 11 or gpio.getmode() == -1) and self.boardmode == 'BOARD': # 11=BCM 10=Board -1=unset
            try:
                gpio.cleanup()
            except:
                pass
            print('changing Boardmode to BOARD')
            gpio.setmode(gpio.BOARD)
        elif self.boardmode == 'BCM' and (gpio.getmode() == 10 or gpio.getmode() == -1) :
            try:
                gpio.cleanup()
            except:
                pass
            print('changing Boardmode to BCM')
            gpio.setmode(gpio.BCM)
        else:
            print('Boardmode not changed')
            pass
        
        # setup pin as an input
        gpio.setup(self.sensor_pin, gpio.IN)
        
        # threaded event, to detect voltage falling on anemometer
        # bouncetime is in ms - edges within this time will be ignored
        gpio.add_event_detect(self.sensor_pin, gpio.FALLING, bouncetime=30)
        
        
        # deal with events by calling a function
        gpio.add_event_callback(self.sensor_pin, self.inputEventHandler)

        try:
            # self.sensor_path = glob.glob(base_path + self.sensorid)[0] + file_name
            self.anemometer_startthread()
        except:
            print("Bad sensor path")
    
    #---------------------------------------------------------
    def anemometer_startthread(self):
        self.thread_anemometer = threading.Thread(target = self.handle_anemometer_recieve)
        ##thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_anemometer.setDaemon(True)
        self.thread_anemometer.start()
    
    #---------------------------------------------------------
    def handle_anemometer_recieve(self):
        while self.thread_status:
            currenttime = time.time()
            #print(currenttime)
            measuretime = currenttime - self.starttime
            if measuretime >= 10:
                self.windspeed = ((self.count / 2) * (2 * 7.5 * math.pi) / measuretime) * 2.5
                self.windspeed = self.windspeed / 100
                self.anemometer_dict = {"windspeed":self.windspeed, "starttime":self.starttime, "stoptime":currenttime, "measuretime":measuretime, "triggercount":self.count}
                # print('windspeed')
                # print(self.windspeed)
                # print(self.anemometer_dict)
                
                self.windspeedlist.append(self.windspeed)
                self.listcount += 1
                self.count = 0
                self.starttime = time.time()
                measuretime = None
            
            ##zwei messungen 10min Durchschnitt und einmal kürzer
            
            ## Formel
            ## Geschwindigkeit = ((Runden x (2 x Radius x Pi)) / Zeit) x 2,5
            ## cwind=(x * (2*r*Π)/t)* 2.5
            # Wobei r, der mittlere Löffelradius (7cm) ist und x Runden (2 klicks pro Runde) in der Zeit t 
            # gemessen wurden. Der Wert 2.5 ist ein Literatur Wert. Er kommt zustande 
            # da der konvexe angeströmte Löffel das Anemometer abbremst, was 
            # kompensiert werden muss. (Ältere Literatur spricht noch von einem Wert 
            # von 3.0) Die Reibung der Aufhängung ist zwar damit noch nicht 
            # kompensiert, aber Messungen habe gezeigt, dass der Wert ziemlich gut 
            # stimmt.
        
            averagemesuretime = currenttime - self.averagestarttime
            if averagemesuretime >= 600: # 10 min
                self.windaverage = sum(self.windspeedlist) / self.listcount
                # print('windaverage')
                # print(self.windaverage)
                self.windspeedlist = []
                self.listcount = 0
                averagemesuretime = None
                self.averagestarttime = time.time()
            
    # def read_anemometer(self):
        
        # self.loopcounter = self.loopcounter + 1
        # time.sleep(1)
    
    #---------------------------------------------------------
    def inputEventHandler(self, pin):
        ''' count the edges and calculate windspeed...
            with "triggerflanke" you decide how much falling edges to count
            until we start the speed calculation
            small values will result in short reaction time und precise values
            high values will take longer and give a good average over the time
            very high values may need a longer sleep value in the main method
            espacially at low wind speeds
        '''
        self.count += 1
        #print(self.count)
        # triggerflanke = 10
        # if self.count == triggerflanke:
            ##the sensor ticks twice per rotation (2 falling edges)
            ##so with triggerflanke=20 this happens after ten rotations
            # stoptime = time.time()
            # currenttime = (stoptime - self.starttime)
            ##calculating windspeed
            # self.windspeed = triggerflanke / (currenttime * 1.3)
            # self.count = 0
            # self.anemometer_dict = {"windspeed":self.windspeed, "starttime":self.starttime, "stoptime":stoptime, "triggerflanke":triggerflanke}
            # self.starttime = time.time()
            ##print(self.anemometer_dict)
    
    #---------------------------------------------------------
    def cleanup(self):
        GPIO.cleanup() # don't leave a mess
    
    #---------------------------------------------------------
    def get_windspeed(self):
        return self.windspeed
    
    #---------------------------------------------------------
    def get_windaverage(self):
        return self.windaverage
    
    #---------------------------------------------------------
    def get_anemometer_dict(self):
        return self.anemometer_dict
    
    #---------------------------------------------------------
    def cleanup(self):
        self.thread_status = False

class th_anemometer(cl_anemometer):   
    
    #---------------------------------------------------------
    def __init__(self):
        pass


class cl_fact_anemometer(ABC):
    __o_instance = None
    
    #---------------------------------------------------------
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_anemometer.__o_instance = i_instance
    
    #---------------------------------------------------------
    @classmethod        
    def get_instance(self, gpio_pin):
        if cl_fact_anemometer.__o_instance is not None:
            return(cl_fact_anemometer.__o_instance)
        cl_fact_anemometer.__o_instance = cl_anemometer(gpio_pin)
        return(cl_fact_anemometer.__o_instance)
    
    #---------------------------------------------------------
    def __init__(self):
        pass
        
# test= cl_fact_anemometer().get_instance(33)
# while 1:
    # a=1