
from Calibration import *
import serial
import time
import string
from datetime import datetime


def StoreTemp(temp1):  # store temperature in file for latter viewing
    No=datetime.now().strftime("%Y-%m-%d")
    filename="Temp"+No
    templog=open(filename,"a+")
    templog.write(datetime.now().isoformat()+";")
    if type(temp1=="float"):
        templog.write(str(temp1)+";")
    else:
        for n in temp1:
            templog.write(str(n)+";")
    templog.write('\n')
    templog.close()


def GetTempFromArduino():
    """ Reads value from ADC from arduino and returns calculated temperature 
        as dictionary """
    try:
        ser=serial.Serial(port = '/dev/ttyUSB0',baudrate = 9600,parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE,bytesize = serial.EIGHTBITS, timeout=10)    # open serial communication with arduino
    except serial.SerialException:
        print "Arduino is not responding!!!"
        return None
    sbuf=""
    while ser.inWaiting():
        buf=ser.read(1)
        if buf is "\n" and ser.inWaiting()<7:
            sbuf+=buf  # adds to sum buffer
            break      # goes out of the loop remaining is left for next round
        sbuf+=buf
    import re
    patern="(?=\d{5}\r\n)\d{5}"   # patern for regexpr matching it finds XXXXX\r\n and removes newline characters 
    ADCList=re.findall(patern,sbuf)  # lists all numbers that matches wanted format
    
    if ADCList is None:      # if nothing was recived send None as output 
        print "No DATA avaliable on Serial buffer!!!"
        return None
    print ADCList
        
    # make dict senzor number: ADC value
    TempDict={int(x[0]):calcTemp(int(x[0]),int(x[1:])) for x in ADCList}
    return TempDict,ADCList
       # calculate temperature

def SetTempForArduino(sensorNumber,Temp):
    """ Seting ADC value for Arduino controll"""
    try:
        ser=serial.Serial(port = '/dev/ttyUSB0',baudrate = 9600,parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE,bytesize = serial.EIGHTBITS, timeout=10)    # open serial communication with arduino
    except serial.SerialException:
        print "Arduino is not responding!!!"
        return None
    data="10%04i\n"%calcADC(sensorNumber,Temp) # formats the string output 10 command XXXX ADC value and \n
    print data
    try:
        ser.write(data)
    except serial.SerialException:
        print "Serial write Error!!!"
        return None
    return data

def main():
    ReadCalibratedSet()
    
    while True:
        print "start"
        t=GetTempFromArduino()
        print t
        time.sleep(10)
    # sleep for 2 seconds

if __name__ == "__main__":
   main()
   