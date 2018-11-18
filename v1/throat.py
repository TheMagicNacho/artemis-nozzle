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

x = 1.5*At*(numpy.cos(ang)) # 100 linearly spaced numbers
y = 1.5*At* (numpy.sin(ang))+1.5*At + At # computing the values of sin(x)/x
# compose plot
plt.plot(x,y)
plt.axis('equal')

plt.axis('equal')
plt.axis([-6000, 6000, -6000, 6000])
plt.yscale('linear')
plt.xscale('linear')
plt.grid(color='grey', linestyle='--', linewidth=.9)

plt.title('throat')
plt.show() # show the plot
