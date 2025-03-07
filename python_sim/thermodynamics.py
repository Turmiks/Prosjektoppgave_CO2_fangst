#=========================================================================
#   IMPORTS
#=========================================================================

import numpy as np
import scipy
import constants3
#=========================================================================
#   Constants
#=========================================================================
Hc: list = constants3.Hc

#=========================================================================
#   Functions for numerically solving thermodynamic equations
#=========================================================================

def heat_capacity() -> float:

    pass

def mean_heat_capacity() -> float:

    pass

def henrys_constant(temperature: float, loading: float, constants: list = Hc) -> float:
    
    exponent: float = Hc[4]*loading**2 + Hc[5]/temperature + (Hc[6]*loading)/(temperature**2)
    k_H: float = (Hc[0] + (Hc[1]*loading)/temperature) * np.e**(exponent)


    return k_H

