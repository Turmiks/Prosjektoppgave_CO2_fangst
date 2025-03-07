#=========================================================================
#   Imports
#=========================================================================
import numpy as np
import scipy 

#=========================================================================
#   module containing classes for simulating unit operations in 
#   chemical processing plants
#
#   Created: 06/03/2025
#   Author(s): Iver Mihle Asklund
#   
#=========================================================================

class Absorber():

    def __init__(self, input_stream_1: list, input_stream_2: list, output_stream_1: list, Output_stream_2: list):

        self.input_stream_1 = input_stream_1
        self.input_stream_2 = input_stream_2
        self.output_stream_1 = output_stream_1
        self.input_stream_2 = Output_stream_2

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
    