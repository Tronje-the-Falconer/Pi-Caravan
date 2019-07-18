from abc import ABC
import inspect

from class_kalman_filter import cl_kalman_filter
import smbus, time
import math
import threading

class cl_mpu6050(threading.Thread):
    
    #---------------------------------------------------------
    def __init__(self):
        threading.Thread.__init__(self)
        
        # mpu6050 registers and their addresses
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) for Revision 1
        self.deviceaddress = 0x68       # via i2cdetect
        self.power_mgmt_1 = 0x6B
        self.power_mgmt_2 = 0x6C
        self.smplrt_div = 0x19
        self.config = 0x1A
        self.gyro_config = 0x1B
        self.accel_config = 0x1C
        self.int_enable = 0x38
        self.accel_xout_h = 0x3B
        self.accel_yout_h = 0x3D
        self.accel_zout_h = 0x3F
        self.gyro_xout_h = 0x43
        self.gyro_yout_h = 0x45
        self.gyro_zout_h = 0x47
        self.temp_out_h = 0x41
        
        # scale modifiers
        self.accel_scale_modifier_2g = 16384.0
        self.accel_scale_modifier_4g = 8192.0
        self.accel_scale_modifier_8g = 4096.0
        self.accel_scale_modifier_16g = 2048.0
        
        self.gyro_scale_modifier_250deg = 131.0
        self.gyro_scale_modifier_500deg = 65.5
        self.gyro_scale_modifier_1000deg = 32.8
        self.gyro_scale_modifier_2000deg = 16.4
        
        # pre-defined ranges
        self.accel_range_2g = 0x00
        self.accel_range_4g = 0x08
        self.accel_range_8g = 0x10
        self.accel_range_16g = 0x18
        
        self.gyro_range_250deg = 0x00
        self.gyro_range_500deg = 0x08
        self.gyro_range_1000deg = 0x10
        self.gyro_range_2000deg = 0x18
        
        
        
        self.kalmanX = cl_kalman_filter()
        self.kalmanY = cl_kalman_filter()

        self.RestrictPitch = True    #set to False to restrict roll to ±90deg instead - please read: http://www.freescale.com/files/sensors/doc/app_note/AN3461.pdf
        self.radToDeg = 57.2957786
        self.kalAngleX = 0
        self.kalAngleY = 0
        self.mpu6050_dict = None
        self.mpu6050_raw_dict = None
        self.thread_status = True

        try:
            #write to sample rate register
            self.bus.write_byte_data(self.deviceaddress, self.smplrt_div, 7)

            #Write to power management register
            self.bus.write_byte_data(self.deviceaddress, self.power_mgmt_1, 1) # activate to call module

            #Write to Configuration register
            #Setting DLPF (last three bit of 0X1A to 6 i.e '110' It removes the noise due to vibration.) https://ulrichbuschbaum.wordpress.com/2015/01/18/using-the-mpu6050s-dlpf/
            self.bus.write_byte_data(self.deviceaddress, self.config, int('0000110',2))

            #Write to Gyro configuration register
            self.bus.write_byte_data(self.deviceaddress, self.gyro_config, 24)

            #Write to interrupt enable register
            self.bus.write_byte_data(self.deviceaddress, self.int_enable, 1)
            
            
            # self.bus.write_byte_data(self.deviceaddress, 0x1A, 6) #deeppassfilter on
            # self.set_gyro_range(self.gyro_range_250deg)
            # self.set_accel_range(self.accel_range_2g)
            time.sleep(1)
            
            # read Accelerometer raw value
            self.accX = self.read_raw_data(self.accel_xout_h)
            self.accY = self.read_raw_data(self.accel_yout_h)
            self.accZ = self.read_raw_data(self.accel_zout_h)
            
            # read temperature raw value
            self.temp = self.read_raw_data(self.temp_out_h)
            self.temperature = (self.temp / 340.0) + 36.53
            
            if (self.RestrictPitch):
                self.roll = math.atan2(self.accY, self.accZ) * self.radToDeg
                self.pitch = math.atan(-self.accX/math.sqrt((self.accY**2)+(self.accZ**2))) * self.radToDeg
            else:
                self.roll = math.atan(self.accY/math.sqrt((self.accX**2)+(self.accZ**2))) * self.radToDeg
                self.pitch = math.atan2(-self.accX, self.accZ) * self.radToDeg
            #print(self.roll)
            self.kalmanX.setAngle(self.roll)
            self.kalmanY.setAngle(self.pitch)
            self.gyroXAngle = self.roll;
            self.gyroYAngle = self.pitch;
            self.compAngleX = self.roll;
            self.compAngleY = self.pitch;

            self.timer = time.time()
            self.flag = 0
            
            self.mpu6050_startthread()
            self.running = True # setting the thread running to true
        except Exception as e:
            print("No connection to gyroscope")
            print(e)
            self.running = False
    
    #---------------------------------------------------------
    def mpu6050_startthread(self):
        self.thread_mpu6050 = threading.Thread(target = self.handle_mpu6050_recieve)
        #thread2 = threading.Thread(target = user_input) #optional second thread
        self.thread_mpu6050.setDaemon(True)
        self.thread_mpu6050.start()
    
    #---------------------------------------------------------
    def handle_mpu6050_recieve(self):
        while self.thread_status:
            if(self.flag > 100): #Problem with the connection
                print("There is a problem with the connection")
                flag=0
                continue
            try:
                # read Accelerometer raw value
                self.accX = self.read_raw_data(self.accel_xout_h)
                self.accY = self.read_raw_data(self.accel_yout_h)
                self.accZ = self.read_raw_data(self.accel_zout_h)

                # read Gyroscope raw value
                self.gyroX = self.read_raw_data(self.gyro_xout_h)
                self.gyroY = self.read_raw_data(self.gyro_yout_h)
                self.gyroZ = self.read_raw_data(self.gyro_zout_h)
                
                # read temperature raw value
                self.temp = self.read_raw_data(self.temp_out_h)
                
                self.dt = time.time() - self.timer
                self.timer = time.time()
                
                self.temperature = (self.temp / 340.0) + 36.53
                
                if (self.RestrictPitch):
                    self.roll = math.atan2(self.accY, self.accZ) * self.radToDeg
                    self.pitch = math.atan(-self.accX/math.sqrt((self.accY**2)+(self.accZ**2))) * self.radToDeg
                else:
                    self.roll = math.atan(self.accY/math.sqrt((self.accX**2)+(self.accZ**2))) * self.radToDeg
                    self.pitch = math.atan2(-self.accX, self.accZ) * self.radToDeg

                self.gyroXRate = self.gyroX/131
                self.gyroYRate = self.gyroY/131

                if (self.RestrictPitch):

                    if((self.roll < -90 and self.kalAngleX >90) or (self.roll > 90 and self.kalAngleX < -90)):
                        self.kalmanX.setAngle(roll)
                        self.complAngleX = roll
                        self.kalAngleX   = roll
                        self.gyroXAngle  = roll
                    else:
                        self.kalAngleX = self.kalmanX.getAngle(self.roll, self.gyroXRate, self.dt)

                    if(abs(self.kalAngleX)>90):
                        self.gyroYRate  = -self.gyroYRate
                        self.kalAngleY  = self.kalmanY.getAngle(self.pitch, self.gyroYRate, self.dt)
                #else:

                    if((self.pitch < -90 and self.kalAngleY >90) or (self.pitch > 90 and self.kalAngleY < -90)):
                        self.kalmanY.setAngle(self.pitch)
                        self.complAngleY = self.pitch
                        self.kalAngleY   = self.pitch
                        self.gyroYAngle  = self.pitch
                    else:
                        self.kalAngleY = self.kalmanY.getAngle(self.pitch, self.gyroYRate, self.dt)

                    if(abs(self.kalAngleY)>90):
                        self.gyroXRate  = -self.gyroXRate
                        self.kalAngleX = self.kalmanX.getAngle(self.roll, self.gyroXRate, self.dt)

                #angle = (rate of change of angle) * change in time
                self.gyroXAngle = self.gyroXRate * self.dt
                self.gyroYAngle = self.gyroYAngle * self.dt
                
                #compAngle = constant * (old_compAngle + angle_obtained_from_gyro) + constant * angle_obtained from accelerometer
                self.compAngleX = 0.93 * (self.compAngleX + self.gyroXRate * self.dt) + 0.07 * self.roll
                self.compAngleY = 0.93 * (self.compAngleY + self.gyroYRate * self.dt) + 0.07 * self.pitch

                if ((self.gyroXAngle < -180) or (self.gyroXAngle > 180)):
                    self.gyroXAngle = self.kalAngleX
                if ((self.gyroYAngle < -180) or (self.gyroYAngle > 180)):
                    self.gyroYAngle = self.kalAngleY

                #print("Angle X: " + str(self.kalAngleX)+"   " +"Angle Y: " + str(self.kalAngleY))
                #print(str(roll)+"  "+str(gyroXAngle)+"  "+str(compAngleX)+"  "+str(kalAngleX)+"  "+str(pitch)+"  "+str(gyroYAngle)+"  "+str(compAngleY)+"  "+str(kalAngleY))
                
                self.mpu6050_dict = {"gyroskop_xout":self.kalAngleX, "gyroskop_yout": self.kalAngleY, "temperature":self.temperature, "time":self.timer }
                time.sleep(0.005)

            except Exception as e:
                print(e)
                self.flag += 1

    #---------------------------------------------------------
    def read_raw_data(self, addr):
    #Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(self.deviceaddress, addr)
        low = self.bus.read_byte_data(self.deviceaddress, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

    #---------------------------------------------------------
    def get_mpu6050_dict(self):
        return self.mpu6050_dict    
    
    
     #---------------------------------------------------------
    def set_gyro_range(self, gyro_range):
        """Sets the range of the gyroscope to range.
        gyro_range -- the range to set the gyroscope to. Using a pre-defined
        range is advised.
        """
        # First change it to 0x00 to make sure we write the correct value later
        self.bus.write_byte_data(self.deviceaddress, self.gyro_config, 0x00)

        # Write the new range to the ACCEL_CONFIG register
        self.bus.write_byte_data(self.deviceaddress, self.gyro_config, gyro_range)
    
    #---------------------------------------------------------
    def set_accel_range(self, accel_range):
        """Sets the range of the accelerometer to range.
        accel_range -- the range to set the accelerometer to. Using a
        pre-defined range is advised.
        """
        # First change it to 0x00 to make sure we write the correct value later
        self.bus.write_byte_data(self.deviceaddress, self.accel_config, 0x00)

        # Write the new range to the ACCEL_CONFIG register
        self.bus.write_byte_data(self.deviceaddress, self.accel_config, accel_range)
        
    #---------------------------------------------------------
    def cleanup(self):
        self.thread_status = False
        
class th_mpu6050(cl_mpu6050):   
    
    #---------------------------------------------------------
    def __init__(self):
        pass


class cl_fact_mpu6050(ABC):
    __o_instance = None
    
    #---------------------------------------------------------
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_mpu6050.__o_instance = i_instance
    
    #---------------------------------------------------------
    @classmethod        
    def get_instance(self):
        if cl_fact_mpu6050.__o_instance is not None:
            return(cl_fact_mpu6050.__o_instance)
        cl_fact_mpu6050.__o_instance = cl_mpu6050()
        return(cl_fact_mpu6050.__o_instance)
    
    #---------------------------------------------------------
    def __init__(self):
        pass