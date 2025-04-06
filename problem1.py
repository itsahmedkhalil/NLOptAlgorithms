import numpy as np

from functions import Quadratic
from params import initialize
from benchmark import benchmark_algorithms

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs

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

# Benchmarking algorithms
algorithms = [
    ('Gradient Descent', gradient_descent),
    ('Modified Newton', modified_newton),
    ('BFGS', bfgs),
    ('L-BFGS', lbfgs),
]

# Run the benchmark
results_p1 = benchmark_algorithms(algorithms, problem1, x0_p1, options)

# Print results
for name, result in results_p1.items():
    print(f"Algorithm: {name}")
    print(f"Final x: {result['x']}")
    print(f"Function value: {result['f']}")
    print(f"Iterations: {result['i']}")
    print(f"Time: {result['t']}")
    print(f"Output: {result['o']}")
    print("\n")



