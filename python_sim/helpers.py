#=========================================================================
#   IMPORTS
#=========================================================================
#   standard packages
from time import time 

#   3rd party packages
import numpy as np
import scipy

#   local
from .constants3 import *
from .thermodynamics import molar_mass

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
def wtm_frac(components: list[str]=None, fractions: list[float]=None, total: float=None) -> list[float]:
    
    if components == None or fractions == None or total == None:
        return None
    
    assert(len(components) == len(fractions)), 'inconsistent list length'

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

  
def timeit(func): 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s') 
        return result 
    return wrap_func 

#=========================================================================
#   Classes
#=========================================================================
class Substance():

    def __init__(self, name: str, elements: list,
                 formation_enthalpy: float, heat_capacity: float,
                 mol_mass: float=None):

        self.name = name
        self.elements = elements
        self.formation_enthalpy = formation_enthalpy
        self.heat_capacity = heat_capacity
        self.mol_mass = mol_mass
        pass

class Stream():
    
    def __init__(
            self, composition: list[str]=None, wth_fractions: list[float]=None, flow_rate: float=None,
            temperature: float=298, pressure: float=10e5, enthalpy: float=None, loading: float=None, phase: str='liquid'):
        
        #   material attributes
        self.flow_rate = flow_rate  #   massflow [Kg/s]
        self.composition = composition  #   list of capitalized strings defining stream components
        self.wth_fractions = wth_fractions  #   weight fractions of stream components
        self.mol_fractions = wtm_frac(composition, wth_fractions, flow_rate)    #   molar fractions
        self.loading = None     # applicable to streams 4, 5, 6 and 7
        try:
            self.component_masses = [w*molar_mass(c) for w, c in zip(wth_fractions, composition)]   #   total masses of components
        except:
            self.component_masses = [None]*len(composition)

        #   thermodynamic attributes
        self.temperature = temperature  #   [Kelvin]
        self.heat_capacity = None   #   [J/(kg*K)]
        self.pressure = pressure    #   [Pa]
        self.enthalpy = enthalpy    #   [Joule]
        self.phase = phase          #   string denoting phase ['gas', 'liquid', 'solid']

        pass
    
    def update(self, flow_rate: float=None, composition: list=None,
               wth_fractions: list=None, loading: float=None,
               temperature: float=None, pressure: float=None,
               enthalpy: float=None, phase: str=None
               ) -> None:
        
        if flow_rate is not None:
            self.flow_rate = flow_rate
        if composition is not None:
            self.composition = composition
        if wth_fractions is not None:
            self.wth_fractions = wth_fractions
        if loading is not None:
            self.loading = loading
        if temperature is not None:
            self.temperature = temperature
        if pressure is not None:
            self.pressure = pressure
        if enthalpy is not None:
            self.enthalpy = enthalpy
        if phase is not None:
            self.phase = phase
        
        return None

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
        for i in enumerate(self.composition):
            print(f'{i[1]}: {self.wth_fractions[i[0]]}')
            print('-'*30)
        print(f'Temperatur: {self.temperature}K')
        print('-'*30)
        print(f'Trykk: {self.pressure} Pa')
        print('-'*30)
        print(f'Entalpi: {self.enthalpy} Joule')
        print('-'*30)
        print(f'Tilstand: {self.phase}')
        
    
