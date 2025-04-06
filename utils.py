import numpy as np
import matplotlib.pyplot as plt


# Set sine function from radians to degrees
def sind(degrees):
    return np.sin(np.deg2rad(degrees))

# Set cosine function from radians to degrees
def cosd(degrees):
    return np.cos(np.deg2rad(degrees))

# Plot the gradient norm history
def plot_gradient_norm(results, problem_name):
    """
    Plot the gradient norm history for all algorithms.

    Parameters:
    - results: Dictionary containing the results of each algorithm.
    - problem_name: Problem number.
    """

    # Find the largest number of iterations excluding gradient descent
    max_iters_all = 0
    max_iters_exc_gd = 0
    for name, result in results.items():
        if 'Gradient Descent' not in name:
            max_iters_exc_gd = max(max_iters_exc_gd, result['i'])

        max_iters_all = max(max_iters_all, result['i'])

    # Make two plots: one with the full number of iterations and one with the largest number of iterations excluding gradient descent
    zoom_iterations = max(max_iters_exc_gd, 10)
    max_iters_all = max(max_iters_all, 10)

    plt.figure(figsize=(20, 10))
    plt.subplot(1, 2, 1)
    for name, result in results.items():
        plt.plot(result['h'][:max_iters_all], label=name, alpha=0.7)
    plt.yscale('log')
    plt.xlabel('Iterations')
    plt.ylabel(r'Gradient Norm, $\|\nabla f(x_k)\|$')
    plt.title(f'Gradient Norm History for {problem_name}')
    plt.legend(loc='lower right')
    plt.grid()
    
    plt.subplot(1, 2, 2)
    for name, result in results.items():
        plt.plot(result['h'][:zoom_iterations], label=name, alpha=0.7)
    plt.yscale('log')
    plt.xlabel('Iterations')
    plt.ylabel(r'Gradient Norm, $\|\nabla f(x_k)\|$')
    plt.title(f'Gradient Norm History for {problem_name}, First {zoom_iterations} Iterations')
    plt.legend(loc='lower right')
    plt.grid()
    
    plt.tight_layout()
    plt.savefig(f'figures/{problem_name}_grad_norm.png')
    plt.show()
    