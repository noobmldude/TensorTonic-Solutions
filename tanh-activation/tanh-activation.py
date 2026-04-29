import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    ex = np.exp(x)
    enx = np.exp(-x)
    return (ex - enx)/(ex + enx)