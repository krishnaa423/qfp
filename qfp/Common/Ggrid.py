import numpy as np

class Ggrid:

    def __init__(self):
        self.ecut = 20      # In Hartree a.u.
        self.gmax = 32
        self.gx, self.gy, self.gz = np.mgrid[0:self.gmax, 0:self.gmax, 0:self.gmax]
