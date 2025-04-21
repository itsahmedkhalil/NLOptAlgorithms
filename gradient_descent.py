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
    print("Running gradient descent.\n")
    time_start = time.time()
    
    # Get Algorithm parameters
    max_iters = options['max_iter']
    tol = options['tol']

    # Initialize numpy arrays to store values
    #fx = np.zeros(max_iters)              # values of f(xk)       (1, max_iters)
    fx = np.array([])
    grad = np.zeros((len(x0),max_iters))        # values of \nablaf(xk) (n, max_iters)
    # grad_norm_hist = np.zeros(max_iters)   # values of norm(\nablaf(xk))(1, max_iters)
    grad_norm_hist = np.array([])   # values of norm(\nablaf(xk))(1, max_iters)
    x_hist = np.zeros((len(x0), max_iters))   # (n, max_iters)
    alpha_hist = np.zeros(max_iters)  # (1, max_iters)

    f_evals = 0
    g_evals = 0
    h_evals = 0

    x = x0.copy()
    
    grad_0_norm = np.linalg.norm(problem.gradient(x))
    output = "Failed. Maximum iterations reached. \n"    
    
    for itr in range(options['max_iter']):
        
        # Compute values at step itr (k)
        fx_k  = problem.function(x)
        f_evals += 1
        grad_k = problem.gradient(x)
        g_evals += 1

        # Store values
        # fx[itr] = fx_k
        fx = np.append(fx, fx_k)  # Append the function value
        grad[:, itr] = grad_k

        # Store values for information purposes
        x_hist[:,itr] = x
        grad_k_norm = np.linalg.norm(grad_k)
        #grad_norm_hist[itr] = grad_k_norm
        grad_norm_hist = np.append(grad_norm_hist, grad_k_norm)

        ## 1. Compute search direction.
        p_k = get_search_direction(grad_k, options)
        
        # Check convergence
        if grad_k_norm < tol * max(grad_0_norm, 1):
            output = "Converged. Gradient norm is below tolerance."
            break

        ## 2. Search step size
        alpha_k, f_evals, g_evals = search(x, problem, p_k, f_evals, g_evals, options)
        
        # Store alpha
        alpha_hist[itr] = alpha_k
        
        x = x + alpha_k * p_k

        print(f"{'iter':>6} {'f':>9} {'||grad||':>9} {'alpha':>9}")
        print(f"{itr:6d} {fx_k:9.2e} {grad_k_norm:9.2e} {alpha_k:9.2e}")
    
    print(output)
    
    return x_hist, fx, itr, time.time() - time_start, output, grad_norm_hist, f_evals, g_evals, h_evals

def get_search_direction(grad_k: np.ndarray, options: dict)-> np.ndarray:
    """ This function computes the search direction according to the algorithm of choice
    
    Parameters:
    - gradk: gradient at time step k
    - Hk: Hessian or approx (BFGS, LBFGS, DFP) at time step k

    Returns:
    - pk: Search direction used for every iteration step"""

    ######## Implementation ########
    return -grad_k
