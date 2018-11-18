import scipy as sp
import configparser
config = configparser.ConfigParser()
config['USER'] = {
    'g': '1.4',     #gamma
    'R': '287.04',  # J?/ (kg ? K)
    'p_amb': 1 * sp.constants.atm # DO NOT CHANGE
    'p_0' : 2.0 * sp.constants.atm # DO N   OT CHANGE
    'T_0': '9000' #tempature of gumbustion k
    'p_B':  '32' #pressure engine (back) in bar
}



