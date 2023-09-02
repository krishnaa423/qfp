import numpy as np

class Cell:

    def __init__(self):
        self.a = np.eye((3, 3))       # Each column is a vector. The columns are ordered x, y, z
        self.nat = 2
        self.apos = np.array([])        # (nat, 3) 
        self.atyp = np.array([])        # (nat,)