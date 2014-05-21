__author__ = 'ivke'
import Regresion
import serial
import time
import string
from datetime import datetime

sTempBuf=0


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
    """ Reads value from ADC from arduino and returns calculated temepratures 
        as dictionary """
    ser=serial.Serial('/dev/ttyUSB0',9600)    # open serial communication with arduino
    print(ser.readline())   # test
        
    while ser.inWaiting():     # read from serial buffer
        sbuf+=ser.read()
    
    ADCList=string.split(sbuf,"\\n")  # divide data into different measurements
    if ADCList[-1] is not None:      # if last item is None than whole temperature data was transfered
        sbuf=ADCList[-1]              # if not set sbuf to incomplete temperature data transfered
    
    del ADCList[-1]      # delite last item in list
    TempDict={int(x[0]):Regresion.calcTemp(int(x[0]),int(x[1:])) for x in ADCList}  # make dict senzor number: ADC value
       # calculate temperature
def SetTempForArduino(sensorNumber,Temp):
    """ Seting ADC value for Arduino controll""" 

# sleep for 2 seconds