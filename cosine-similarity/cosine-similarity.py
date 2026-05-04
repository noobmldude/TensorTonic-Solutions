import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)
    print("norma: ", norma)
    print("normb: ", normb)
    if not norma or not normb:
        return 0.0
    dot = np.dot(a,b)
    print('np.dot(a,b)', dot)
    return dot/(norma * normb)
    