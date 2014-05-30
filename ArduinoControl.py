import serial
from Calibration import *


class ArduinoControler(object):
    "Class interacting with arduino, sending, getting data throu serial port."
    def __init__(self,NSensor,DataLength):
        " Initalize Arduino relevant data, number of sensors, data Length that is send via USB. Actual is dataLength +2 bytes for \r and \n"
        self.NumberSensors=NSensor
        self.DataLength=DataLength
        # initalize serial port
        try:
            self.ser=serial.Serial(port = '/dev/ttyUSB0',baudrate = 9600)    # open serial communication with arduino
            self.ser.flushInput()
            print self.ser.inWaiting()
            sleep(10)
            print self.ser.inWaiting()
            self.ser.read(self.ser.inWaiting())
            
        except self.ser.SerialException:
                print "Arduino is not responding!!!"
        # initalize 
    def SetSensorNumber(self,NSensor):
        self.NumberSensors=NSensor
    
    def GetSensorNumber(self):
        self.ser.read()
    
    def GetADCData(self):
        " Reads value from ADC from arduino and returns calculated temperature as dictionary "
        try:
            self.ser.inWaiting()
                    
        except self.ser.SerialException:
            print "Arduino is not responding!!!"
            return None
        
        sbuf=""
    
        while self.ser.inWaiting():
            buf=self.ser.read(1)
            if buf is "\n" and self.ser.inWaiting()<(self.DataLength+2):
                sbuf+=buf  # adds to sum buffer
                break      # goes out of the loop remaining is left for next round
            sbuf+=buf
        # code for extractin valid entries, all other are discharged
        import re
        patern="(?=\d{%i}\r\n)\d{%i}" % (self.DataLength,self.DataLength) # patern for regexpr matching it finds XXXXX\r\n and removes newline characters 
        
        self.ADCList=re.findall(patern,sbuf)  # lists all numbers that matches wanted format
        
        if self.ADCList is None:      # if nothing was recived send None as output 
            print "No DATA avaliable on Serial buffer!!!"
            # should triger exception
        
        print self.ADCList
            
        # make dict sensor number: ADC value to get latest readings and to organize it
        self.ADCDict={int(x[0]):int(x[1:]) for x in self.ADCList}
    
    def SetCmDArduino(self,cmd,Data):
        """ Sending command and data to Arduino via Serial"""
        try:
            self.ser.flushOutput( ) #flush output of the serial 
        except serial.SerialException:
            print "Arduino is not responding!!!"
            return False
        
        if not isinstance(Data,basestring): # check if Data is string
            data=str(Data)     #if not convert to string
        else: data=Data
        
        data="%02i%s\n"% (cmd,data) # formats the string output XX command rest is data and \n
        
        print data
        try:
            self.ser.write(data)
        except serial.SerialException:
            print "Serial write Error!!!"
            return False
        return True      


class TempControler(ArduinoControler):
    """ """ 
    def __init__(self,NSensor=8,DataLength=5):
        super(TempControler,self).__init__(NSensor,DataLength) # inherits initfunction from parent - sets for 8 sensors with 10 bit ADC - 1 ditit for senzor number and 4 ditigs for value 
        self.kx,self.kint=ReadCalibratedSet()  # read Data for temperature calculation (derived from calibration)
        self.TempDict={}
    
    def GetTemp(self,sensor):
        """ To be implemented  """
        pass
    
    def GetTempDict(self): 
        """ Gets data from Arduino ADC and transforms it to Temperature"""
        
        self.GetADCData()
        
        for k,n in self.ADCDict.items():   # loops over ADCDict and sets temperature using calcTemp function
            self.TempDict[k]=self.calcTemp(k,n)
        return self.TempDict
    
    def SetTemp(self,sensor,temp):  # sets target ADC value for wanted temperature on Sensor....
        """ """
        ADCV=self.calcADC(sensor,temp)
        if ADCV>1023:  # maximum value for 10 bit ADC
            print "Temperature is set to hight!"
            ADCV=1023
        
        data="%i%04i" % (sensor,ADCV) # output for arduino 
        self.SetCmDArduino(10,data)  # 10 is command for set temperature
    
    def calcTemp(self,senzorNumber,bufval):   # calculate temperature from ADC from calibration data
        return round(bufval*self.kx[int(senzorNumber)]+self.kint[int(senzorNumber)])
    
    def calcADC(self,senzorNumber,temp):  # calculate set ADC from calibration data
        return int(round((temp-self.kint[int(senzorNumber)])/self.kx[int(senzorNumber)],0))

def main():
    tm=TempControler()
    while True:
        tm.GetTempDict()
        print tm.TempDict
        sleep(5)


if __name__ == "__main__":
    main()
        