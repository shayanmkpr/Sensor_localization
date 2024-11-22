import numpy as np
from cost import cost
from gradient import gradient

def opt(x , i, step, size , gradient_step , N):
    u = x[i , : , :]
    v = u[i , :] - (step * gradient(x , i , size , gradient_step , N))/np.linalg.norm(gradient(x , i , size , gradient_step , N))
    u[i , :] = v
    return u