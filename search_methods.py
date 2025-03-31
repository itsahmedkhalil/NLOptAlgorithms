import numpy as np

def armijo_line_search(x, problem, options):
    """Armijo line search algorithm.
    
    Parameters:
    - x: Current point.
    - problem: Problem object with function, gradient, and hessian methods.
    - options: Dictionary with algorithm parameters.
    
    Returns:
    - alpha: Step size.
    """
    
    alpha = 1.0
    f_val = problem.function(x)
    grad = problem.gradient(x)
    
    while True:
        new_x = x - alpha * grad
        new_f_val = problem.function(new_x)
        
        if new_f_val <= f_val + options['c1'] * alpha * np.dot(grad, grad):
            break
        
        alpha *= options['tau']
    
    return alpha

def wolfe_line_search(x, problem, options):
    """Wolfe line search algorithm.
    
    Parameters:
    - x: Current point.
    - problem: Problem object with function, gradient, and hessian methods.
    - options: Dictionary with algorithm parameters.
    
    Returns:
    - alpha: Step size.
    """
    
    alpha = 1.0
    alpha_l = 0
    alpha_u = np.inf
    p_k = -problem.gradient(x)

    while True:
        phi_alpha = problem.function(x + alpha * p_k)
        phi_0 = problem.function(x)
        phi_prime_0 = np.dot(problem.gradient(x), p_k)

        if phi_alpha > phi_0 + options['c1'] * alpha * phi_prime_0:
            alpha_u = alpha
        else:
            phi_prime_alpha = np.dot(problem.gradient(x + alpha * p_k), p_k)
            if phi_prime_alpha < options['c2'] * phi_prime_0:
                alpha_l = alpha
            else:
                break

        if alpha_u < np.inf:
            alpha = (alpha_l + alpha_u) / 2
        else:
            alpha *= 2

    return alpha