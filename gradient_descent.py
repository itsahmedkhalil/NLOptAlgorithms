import numpy as np
import time

def gradient_descent(x0, problem, options, search):
    """Gradient descent algorithm with line search.
    
    Parameters:
    - x0: Initial point.
    - problem: Problem object with function, gradient, and hessian methods.
    - options: Dictionary with algorithm parameters.
    - search: Search method for line search.
    
    Returns:
    - x: Solution.
    - f_val: Function value at the solution.
    """

    time_start = time.time()

    x = x0.copy()
    grad_0 = problem.gradient(x)
    grad_norm_hist = []
    output = "Failed. Maximum iterations reached."    
    
    for itr in range(options['max_iter']):
        p_k = -problem.gradient(x)
        grad_norm_hist.append(np.linalg.norm(p_k))
        
        # Check convergence
        if np.linalg.norm(p_k) < options['tol'] * max(np.linalg.norm(grad_0), 1):
            output = "Converged. Gradient norm is below tolerance."
            break

        alpha = search(x, problem, options)
        x = x + alpha * p_k

    return x, problem.function(x), itr, time.time() - time_start, output, grad_norm_hist
