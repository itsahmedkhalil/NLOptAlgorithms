import numpy as np

def initialize() -> dict:

    """This function sets some default values for parameters 
     used in the algorithm 
     
     Returns:
     - options: Dictionary with all parameters needed for a given algorithm
     """

    options = {}
    # Set parameters
    options['c1'] = 10**-4
    options['c2'] = 0.9
    options['max_iter'] = 100
    options['epsilon_min'] = 10e-8
    options['tol'] = 10e-8
    options['eta'] = 0.01
    options['tau'] = 0.5
    options['beta'] = 10e-4
    
    return options