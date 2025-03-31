import numpy as np
import time

def dfp(x0, problem, options, search):
    """DFP algorithm with line search.
    
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
    
    H_k = np.eye(len(x))

    for itr in range(options['max_iter']):
        grad_k = problem.gradient(x)
        grad_norm_hist.append(np.linalg.norm(grad_k))

        # Check convergence
        if np.linalg.norm(grad_k) < options['tol'] * max(np.linalg.norm(grad_0), 1):
            output = "Converged. Gradient norm is below tolerance."
            break

        p_k = -H_k @ grad_k

        alpha_k = search(x, problem, options)
        x = x + alpha_k * p_k

        s_k = alpha_k * p_k
        y_k = problem.gradient(x) - grad_k

        if y_k @ s_k > options['epsilon_min'] * np.linalg.norm(y_k) * np.linalg.norm(s_k):
            H_k = H_k - np.outer(H_k @ y_k, H_k @ y_k) / np.dot(y_k, H_k @ y_k) + np.outer(s_k, s_k) / np.dot(y_k, s_k) 

    return x, problem.function(x), itr, time.time() - time_start, output, grad_norm_hist