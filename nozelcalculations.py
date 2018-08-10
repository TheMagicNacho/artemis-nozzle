#Initial Calculations
#Based on lectures from Rick Newlands 18APR2017


import math
import cmath
import pylab
import numpy

At = 4799.46349 #Area of throat / import from previous Calculations
Ae = 13395.7121647 #Area of exit / import from previous calculations
Aco = 7.79015734942 #Area Coeficent / import from previous calculation
#ang = range(-135, -90)

Lcone = (((Aco - 1) * At) / math.tan(15)) # for an 80% bell from equ. 1
Dt= math.sqrt(4*At/ math.pi )
De= math.sqrt(4*Ae/ math.pi )

########PIRINT IT###########
#print("")
print("-------NOZEL CALCULATIONS-------")
print("USER DEFINED VARIABLES")
print "Cone Length:", Lcone
print "Area Exit:", Ae
print "Area Throat:", At
print "ae/at:", Ae/At
print "Diamiter Throat:", Dt
print "Diamiter Exit:", De
