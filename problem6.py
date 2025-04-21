import numpy as np
import pandas as pd

from functions import Quartic
from params import initialize
from benchmark import *
from utils import *

from bfgs import bfgs
from gradient_descent import gradient_descent
from modified_newton import modified_newton
from lbfgs import lbfgs
from dfp import dfp
from newton_cg import newton_cg

prob = 'Problem6'

# Initialize parameters
options = initialize() 

# Initialize random seed
np.random.seed(0)

# Setup Problem 6
# Quartic function 2
# n = 4, sigma = 1e4
# Starting point x0 = [cos(70), sin(70), cos(70), sin(70)]
A = np.array([[5, 1, 0, 0.5],
              [1, 4, 0.5, 0],
              [0, 0.5, 3, 0],
              [0.5, 0, 0, 2]])
sigma = 1e4
x0 = np.array([cosd(70), sind(70), cosd(70), sind(70)])
problem = Quartic(A, sigma)

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