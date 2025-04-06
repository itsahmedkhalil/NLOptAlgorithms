import numpy as np
import pandas as pd

from functions import Quadratic
from params import initialize
from benchmark import benchmark_algorithms
from utils import plot_gradient_norm

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs

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
Q = np.random.rand(n, n)
Q = Q.T @ Q
Q = kappa * Q / np.linalg.norm(Q, ord=2)
q = np.random.rand(n)
x0 = 20 * np.random.rand(n) - 10
problem = Quadratic(Q, q)

# Benchmarking algorithms
algorithms = [
    ('Gradient Descent', gradient_descent),
    ('Modified Newton', modified_newton),
    ('BFGS', bfgs),
    ('L-BFGS', lbfgs),
]

# Run the benchmark
results = benchmark_algorithms(algorithms, problem, x0, options)

# Save results to csv file
df = pd.DataFrame(results)
df.to_csv(f'data/{prob}.csv', index=False)

# Plot gradient norm history
plot_gradient_norm(results, prob)

