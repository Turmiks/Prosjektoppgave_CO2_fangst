#=========================================================================
#   IMPORTS
#=========================================================================

import numpy as np
import scipy

#   local
from python_sim.constants3 import *
import python_sim.thermodynamics
import python_sim.unit_operations

#=========================================================================
#   Constants
#=========================================================================

mol_mass: dict = {'CO2': Mw[0],
                  'H2O' : Mw[1],
                  'N2' : Mw[2],
                  'O2' : Mw[3],
                  'MEA' : MwMEA,
                  }

#=========================================================================
#   Helper functions
#=========================================================================

def startup_splash(title: str, version: str, simtype:str = 'CO2-capture') -> None:
    
    ver: str = f'version: {version}'
    print('='*69)
    print(f'|{title.center(67)}|')
    print(f'|{ver.center(67)}|')
    print('|' + '-'*67 + '|')
    print(f'|{(f'Simulation: {simtype}').center(67)}|')
    print('='*69)

    return None


def table(title: str, header: list[str], rows: list[list[float|str]],) -> None:
    head_row: str = '|'
    for i in header:
        head_row += (i.center(15) + '|')

    print(title.center(len(head_row)))
    print('|' + '='*(len(head_row)-2) + '|')
    print(head_row)
    print('|' + '='*(len(head_row)-2) + '|')
    
    for row in rows:
        current_row: str = '|'
        for place in row:
            current_row += (str(place)).center(15) + '|'
        
        print(current_row)
        print('|' + '-'*(len(head_row)-2) + '|')
            
    return None

# UNFINISHED
def wth2mol_frac(components: list[str], fractions: list[float], total: float) -> list:
    
    assert(len(components) == len(fractions)), 'error in specified arguments'

    component_masses: list = [fractions[i[0]]*total for i in enumerate(fractions)]
    component_amounts: list = []

    for i in enumerate(components):
        amount: float = component_masses[0]/mol_mass[i[1]]
        component_amounts.append(amount)

    mol_frac: list = []

    for i in component_amounts:
        fraction: float = i/ sum(component_amounts)
        mol_frac.append(fraction)

    return mol_frac



#=========================================================================
#   Classes
#=========================================================================

class Stream():
    
    def __init__(
            self, components: list[str], wth_fractions: list[float], flow_rate: float,
            temperature: float, pressure: float,
            enthalpy: float, phase: str):
        
        self.flow_rate = flow_rate
        self.components = components
        self.wth_fractions = wth_fractions
        self.temperature = temperature
        self.pressure = pressure
        self.enthalpy = enthalpy
        self.phase = phase
        self.listed: list = [self.flow_rate, self.components,
                             self.wth_fractions, self.temperature,
                             self.pressure, self.enthalpy,
                             self.phase,]
        pass

    def change_temp(self, new_temp: float) -> None:
        print(f'changed temperature from {self.temperature}K to {new_temp}K')
        self.temperature = new_temp

    def printout(self) -> None:
        print('Strømmedata:')
        print(f'-'*30)
        print(f'massestrøm: {self.flow_rate}')
        print('-'*3)
        print('Vektfraksjoner:')
        print('-'*30)
        for i in enumerate(self.components):
            print(f'{i[1]}: {self.wth_fractions[i[0]]}')
            print('-'*30)
        print(f'Temperatur: {self.temperature}K')
        print('-'*30)
        print(f'Trykk: {self.pressure} Pa')
        print('-'*30)
        print(f'Entalpi: {self.enthalpy} Joule')
        print('-'*30)
        print(f'Tilstand: {self.phase}')
        
    
    
""" tit: str = 'Tabell over ferdig data'
a = ['kollonne 1', 'kollonne 2', 'kollonne 3', 'kollonne 4']
b = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

table(tit, a, b) """