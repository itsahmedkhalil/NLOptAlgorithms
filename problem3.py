import numpy as np
import pandas as pd

from functions import Quadratic
from params import initialize
from benchmark import benchmark_algorithms
from utils import Q_generate, plot_all, save_data

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs
from dfp import dfp
from newton_cg import newton_cg

prob = 'Problem3'

# Initialize parameters
options = initialize() 

# Initialize random seed
np.random.seed(0)

# Setup Problem 3
# Randomly generated convex quadratic function
# n = 1000, kappa = 10
# Starting point x0 = 20 * np.random.rand(n) - 10
n = 1000
kappa = 10
Q = Q_generate(n, kappa)
q = np.random.rand(n)
x0 = 20 * np.random.rand(n) - 10
problem = Quadratic(Q, q)

# Benchmarking algorithms
algorithms = [
    ('GD', gradient_descent),
    ('MN', modified_newton),
    ('BFGS', bfgs),
    ('L-BFGS', lbfgs),
    ('DFP', dfp),
    ('NCG', newton_cg)
]

# Run the benchmark
results = benchmark_algorithms(algorithms, problem, x0, options)

# Save the results
save_data(results, prob)

# plot the gradient norm history, the function value history, the total time, and the total iterations
plot_all(results, prob)

