import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    eps = 0.00000000001
    return 1 / (1+np.exp(-x)+eps)
    pass