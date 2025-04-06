import numpy as np
import pandas as pd

from functions import Genhumps
from params import initialize
from benchmark import benchmark_algorithms
from utils import plot_gradient_norm

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs

prob = 'Problem12'

# Initialize parameters
options = initialize() 

# Initialize random seed
np.random.seed(0)

# Setup Problem 12
# Genhumps function n = 5
# Starting point x0 = [-506.2, 506.2, ..., 506.2]
n = 5
x0 = np.ones(n) * 506.2
x0[0] = -506.2
problem = Genhumps()

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

