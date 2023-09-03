import sys
sys.path.append('..')
import Common
import numpy as np

class Rho:
    '''
    Charge density. 
    '''

    def __init__(self, g: Common.Ggrid):
        self.rho_size = (g.gmax, g.gmax, g.gmax)
        self.rho = np.zeros(self.rho_size, dtype='f16')  # (gmax, gmax, gmax). 

    def get_rho(self):
        return self.rho