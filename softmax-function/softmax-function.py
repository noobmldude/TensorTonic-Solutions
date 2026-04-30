import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    print(np.max(x,axis=-1 , keepdims=True))
    ex = np.exp(x-np.max(x,axis=-1, keepdims=True))
    print(ex)
    sumex= np.sum(ex,axis=-1, keepdims=True)
    print(sumex)
    smax = ex/sumex
    print(smax)
    return smax
    pass