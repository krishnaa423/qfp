import numpy as np

class Cell:

    def __init__(self, 
            a: np.ndarray = np.eye((3, 3)), 
            nat: int = 2,
            apos: np.ndarray = np.ndarray([]), 
            atyp: np.ndarray = np.ndarray([]) 
        ):
        self.a = a       # Each column is a vector. The columns are ordered x, y, z
        self.nat = nat
        self.apos = apos        # (nat, 3) 
        self.atyp = atyp        # (nat,)