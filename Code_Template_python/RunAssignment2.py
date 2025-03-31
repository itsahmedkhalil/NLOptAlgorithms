import numpy as np
from OptAlg import opt_alg
from params import initialize
from rosenbrock import rosenbrock_func
from rosenbrock import rosenbrock_grad
from rosenbrock import rosenbrock_hessian

# This is the main file to run the programming problem in the assignment

# Methods implemented
methods_list = ['steepest_descent', 'newton', 'modified_newton']

# Problem 1

# Starting point
x0 = np.array([[-1.2], 
               [1.0]])

# Print the starting point
print('Starting point:\n')
n = len(x0)
for i in range(n):
    print(f'x0[{i:4d}] = {x0[i, 0]:15.8e}')

# Loop through the different methods
for j in range(len(methods_list)):
    # Options
    options = initialize()  # Initializes default values for some parameters
    options['method'] = methods_list[j]

    # Set other options (use a meaningful name as in algorithm description)
    options['rho'] = 0.5  # example value

    # Define the objective structure
    obj = {
        'func': rosenbrock_func,
        'grad': rosenbrock_grad,
        'hess': rosenbrock_hessian,
    }

    # Optimize the function
    sol, status = opt_alg(x0, obj, options)

    # Print the return status
    print(f'\nReturn status: {status}\n')

    # Print the optimal solution
    print('Optimal solution:')
    for i in range(sol.shape[0]):
        print(f'x[{i:4d}] = {sol[i, 0]:15.8e}')

# Problem 2
# You need to implement this!

# Problem 3
# You need to implement this!
# etc...