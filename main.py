import numpy as np
np.random.seed(0)

from functions import *
from params import initialize
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from bfgs import bfgs
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

    # Run modified Newton with Armijo line search
    x_mn, f_mn, i_mn, t_mn, o_mn, h_mn = modified_newton(x0, problem1, options, armijo_line_search)
    results[f'problem{i}']['mn'] = {
        'x': x_mn,
        'f': f_mn,
        'i': i_mn,
        't': t_mn,
        'o': o_mn,
        # 'h': h_mn
    }

    # Run modified Newton with Wolfe line search
    x_mnW, f_mnW, i_mnW, t_mnW, o_mnW, h_mnW = modified_newton(x0, problem1, options, wolfe_line_search)
    results[f'problem{i}']['mnW'] = {
        'x': x_mnW,
        'f': f_mnW,
        'i': i_mnW,
        't': t_mnW,
        'o': o_mnW,
        # 'h': h_mnW
    }

    # Run BFGS with Armijo line search
    x_bfgs, f_bfgs, i_bfgs, t_bfgs, o_bfgs, h_bfgs = bfgs(x0, problem1, options, armijo_line_search)
    results[f'problem{i}']['bfgs'] = {
        'x': x_bfgs,
        'f': f_bfgs,
        'i': i_bfgs,
        't': t_bfgs,
        'o': o_bfgs,
        # 'h': h_bfgs
    }

    # Run BFGS with Wolfe line search
    x_bfgsW, f_bfgsW, i_bfgsW, t_bfgsW, o_bfgsW, h_bfgsW = bfgs(x0, problem1, options, wolfe_line_search)
    results[f'problem{i}']['bfgsW'] = {
        'x': x_bfgsW,
        'f': f_bfgsW,
        'i': i_bfgsW,
        't': t_bfgsW,
        'o': o_bfgsW,
        # 'h': h_bfgsW
    }

# Print results
print("Results", results)



