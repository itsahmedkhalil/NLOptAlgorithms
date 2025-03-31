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
    f_val = problem.function(x)
    grad = problem.gradient(x)
    
    while True:
        new_x = x - alpha * grad
        new_f_val = problem.function(new_x)
        
        if new_f_val <= f_val + options['c1'] * alpha * np.dot(grad, grad):
            if np.dot(problem.gradient(new_x), grad) >= options['c2'] * np.dot(grad, grad):
                break
        
        alpha *= options['tau']
    
    return alpha
