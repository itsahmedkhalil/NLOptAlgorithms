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
    print("Running DFP.\n")
    time_start = time.time()
    
    # Get Algorithm parameters
    max_iters = options['max_iter']
    tol = options['tol']
    eps = options['epsilon_min']

    # Initialize numpy arrays to store values
    fx = np.zeros(max_iters)              # values of f(xk)       (1, max_iters)
    grad = np.zeros((len(x0),max_iters))        # values of \nablaf(xk) (n, max_iters)
    grad_norm_hist = np.zeros(max_iters)   # values of norm(\nablaf(xk))(1, max_iters)
    x_hist = np.zeros((len(x0), max_iters))   # (n, max_iters)
    alpha_hist = np.zeros(max_iters)  # (1, max_iters)
    # s = []               # (L-BFGS)
    # y = []               # (L-BFGS)
    
    x = x0.copy()
    
    grad_0_norm = np.linalg.norm(problem.gradient(x))
    output = "Failed. Maximum iterations reached."     
    
    hessian_k = np.eye(len(x))

    for itr in range(options['max_iter']):
        # Compute values at step itr (k)
        fx_k  = problem.function(x)
        grad_k = problem.gradient(x)

        # Store values
        fx[itr] = fx_k
        grad[:, itr] = grad_k

        # Store values for information purposes
        x_hist[:,itr] = x
        grad_k_norm = np.linalg.norm(grad_k)
        grad_norm_hist[itr] = grad_k_norm

        ## 1. Compute search direction. The hessian at time step k.
        ## Note: On newton method approximations -> hessiank NOT problem.hessian(x)
        p_k = get_search_direction(grad_k, hessian_k, options)

        # Check convergence
        if grad_k_norm < tol * max(grad_0_norm, 1):
            output = "Converged. Gradient norm is below tolerance."
            break

        ## 2. Search step size
        alpha_k = search(x, problem, p_k, options)
        
        # Store alpha
        alpha_hist[itr] = alpha_k

        x = x + alpha_k * p_k

        s_k = alpha_k * p_k
        y_k = problem.gradient(x) - grad_k

        if y_k @ s_k > eps * np.linalg.norm(y_k) * np.linalg.norm(s_k):
            hessian_k = dfp_update(s_k, y_k, hessian_k)

        print(f"{'iter':>6} {'f':>9} {'||grad||':>9} {'alpha':>9}")
        print(f"{itr:6d} {fx_k:9.2e} {grad_k_norm:9.2e} {alpha_k:9.2e}")
    print(output)        
    return x, problem.function(x), itr, time.time() - time_start, output, grad_norm_hist

def get_search_direction(grad_k: np.ndarray, Hk: np.ndarray, options: dict)-> np.ndarray:
    """ This function computes the search direction according to the algorithm of choice
    
    Parameters:
    - gradk: gradient at time step k
    - Hk: Hessian or approx (BFGS, LBFGS, DFP) at time step k

    Returns:
    - pk: Search direction used for every iteration step"""

    ######## Implementation ########

    ## Hk is inverse Hessian
    return -Hk @ grad_k

def dfp_update(s_k, y_k, H_k):
    """ DFP equation for updating the approximate inverse Hessian
    
    Parameters:
    - s_k:  Something about the secant equation dont remember
    - y_k:  same

    Returns:
    - H_kp1: Approximate Hessian Inverse at time step k + 1
    """
    rho_k = 1.0 / (y_k @ s_k)
    I = np.eye(len(s_k))
    H_kp1 = H_k + np.outer(s_k, s_k) * rho_k - (H_k @ np.outer(y_k, y_k) @ H_k) / (y_k @ H_k @ y_k)
    return H_kp1

