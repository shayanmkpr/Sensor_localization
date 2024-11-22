import numpy as np
import networkx as nx
from consensus import consensus
from check_feasibility import check
from cost import cost
from gradient import gradient
from network import new_net
from optimize import opt
from plot import plot_positions
from check_cons import convergence_check , coverage_constraint_check , threshold_distance_constraint_check
import matplotlib.pyplot as plt

def strongly_connected(size , N , step , iteration , gradient_step):
    x = np.random.random(size=(N, N, 2)) * 100
    starting_positions = np.zeros((N,2))
    finishing_positions = np.zeros((N,2))
    #init network
    a = new_net(N)
    #initializing starting positions:
    for i in range(N):
        starting_positions[i , :] = x[i , i , :]
    print("starting_positions" , starting_positions)
    w = np.zeros((N , N , 2))
    cost_values = []
    for k in range(iteration):
        print("iteration number" , k)
        #consensus between connected agents
        w = consensus(a , x , N)
        #optimize each agent locally
        for j in range(N):
            u = opt(w , j , step , size , gradient_step , N)
            w[j] = u
            print("agent" , j , "position" , u[j])
        #check if agents are in the space with size "size"
        for j in range(N):
            pos  = w[j , j , :]
            pos = check(pos , size)
            w[j , j , :] = pos
            print("agent" , j , " feasible position" , u[j])
            finishing_positions[j] = pos

        # threshold distance constraint check
        if not threshold_distance_constraint_check(w, N):
            print("Threshold distance constraint violated. Adjusting positions.")
            for j in range(N):
                finishing_positions[j] = check(finishing_positions[j], size)
        print("cost = " , cost(w , size))
        cost_values.append(cost(w, size))
    plt.plot(cost_values, label="Cost Function")
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    plt.legend()
    plt.show()
    plot_positions(starting_positions, finishing_positions, size)
    return finishing_positions

strongly_connected(100 , 4 , 0.01 , 700 , 1)