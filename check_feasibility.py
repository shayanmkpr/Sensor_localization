import numpy as np

def check(pos,SIZE):
    x, y = pos
    # Check if the position is out of bounds
    x = max(0, min(x, SIZE))
    y = max(0, min(y, SIZE))
    return np.array([x, y])