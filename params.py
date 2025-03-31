import numpy as np

def initialize(c1, c2, max_iter, epsilon_min, tol, eta, tau, beta) -> dict:

    """This function sets some default values for parameters 
     used in the algorithm 
     
     Returns:
     - options: Dictionary with all parameters needed for a given algorithm
     """

    options = {}

    options['c1'] = c1
    options['c2'] = c2
    options['max_iter'] = max_iter
    options['epsilon_min'] = epsilon_min
    options['tol'] = tol
    options['eta'] = eta
    options['tau'] = tau
    options['beta'] = beta
    
    return options