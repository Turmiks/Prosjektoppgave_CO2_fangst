#=========================================================================
#   Imports
#=========================================================================
import numpy as np
import scipy 

#   local
from .constants3 import *

#=========================================================================
#   module containing classes for simulating unit operations in 
#   chemical processing plants
#
#   Created: 06/03/2025
#   Author(s): Iver Mihle Asklund
#   
#=========================================================================

class Absorber():

    def __init__(self, feed_stream_1: object, feed_stream_2: object, capture_rate: float):

        self.feed_stream_1 = feed_stream_1
        self.feed_stream_2 = feed_stream_2
        self.capture_rate = capture_rate
        self.output_stream_1 = None
        self.input_stream_2 = None
        pass

    def operate(self) -> None:


        return None


class Stripper():

    def __init__(self):
        
        pass


class Pump():

    def __init__(self, inlet: object):
        
        pass


class HeatExchanger():

    def __init__(self, exch_coeff: float, exch_area: float, xflow=True):

        self.exch_coeff = exch_coeff    # U
        self.exch_area = exch_area      # A
        self.xflow = xflow              # crossflow > Motstrøms

        
        pass
    
    def operate(self, inlet_hot: object, inlet_cold: object):
        outlet_hot: object = []
        outlet_cold:object = []
        data: list = []

        return outlet_hot, outlet_cold, data
    

class Cooler():

    def __init__(self,):
        pass