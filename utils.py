import numpy as np
import matplotlib.pyplot as plt

def plot_styles():
    """
    Define a color map for the algorithms.
    """

    color_map = {
        'GD':       'C0',
        'MN':       'C1',
        'BFGS':     'C2',
        'L-BFGS':   'C3',
        'DFP':      'C4',
        'NCG':      'C5'
    }

    line_styles = {
        'a':    '-',
        'W':    '--'
    }

    return color_map, line_styles


# Set sine function from radians to degrees
def sind(degrees):
    return np.sin(np.deg2rad(degrees))

# Set cosine function from radians to degrees
def cosd(degrees):
    return np.cos(np.deg2rad(degrees))

def Q_generate(n: int, k: float):
    eigenvalues = np.linspace(1, k, n)
    Q = np.random.randn(n, n) 
    Q, _ = np.linalg.qr(Q) # QR Decomposition, Q is orthogonal
    Q = Q @ np.diag(eigenvalues) @ Q.T
    return Q

def parse_algorithm_name(name):
    """
    Separate the base algorithm name from the trailing 'W' variant.
    If 'W' is present at the end of the name, we assume it indicates
    the second line-search variant (dashed line).

    Returns (base_name, variant_indicator):
      - base_name: e.g. "Gradient Descent", "BFGS", etc.
      - variant_indicator: 'W' if it ends with 'W', else 'NoW'
    """
    if name.endswith('-w'):
        return name[:-2].strip(), 'w'
    elif name.endswith('-a'):
        return name[:-2].strip(), 'a'


def plot_gradient_norm(results, problem_name, plot_styles=plot_styles):
    """
    Plot the gradient norm history for the 12 algorithms:
      - 6 base algorithms (GD, Modified Newton, BFGS, L-BFGS, DFP, Newton CG)
      - 6 'W' variants
    Using color to differentiate the base algorithm, and line style + linewidth
    to differentiate 'W' vs. non-'W'.
    """

    color_map, line_styles = plot_styles()

    # Find iteration limits
    max_iters_all = 0
    max_iters_exc_gd = 0
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)
        if base_name != 'Gradient Descent':
            # exclude DFP only for problem 12 or problem 7
            if base_name != 'DFP' and (problem_name == 'Problem12' or problem_name == 'Problem7'):
                max_iters_exc_gd = max(max_iters_exc_gd, result['i'])
        max_iters_all = max(max_iters_all, result['i'])

    # Zoomed-in iteration count
    zoom_iterations = max(max_iters_exc_gd, 10)
    max_iters_all   = max(max_iters_all, 10)

    plt.figure(figsize=(10, 5))

    # --- Left subplot: full iteration range ---
    plt.subplot(1, 2, 1)
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)

        color = color_map.get(base_name, 'black')
        ls    = line_styles.get(variant, '-')

        # Make dashed lines slightly thicker
        if variant == 'W':
            lw = 2.5  # thicker line for dashed
        else:
            lw = 2.0

        plt.plot(result['h'][:max_iters_all],
                 label=name,
                 color=color,
                 linestyle=ls,
                 linewidth=lw,
                 alpha=0.8)
    plt.yscale('log')
    plt.xlabel('Iterations')
    plt.ylabel(r'Gradient Norm, $\|\nabla f(x_k)\|$')
    plt.title(f'{problem_name} - Gradient Norm (All Iterations)')
    plt.legend(loc='best', fontsize=8)
    plt.grid()

    # --- Right subplot: zoomed-in view of first few iterations ---
    plt.subplot(1, 2, 2)
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)

        color = color_map.get(base_name, 'black')
        ls    = line_styles.get(variant, '-')
        if variant == 'W':
            lw = 2.5
        else:
            lw = 2.0

        plt.plot(result['h'][:zoom_iterations],
                 label=name,
                 color=color,
                 linestyle=ls,
                 linewidth=lw,
                 alpha=0.8)
    plt.yscale('log')
    plt.xlabel('Iterations')
    plt.ylabel(r'Gradient Norm, $\|\nabla f(x_k)\|$')
    plt.title(f'{problem_name} - Gradient Norm (First {zoom_iterations} Iters)')
    plt.legend(loc='best', fontsize=8)
    plt.grid()

    plt.tight_layout()
    plt.savefig(f'figures/{problem_name}_grad_norm.png', dpi=150)
    plt.show()


def plot_function_value(results, problem_name, plot_styles=plot_styles):
    """
    Plot the function value history for the 12 algorithms.
    Similar approach: same color map, same line style distinctions.
    """
    color_map, line_styles = plot_styles()

    max_iters_all = 0
    max_iters_exc_gd = 0
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)
        if base_name != 'Gradient Descent':
            # exclude DFP only for problem 12 or problem 7
            if base_name != 'DFP' and (problem_name == 'Problem12' or problem_name == 'Problem7'):
                max_iters_exc_gd = max(max_iters_exc_gd, result['i'])
        max_iters_all = max(max_iters_all, result['i'])

    zoom_iterations = max(max_iters_exc_gd, 10)
    max_iters_all   = max(max_iters_all, 10)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)

        color = color_map.get(base_name, 'black')
        ls    = line_styles.get(variant, '-')
        lw    = 2.5 if variant == 'W' else 2.0

        plt.plot(result['f'][:max_iters_all],
                 label=name,
                 color=color,
                 linestyle=ls,
                 linewidth=lw,
                 alpha=0.8)
    plt.yscale('log')
    plt.xlabel('Iterations')
    plt.ylabel(r'Function Value, $f(x_k)$')
    plt.title(f'{problem_name} - Function Value (All Iterations)')
    plt.legend(loc='best', fontsize=8)
    plt.grid()

    # --- Right subplot: zoomed-in view ---
    plt.subplot(1, 2, 2)
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)

        color = color_map.get(base_name, 'black')
        ls    = line_styles.get(variant, '-')
        lw    = 2.5 if variant == 'W' else 2.0

        plt.plot(result['f'][:zoom_iterations],
                 label=name,
                 color=color,
                 linestyle=ls,
                 linewidth=lw,
                 alpha=0.8)
    plt.yscale('log')
    plt.xlabel('Iterations')
    plt.ylabel(r'Function Value, $f(x_k)$')
    plt.title(f'{problem_name} - Function Value (First {zoom_iterations} Iters)')
    plt.legend(loc='best', fontsize=8)
    plt.grid()

    plt.tight_layout()
    plt.savefig(f'figures/{problem_name}_function_value.png', dpi=150)
    plt.show()


def plot_time_iterations(results, problem_name, plot_styles=plot_styles):
    """
    Plot the total time taken and the total number of iterations for each algorithm,
    side by side in one figure.
    """
    color_map, line_styles = plot_styles()

    # Create a figure with 2 subplots (side by side)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Left subplot: Total time
    ax_time = axes[0]
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)
        color = color_map.get(base_name, 'black')
        ax_time.bar(name, result['t'], color=color)

    ax_time.set_title(f'{problem_name} - Total Time')
    ax_time.set_xlabel('Algorithms')
    ax_time.set_ylabel('Time (seconds)')
    ax_time.tick_params(axis='x', rotation=45)

    # Right subplot: Total iterations
    ax_iter = axes[1]
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)
        color = color_map.get(base_name, 'black')
        ax_iter.bar(name, result['i'], color=color)

    ax_iter.set_title(f'{problem_name} - Total Iterations')
    ax_iter.set_xlabel('Algorithms')
    ax_iter.set_ylabel('Number of Iterations')
    ax_iter.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.savefig(f'figures/{problem_name}_time_iterations_side_by_side.png', dpi=150)
    plt.show()

def plot_all(results, problem_name):
    """
    Plot all relevant information for the algorithms:
      - Gradient Norm
      - Function Value
      - Total Time
      - Total Iterations
    """
    plot_gradient_norm(results, problem_name)
    plot_function_value(results, problem_name)
    plot_time_iterations(results, problem_name)