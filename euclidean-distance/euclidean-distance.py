import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    print(x.shape)
    diff = x -y
    print(diff.shape)
    sumsq= np.sum(diff**2)
    print(sumsq)
    sqrt = np.sqrt(sumsq)
    print(sqrt)
    return sqrt