import sys 
sys.path.append('..')
import Common 
import Rho
import numpy as np

class Vh:

    def __init__(self, g: Common.Ggrid, cell: Common.Cell):
        self.vh = np.array([])
        self.g = g
        self.cell = cell

    def fill_vh(self, rho: Rho.Rho):
        
        gx = self.g.gx.flatten()
        gy = self.g.gy.flatten()
        gz = self.g.gz.flatten()

        Gx, Gy, Gz = np.meshgrid(gx, gy, gz)
        Gxp, Gyp, Gzp = np.meshgrid(gx, gy, gz)

        self.vh = rho.rho[Gx - Gxp, Gy - Gyp, Gz - Gzp]/( (Gx - Gxp)**2 + (Gy - Gyp)**2 + (Gz - Gzp)**2)

    def get_vh(self):
        return self.vh

