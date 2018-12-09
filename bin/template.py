import numpy as np
import scipy as sp

from scipy import constants
from scipy import optimize

import matplotlib.pyplot as plt
from user import *

from skaero.gasdynamics import isentropic

A_r = 2.5

fl = isentropic.IsentropicFlow(gamma=g)
M_e_sub, M_e_sup = isentropic.mach_from_area_ratio(fl, A_r)


f = open("./reports/final.txt", 'w')
f.write('SECTION ONE:  NOZZLE THEORETICS' '\n')
f.write('FROM:  one.py' '\n')
f.write('-Defined Constant Parematers-' + '\n')
f.write ("Gamma: %s" % g + '\n')
f.write('-BETA SECTIONS-' + '\n')
f.write ("Isontropic Flow: %s" % fl + '\n')
f.close()

exit()