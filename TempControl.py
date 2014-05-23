
from Calibration import calcTemp
import serial
import time
import string
from datetime import datetime

sbuf=""


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
    ser=serial.Serial(port = '/dev/ttyUSB0',baudrate = 9600,parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE,bytesize = serial.EIGHTBITS, timeout=10)    # open serial communication with arduino
    global sbuf        
    sbuf+=ser.read(ser.inWaiting())  # reads from serial buffer
    print sbuf
    ADCList=sbuf.split()  # divide data into different measurements
    if ADCList[-1] is not "":      # if last item is None than whole temperature data was transfered
        sbuf=ADCList[-1]
    else: sbuf= ""              # if not set sbuf to incomplete temperature data transfered
    print ADCList
    del ADCList[-1]      # delete last item in list
    
    # make dict senzor number: ADC value
    TempDict={int(x[0]):calcTemp(int(x[0])-1,int(x[1:])) for x in ADCList}
    return TempDict,ACDList
       # calculate temperature

def SetTempForArduino(sensorNumber,Temp):
    """ Seting ADC value for Arduino controll""" 

def main():
    while True:
        print "start"
        t=GetTempFromArduino()
        print t
        time.sleep(10)
    # sleep for 2 seconds

if __name__ == "__main__":
   main()
   