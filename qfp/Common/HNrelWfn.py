import numpy as np
from scipy.special import genlaguerre, sph_harm
import Rgrid
import Cell

class HNrelWfn:

    def __init__(self, n, l, m, Z, loc):
        self.n  = n
        self.l  = l
        self.m  = m
        self.Z = Z

    def get_wfn(self, rgrid: Rgrid.Rgrid, cell: Cell.Cell, loc: np.ndarray) -> np.ndarray:
        '''
        Get the hydrogen like atom solution on a given rgrid and cell.  

        loc: location of atom in fractional coordinates. (3,)
        '''

        # region: Get x, y, z, rad, theta, phi. 

        # Flatten rx, ry, rz.  
        num_points = rgrid.rmax**3
        points = np.zeros((num_points, num_points, num_points), dtype='f8')
        points[:, 0] = rgrid.rx.flatten()
        points[:, 1] = rgrid.ry.flatten()
        points[:, 2] = rgrid.rz.flatten()

        # Get cart. 
        cart = points*cell.a        # Columns are x, y, z. 
        loc_x, loc_y, loc_z = loc*cell.a 
        x = cart[:, 0] - loc_x
        y = cart[:, 1] - loc_y
        z = cart[:, 2] - loc_z
        

        # Get rad, theta, phi. 
        rad = np.sqrt(x**2 + y**2 + z**2)
        theta = np.arccos(z/rad)
        phi = np.sign(y)*np.arccos(x/np.sqrt(x**2 + y**2))
        # endregion. 

        # region: Get normalized wfn.
        rho = self.Z*rad/self.n     # From wikipedia for hydrogen like atom solution. 
        wfn = rho**self.l\
            *np.exp(-rho/2)\
            *genlaguerre(self.n, 2*self.l+1)(rho)\
            *sph_harm(self.m, self.l)(theta, phi)
        wfn /= np.sum(np.abs(wfn)**2)  # Normalize the wavefunction. 
        # endregion. 

        # region: Reshape and return the result.
        wfn = wfn.reshape((rgrid.rmax, rgrid.rmax, rgrid.rmax))
        return wfn  # (rmax, rmax, rmax)
        # endregion. 