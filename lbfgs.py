import numpy as np
import time

def lbfgs(x0, problem, options, search):
    """ L-BFGS algorithm with line search.
    
    Parameters:
    - x0: Initial point.
    - problem: Problem object with function, gradient, and hessian methods.
    - options: Dictionary with algorithm parameters.
    - search: Search method for line search.
    
    Returns:
    - x: Solution.
    - f_val: Function value at the solution.
    """

    print("Running L-BFGS.\n")
    time_start = time.time()

    # Get Algorithm parameters
    max_iters = options['max_iter']
    tol = options['tol']
    eps = options['epsilon_min']
    gamma_k = options['gamma_init']

    m = min(options['m'], len(x0)) 

    # Initialize numpy arrays to store values
    fx = np.zeros(max_iters)              # values of f(xk)       (1, max_iters)
    grad = np.zeros((len(x0),max_iters))        # values of \nablaf(xk) (n, max_iters)
    grad_norm_hist = np.zeros(max_iters)   # values of norm(\nablaf(xk))(1, max_iters)
    x_hist = np.zeros((len(x0), max_iters))   # (n, max_iters)
    alpha_hist = np.zeros(max_iters)  # (1, max_iters)
    
    s = []
    y = []

    x = x0.copy()

    grad_0_norm = np.linalg.norm(problem.gradient(x))
    output = "Failed. Maximum iterations reached."
    hessian_0 = np.eye(len(x))

    f_evals = 0
    g_evals = 0
    h_evals = 0

    for itr in range(max_iters):
        # Compute values at step itr (k)
        fx_k  = problem.function(x)
        f_evals += 1
        grad_k = problem.gradient(x)
        g_evals += 1

        # Store values
        fx[itr] = fx_k
        grad[:, itr] = grad_k

        # Store values for information purposes
        x_hist[:,itr] = x
        grad_k_norm = np.linalg.norm(grad_k)
        grad_norm_hist[itr] = grad_k_norm

        ## 1. Compute search direction.
        hessian_k = gamma_k * hessian_0

        p_k = -two_loop_recursion(hessian_k, grad_k, s, y)

        # Check convergence
        if grad_k_norm < tol * max(grad_0_norm, 1):
            output = "Converged. Gradient norm is below tolerance."
            break

        # 2. Perform line search to find alpha
        alpha_k, f_evals, g_evals = search(x, problem, p_k, f_evals, g_evals, options)
        
        alpha_hist[itr] = alpha_k

        x = x + alpha_k * p_k

        s_k = alpha_k * p_k
        y_k = problem.gradient(x) - grad_k
        g_evals += 1

        if y_k @ s_k > eps * np.linalg.norm(y_k) * np.linalg.norm(s_k):
            # Update memory
            if len(s) >= m:
                s.pop(0)
                y.pop(0)

            s.append(s_k)
            y.append(y_k)

        gamma_k = (s_k @ y_k) / (y_k @ y_k) if y_k @ y_k > 1e-15 else 1.0
        print(f"{'iter':>6} {'f':>9} {'||grad||':>9} {'alpha':>9}")
        print(f"{itr:6d} {fx_k:9.2e} {grad_k_norm:9.2e} {alpha_k:9.2e}")
    print(output) 
    return x_hist, fx, itr, time.time() - time_start, output, grad_norm_hist, f_evals, g_evals, h_evals

def two_loop_recursion(H0_k, gradk, sks, yks):

    q = gradk.copy()
    m = len(sks)
    p_l = np.zeros(m)
    alpha = np.zeros(m)

    for l in range(m-1, -1, -1):
        p_l[l] = 1/(yks[l].T @ sks[l])
        alpha[l] = p_l[l] * (sks[l].T @ q)
        q -= alpha[l] * yks[l]

    r = H0_k @ q
    for j in range(m):
        beta = p_l[j] * (yks[j].T @ r)
        r += sks[j] * (alpha[j] - beta)
    return r