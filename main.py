import numpy as np
np.random.seed(0)

from functions import *
from params import initialize
from gradient_descent import gradient_descent
from search_methods import armijo_line_search, wolfe_line_search


# Set parameters
c1 = 10**-4
c2 = 0.9
max_iter = 10000
epsilon_min = 10e-8
tol = 10e-8
eta = 0.01
tau = 0.5
beta = 1e-4

options = initialize(c1, c2, max_iter, epsilon_min, tol, eta, tau, beta) 


# Setup Problem 1
# Randomly generated convex quadratic function 
# n = 10, kappa = 10
# Starting point x0 = 20 * np.random.rand(n) - 10

n = 10
kappa = 10
Q = np.random.rand(n, n)
Q = Q.T @ Q
Q = kappa * Q / np.linalg.norm(Q, ord=2)
q = np.random.rand(n)
x0 = 20 * np.random.rand(n) - 10

problem1 = Quadratic(Q, q)

results = {
    'problem1': {},
    # 'problem2': {},
    # 'problem3': {},
    # 'problem4': {},
    # 'problem5': {},
    # 'problem6': {},
    # 'problem7': {},
    # 'problem8': {},
    # 'problem9': {},
    # 'problem10': {}
}

for i in range(1, len(results.values())+1):
    
    # Run gradient descent with Armijo line search
    x_gd, f_gd, i_gd, t_gd, o_gd, h_gd = gradient_descent(x0, problem1, options, armijo_line_search)

    results[f'problem{i}']['gd'] = {
        'x': x_gd,
        'f': f_gd,
        'i': i_gd,
        't': t_gd,
        'o': o_gd,
        # 'h': h_gd
    }

    # Run gradient descent with Wolfe line search
    x_gdW, f_gdW, i_gdW, t_gdW, o_gdW, h_gdW = gradient_descent(x0, problem1, options, wolfe_line_search)

    results[f'problem{i}']['gdW'] = {
        'x': x_gdW,
        'f': f_gdW,
        'i': i_gdW,
        't': t_gdW,
        'o': o_gdW,
        # 'h': h_gdW
    }



# Print results
print("Results", results)



