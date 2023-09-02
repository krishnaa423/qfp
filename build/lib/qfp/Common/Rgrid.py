import numpy as np

class Rgrid:

    def __init__(self):
        self.rmax = 32      # Max grid points in a given direction. 
        self.rx, self.ry, self.rz = np.meshgrid(
            np.arange(0, 1, 1.0/self.rmax), 
            np.arange(0, 1, 1.0/self.rmax), 
            np.arange(0, 1, 1.0/self.rmax),
            indexing='ij' 
        )
