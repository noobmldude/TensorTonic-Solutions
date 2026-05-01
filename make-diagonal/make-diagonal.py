import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Manual Loop solution
    # size = len(v)
    # D = np.zeros((size,size))
    # for i in range(size):
    #     D[i,i] = v[i]
    # return D
    
    # One-liner using Numpy
    return np.diag(v)
    