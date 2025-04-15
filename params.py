import numpy as np

def initialize() -> dict:

    """This function sets some default values for parameters 
     used in the algorithm 
     
     Returns:
     - options: Dictionary with all parameters needed for a given algorithm
     """

    options = {}
    # Set parameters
    options['c1'] = 1e-4 == 10**(-4)
    options['c2'] = 0.9
    options['max_iter'] = 10000
    options['epsilon_min'] = 10e-8
    options['tol'] = 10e-8
    options['eta'] = 0.01
    options['tau'] = 0.4
    options['beta'] = 10e-4
    options['gamma_init'] = 1
    options['m'] = 10
    
    return options