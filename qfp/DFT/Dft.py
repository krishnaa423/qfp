import DftInput
from petsc4py import PETSc

class Dft:

    def __init__(self, dft_input: DftInput.DftInput):
        self.dft_input = dft_input        
        self.t = []
        self.vion = []
        self.vh = []
        self.vxc = []
        self.v = []
        self.max_iter = 20
        self.max_error = 1e-6

    def init_guess(self):
        pass

    def single_scf_cycle(self):
        pass

    def get_error(self):
        pass
    
    def run(self):
        iter = 0
        error = 0

        # Init. 
        self.init_guess()

        # Run self-consistency cycle. 
        while True:

            # Step. 
            iter += 1

            # Step. 
            self.single_scf_cycle()

            # Get error. 
            error = self.get_error()

            # Quit if converged. 
            if error < self.max_error or iter > self.max_iter:
                break