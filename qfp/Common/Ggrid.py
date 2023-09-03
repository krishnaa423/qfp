import numpy as np
import Cell 

class Ggrid:

    def __init__(self,
            cell: Cell.Cell, 
            ecut: float = 20.0  # In Hartree a.u.
        ):
        self.ecut = ecut      
        self.gmax = 32   # Need to be calculated from cell parameters. 
        self.gx, self.gy, self.gz = np.mgrid[0:self.gmax, 0:self.gmax, 0:self.gmax]
