
import numpy as np
import scipy as sp

from scipy import constants, optimize

import matplotlib.pyplot as plt
from skaero.gasdynamics import isentropic, shocks


# 0. Given conditions
# Taken from exercises 2 and 18

# Parameters
gamma = g = 1.4
R = 287.04  # J / (kg · K)
p_amb = 1 * sp.constants.atm  # Pa

# Inlet conditions
p_0 = 2.0 * sp.constants.atm  # Pa
T_0 = 300  # K

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

radius = np.sqrt(A(x) / np.pi) * 10  # dm

# Plot nozzle shape
nozzle = plt.fill_between(x, radius, -radius, facecolor="#cccccc")
plt.xlim(0, 3)
plt.title("Nozzle")
plt.xlabel("x (m)")
plt.ylabel("Radius (dm)")
plt.plot()


# 1. Back pressure pB is ambient pressure
p_B = p_amb
# 2. Find minimum area in domain
A_e = A(x[-1])  # m^2
A_c = np.min(A(x))  # m^2
# 3. Compute subsonic and supersonic Mach number at the exit
fl = isentropic.IsentropicFlow(gamma=g)
# M_e_sub, M_e_sup = isentropic.mach_from_area_ratio(fl, A_e / A_c)

# print(M_e_sub, M_e_sup)

