import scipy as sp
from scipy import constants
"""
# V 1.1
g = 1.4
R = 287.04  # J?/ (kg ? K)
T_0 = 673.504 #k
p_b2 = 10  #] pressure in chamber


# V 1.2
H = 4686.79  #Specific Heat (Kj/Mol) AKA Enthalpy
T_0 = 673.504 #Combustion Chamber Temp (K) - derived from abdatic
Pc = 25 #Combustion Chamber Presure (bar) - based on research from S. Krishnan1*, Ahn Sang-Hee2, Lee Choong-Won2
vcc = 2 #Combustion Chamber Volume  (L) - guessed size of rocket
payload = 2 # in kg
P_B = 10 #ambiant presure - estimated combustion of
n = 230 #Number of moles from combustion product
"""


# v 1.3
#User Defined Variables
H = 4686.79  #Specific Heat (Kj/Mol) AKA Enthalpy
Tc = 673.504 #Combustion Chamber Temp (K) - derived from abdatic
Pc = 25 #Combustion Chamber Presure (bar) - based on research from S. Krishnan1*, Ahn Sang-Hee2, Lee Choong-Won2
vcc = 2 #Combustion Chamber Volume  (L) - guessed size of rocket
payload = 2 # in kg
Pa = 10 #ambiant presure - estimated combustion of
n = 230 #Number of moles from combustion product