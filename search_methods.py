import numpy as np
from typing import Callable

def armijo_line_search(xk: np.ndarray,
                       problem,
                       pk: np.ndarray,
                       options: dict) -> float:
    """Armijo line search algorithm.
    
    Parameters:
    - xk: Current point at time step k. (n,1)
    - problem: problem object with function, gradient, and Hessian.
    - pk: Current search direction (n,1)
    - options: Dictionary with algorithm parameters.
    
    Returns:
    - alpha: Step size.
    """
    
    alpha = 1.0

    # Get line search parameters
    c1  = options['c1']
    tau = options['tau']

    # Define just for readability
    f = problem.function
    fk = f(xk)
    grad_k = problem.gradient(xk)
    
    while f(xk + alpha * pk) > fk + c1 * alpha * grad_k.T @ pk:
        alpha *= tau
    
    return alpha

def wolfe_line_search(xk: np.ndarray,
                       problem,
                       pk: np.ndarray,
                       options: dict) -> float:
    """Wolfe line search algorithm.
    
    Parameters:
    - xk: Current point at time step k. (n,1)
    - problem: problem object with function, gradient, and Hessian.
    - pk: Current search direction (n,1)
    - options: Dictionary with algorithm parameters.
    
    Returns:
    - alpha: Step size.
    """
    
    # Initialize alpha and its bounds
    alpha = 1.0
    alpha_l = 0
    alpha_u = np.inf
    
    # Get line search parameters
    c1 = options['c1']
    c2 = options['c2']

    # Define just for readability
    f = problem.function
    grad_f = problem.gradient

    # Define phi(alpha) and its directional derivative phi'(alpha)
    phi = lambda alp: f(xk + alp * pk) 
    phi_prime = lambda alp: grad_f(xk + alp * pk).T  @ pk
    
    while True:

        if phi(alpha) > phi(0) + c1 * alpha * phi_prime(0):
            alpha_u = alpha
        else:
            if phi_prime(alpha) < c2 * phi_prime(0):
                alpha_l = alpha
            else:
                return alpha

        if alpha_u < np.inf:
            alpha = (alpha_l + alpha_u) / 2
        else:
            alpha *= 2
    