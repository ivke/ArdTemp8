__author__ = 'ivke'
import Regresion
import serial
from time import sleep
from scipy import stats

def readTemp(DigV):
    try:
        print('Temperature sensor calibration!, when temperature is stable enter value (Hit Ctrl-C to start)')
        print("Value at: ",DigV)
        sleep(5)  # sleep for 5 seconds
          # print temperature on terminal
        return(0) # return 0 if no value was entered

    except KeyboardInterrupt: # if Ctrl-C was pressed KeyboardInterupt was triggered
        x = int(raw_input('Input Temp:'))  # insert the input
        print('Input temperature was ', x) # print temperature input
        yorno = raw_input("Insert (yes)/delete (n)")   # yes to store
        if (yorno=='y'):
            return x     # return entered temp
        else:
            return 0     # return 0 otherwise


print("Wait communication with system....")
n=0
calValx=[]
calValy=[]


while (n<5) :
    ser=serial.Serial('/dev/ttyUSB0',9600)
    sbuf=ser.readline()
    sTempBuf=sbuf[0:4]
    print(sTempBuf)
    cbuf=readTemp(sTempBuf)
    print(cbuf, " ",n)
    if cbuf!=0:
        n=n+1
        calValy.append(int(cbuf))
        calValx.append(int(sTempBuf))

kreg, kint=Regresion(calValx,calValy)
    calcTemp()
print(slope)
