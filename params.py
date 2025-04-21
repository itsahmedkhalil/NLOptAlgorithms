import numpy as np
def initialize() -> dict:

    """This function sets some default values for parameters 
     used in the algorithm 
     
     Returns:
     - options: Dictionary with all parameters needed for a given algorithm
     """

    options = {}
    # Set parameters
    options['c1'] = 1e-4
    options['c2'] = 0.9
    options['max_iter'] = int(1e3)
    options['epsilon_min'] = 1e-8
    options['tol'] = 1e-6
    options['eta'] = 0.01
    options['tau'] = 0.9
    options['beta'] = 1e-4
    options['gamma_init'] = 1
    options['m'] = 10
    options['max_time'] = 15


    # leave np.array([]) if you don't want to perform multiple values
    options['tau_list'] = np.array([0.1, 0.3, 0.9]) # 0 < tau < 1
    options['c2_list'] = np.array([0.5, 0.6, 0.7, 0.8, 0.9])  # 0 < c1 < c2 < 1
    
    return options