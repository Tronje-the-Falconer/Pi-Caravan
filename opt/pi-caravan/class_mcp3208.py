#from spidev import SpiDev
import spidev
import time
 
class MCP3208:
        def __init__(self, spi_channel=0):
                self.spi_channel = spi_channel
                self.conn = spidev.SpiDev(0, spi_channel)
                self.conn.max_speed_hz = 1000000 # 1MHz

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
                
if __name__ == '__main__':
        mcp3208 = MCP3208(0)

        val =  [0]*8
        volt = [0.0]*8
        count = 0
        N = 100
        while True:
                count += 1
                
                for i in range(8):
                    val[i] += mcp3208.read(i) # werte werden 100 mal gelesen und aufaddiert
                    # print('Raw' +str(i) + ' ' + str(val[i])) # 4008188

                if count == N:
                    for i in range(8):
                        val[i] /= N # Werte müssen durch 100 getreilt werden um durchschnitt zu erhalten
                        # print('N' + str(i) + ' ' + str(val[i])) # 4081.88
                        volt[i] = val[i]*3.3/4095.0 # berechnung der anliegenden Spannung
                        print(str(i) + '___' + str(volt[i]))
                    count = 0
                    
                    
                    for i in range(8):
                        val[i] = 0
        

    