import numpy as np
import pandas as pd

from functions import Quartic
from params import initialize
from benchmark import benchmark_algorithms
from utils import cosd, sind, plot_all

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
# n = 4, sigma = 10e4
# Starting point x0 = [cos(70), sin(70), cos(70), sin(70)]
A = np.array([[5, 1, 0, 0.5],
              [1, 4, 0.5, 0],
              [0, 0.5, 3, 0],
              [0.5, 0, 0, 2]])
sigma = 10e4
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

# Save results to csv file
df = pd.DataFrame(results)
df.to_csv(f'data/{prob}.csv', index=False)

# plot the gradient norm history, the function value history, the total time, and the total iterations
plot_all(results, prob)