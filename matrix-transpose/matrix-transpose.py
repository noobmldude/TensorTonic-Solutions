import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    AT = np.zeros((A.shape[1], A.shape[0]))
    print("Shape of A: ", A.shape)
    print("Shape of AT: ", AT.shape)
    for i in range(AT.shape[0]):
        print("i=", i)
        for j in range(AT.shape[1]):
            print("i, j =", i, j)
            AT[i,j]= A[j,i]
    return AT