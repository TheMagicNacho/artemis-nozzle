# Import necessary packages
import numpy as np
import scipy as sp

from scipy import constants, optimize

import matplotlib.pyplot as plt

from skaero.gasdynamics import isentropic, shocks

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
    """
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

exit()