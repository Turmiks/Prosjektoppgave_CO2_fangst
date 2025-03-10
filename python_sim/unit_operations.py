#=========================================================================
#   Imports
#=========================================================================
import numpy as np
import scipy 

#   local
import python_sim.constants3
import python_sim.helpers
import python_sim.thermodynamics
#=========================================================================
#   module containing classes for simulating unit operations in 
#   chemical processing plants
#
#   Created: 06/03/2025
#   Author(s): Iver Mihle Asklund
#   
#=========================================================================

class Absorber():

    def __init__(self, input_stream_1: object, input_stream_2: object,
                 output_stream_1: object, Output_stream_2: object,
                 capture_rate: float):

        self.input_stream_1 = input_stream_1
        self.input_stream_2 = input_stream_2
        self.output_stream_1 = output_stream_1
        self.input_stream_2 = Output_stream_2
        self.capture_rate = capture_rate
        pass


class Stripper():

    def __init__(self):
        
        pass


class Pump():

    def __init__(self):
        
        pass


class HeatExcanger():

    def __init__(self):
        
        pass
    