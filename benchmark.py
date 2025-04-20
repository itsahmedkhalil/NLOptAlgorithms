from search_methods import armijo_line_search, wolfe_line_search

def benchmark_algorithms(algorithms, problem, x0, options):

    """
    Benchmark different optimization algorithms on a given problem.

    Parameters:
    - algorithms: List of tuples (algorithm_name, algorithm_function).
    - problem: Problem object with function, gradient, and Hessian.
    - x0: Initial guess for the optimization.
    - options: Dictionary with algorithm parameters.

    Returns:
    - results: Dictionary with results for each algorithm.
    """

    results = {}

    for name, algorithm in algorithms:
        print(f"Running {name} with Armijo.\n")
        x, f, i, t, o, h, f_eval, g_eval, h_eval = algorithm(x0, problem, options, armijo_line_search)
        results[name +'-a'] = {
            'x': x,
            'f': f,
            'i': i,
            't': t,
            'o': o,
            'h': h,
            'f_eval': f_eval,
            'g_eval': g_eval,
            'h_eval': h_eval
        }

        print(f"Running {name} with Wolfe.\n")
        x, f, i, t, o, h, f_eval, g_eval, h_eval = algorithm(x0, problem, options, wolfe_line_search)
        results[name + '-w'] = {
            'x': x,
            'f': f,
            'i': i,
            't': t,
            'o': o,
            'h': h,
            'f_eval': f_eval,
            'g_eval': g_eval,
            'h_eval': h_eval
        }

    return results


def benchmark_algorithms_c2_tau(algorithms, problem, x0, options):

    """
    Benchmark different optimization algorithms on a given problem.

    Parameters:
    - algorithms: List of tuples (algorithm_name, algorithm_function).
    - problem: Problem object with function, gradient, and Hessian.
    - x0: Initial guess for the optimization.
    - options: Dictionary with algorithm parameters.

    Returns:
    - results: Dictionary with results for each algorithm.
    """

    results = {}

    for name, algorithm in algorithms:


        for tau in options['tau_list']:
            options['tau'] = tau

            print(f"Running {name} with Armijo, tau = {tau}.\n")
            x, f, i, t, o, h, f_eval, g_eval, h_eval = algorithm(x0, problem, options, armijo_line_search)
            results[name + '-a'+ f'_{tau}tau'] = {
            'x': x,
            'f': f,
            'i': i,
            't': t,
            'o': o,
            'h': h,
            'f_eval': f_eval,
            'g_eval': g_eval,
            'h_eval': h_eval
            }
            

        for c2 in options['c2_list']:
            options['c2'] = c2

            print(f"Running {name} with Wolfe, c2 = {c2}.\n")
            x, f, i, t, o, h, f_eval, g_eval, h_eval = algorithm(x0, problem, options, wolfe_line_search)
            results[name + '-w'+ f"_{c2}c2"] = {
            'x': x,
            'f': f,
            'i': i,
            't': t,
            'o': o,
            'h': h,
            'f_eval': f_eval,
            'g_eval': g_eval,
            'h_eval': h_eval
            }
            

    return results
