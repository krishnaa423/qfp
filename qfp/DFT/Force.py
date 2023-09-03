import sys 
sys.path.append('..')
import numpy as np
import Common 

class Force:

    def __init__(self, cell: Common.Cell):
        self.force = np.zeros((cell.nat, 3), dtype='f8')