# Import necessary packages
import numpy as np
import scipy as sp
import math
import cmath
from scipy import constants
from scipy import optimize

import matplotlib.pyplot as plt
from user import *

from skaero.gasdynamics import isentropic

# 0. Given conditions
# Parameters
"""
g = 1.4
R = 287.04  # J?/ (kg ? K)
p_amb = 1 * sp.constants.atm  # Pa
p_0 = 2.0 * sp.constants.atm  # Pa
T_0 = 9000 #k
"""

# Longitudinal axis of the nozzle
x = np.linspace(0, 3, 151)

# Geometry of the nozzle
def A(x):
    """Cross sectional area of the nozzle, in m^2.

    Notice that this function also contains a couple of workarounds
    to circunvent some odd behaviour of numpy.piecewise.
    """q
    def A_1(x):
        return (2.0 * x ** 3 - 3.0 * x ** 2 + 2.0) / 100

    def A_2(x):
        return (-3.0 * x ** 3 / 8.0 + 9.0 * x ** 2 / 4.0 - 27.0 * x / 8.0 + 5.0 / 2.0) / 100
    x = np.asarray(x, dtype=float)
    # For avoiding np.piecewise bug
    if not x.shape:
        x = np.asarray([x])
    result = np.piecewise(x, [(0.0 <= x) & (x < 1.0), (1.0 <= x) & (x <= 3.0)], [A_1, A_2])
    if len(result) == 1:
        result = result[0]
    return result

radius = np.sqrt(A(x) / np.pi) * 100  # cm

# Plot nozzle shape
nozzle = plt.fill_between(x, radius, -radius, facecolor="#cccccc")
plt.xlim(0, 3)
plt.title("Nozzle Profile")
plt.xlabel("x (m)")
plt.ylabel("Radius (cm)")
plt.savefig('./reports/img/con-div')



# 1. Back pressure pB is ambient pressure aka Engine Pressure
p_B = p_b2
p_amb =  1 * sp.constants.atm
# 2. Find minimum area in domain
A_e = A(x[-1])  # m^2
A_c = np.min(A(x))  # m^2
# 2.5 calulate size of nozzles components
D_e = 2 * np.sqrt(A_e / np.pi)
D_c = 2 * np.sqrt(A_c / np.pi)
# 3. Compute subsonic and supersonic Mach number at the exit
fl = isentropic.IsentropicFlow(gamma=1.4)
A_r = A_e / A_c





f = open("./reports/final.txt", 'w')
f.write('SECTION ONE:  NOZZLE THEORETICS' '\n')
f.write('FROM:  one.py' '\n')
f.write('-Defined Constant Parematers-' + '\n')
f.write ("Gamma: %s" % g + '\n')
f.write ("Energy [kg / K]: %s" % R + '\n')
f.write ("Est. Combustion Temp [K]: %s" % T_0 + '\n')
f.write ("Atmospheric Pressure [pa]: %s" % p_amb + '\n')
f.write ("chamber pressure [pa]: %s" % p_B + '\n')
f.write(''+ '\n')
f.write('-Engine Designs-' + '\n')
f.write ("Nozzle Ratio: %s" % A_r + '\n')
A_cc = A_c * 10000 #convert to cm squared
f.write ("Area Throat[cm^2]: %s" % A_cc  + '\n')
A_ec = A_e * 10000 #convert to cm squared
f.write ("Area Exit [cm^2]: %s" % A_ec + '\n')
f.write('---------' + '\n')
D_ec = D_e * 100 #convert to cm
f.write ("Diameter Exit [cm]: %s" % D_ec + '\n')
D_cc = D_c * 100 #convert to cm
f.write ("Diameter Throat [cm]: %s" % D_cc + '\n')

f.write('-BETA SECTIONS-' + '\n')
f.write ("Isontropic Flow: %s" % fl + '\n')



f.close()



exit()