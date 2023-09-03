import sys
sys.path.append('..')
import Common
import numpy as np

class T:
    '''
    Kinetic energy.  
    '''

    def __init__(self, g: Common.Ggrid):
        self.nrows = g.gmax**3
        self.ncols = g.gmax**3
        self.mat_size = (self.nrows, self.ncols)
        self.T = np.zeros(self.mat_size, dtype='f16')  # (gmax, gmax, gmax). 
        self.g = g

    def fill_T(self):
        # Fill the diagonal values. Assuming only one k-point. 

        gx = self.g.gx.flatten()
        gy = self.g.gy.flatten()
        gz = self.g.gz.flatten()

        for row in range(self.nrows):
            diag_value = (gx**2 + gy**2 + gz**2)/2
            self.T[row, row] = diag_value
