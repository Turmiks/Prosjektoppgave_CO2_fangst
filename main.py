#=========================================================================
#   IMPORTS
#=========================================================================
import numpy as np
import scipy
""" import python_sim as ps
from python_sim import helpers
from python_sim import constants3 """
from python_sim.constants3 import *
import python_sim.helpers as ps
import python_sim.thermodynamics as thermo
import python_sim.unit_operations as unit
#=========================================================================
#   Main script for simulating a process for CO2 capture given
#   as a group project in TKP4120
#
#   Created: 06/03/2025
#   Author(s): Iver Mihle Asklund
#   

version:str = '0.0.1'
#=========================================================================
#   Fetching and consolidating stream data fram constants3.py
#=========================================================================
mol_mass: dict = {'CO2': Mw[0],
                  'H2O' : Mw[1],
                  'N2' : Mw[2],
                  'O2' : Mw[3],
                  'MEA' : MwMEA,
                  }
stream_1_wth_frac: list = [wc1, wh1, wn1, wo1]

stream_1: object = ps.Stream(['CO2','H2O','N2', 'O2'],
                                     stream_1_wth_frac,
                                     100, 273.15, 10e5, 100,
                                     phase='gas')



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

        stream_1.change_temp(313.15)
        print(ps.wth2mol_frac(stream_1.components, stream_1.wth_fractions, stream_1.flow_rate))
        print('Simulation finished')
        stream_1.printout()
        print('\n')
        print('creating table...')


    return None


if __name__ == '__main__':
    main(version)
