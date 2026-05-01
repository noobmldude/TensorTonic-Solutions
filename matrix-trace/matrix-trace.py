import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.array(A)
    dim = A.shape[0] # since it is square matrix, I can take any axis
    print("shape of A: ", A.shape )
    sum = 0
    for i in range(dim):
        print("(i,j) = ",i , i )
        sum += A[i,i]
    print("sum: ", sum)
    return sum
