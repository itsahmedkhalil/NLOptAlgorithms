import numpy as np
import time

def newton_cg(x0, problem, options, search):
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
    fx = np.zeros(max_iters)              # values of f(xk)       (1, max_iters)
    grad = np.zeros((len(x0),max_iters))        # values of \nablaf(xk) (n, max_iters)
    grad_norm_hist = np.zeros(max_iters)   # values of norm(\nablaf(xk))(1, max_iters)
    x_hist = np.zeros((len(x0), max_iters))   # (n, max_iters)
    alpha_hist = np.zeros(max_iters)  # (1, max_iters)
    
    x = x0.copy()
    
    grad_0_norm = np.linalg.norm(problem.gradient(x))
    output = "Failed. Maximum iterations reached. \n"    
    
    for itr in range(options['max_iter']):
        
        # Compute values at step itr (k)
        fx_k  = problem.function(x)
        grad_k = problem.gradient(x)
        hessian_k = problem.hessian(x)

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
            output = "Converged. Gradient norm is below tolerance. \n"
            break

        ## 2. Search step size
        alpha_k = search(x, problem, p_k, options)
        
        # Store alpha
        alpha_hist[itr] = alpha_k
        
        x = x + alpha_k * p_k

        print(f"{'iter':>6} {'f':>9} {'||grad||':>9} {'alpha':>9}")
        print(f"{itr:6d} {fx_k:9.2e} {grad_k_norm:9.2e} {alpha_k:9.2e}")
    print(output)
    return x, problem.function(x), itr, time.time() - time_start, output, grad_norm_hist


def get_search_direction(grad_k: np.ndarray, H_k: np.ndarray, options: dict)-> np.ndarray:
    """ This function computes the search direction according to the algorithm of choice
    
    Parameters:
    - gradk: gradient at time step k
    - Hk: Hessian or approx (BFGS, LBFGS, DFP) at time step k

    Returns:
    - pk: Search direction used for every iteration step"""

    ######## Implementation ########
    j = 0
    z = np.zeros_like(grad_k)
    r = grad_k.copy()
    d = -grad_k.copy()
    j_max = len(grad_k) + 10 

    while True:
        if d.T @ H_k @ d <= 0:
            if j == 0:
                pk = -grad_k
                return pk
            else:
                pk = z
                return pk
        else:
            alpha_j = np.dot(r,r) / (d.T @ H_k @ d)
            z1 = z + alpha_j * d
            r1 = r + alpha_j * H_k @ d

            if np.linalg.norm(r1) <= options['eta'] * np.linalg.norm(grad_k):
                pk = z1  
                return pk
                
            beta = np.dot(r1,r1) / np.dot(r,r)
            d1 = -r1 + beta * d
            d = d1
            z = z1
            r = r1
            j = j + 1

            if j > j_max:
                print('did not find available direction in Newton_CG')
                pk = z
                return pk
