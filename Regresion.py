__author__ = 'ivke'

import scipy.stats as stats
from datetime import datetime

def Regresion(X,Y):  # gets array of Xs and Ys and do a liear regresion. Store values in file CalibratedTemp.txt
    sslope, intercept, r_value,p_value, std_err=stats.linregress(X,Y)
    print(slope)
    from datetime import datetime

    f=open('CalibratedTemp.txt','a+')   #open file in append read mode
    f.write(str(datetime.now())+"\n" )    # write date and time
    f.write("Slope:\n")                   # write parameters form linear rgresion
    f.write(slope)
    f.write("\n")
    f.write("Intercept:\n")
    f.write(intercept)
    f.write("\n")
    f.write("R_value:\n")
    f.write(r_value)
    f.write("\n")
    f.write("p-value:\n")
    f.write(p_value)
    f.write("\n")
    f.write("STd_err:\n")
    f.write(std_err)
    f.write("\n")
    f.close()
    return sslope,intercept

def calcTemp(bufval,kx,kint):
    return bufval*kx+kint