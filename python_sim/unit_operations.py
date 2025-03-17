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
        self.output_stream_1 = feed_stream_1    # PLACEHOLDER
        self.output_stream_2 = feed_stream_2    # PLACEHOLDER
        pass

    def operate(self) -> None:
        #co2 dissolves
        #co2 is absorbed


        return None


class Stripper():

    def __init__(self, feed_stream_top: object, feed_stream_bottom: object, output_stream_top: object,
                 output_stream_bottom: object):
        
        pass


class Pump():

    def __init__(self, inlet: object):
        
        self.inlet = inlet
        self.heat = None
        self.work_rev = None
        self.work_real = None
        self.outlet = inlet     #   PLACEHOLDER
        pass

    def operate(self) -> None:

        return self.outlet


class HeatExchanger():

    def __init__(self, hot_stream: object, cold_stream: object, exch_coeff: float, exch_area: float, xflow=True):
        self.hot_stream = hot_stream    # hot feed stream, to be cooled
        self.cold_stream = cold_stream  # cold feed stream, to be heated
        self.exch_coeff = exch_coeff    # U
        self.exch_area = exch_area      # A
        self.xflow = xflow              # crossflow > Motstrøms

        self.output_stream_hot = self.hot_stream    # PLACEHOLDER
        self.output_stream_cold = self.cold_stream  # PLACEHOLDER
        
        pass
    
    def operate(self):
        outlet_hot: object = self.hot_stream    # PLACEHOLDER
        outlet_cold:object = self.cold_stream   # PLACEHOLDER
        data: list = []

        return outlet_hot, outlet_cold, data
    

class Compressor():

    def __init__(self, feed_stream: object, efficiency: float, stages: int=3):
        self.feed_stream = feed_stream
        self.stages = stages
        self.heat = None
        self.work_rev = 1   #   PLACEHOLDER VALUE
        self.work_real = self.work_rev/efficiency

        pass

    def operate(self) -> None:

        pass