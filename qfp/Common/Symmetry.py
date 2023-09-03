import numpy as np
import Cell 

class Symmetry:

    def __init__(self, cell: Cell.Cell):
        # Determine the symmetry matrices from cell. 
        self.nmat = 10
        self.sym_mats = np.array([]) # (nmat, 4, 4). Affine matrices 