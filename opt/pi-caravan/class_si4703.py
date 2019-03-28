import threading

class si4703(threading.Thread):
   
    import smbus
    i2c = smbus.SMBus(1)
    
    def __init__(self, pin_rst= 40, pin_sda=3, i2c_adress=0x10, boardmode='BOARD'):
        print " "
        print "[__init__] Initializing si4703 class"
        
        self.pin_rst = pin_rst
        self.pin_sda = pin_sda
        self.boardmode = boardmode
        self.i2cAddress =  i2c_adress
        self.registers  = [0] * 16  # create 16 registers for SI4703
        self.readreg    = [0] * 32  # read 32 bytes
        
        #create list to write registers
        #only need to write registers 2-7 and since first byte is in the write
        # command then only need 11 bytes to write
        self.writereg   = [0] * 11
        
    def init(self):
        print "[init] Initializing si4703 radio module"
        
        import time
        import RPi.GPIO as gpio
        
        gpio.setwarnings(False)
        
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
        
        gpio.setup(self.pin_rst, gpio.OUT)    ## RST
        gpio.setup(self.pin_sda, gpio.OUT)     ## SDA Data
        
        print "[init] Setting up RST on GPIO pin " + str(self.pin_rst)
        print "[init] Setting up SDA on GPIO pin " + str(self.pin_sda)

        # init code needs to activate 2-wire (i2c) mode
        # the si4703 will not show up in i2cdetect until
        # you do these steps to put it into 2-wire (i2c) mode
        gpio.output(self.pin_sda, gpio.LOW) 
        time.sleep(.1)                
        gpio.output(self.pin_rst, gpio.LOW)
        time.sleep(.1)
        gpio.output(self.pin_rst, gpio.HIGH)
        time.sleep(0.5)
        
        # Read registers value from i2c
        self.readRegisters()
        
        # do init step, turn on oscillator
        self.registers[addresses.OSCILLATOR] = 0x8100
        self.writeRegisters()
        time.sleep(1)
        
        #Enable the Radio IC and turn off muted
        self.readRegisters()
        self.registers[addresses.POWERCFG] = 0x4001
        self.writeRegisters()
        time.sleep(.1)
        
        self.readRegisters()
        
        # Enable RDS
        print "[init] Enabling RDS"
        self.registers[addresses.SYSCONFIG1] |= (1<<12) 
        
        # Initialize volume
        print "[init] Initializing volume"
        self.registers[addresses.SYSCONFIG2] &= 0xFFF0; # Clear volume bits 
        self.registers[addresses.SYSCONFIG2] = 0x0000;  #Set volume to lowest 
        self.registers[addresses.SYSCONFIG3] = 0x0100;  #Set extended volume range (too loud for me without this) 
        
        # Write the configuration
        self.writeRegisters()
        
        print "[init] si4703 module initialization complete!"
        
    def readRegisters(self):
        print "[readRegisters] Reading registers"
       
        # Read bulk data from i2c
        self.readreg = self.i2c.read_i2c_block_data(self.i2cAddress, self.readreg[16], 32)
        
        self.registers[10] = self.readreg[0]  * 256 + self.readreg[1]
        self.registers[11] = self.readreg[2]  * 256 + self.readreg[3]
        self.registers[12] = self.readreg[4]  * 256 + self.readreg[5]
        self.registers[13] = self.readreg[6]  * 256 + self.readreg[7]
        self.registers[14] = self.readreg[8]  * 256 + self.readreg[9]
        self.registers[15] = self.readreg[10] * 256 + self.readreg[11]
        self.registers[0]  = self.readreg[12] * 256 + self.readreg[13]
        self.registers[1]  = self.readreg[14] * 256 + self.readreg[15]
        self.registers[2]  = self.readreg[16] * 256 + self.readreg[17]
        self.registers[3]  = self.readreg[18] * 256 + self.readreg[19]
        self.registers[4]  = self.readreg[20] * 256 + self.readreg[21]
        self.registers[5]  = self.readreg[22] * 256 + self.readreg[23]
        self.registers[6]  = self.readreg[24] * 256 + self.readreg[25]
        self.registers[7]  = self.readreg[26] * 256 + self.readreg[27]
        self.registers[8]  = self.readreg[28] * 256 + self.readreg[29]
        self.registers[9]  = self.readreg[30] * 256 + self.readreg[31]
        
    def writeRegisters(self):
        print "[readRegisters] Writting registers"
        
        cmd, self.writereg[0] = divmod(self.registers[2], 1<<8)
        
        self.writereg[1], self.writereg[2]  = divmod(self.registers[3], 1<<8)
        self.writereg[3], self.writereg[4]  = divmod(self.registers[4], 1<<8)
        self.writereg[5], self.writereg[6]  = divmod(self.registers[5], 1<<8)
        self.writereg[7], self.writereg[8]  = divmod(self.registers[6], 1<<8)
        self.writereg[9], self.writereg[10] = divmod(self.registers[7], 1<<8)
        
        w6 = self.i2c.write_i2c_block_data(self.i2cAddress, cmd, self.writereg)
        
        self.readreg[16] = cmd #readreg
        
        self.readRegisters()
        
    #####################################################################################
    ##    FUNCTIONALITIES
    #####################################################################################
    def getVolume(self):
        self.readRegisters()
        volume = self.registers[addresses.SYSCONFIG2]
        return volume
    
    def setVolume(self, volume):
        print "[setVolume] Set volume = ", volume
        if volume > 15:
            volume = 15
        if volume < 0:
            volume = 0
        self.readRegisters()
        self.registers[addresses.SYSCONFIG2] &= 0xFFF0  # Clear volume bits
        self.registers[addresses.SYSCONFIG2] = volume   # Set volume
        self.writeRegisters()
        
    def getChannel(self):
        self.readRegisters()
        channel = self.registers[addresses.READCHAN] & 0x03FF
        channel *= 2
        channel += 875
        return channel
        
    def setChannel(self, channel):
        print "[changeChannel] Changing channel to ", channel
        if channel < 878 or channel > 1080:
           return 
        
        channel *= 10
        channel -= 8750
        channel /= 20
        self.readRegisters()
        self.registers[addresses.CHANNEL] &= 0xFE00;    # Clear out the channel bits
        self.registers[addresses.CHANNEL] |= channel;   # Mask in the new channel
        self.registers[addresses.CHANNEL] |= (1<<15);   # Set the TUNE bit to start
        self.writeRegisters()
        while 1:
            self.readRegisters()
            if ((self.registers[addresses.STATUSRSSI] & (1<<14)) != 0):
                break
        self.registers[addresses.CHANNEL] &= ~(1<<15)
        self.writeRegisters()
        
    def seek(direction):
        self.readRegisters()
        self.registers[addresses.POWERCFG] |= (1<<10 )
        if direction == 0:
            self.registers[addresses.POWERCFG] &= ~(1<<1)
        else:
            self.registers[addresses.POWERCFG] |= (1<<9)
        self.registers[addresses.POWERCFG] |= (1<<8)
        self.writeRegisters()
        while 1:
            self.readRegisters()
            if ((self.registers[addresses.STATUSRSSI] & (1<<14)) != 0):
                break
        print "Trying Station ", float(float(self.getChannel())/float(10))
        self.readRegisters()
        valuesfbl = self.registers[addresses.STATUSRSSI] & (1<<13)
        self.registers[addresses.POWERCFG] &= ~(1<<8)
        self.writeRegisters()
        
class addresses:
    # Register addresses
    DEVICEID = 0x00
    CHIPID = 0x01
    POWERCFG = 0x02
    CHANNEL = 0x03
    SYSCONFIG1 = 0x04
    SYSCONFIG2 = 0x05
    SYSCONFIG3 = 0x06
    OSCILLATOR = 0x07
    STATUSRSSI = 0x0A
    READCHAN = 0x0B
    RDSA = 0x0C
    RDSB = 0x0D
    RDSC = 0x0E
    RDSD = 0x0F