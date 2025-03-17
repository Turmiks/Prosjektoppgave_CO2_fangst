#=========================================================================
#   IMPORTS
#=========================================================================
import numpy as np
import scipy

#   Local imports
import python_sim as ps
from python_sim.constants3 import *
#=========================================================================
#   Main script for simulating a process for CO2 capture given
#   as a group project in TKP4120
#
#   Created: 06/03/2025
#   Author(s): Iver Mihle Asklund
#   

version:str = '0.0.5'
#=========================================================================
#   Fetching and consolidating stream data fram constants3.py
#=========================================================================

print('establishing streams...')

stream_1: object = ps.Stream(composition = ['CO2','H2O','N2', 'O2'],
                             wth_fractions = [wc1, wh1, wn1, wo1],
                             flow_rate = 100,
                             temperature = T[0],
                             pressure = p[0]*10**5,
                             phase = 'gas',)

stream_2: object = ps.Stream(composition = ['CO2', 'N2', 'O2'],
                             wth_fractions = [None, None, None],
                             flow_rate = None,
                             temperature = T[1],
                             pressure = p[1]*10**5,
                             enthalpy = None,
                             phase = 'gas',)

stream_3: object = ps.Stream(composition = [],
                             wth_fractions = None,
                             flow_rate = None,
                             temperature = T[2],
                             pressure = p[2]*10**5,
                             enthalpy = None,
                             loading = alpha3,
                             phase = 'liquid',)

stream_4: object = ps.Stream(composition = [],
                             wth_fractions = None,
                             flow_rate = None,
                             temperature = T[3],
                             pressure = p[3]*10**5,
                             enthalpy = None,
                             loading = alpha4,
                             phase = 'liquid',)

stream_5: object = ps.Stream(composition = [],
                             wth_fractions = None,
                             flow_rate = None,
                             temperature = T[4],
                             pressure = p[4]*10**5,
                             enthalpy = None,
                             phase = 'gas',)

stream_6: object = ps.Stream(composition = [],
                             wth_fractions = None,
                             flow_rate = None,
                             temperature = T[5],
                             pressure = p[5]*10**5,
                             enthalpy = None,
                             phase = 'gas',)

stream_7: object = ps.Stream(composition = [],
                             wth_fractions = None,
                             flow_rate = None,
                             temperature = T[6],
                             pressure = p[6]*10**5,
                             enthalpy = None,
                             phase = 'gas',)

stream_8: object = ps.Stream(composition = [],
                             wth_fractions = None,
                             flow_rate = None,
                             temperature = T[7],
                             pressure = p[7]*10**5,
                             enthalpy = None,
                             phase = 'gas',)

stream_9: object = ps.Stream(composition = ['CO2'],
                             wth_fractions = [1],
                             flow_rate = None,
                             temperature = T[8],
                             pressure = p[8]*10**5,
                             phase = 'gas')

stream_10: object = ps.Stream(composition = ['H2O'],
                              wth_fractions = [1],
                              flow_rate = None,
                              temperature = 298,
                              pressure = 1,
                              enthalpy = None,
                              phase = 'liquid')

stream_11: object = ps.Stream(composition = ['H2O'],
                              wth_fractions = [1],
                              flow_rate = None,
                              temperature = None,
                              pressure = 1,
                              enthalpy = None,
                              phase = 'liquid')

V3_out: object = ps.Stream(composition = ['H2O'],
                              wth_fractions = [1],
                              flow_rate = None,
                              temperature = None,
                              pressure = 1,
                              enthalpy = None,
                              phase = 'liquid')
#=========================================================================
#   Creating unit operation objects
#=========================================================================
print('creating unit operations...')

absorber_K1: object = ps.Absorber(feed_stream_1 = stream_1,
                                  feed_stream_2 = stream_3,
                                  output_stream_bot = stream_4,
                                  output_stream_top = stream_2,
                                  capture_rate = wcapture)

""" stripper_K2: object = ps.Stripper(stream_5,
                                  stream_8)  """  #   NOT COMPLETED

pump_P1: object = ps.Pump(stream_4)

exchanger_V1: object = ps.HeatExchanger(hot_stream = stream_6,
                                        cold_stream = stream_4,
                                        exch_coeff = U,
                                        exch_area = None)

cooler_V2: object = ps.HeatExchanger(hot_stream = stream_7,
                                     cold_stream = stream_10,
                                     exch_coeff = U,
                                     exch_area = None)

cooler_V3: object = ps.HeatExchanger(hot_stream = stream_8,
                                     cold_stream = V3_out,
                                     exch_coeff = U,
                                     exch_area = None)

# boiler_V4: object = ps.HeatExchanger()

#   REFLUXTANK T-1

compressor_C1: object = ps.Compressor(feed_stream = stream_9, efficiency = eta)


#=========================================================================
#   Main function
#=========================================================================

def main(version: str, mode:str='std'):
    ps.startup_splash('Chemical process simulator', version)
    run: bool = True
    while run:
        user_run: str = input('Would you like to run the simulator? y/n: ')
        if user_run.lower() in ['y', 'yes', 'ja']:
            run = True
            
        elif user_run.lower() in ['n', 'no', 'nei']:
            print('goodbye')
            run = False
            quit()
        else:
            print('invalid user input, please try again')
            user_run: str = input('Would you like to run the simulator? y/n: ')
        print('running...')

        #   running simulation until approx. steady state
        not_steady: bool = True
        while not_steady:
            #main process simulation

            # 1 + 3 into absorber, 2 + 4 out
            absorber_K1.operate()
            stream_2 = absorber_K1.output_stream_1
            stream_4 = absorber_K1.output_stream_2
            # 4 into pump
            pump_P1.operate()
            # 4 through heat exchanger becomes 5
            exchanger_V1.operate()
            stream_5 = exchanger_V1.output_stream_hot
            # 5 into stripper with return flow from boiler, 6 + 8 + 9 out
            #stripper_K2.operate()
            # 8 to heat exchanger, becomes 12

            # 12 + 9 to reflux tank, becomes 9

            # 9 to compressor
            compressor_C1.operate()
            product_stream: object = ps.Stream(['CO2'], [1], phase='gas')



            previous_result: str = 'PLACEHOLDER'
            current_result: str = 'PLACEHOLDER'
            if current_result == previous_result:
                not_steady = False
                continue


        stream_1.change_temp(313.15)
        print(ps.wtm_frac(stream_1.composition, stream_1.wth_fractions, stream_1.flow_rate))
        print('Simulation finished')
        stream_1.printout()
        print('\n')


        #   DEBUG PRINT
        print('printing stream data...')
        streams = [stream_1,stream_2,stream_3, stream_4,stream_5,stream_6,stream_7,stream_8,stream_9,stream_10,stream_11]
        nr = 0
        for stream in streams:
            nr += 1
            print(f'stream {nr}')
            for property in stream.__dict__:
                print(str(property) + ' : ' + str(stream.__dict__[property]))
            print('*'*60)

    return None


if __name__ == '__main__':
    main(version)
