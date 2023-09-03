from mpi4py import MPI

class MpiInfo:

    def __init__(self):
        comm = MPI.COMM_WORLD
        self.np = comm.Get_size()
        self.pidx = comm.Get_rank()