import serial
from time import sleep
from scipy import stats

kx={}
kint={}

def readTemp(DigV):
    try:
        print('Temperature sensor calibration!, when temperature is stable enter value (Hit Ctrl-C to start)')
        print("Value at: ",DigV)
        sleep(5)  # sleep for 5 seconds
          # print temperature on terminal
        return(0) # return 0 if no value was entered

    except KeyboardInterrupt: # if Ctrl-C was pressed KeyboardInterupt was triggered
        x = raw_input('Input Temp:')  # insert the input
        print('Input temperature was ', x) # print temperature input
        yorno = raw_input("Insert (yes)/delete (n)")   # yes to store
        if (yorno=='y'):
            return int(x)     # return entered temp
        elif (yorno=='e'):
            return 'e'     # return 0 otherwise
        else:
            return 0


def SetRegresionCoef(senzorNumber,X,Y):  
    """ gets array of Xs and Ys and do a linear regression. Store values in file CalibratedTemp.txt"""
    
    sslope, intercept, r_value,p_value, std_err=stats.linregress(X,Y)  # calculate linear regresion on values
    print(sslope)
    from datetime import datetime
    f=open('CalibratedTemp.txt','r')   #open file in append read mode
    tekst=f.readlines() #read all the file
    f.close()
    f=open('CalibratedTemp.txt','w')   #erase file and open file for input
    print tekst
    if not tekst:
        print "pisem v fajl2!"
        f.write("jebiga\n")
        f.write("%i; Date: %s; Slope: %1.5f; Intercept: %1.5f; R_value: %1.5f; p-value: %1.5f; STD_error:%1.5f;\n" % (senzorNumber, str(datetime.now()),sslope,intercept,r_value,p_value,std_err))    # write date and time
        return sslope,intercept
    for i in tekst:
        if int(i[0])== senzorNumber:
            f.write("%i; Date: %s; Slope: %1.5f; Intercept: %1.5f; R_value: %1.5f; p-value: %1.5f; STD_error:%1.5f;\n" % (senzorNumber, str(datetime.now()),sslope,intercept,r_value,p_value,std_err))    # write date and time
            
        else:
            f.write(tekst)
    return sslope,intercept

def calcTemp(senzorNumber,bufval):   # calculate temperature from ADC from calibration data
    return round(bufval*kx[int(senzorNumber)]+kint[int(senzorNumber)])

def calcADC(senzorNumber,temp):  # calculate set ADC from calibration data
    return int(round((temp-kint[int(senzorNumber)])/kx[int(senzorNumber)],0))

def ReadCalibratedSet():
    """  """
    import os
    os.chdir("/home/ivke/workspace/TempControl/")
    f=open('CalibratedTemp.txt','r')  # open file for regression line parameters
    ftext=f.readlines()      # read all file into ftext
    for n in ftext:
        sID=int(n[0]) # senzor index
        import re
        m1=re.search("(?<=\Slope: )[0-9\.]*",n)
        m2=re.search("(?<=\Intercept: )[0-9\.]*",n)
        global kx, kint
        kx[sID]=float(m1.group(0))   # 
        kint[sID]=float(m2.group(0))  # read last 10th line
    
   

def main():
    n=0
    print("Wait communication with system....")
    calValx=[]
    calValy=[]
    sID=raw_input("Type sensor number: ")
    sID=int(sID)
    from TempControl import GetTempFromArduino
    while True :
        temp,ADCV=GetTempFromArduino()
        print temp
        ADCDict={int(x[0]):int(x[1:]) for x in ADCV}
        print ADCDict
        itemp=readTemp(ADCDict[sID])
        if itemp=='e':
            break
        elif itemp==0: 
            pass
        else:
            print "pisem ..." + str(n)
            print str(itemp) + " " + str(ADCDict[sID])
            n+=1
            calValy.append(itemp)
            calValx.append(ADCDict[sID])
    
    if n<3:
        pass
    else:
        print "pisem v fajl"
        SetRegresionCoef(sID,calValx,calValy)
    
    return calValx, calValy

if __name__ == "__main__":
    main()
