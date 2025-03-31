import numpy as np
from typing import Callable

def armijo_backtracking(xk: np.ndarray,
                        fk: float,
                        gradk: np.ndarray,
                        pk: np.ndarray,
                        alpha_init: float,
                        obj_func: Callable[[np.ndarray], float],
                        options: dict) -> float:
    """
    Armijo backtracking line search.

    This function computes the steplength parameter alpha 

    Parameters:
    - xk: current point at time step k
    - fk: value of f(xk)
    - gradk: value of gradient of f(xk)
    - pk: search direction
    - alpha_init: initial step size
    - obj_func: objective function used to compute f(xk+1)
    - options: dictionary with the defined parameters for the problem

    Returns:
    - alpha: Step length satisfying Armijo condition
    """

    ### This is just a reference file
    ### You need to give all the necessary input parameters ####
    
    ### You can get the parameters used in the Armijobacktracking 
    ### linesearch
    c1 = options['c1']

    ### You need to write your code here.  
    alpha = 0*c1; # This is wrong!

    return alpha



