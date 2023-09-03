import sys
sys.path.append('..')
import numpy as np

class Eig:

    def __init__(self, neig):
        self.neig = neig
        self.eig = np.array([])