import numpy as np
from petsc4py import PETSc

x, y = np.meshgrid(np.arange(0, 1, 0.1), np.arange(0, 1, 0.1), indexing='ij')

print(x)
print(y)