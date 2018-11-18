#Initial Calculations
#Based on lectures from Rick Newlands 18APR2017


import math
import cmath
import pylab
import numpy

At = 4799.46349 #Area of throat / import from previous calculations in mm square
Ae = 13395.7121647 #Area of exit / import from previous calculations in mm square
Aco = 7.79015734942 #Area Coeficent / import from previous calculation
Me = 12.8110091038 # exhaust mach number - assumes speed of sound is 295.26992 at stratosphere / import from previous calculations
#ang = range(-135, -90)
Aratio = Ae / At

#Lcone = (((Aco - 1) * At) / math.tan(15)) # for an 80% bell from equ. 1 OLD
Mang =  (numpy.arcsin(1 / Me)) * (180 / math.pi)   # calculate mach angle then convert from radian to degrees (for python's sake- dont' judge me)


Dt = 2 * math.sqrt((At / math.pi))
De = 2 * math.sqrt((Ae / math.pi))
Lcone = (Dt / 2) * ( math.sqrt(Ae / At) - 1 ) * (numpy.arctan(Mang))

########PIRINT IT###########
print("-------NOZEL CALCULATIONS-------")
print("USER DEFINED VARIABLES")
print "Area Exit:", Ae
print "Area Throat:", At
print("--------------")
print("CALCULATED OUT")
print "Mach Angle (deg):", Mang
print "Expansion Ratio:", Aratio
print "Diamiter Throat (mm):", Dt
print "Diamiter Exit (mm):", De
print "Cone Length (mm):", Lcone
