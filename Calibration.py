__author__ = 'ivke'
import serial
from time import sleep
from scipy import stats
from datetime import datetime

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



def SetRegresionCoef(senzorNumber,X,Y):  # gets array of Xs and Ys and do a liear regresion. Store values in file CalibratedTemp.txt
    sslope, intercept, r_value,p_value, std_err=linregress(X,Y)
    print(slope)
    from datetime import datetime
    f=open('CalibratedTemp.txt','a+')   #open file in append read mode
    f.write("Date: %s , Senzor Number: %i;\\n", str(datetime.now()),senzorNumber)    # write date and time
    f.write("Slope:\\n")                   # write parameters form linear rgresion
    f.write(slope+"\\n")
    f.write("Intercept:\\n")
    f.write(intercept+"\\n")
    f.write("R_value:\\n")
    f.write(r_value+"\\n")
    f.write("p-value:\\n")
    f.write(p_value+"\\n")
    f.write("STd_err:\\n")
    f.write(std_err+"\\n")
    f.close()
    return sslope,intercept

def calcTemp(senzorNumber,bufval):
    return bufval*kx[senzorNumber]+kint[senzorNumber]

def ReadCalibratedSet():
    f=open('CalibratedTemp.txt','r')  # open file for regresion line parameters
    ftext=f.readlines()      # read all file into ftext
    for n in range(1,8):
        kx[n]=float(ftext[11*n-8])   # read last 12th line
        kint[n]=float(ftext[11*n-6])  # read last 10th line
    return kx, kint


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

