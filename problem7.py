import numpy as np
import pandas as pd

from functions import Rosenbrock2D
from params import initialize
from benchmark import benchmark_algorithms
from utils import plot_gradient_norm

from bfgs import bfgs
from dfp import dfp
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs
from newton_cg import newton_cg

prob = 'Problem7'

# Initialize parameters
options = initialize() 

# Initialize random seed
np.random.seed(0)

# Setup Problem 7
# Rosenbrock function n = 2
# Starting point x0 = [-1.2, 1]
x0 = np.array([-1.2, 1])
problem = Rosenbrock2D()

# Benchmarking algorithms
algorithms = [
    ('Gradient Descent', gradient_descent),
    ('Modified Newton', modified_newton),
    ('BFGS', bfgs),
    ('L-BFGS', lbfgs),
    ('DFP',dfp),
    ('Newton CG', newton_cg)
]

# Run the benchmark
results = benchmark_algorithms(algorithms, problem, x0, options)

# Save results to csv file
df = pd.DataFrame(results)
df.to_csv(f'data/{prob}.csv', index=False)

# Plot gradient norm history
plot_gradient_norm(results, prob)

