import numpy as np

from bfgs import bfgs
from functions import *
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from params import initialize
from search_methods import armijo_line_search, wolfe_line_search
from utils import sind, cosd


# Initialize parameters
options = initialize() 

# Initialize random seed
np.random.seed(0)

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
x0_p1 = 20 * np.random.rand(n) - 10
problem1 = Quadratic(Q, q)

# Setup Problem 2
# Randomly generated convex quadratic function
# n = 10, kappa = 1000
# Starting point x0 = 20 * np.random.rand(n) - 10
n = 10
kappa = 1000
Q = np.random.rand(n, n)
Q = Q.T @ Q
Q = kappa * Q / np.linalg.norm(Q, ord=2)
q = np.random.rand(n)
x0_p2 = 20 * np.random.rand(n) - 10
problem2 = Quadratic(Q, q)

# Setup Problem 3
# Randomly generated convex quadratic function
# n = 1000, kappa = 10
# Starting point x0 = 20 * np.random.rand(n) - 10
n = 1000
kappa = 10
Q = np.random.rand(n, n)
Q = Q.T @ Q
Q = kappa * Q / np.linalg.norm(Q, ord=2)
q = np.random.rand(n)
x0_p3 = 20 * np.random.rand(n) - 10
problem3 = Quadratic(Q, q)

# Setup Problem 4
# Randomly generated convex quadratic function
# n = 1000, kappa = 1000
# Starting point x0 = 20 * np.random.rand(n) - 10
n = 1000
kappa = 1000
Q = np.random.rand(n, n)
Q = Q.T @ Q
Q = kappa * Q / np.linalg.norm(Q, ord=2)
q = np.random.rand(n)
x0_p4 = 20 * np.random.rand(n) - 10
problem4 = Quadratic(Q, q)

# Setup Problem 5
# Quartic function 1
# n = 4, sigma = 10e-4
# Starting point x0 = [cos(70), sin(70), cos(70), sin(70)]
A = np.array([[5, 1, 0, 0.5],
              [1, 4, 0.5, 0],
              [0, 0.5, 3, 0],
              [0.5, 0, 0, 2]])
sigma = 10e-4
x0_p5 = np.array([cosd(70), sind(70), cosd(70), sind(70)])
problem5 = Quartic(A, sigma)

# Setup Problem 6
# Quartic function 2
# n = 4, sigma = 10e4
# Starting point x0 = [cos(70), sin(70), cos(70), sin(70)]
A = np.array([[5, 1, 0, 0.5],
              [1, 4, 0.5, 0],
              [0, 0.5, 3, 0],
              [0.5, 0, 0, 2]])
sigma = 10e4
x0_p6 = np.array([cosd(70), sind(70), cosd(70), sind(70)])
problem6 = Quartic(A, sigma)

# Setup Problem 7
# Rosenbrock function n = 2
# Starting point x0 = [-1.2, 1]
x0_p7 = np.array([-1.2, 1])
problem7 = Rosenbrock2D()

# Setup Problem 8
# Rosenbrock function n = 100
# Starting point x0 = [-1.2, 1, ..., 1]
n = 100
x0_p8 = np.ones(n)
x0_p8[0] = -1.2
problem8 = RosenbrockND(n)

# Setup Problem 9
# Data fit
# Starting point x0 = [1, 1]
x0_p9 = np.array([1, 1])
y = np.array([1.5, 2.25, 2.625])
problem9 = DataFit(y)

# Setup Problem 10
# Exponential function n = 10
# Starting point x0 = [1, 0, ..., 0]
n = 10
x0_p10 = np.zeros(n)
x0_p10[0] = 1
problem10 = Exponential(n)

# Setup Problem 11
# Exponential function n = 1000
# Starting point x0 = [1, 0, ..., 0]
n = 1000
x0_p11 = np.zeros(n)
x0_p11[0] = 1
problem11 = Exponential(n)

# Setup Problem 12
# Genhumps function n = 5
# Starting point x0 = [-506.2, 506.2, ..., 506.2]
n = 5
x0_p12 = np.ones(n) * 506.2
x0_p12[0] = -506.2
problem12 = Genhumps()

results = {
    'problem1': {'problem': problem1,
                    'x0': x0_p1},
    'problem2': {'problem': problem2,
                    'x0': x0_p2},
    'problem3': {'problem': problem3,
                    'x0': x0_p3},
    'problem4': {'problem': problem4,
                    'x0': x0_p4},
    'problem5': {'problem': problem5,
                    'x0': x0_p5},
    'problem6': {'problem': problem6,
                    'x0': x0_p6},
    'problem7': {'problem': problem7,
                    'x0': x0_p7},
    'problem8': {'problem': problem8,
                    'x0': x0_p8},
    'problem9': {'problem': problem9,
                    'x0': x0_p9},
    'problem10': {'problem': problem10,
                    'x0': x0_p10},
    'problem11': {'problem': problem11,
                    'x0': x0_p11},
    'problem12': {'problem': problem12,
                    'x0': x0_p12}
}

for i in range(1, len(results.values())+1):
    
    if i == 3 or i == 4:
        # Skip problems 3 and 4 for now
        continue

    # Get the problem and initial point
    problemi = results[f'problem{i}']['problem']
    # print("iteration", i)
    x0 = results[f'problem{i}']['x0']

    # Run gradient descent with Armijo line search
    x_gd, f_gd, i_gd, t_gd, o_gd, h_gd = gradient_descent(x0, problemi, options, armijo_line_search)

    results[f'problem{i}']['gd'] = {
        'x': x_gd,
        'f': f_gd,
        'i': i_gd,
        't': t_gd,
        'o': o_gd,
        # 'h': h_gd
    }

    # Run gradient descent with Wolfe line search
    x_gdW, f_gdW, i_gdW, t_gdW, o_gdW, h_gdW = gradient_descent(x0, problemi, options, wolfe_line_search)

    results[f'problem{i}']['gdW'] = {
        'x': x_gdW,
        'f': f_gdW,
        'i': i_gdW,
        't': t_gdW,
        'o': o_gdW,
        # 'h': h_gdW
    }

    # Run modified Newton with Armijo line search
    x_mn, f_mn, i_mn, t_mn, o_mn, h_mn = modified_newton(x0, problemi, options, armijo_line_search)
    results[f'problem{i}']['mn'] = {
        'x': x_mn,
        'f': f_mn,
        'i': i_mn,
        't': t_mn,
        'o': o_mn,
        # 'h': h_mn
    }

    # Run modified Newton with Wolfe line search
    x_mnW, f_mnW, i_mnW, t_mnW, o_mnW, h_mnW = modified_newton(x0, problemi, options, wolfe_line_search)
    results[f'problem{i}']['mnW'] = {
        'x': x_mnW,
        'f': f_mnW,
        'i': i_mnW,
        't': t_mnW,
        'o': o_mnW,
        # 'h': h_mnW
    }

    # Run BFGS with Armijo line search
    x_bfgs, f_bfgs, i_bfgs, t_bfgs, o_bfgs, h_bfgs = bfgs(x0, problemi, options, armijo_line_search)
    results[f'problem{i}']['bfgs'] = {
        'x': x_bfgs,
        'f': f_bfgs,
        'i': i_bfgs,
        't': t_bfgs,
        'o': o_bfgs,
        # 'h': h_bfgs
    }

    # Run BFGS with Wolfe line search
    x_bfgsW, f_bfgsW, i_bfgsW, t_bfgsW, o_bfgsW, h_bfgsW = bfgs(x0, problemi, options, wolfe_line_search)
    results[f'problem{i}']['bfgsW'] = {
        'x': x_bfgsW,
        'f': f_bfgsW,
        'i': i_bfgsW,
        't': t_bfgsW,
        'o': o_bfgsW,
        # 'h': h_bfgsW
    }

# Print results
# print("Results", results)



