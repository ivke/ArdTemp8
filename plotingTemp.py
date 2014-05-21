__author__ = 'ivke'

from matplotlib.pylab import *
import time

class DrawTemp:
    "draw temperature profile on to graph using matplotlib"
    LineNumb=0
    ion()
    def __init__(self,y,x=None):
        "init of draw temp it draws a line"
        if x:
            print(x)
            self.line, =plot(x,y)
        else:
            self.line, =plot(y)
        self.LineNumb+=1
        draw()

    def Update(self,y,x=None):
        "Updating line with new values"
        self.line.set_ydata(y)
        if x:
            self.line.set_xdata(x)

y=[1,2,3,4,5,6,7,8,9,10]
x=[1,2,3,4,5,6,7,8,9,10]
temp1=DrawTemp(y,x)
temp2=DrawTemp([1,2,3,10,12,13,14,15])
draw()
time.sleep(2)
temp2.Update([10,2,30,10,12,13,14,15])
draw()
time.sleep(2)
