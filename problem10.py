import numpy as np
import pandas as pd

from functions import Exponential
from params import initialize
from benchmark import benchmark_algorithms
from utils import plot_gradient_norm

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs

prob = 'Problem10'

# Initialize parameters
options = initialize() 

# Initialize random seed
np.random.seed(0)

# Setup Problem 10
# Exponential function n = 10
# Starting point x0 = [1, 0, ..., 0]
n = 10
x0 = np.zeros(n)
x0[0] = 1
problem = Exponential(n)

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

