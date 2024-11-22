import numpy as np
from cost import cost

def gradient(x, i, size , gradient_step , N):
    u = x[i , : , :]
    h = gradient_step
    u_x = np.zeros((N, 2))
    u_y = np.zeros((N, 2))
    u_x[i , 0] = h
    u_y[i , 1] = h
    grad_x = (cost(u + u_x, size) - cost(u , size))/h
    grad_y = (cost(u + u_y , size) - cost(u , size))/h
    grad = np.array([grad_x , grad_y])
    return grad