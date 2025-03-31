import numpy as np

def opt_alg(x0: np.ndarray, obj, options: dict) -> tuple[np.ndarray, str]:
    """
    Function for implementing your optimization algorithms.

    Parameters:
    ----------
    - x0 : np.ndarray
           The starting point.

    - obj : object
          Structure containing functions to evaluate objective and its derivatives:
              - obj.func(x): returns objective function value at x
              - obj.grad(x): returns gradient at x
              - obj.hess(x): returns Hessian at x

    - options : dict
         Dictionary containing algorithmic options. Expected keys:
             - 'method': optimization method to use ('steepest descent', 'Newton', 'modified Newton')
             - 'rho': backtracking parameter for line search
             - (PLEASE DESCRIBE YOUR OWN OPTIONS HERE AS WELL)

    Returns:
    -------
    - sol : np.ndarray
          The final solution (i.e., last iterate x).

    - status : str
          Message describing the outcome, e.g.,
          'optimal solution found', 'maximum iterations reached', etc.
    """

    # Use whatever quantities you need to implement the algorithm
    iter_counter = 0

    # Evaluate the objective, gradient, and Hessian
    obj0 = obj.func(x0)
    grad0 = obj.grad(x0)
    hess0 = obj.hess(x0)

    # Print headline — this is one example how you can use the options
    method = options['method']
    if method == 'steepest descent':
        # Steepest Descent
        print("\nRunning Steepest Descent Method\n")
    elif method == 'Newton':
        # Newton's Method
        print("\nRunning Newton's Method\n")
    elif method == 'modified Newton':
        # Modified Newton's Method
        print("\nRunning Newton's Method\n")
    else:
        raise ValueError("Invalid choice of method")

    # Algorithm parameters from options structure
    rho = options['rho']

    # HERE YOU NEED TO IMPLEMENT YOUR ALGORITHM
    print("\n\nHERE YOU NEED TO IMPLEMENT YOUR ALGORITHM\n\n")

    # Example of printing things nicely
    alpha = 0.6  # Of course, you should not use this value but the one from the algorithm
    print(f"{'iter':>6} {'f':>9} {'||grad||':>9} {'alpha':>9}")
    print(f"{iter_counter:6d} {obj0:9.2e} {np.linalg.norm(grad0):9.2e} {alpha:9.2e}")

    # Update your iterates
    # Repeat till the convergence criteria is met

    # Final result
    sol = x0

    # Status message
    status = 'optimal solution found'  # Or other messages, depending on the outcome

    return sol, status
