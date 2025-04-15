import numpy as np
import pandas as pd

from functions import Exponential
from params import initialize
from benchmark import benchmark_algorithms
from utils import plot_all

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs
from dfp import dfp
from newton_cg import newton_cg

prob = 'Problem11'

# Initialize parameters
options = initialize() 

# Initialize random seed
np.random.seed(0)

# Setup Problem 11
# Exponential function n = 1000
# Starting point x0 = [1, 0, ..., 0]
n = 1000
x0 = np.zeros(n)
x0[0] = 1
problem = Exponential(n)

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

# Save results to csv file
df = pd.DataFrame(results)
df.to_csv(f'data/{prob}.csv', index=False)

# plot the gradient norm history, the function value history, the total time, and the total iterations
plot_all(results, prob)

