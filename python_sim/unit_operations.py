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

    def __init__(self, feed_stream_bot: object,
                 feed_stream_top: object, capture_rate: float,
                 output_stream_top: object, output_stream_bot: object):
        """
        Class for creating objects that model absorption column behavior

        :param feed_stream_bot: gaseous stream from which CO2 will be absorbed
        :type feed_stream_bot: object
        :param feed_stream_top: liquid stream containing aqueous MEA solution
        :type feed_stream_top: object
        :param capture_rate: The overall rate at which CO2 is captured from the bottom feed
        :type capture_rate: float
        :param output_stream_top: outlet stream that has been stripped of CO2
        :type output_stream_top: object
        :param output_stream_bot: liquid stream of MEA solution with additional CO2 absorbed
        :type output_stream_bot: object
        """
        self.feed_stream_bot = feed_stream_bot
        self.feed_stream_top = feed_stream_top
        self.capture_rate = capture_rate
        self.output_stream_top = output_stream_top    # PLACEHOLDER?
        self.output_stream_bot = output_stream_bot    # PLACEHOLDER?
        pass

    def operate(self) -> None:
        """
        Method for running calculations on feed and output streams

        :return: Returns Nonetype
        :rtype: None
        """
        #co2 dissolves
        #co2 is absorbed
        

        #   new values for outbound exhaust stream
        wth_frac_top: list[float] = self.feed_stream_bot

        #   new values for outbound liquid stream
        wth_frac_bot: list[float] = self.feed_stream_top

        #   updating properties for outbound streams
        self.output_stream_bot.update(loading=alpha4, )
        self.output_stream_top.update(wth_fractions=wth_frac_top)



        return None


class Stripper():

    def __init__(self, feed_stream_top: object, feed_stream_bot: object, output_stream_top: object,
                 output_stream_bot: object):
        """
        Class for creating objects that model stripper column behavior

        :param feed_stream_top: _description_
        :type feed_stream_top: object
        :param feed_stream_bot: _description_
        :type feed_stream_bot: object
        :param output_stream_top: _description_
        :type output_stream_top: object
        :param output_stream_bot: _description_
        :type output_stream_bot: object
        """
        self.feed_stream_top = feed_stream_top
        self.feed_stream_bot = feed_stream_bot
        self.output_stream_top = output_stream_top
        self.output_stream_bot = output_stream_bot
        pass

    def operate(self) -> None:

        return None

class Pump():

    def __init__(self, inlet: object):
        """
        Class for creating objects modelling fluid pump behavior

        :param inlet: inlet stream for running model calculations
        :type inlet: object
        """
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
        """
        Class for creating objects modelling heat exchanger behavior

        :param hot_stream: inlet stream, hot side
        :type hot_stream: object
        :param cold_stream: inlet stream, cold side
        :type cold_stream: object
        :param exch_coeff: heat transfer coeffisient, usually written as capital U
        :type exch_coeff: float
        :param exch_area: the effective area for exchanging heat between hot and cold side -> A [m²]
        :type exch_area: float
        :param xflow: boolean value declaring which flow type to model, defaults to True
        :type xflow: bool, optional
        """
        self.hot_stream = hot_stream    # hot feed stream, to be cooled
        self.cold_stream = cold_stream  # cold feed stream, to be heated
        self.exch_coeff = exch_coeff    # U
        self.exch_area = exch_area      # A
        self.xflow = xflow              # crossflow > Motstrøms

        self.output_stream_hot = self.hot_stream    # PLACEHOLDER
        self.output_stream_cold = self.cold_stream  # PLACEHOLDER
        self.delta_Q = 0
        pass
    
    def operate(self) -> None:
        self.output_stream_hot = self.cold_stream    # PLACEHOLDER
        self.output_stream_cold = self.hot_stream   # PLACEHOLDER
        self.delta_Q = 0

        
    

class Compressor():

    def __init__(self, feed_stream: object, efficiency: float, stages: int=3):
        """
        Class for creating objects modelling compressor behavior

        :param feed_stream: stream to perform calculations on
        :type feed_stream: object
        :param efficiency: overall compressor efficiency
        :type efficiency: float
        :param stages: number of compressor stages, with intermediate cooling, defaults to 3
        :type stages: int, optional
        """
        self.feed_stream = feed_stream
        self.stages = stages
        self.heat = None
        self.work_rev = 1   #   PLACEHOLDER VALUE
        self.work_real = self.work_rev/efficiency

        pass

    def operate(self) -> None:

        pass