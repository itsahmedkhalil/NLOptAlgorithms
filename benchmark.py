from search_methods import armijo_line_search, wolfe_line_search
import signal

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

        time_max = options['max_time']
        for tau in options['tau_list']:
            options['tau'] = tau

            print(f"Running {name} with Armijo, tau = {tau}.\n")
            # Set the time alarm for algorithm
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(time_max)
            try:
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
                signal.alarm(0)  # Disable the alarm

            except TimeoutException:
                print(f"Algorithm {name} with Armijo and tau = {tau} timed out after {time_max} seconds.\n")
                results[name + '-a'+ f'_{tau}tau'] = {
                'x': x,
                'f': f,
                'i': i,
                't': t,
                'o': f"Not converged. Exceeding maximum execution time {time_max}s",
                'h': h,
                'f_eval': f_eval,
                'g_eval': g_eval,
                'h_eval': h_eval
                }
                signal.alarm(0)
            

        for c2 in options['c2_list']:
            options['c2'] = c2

            print(f"Running {name} with Wolfe, c2 = {c2}.\n")
            #set alarm for algorithm
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(time_max)

            try:
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
                signal.alarm(0)  # Disable the alarm
            except TimeoutException:
                print(f"Algorithm {name} with Wolfe and c2 = {c2} timed out after {time_max} seconds.\n")
                results[name + '-w'+ f"_{c2}c2"] = {
                'x': x,
                'f': f,
                'i': i,
                't': t,
                'o': f"Not converged. Exceeding maximum execution time {time_max}s",
                'h': h,
                'f_eval': f_eval,
                'g_eval': g_eval,
                'h_eval': h_eval
                }
                signal.alarm(0)
            
    return results




'Running Time Check'
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()
