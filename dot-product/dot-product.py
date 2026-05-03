import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x=np.array(x)
    y=np.array(y)
    print("Shape x: ", x.shape)
    print("Shape y: ", y.shape)
    elemult = x * y
    print("Shape x * y: ", elemult.shape)
    dot = np.sum(elemult)
    print("Shape dot product(x,y): ", dot) 
    return dot