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

