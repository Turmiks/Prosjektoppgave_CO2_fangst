#=========================================================================
#   IMPORTS
#=========================================================================

import numpy as np
import scipy

#   local
from .constants3 import *


#=========================================================================
#   Constants
#=========================================================================
Hc: list =  0 #python_sim.constants3.Hc

#=========================================================================
#   Functions for numerically solving thermodynamic equations
#=========================================================================

def heat_capacity(T: float, coeff:list[str|float]) -> float:
    # Function for calculating heat capacity at constant pressure from a list of experimentally determined coefficients
    heat_capacity: float = 0

    for i in enumerate(coeff):
        heat_capacity += float(i[1]) * T**(i[0])
        
    # returns a value rounded to 3 decimal places, rounding should be omitted when used in calculations
    return round(heat_capacity, 3)


def mean_heat_capacity(T0: float, T1: float, coeff: list[str|float]) -> float:
    # Function for calculating mean heat capacity
    upper: float = 0
    lower: float = 0

    # the sum of aT + 1/2 * bT^2 + 1/3 * cT^3 + 1/4 * dT^4
    for value in enumerate(coeff):
        
        upper += (1/float(value[0]+1)) * float(value[1]) * T1**(value[0]+1)
        lower += (1/float(value[0]+1)) * float(value[1]) * T0**(value[0]+1)

        
    mean_heat_capacity: float = (upper - lower) / (T1 - T0)
    
    # Returning a value for mean heat capacity rounded to 3 decimal places
    return round(mean_heat_capacity, 3)


def henrys_constant(temperature: float, loading: float, constants: list = Hc) -> float:
    
    exponent: float = Hc[4]*loading**2 + Hc[5]/temperature + (Hc[6]*loading)/(temperature**2)
    k_H: float = (Hc[0] + (Hc[1]*loading)/temperature) * np.e**(exponent)


    return k_H


def enthalpy(heat: float, pressure: float, volume: float, phase: str='liquid') -> float:

    calculated_enthalpy: float = 0
    if phase == 'liquid':
        calculated_enthalpy = heat + pressure*volume

    return calculated_enthalpy


def loading(CO2_absorbed: float, init_MEA_concentration: float) -> float:
    # calculates loading of MEA solution
    return CO2_absorbed/init_MEA_concentration


def p_co2(K_h: float, alpha: float, K_2: float) -> float:

    numerator: float = K_h*alpha**2
    denominator: float = K_2*(1 - 2*alpha)**2

    return numerator/denominator


def wth_frac_co2(mol_mass_co2: float, alpha: float, mol_mass_MEA: float) -> float:

    numerator: float = mol_mass_co2*alpha
    denominator: float = (1 + (0.7/0.3))*mol_mass_MEA

    return numerator/denominator


def molar_mass(substance: str) -> float:

    mol_mass: dict = {
    'CO2': Mw[0],
    'H2O' : Mw[1],
    'N2' : Mw[2],
    'O2' : Mw[3],
    'MEA' : MwMEA,
    }
    if substance in mol_mass:
        return mol_mass[substance]
    else:
        print(f'molar mass for {substance} is not available')
        return None