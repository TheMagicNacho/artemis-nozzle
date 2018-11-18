#Initial Calculations
#Based on lectures from Rick Newlands 18APR2017

import math
import cmath
import pylab
import numpy
import matplotlib.pyplot as plt

At = 4799.46349 #Area of throat / import from previous Calculations
#Ae = 13395.7121647 #Area of exit / import from previous calculations
#Aco = 7.79015734942 #Area Coeficent / import from previous calculation
ang = range(-135, -90)

#Lcone = (((Aco - 1) * Rt) / math.tan(15))*0.8 # for an 80% bell from equ. 1

x = 0.382*At*(numpy.cos(ang)) # 100 linearly spaced numbers
y = 0.382*At* (numpy.sin(ang))+.382*At + At # computing the values of sin(x)/x
# compose plot
#pylab.plot(x,y)
#pylab.show() # show the plot
plt.plot(x, y)
plt.title("bell contour")
plt.axis('equal')
plt.show()
