import numpy as np
import pandas as pd

from functions import Genhumps
from params import initialize
from benchmark import *
from utils import *

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs
from dfp import dfp
from newton_cg import newton_cg

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

# for multiple tau values(armijo) and multiple c2 values(wolfe)
if options['tau_list'].size > 0 or options['c2_list'].size > 0:
    results_c2_tau = benchmark_algorithms_c2_tau(algorithms, problem, x0, options)
    df = pd.DataFrame(results_c2_tau)
    df.to_csv(f'data/{prob}_tau_c2.csv', index=False)

    plot_all_c2_tau(results_c2_tau, prob)

