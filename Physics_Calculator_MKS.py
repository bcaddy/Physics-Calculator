#!/usr/bin/env python3
"""
    Author: Robert Caddy <r.caddy@pitt.edu>
    Created: 4/16/2019
    Modified: 4/16/2019
    Short Description: Simple calculator for physics and astronomy problems
    Long Description:8
        This utility is used to calculate simple physics problems.  It contains
        many common physical constants and functions for performing common
        operations such as unit conversion.
        
    Dependencies:
        - numpy
"""


import numpy as np


# General Constants
G       = 6.67408E-11       #Gravitational Constant. N m^2 /kg^2
c       = 2.99792458E8      #Speed of light. m/s

# Electrodynamics
e       = 1.60217662E-19    #Elementary Charge. Coulombs
mu_0    = (4*np.pi)*(10**-7)#Permeability of free space. N A^-2
ep_0    = 1/(mu_0*(c**2))   #Permittivity of free space. m^-3 kg^-1 s^4 A^2

# Quantum
h       = 6.62607004E-34    #Plank's constant. J*s
hbar    = h/(2*np.pi)       #Reduceed Plank's constant. J*s
mp      = 1.6726219E-27     #Mass of a proton. kg
me      = 9.10938356E-31    #Mass of an election. kg
mn      = 1.67492716E-27    #Mass of a neutron. kg
mHe     = 6.646476406E-27   #Mass of helium. kg
amu     = 1.66053873E-27    #Atomic Mass Unit. Kg
amu_ev  = 931.4940123       #Atomic Mass Unit. MeV/c^2
NA      = 6.02214199E23     #Avogadro's Number. mol^-1
a0      = 5.294654075E-11   #Bohr Radius. m

# Statistical Mechanics and Thermodynamics
Kb      = 1.38064852E-23    #Boltzmann constant. J/K
Kbev    = 8.6173324E-5      #Boltzmann constant in eV. ev/K
sigmaSB = 2*(np.pi**5)*(Kb**4)/(15*(c**2)*(h**3)) #Stefan-Boltzman constant. W/(m^2*K^4)
a_rad   = 4*sigmaSB/c       #Radiation constant J(m^-3)(K^-4)

##### Astronomical Constants #####

# Solar Constnats
Msun    = 1.9891E30         #Mass of the sun. kg
Rsun    = 6.955E8           #Radius of the sun. m
rhocore = 1.4E5             #Density of the core of the sun. kg/m^3
Lsun    = 3.839E26          #Luminosity of the sun. Watts
Tsun    = 5777              #Effective temperature of the sun. Kelvin

# Earth/Moon Constants
Mearth  = 5.9736E24         #Mass of the Earth. Kg
Rearth  = 6.378136E6        #Radius of the Earth. m
Mmoon   = 7.34767309E22     #Mass of the Earth. Kg
Rmoon   = 1.7371E6          #Radius of the Earth. m

# Misc. Astronomical Constants
AU      = 1.4959787066E11   #Astronomical Unit. m
ly      = 9.460730472E15    #Light Year. m
pc_m    = 3.0856776E16      #Parsec. m
pc_au   = 2.06264806E5      #Parsec. AU
pc_ly   = 3.2615638         #Parsec. ly


#--------------------------------------------------------------------------
# Functions
#--------------------------------------------------------------------------

def J2eV(J):
    '''Convert the argument value in Joules to Electron Volts (eV)'''
    return J*6.242e+18


#--------------------------------------------------------------------------
# Calculations
#--------------------------------------------------------------------------













