import matplotlib.pyplot as plt
import numpy as np

def plot_positions(starting_positions, finishing_positions, size):
    plt.figure(figsize=(12, 5))
    
    # Plot Initial Positions
    plt.subplot(1, 2, 1)
    plt.scatter(starting_positions[:, 0], starting_positions[:, 1], marker='o', color='blue', label='Initial Positions')
    plt.title('Initial Positions')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.xlim(0, size)
    plt.ylim(0, size)
    plt.legend()

    # Plot Final Positions
    plt.subplot(1, 2, 2)
    plt.scatter(finishing_positions[:, 0], finishing_positions[:, 1], marker='o', color='red', label='Final Positions')
    plt.title('Final Positions')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.xlim(0, size)
    plt.ylim(0, size)
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_cost(iterations, cost_values):
    plt.figure(figsize=(8, 5))
    plt.plot(iterations, cost_values, marker='o', color='green')
    plt.title('Cost Function Over Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('Cost Function Value')
    plt.grid(True)
    plt.show()

# def exe_with_plot(size, N, step, iteration, gradient_step):
#     starting_positions = np.zeros((N, 2))
#     finishing_positions = exe(size, N, step, iteration, gradient_step)
#     iterations = np.arange(1, iteration + 1)
#     cost_values = []

#     for k in iterations:
#         x = np.random.random(size=(N, N, 2)) * size
#         starting_positions[:, :] = x[:, np.arange(N), :]

#         # Calculate and store the cost function value for each iteration
#         cost_values.append(cost(x, size))

#     # Plot positions and cost values
#     plot_positions(starting_positions, finishing_positions, size)
#     plot_cost(iterations, cost_values)

# # Example Usage
# exe_with_plot(100, 5, 10, 200, 10)
