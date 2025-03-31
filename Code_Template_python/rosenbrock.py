import numpy as np

def rosenbrock_func(x: np.ndarray) -> float:
    """
    The Rosenbrock function.

    Parameters
    ----------
    x : np.ndarray
        Input vector of shape (n,)

    Returns
    -------
    float
        The Rosenbrock function value at x
    """
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def rosenbrock_grad(x: np.ndarray) -> np.ndarray:
    """ This function computes the gradient of the 
        Rosenbrock Function

    Parameters
    ----------
    x : np.ndarray
        Input vector (n,1)

    Returns
    -------
    grad : np.ndarray
           Rosenbrock gradient (n,1)"""

    n=len(x)
    ### You need to implement this! 
    ### Compute the analytical gradient and implement the formula.
    grad=np.zeros(n,1)
    return grad



def rosenbrock_hessian(x: np.ndarray) -> np.ndarray:
    """ This function computes the Hessian of the Rosenbrock
    Function

    Parameters
    ----------
    x : np.ndarray
        Input vector (n,1)
    
    Returns
    -------
    H : np.ndarray
        Rosenbrock Hessian (n,n)"""
    
    n=len(x)
    ### You need to implement this!
    ### Compute the analytical Hessian and implement the formula.
    
    H = np.zeros(n,n); ### % This is wrong!
    return H