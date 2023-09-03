import sys
sys.path.append('..')
import numpy as np
import Common

class DftInput:

    def __init__(self, ecut, cell: Common.Cell):
        self.ecut = 20  # Cutoff in Hartree energy. 
        self.cell = cell 