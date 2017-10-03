__author__ = 'Rohin Kumar Y'
from scipy import integrate
import numpy as np
import math as m
#from . import *
from param import *
#from correlcalc import *

#Om = param.Om
#Ol = param.Ol

def Ezs(zv):
    """Hubble papameter in H0 units"""
    return 1.0/m.sqrt(Om*(1.0+zv)**3+(1.0-Om-Ol)*(1.0+zv)**2+Ol)

Ez=np.vectorize(Ezs)

def DC_LCDMs(z):
    """Method to calculate comoving distance for LCDM model"""
    return integrate.quad(Ez, 0, z)[0]

DC_LCDM=np.vectorize(DC_LCDMs)

def DC_LC(z):
    """Method for comoving distance in Linear Coasting model"""
    return np.log(1.0+z)

def comov(z,model):
    """Method to calculate comoving distance of given redshifts for input model. Units in c/H0"""
    #More models such as wcdm to be added
    if model=='lcdm':
        return DC_LCDM(z)
    elif model=='lc':
        return DC_LC(z)
    else:
        print("Only 'lcdm' and 'lc' models supported for now")
        return None
