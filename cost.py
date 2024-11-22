import numpy as np
def cost(x,size):
    for n in range(3):
        for m in range(3):
            J = np.sum(np.exp(np.sqrt((x[:,0] - (n*(size/3)))**2 + (x[:,1] - (m*(size/3)))**2)))
    return J