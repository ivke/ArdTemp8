__author__ = 'ivke'
import Regresion
import serial
import time
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


def ReadSet():
    f=open('CalibratedTemp.txt','r')  # open file for regresion line parameters
    ftext=f.readlines()      # read all file into ftext
    kx=float(ftext[len(ftext)-10])   # read last 10th line
    kint=float(ftext[len(ftext)-8])  # read last 8th line
    return kx, kint

kx,kint=1,0     #ReadSet()
ser=serial.Serial('/dev/ttyUSB0',9600)    # open serial communication with arduino
print(ser.readline())

sbuf=""

while True:
       # read buffer from arduino
    sbuf=sbuf+ser.read(ser.inWaiting()) #read character at a time if serial is stuck
    if '\n' in sbuf:  # if end of the line is reached process buffer
        print(sbuf)   # see what is in buffer
        sTempBuf=int(sbuf[len(sbuf)-5:len(sbuf)]) # fetch last 5 characters
        print(sTempBuf)    # print calculated last number
        print(Regresion.calcTemp(sTempBuf,kx=0.3,kint=0))   # calculate temperature
        StoreTemp(Regresion.calcTemp(sTempBuf,kx=0.3,kint=0))
    time.sleep(2)    # sleep for 2 seconds