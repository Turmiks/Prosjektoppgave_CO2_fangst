#=========================================================================
#   IMPORTS
#=========================================================================

import numpy as np
import scipy
import constants3
#=========================================================================
#   Constants
#=========================================================================



#=========================================================================
#   Helper functions
#=========================================================================


#=========================================================================
#   Classes
#=========================================================================

class stream():
    
    def __init__(self, components: list, flow_rate: float, temperature: float, pressure: float, phase: str):
        self.flow_rate = flow_rate
        self.components = components
        self.temperature = temperature
        self.pressure = pressure
        self.phase = phase

        pass
    