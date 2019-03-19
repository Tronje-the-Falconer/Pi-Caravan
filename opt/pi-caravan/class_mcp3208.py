from abc import ABC
import inspect

import spidev
import time
import threading
 
class cl_mcp3208(threading.Thread):
    def __init__(self, spi_channel):
        threading.Thread.__init__(self)
        self.spi_channel = spi_channel
        self.conn = spidev.SpiDev(0, spi_channel)
        self.conn.max_speed_hz = 1000000 # 1MHz
        
        self.value =  [0]*8
        self.volt = [0.0]*8
        self.count = 0
        self.measurecount = 100
        
        self.channel_0 = None
        self.channel_1 = None
        self.channel_2 = None
        self.channel_3 = None
        self.channel_4 = None
        self.channel_5 = None
        self.channel_6 = None
        self.channel_7 = None
        
        try:
            self.mcp3208_startthread()
        except Exception as e:
            print("Error")
            print(e)
    
    def mcp3208_startthread(self):
        self.thread_mcp3208 = threading.Thread(target = self.handle_mcp3208_recieve)
        #thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_mcp3208.setDaemon(False)
        self.thread_mcp3208.start()
    
    def handle_mcp3208_recieve(self):
        timestamp = time.time()
        while 1:
                
            for i in range(8):
                self.value[i] += self.read(i) # werte werden 100 mal gelesen und aufaddiert
                #print('Raw' +str(i) + ' ' + str(self.value[i])) # 4008188
               



                if i == 6:
                    currenttime = time.time()
                    timecheck = currenttime - timestamp
                    if timecheck > 10:
                        value = self.read(i)
                        voltage = value*3.3/4095.0 # berechnung der anliegenden Spannung
                        linestring = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + '  ' + str(value) + ' Digits , Volt: ' + str(voltage)
                        print(linestring)
                        with open('/opt/pi-caravan/werte.txt', 'a') as file:
                            file.write(linestring)
                        timestamp = currenttime

                        

            if self.count == self.measurecount:
                for i in range(8):
                    self.value[i] /= self.measurecount # Werte müssen durch 100 getreilt werden um durchschnitt zu erhalten
                    if i == 0:
                        self.channel_0 = self.value[i] # Nullbasiert
                    elif i == 1:
                        self.channel_1 = self.value[i]
                    elif i == 2:
                        self.channel_2 = self.value[i]
                    elif i == 3:
                        self.channel_3 = self.value[i]
                    elif i == 4:
                        self.channel_4 = self.value[i]
                    elif i == 5:
                        self.channel_5 = self.value[i]
                    elif i == 6:
                        self.channel_6 = self.value[i]
                    elif i == 7:
                        self.channel_7 = self.value[i]
                    
                    #print('measurecount' + str(i) + ' ' + str(self.value[i])) # 4081.88
                    #self.volt[i] = self.value[i]*3.3/4095.0 # berechnung der anliegenden Spannung
                    #print(str(i) + '___' + str(self.volt[i]))
                self.count = 0
                
                
                for i in range(8):
                    self.value[i] = 0
    
    def __del__( self ):
        self.close

    def close(self):
        if self.conn != None:
            self.conn.close
            self.conn = None

    def read(self, adc_channel=0):
        # start bit, single end / diff bit (1/0), 3-bit channel number
        cmd1 = 4 | 2 | (( adc_channel & 4) >> 2)
        cmd2 = (adc_channel & 3) << 6
        
        # send 3 bytes command and get 3 bytes back from MC3208 - the last 12 bits are the measurement
        reply_bytes = self.conn.xfer2([cmd1, cmd2, 0])
        reply = ((reply_bytes[1] & 15) << 8) + reply_bytes[2]

        return reply
        
    def get_value(self, channel):
        if channel == 0:
            if self.channel_0 != None:
                return self.channel_0
            else:
                return 9999
        elif channel == 1:
            if self.channel_1 != None:
                return self.channel_1
            else:
                return 9999
        elif channel == 2:
            if self.channel_2 != None:
                return self.channel_2
            else:
                return 9999
        elif channel == 3:
            if self.channel_3 != None:
                return self.channel_3
            else:
                return 9999
        elif channel == 4:
            if self.channel_4 != None:
                return self.channel_4
            else:
                return 9999
        elif channel == 5:
            if self.channel_5 != None:
                return self.channel_5
            else:
                return 9999
        elif channel == 6:
            if self.channel_6 != None:
                return self.channel_6
            else:
                return 9999
        elif channel == 7:
            if self.channel_7 != None:
                return self.channel_7
            else:
                return 9999
        else:
            pass

class th_mcp3208(cl_mcp3208):   

    
    def __init__(self):
        pass


class cl_fact_mcp3208(ABC):
    __o_instance = None
    
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_mcp3208.__o_instance = i_instance
        
    @classmethod        
    def get_instance(self, spi_channel=0):
        if cl_fact_mcp3208.__o_instance is not None:
            return(cl_fact_mcp3208.__o_instance)
        cl_fact_mcp3208.__o_instance = cl_mcp3208(spi_channel)
        return(cl_fact_mcp3208.__o_instance)

    def __init__(self):
        pass  