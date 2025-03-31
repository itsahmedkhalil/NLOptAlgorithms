import numpy as np
import time

def modified_newton(x0, problem, options, search):
    """Modified Newton's method with line search.
    
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
        grad_k = problem.gradient(x)
        grad_norm_hist.append(np.linalg.norm(grad_k))
        
        # Check convergence
        if np.linalg.norm(grad_k) < options['tol'] * max(np.linalg.norm(grad_0), 1):
            output = "Converged. Gradient norm is below tolerance."
            break

        hess_k = problem.hessian(x)

        smallest_eig = np.min(np.linalg.eigvals(hess_k))
        if smallest_eig > 0:
            delta_k = 0
        else:
            delta_k = -smallest_eig + options['beta']

        while True:
            try:
                np.linalg.cholesky(hess_k + delta_k * np.eye(hess_k.shape[0]))
                break
            except:
                delta_k = max(2 * delta_k, options['beta'])

        p_k = -np.linalg.solve(hess_k + delta_k * np.eye(hess_k.shape[0]), grad_k)

        alpha_k = search(x, problem, options)
        x = x + alpha_k * p_k

    return x, problem.function(x), itr, time.time() - time_start, output, grad_norm_hist
