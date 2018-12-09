#import important items
import numpy as np
import scipy as sp
import math
import cmath
from scipy import constants
from scipy import optimize
import matplotlib.pyplot as plt
#from bin.user import *
from user import *
from skaero.gasdynamics import nozzles

#Initial Calculations
cstar = 903.5 #constant of compressability
Pe = (n * 0.08205 / vcc) * Tc  #exhaust presure - assumes ideal gas constant
r = H / (Tc+258) #specific heat ratio
Fr = (payload * 20) * ( 76000.00 + 9.80665) # force required in Newtons

#Throat
Tt = Tc * (2/H+1) #throat temp (K)
Pt = Pc * (2/H+1) ** (H/(H-1)) #presure (bar)
Dt = Pt / (r*Tt)  #density
Vt = math.sqrt(r*0.08205*Tt) #Velocity at throat - assumes ideal gas constant
mt = Vt / 295.26992  # throat mach number - assumes speed of sound is 295.26992 at stratosphere
At = payload / (mt * Dt)

#coefficents
Aco = (math.pow (1 + mt**2 * (r-1)/2,((r+1)/(r-1)/2)) * math.pow ((r+1)/2, -((r+1)/(r-1)/2))) / mt

#exhaust
Ae = At * math.sqrt(Aco) # area of exhaust diameter (MM)
Te = Tc / (1+((H-1)/2)*Vt**2)  #exhaust Temp in k
De = Pe / (r*Te)  #desnsity
cf = Fr / At * Pc # thrust coefficient, simplified

#final
Ve = math.sqrt(cf * cstar) #velocity at exit
mdot = (Pc * At) / cstar #mass flow rate
Ve = math.sqrt(cf * cstar) #velocity at exit
Me = Ve / 295.26992 # exhaust mach number - assumes speed of sound is 295.26992 at stratosphere
isp = Ve / 9.80665 #specific impulse - assume gravity 9.8 m/s
Tsum = Tt + Tc #sum of temp to find average
Tavg = Tsum / 2 # avg temp
mu = np.arcsin(1 / Me) #mach angle
Lcone = (Dt / 2) * ( math.sqrt(Ae / At) - 1 ) * (np.arctan(mu))

#write it out
f = open("./reports/report.html", 'w')
f.write('SECTION ONE:  NOZZLE THEORETICS' '<br>')
f.write('FROM:  V1.3' '<br>')
f.write('----------' + '<br>')
f.write('-USER DEFINED CONSTANTS-' + '<br>')
f.write ("Specific Heat: %s" % H + '<br>')
f.write ("Combustion Chamber Tem (k): %s" % Tc + '<br>')
f.write ("Combustion Chamber Pressure (bar) %s" % Pc + '<br>')
f.write ("Combustion Chamber Volume (l): %s" % vcc + '<br>')
f.write ("Ambiant Pressure (bar): %s" % Pa + '<br>')
f.write('----------' + '<br>')
f.write('ENGINE THEORETICS' + '<br>')
f.write ("Average Operating Temps (k): %s" % Tavg + '<br>')
f.write ("Exit Mach: %s" % Me + '<br>')
f.write ("Specific Impulse (sec): %s" % isp + '<br>')
f.write ("Mass Flow Rate (kg/s): %s" % mdot + '<br>')
f.write('----------' + '<br>')
f.write('ENGINE DESIGNS' + '<br>')
At_c = At / 10
f.write ("Area Throat (cm^2): %s" % f'{At_c:.6f}' + '<br>')
Ae_c = Ae / 10
f.write ("Area Exit (cm^2): %s" % f'{Ae_c:.6f}' + '<br>')
Dt = 2 * np.sqrt(At_c / 3.14159265359)
f.write ("Diameter Throat (cm): %s" % f'{Dt:.6f}' + '<br>')
De = 2 * np.sqrt(Ae_c / 3.14159265359)
f.write ("Diameter Exit (cm): %s" % f'{De:.6f}' + '<br>')
Lcone_c = Lcone / 10
f.write ("Cone Length (cm): %s" % f'{Lcone:.6f}' + '<br>')
f.write ("Mach Angle: %s" % mu + '<br>')
f.close()

"""


"""
exit()