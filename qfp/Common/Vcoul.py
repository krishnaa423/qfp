import numpy as np


class Vcoul:
    '''
    Vcoul generates the coulomb potential. Will generate the spherically symmetric and truncated potential
    for now. 
    '''

    def __init__(self, trunc_radius: float):
        self.rc = trunc_radius      # rc is the truncation radius. 

    def get_sph_vcoul(self, q):
        return 4*np.pi/q**2*(1 - np.cos(self.rc*q))

