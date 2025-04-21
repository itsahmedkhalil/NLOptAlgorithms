import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import re

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
        'w':    '--'
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
    max_iters_exc = 0
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)
        if base_name != 'GD':
            # exclude DFP only for problem 12 or problem 7
            if base_name != 'DFP' and (problem_name == 'Problem12' or problem_name == 'Problem7'):
                max_iters_exc = max(max_iters_exc, result['i'])
        max_iters_all = max(max_iters_all, result['i'])

    # Zoomed-in iteration count
    zoom_iterations = max(max_iters_exc, 10)
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
    max_iters_exc = 0
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)
        if base_name != 'GD':
            # exclude DFP only for problem 12 or problem 7
            if base_name != 'DFP' and (problem_name == 'Problem12' or problem_name == 'Problem7'):
                max_iters_exc = max(max_iters_exc, result['i'])
        max_iters_all = max(max_iters_all, result['i'])

    zoom_iterations = max(max_iters_exc, 10)
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
    plt.yscale('symlog')
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
    plt.yscale('symlog')
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
        # dashed bar for 'w' variant
        if variant == 'w':
            ax_time.bar(name, result['t'], color=color, hatch='//')
        else:
            ax_time.bar(name, result['t'], color=color)

    ax_time.set_title(f'{problem_name} - Total Time')
    ax_time.set_xlabel('Algorithms')
    ax_time.set_ylabel('Time (seconds)')
    ax_time.set_yscale('log')
    ax_time.tick_params(axis='x', rotation=45)

    # Right subplot: Total iterations
    ax_iter = axes[1]
    for name, result in results.items():
        base_name, variant = parse_algorithm_name(name)
        color = color_map.get(base_name, 'black')
        # dashed bar for 'w' variant
        if variant == 'w':
            ax_iter.bar(name, result['i'], color=color, hatch='//')
        else:
            ax_iter.bar(name, result['i'], color=color)

    ax_iter.set_title(f'{problem_name} - Total Iterations')
    ax_iter.set_xlabel('Algorithms')
    ax_iter.set_ylabel('Number of Iterations')
    ax_iter.set_yscale('log')
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


def save_data(results, prob_id):
    """Write results to CSV / markdown, then refresh the README."""
    df = pd.DataFrame(results).T

    df.to_csv(f"data/{prob_id}.csv", index=False)
    df = df.drop(columns=['x', 'f', 'h'])
    df.columns = ['Iters', 'Time', 'Convergence',
                  'Func Evals', 'Grad Evals', 'Hess Evals']
    df.to_markdown(f"data/{prob_id}.md",  index=True)

    update_readme("README.md", prob_id)


def extract_table(md_path: str) -> str:
    """Return the *first* markdown table found in a file."""
    with open(md_path, "r") as fh:
        lines = fh.readlines()

    tbl = []
    for line in lines:
        if "|" in line:
            tbl.append(line)
        elif tbl:           # we were in a table and hit a blank line
            break
    return "".join(tbl).rstrip() + "\n"     # keep a trailing newline

def update_readme(readme_path: str, pid: int):
    """Replace the block between the BEGIN/END markers for one problem."""
    readme = Path(readme_path).read_text()

    start = f"<!-- BEGIN_{pid}_TABLE -->"
    end   = f"<!-- END_{pid}_TABLE -->"

    pattern = re.compile(
        rf"{re.escape(start)}.*?{re.escape(end)}",
        flags=re.DOTALL,
    )

    table_md = extract_table(f"data/{pid}.md")
    replacement = f"{start}\n{table_md}{end}"

    # If the problem block already exists, overwrite it;
    # otherwise, just append a new block at the end of the file.
    if pattern.search(readme):
        readme = pattern.sub(replacement, readme)
    else:
        readme = readme.rstrip() + "\n\n" + replacement

    Path(readme_path).write_text(readme)


def plot_function_value_c2_tau(results, problem_name):
    """
    Plot the function value history for the different c2 and tau.
    """
    algorithm_names = ['GD', 'MN', 'BFGS', 'L-BFGS', 'DFP', 'NCG']
    plt.figure(figsize=(14, 7))

    
    for i, algo_name in enumerate(algorithm_names):
        plt.subplot(2,3,i+1)
        plt.title(algo_name)

        max_iter = 10
        for name, result in results.items():
            
            if name.startswith(algo_name):
                # wolf use -- line style, armijo use - line style
                if '-w' in name:
                    line_style = '--'
                    lable_name = name.split('_')[1]+'_w'
                elif '-a' in name:
                    line_style = '-'
                    lable_name = name.split('_')[1]+'_a'
                

                plt.plot(result['f'], label=lable_name, linestyle=line_style, alpha=0.5)
                max_iter = max(max_iter, result['i'])

        plt.yscale('symlog')
        plt.ylabel(r'Function Value, $f(x_k)$')
        plt.xlabel('Iterations')
        plt.legend(loc='best', fontsize=6)
        plt.grid(True)

        if max_iter <= 10:
            plt.xlim(0, 10)
            plt.xticks(range(0, 11, 2))
        else:
            plt.xlim(0, max_iter)
 
    plt.suptitle(f'{problem_name} - Function Value with Different c2 and tau', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'figures/{problem_name}_c2_tau_fx.png', dpi=150)
    plt.show()

# only show the first 10 iterations value
def plot_function_value_c2_tau_zoom(results, problem_name):
    """
    Plot the function value history for the different c2 and tau.
    """
    algorithm_names = ['GD', 'MN', 'BFGS', 'L-BFGS', 'DFP', 'NCG']
    plt.figure(figsize=(14,7))

    
    for i, algo_name in enumerate(algorithm_names):
        plt.subplot(2,3,i+1)
        plt.title(algo_name)

        for name, result in results.items():
            
            if name.startswith(algo_name):
                # wolf use -- line style, armijo use - line style
                if '-w' in name:
                    line_style = '--'
                    lable_name = name.split('_')[1]+'_w'
                elif '-a' in name:
                    line_style = '-'
                    lable_name = name.split('_')[1]+'_a'
                

                plt.plot(result['f'], label=lable_name, linestyle=line_style, alpha=0.5)

        plt.yscale('symlog')
        plt.ylabel(r'Function Value, $f(x_k)$')
        plt.xlabel('Iterations')
        plt.legend(loc='best', fontsize=6)
        plt.grid(True)
        plt.xlim(0, 10)
        plt.xticks(range(0, 11, 2))

 
    plt.suptitle(f'{problem_name} - Function Value with Different c2 and tau (zoom)', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'figures/{problem_name}_c2_tau_fx_zoom.png', dpi=150)
    plt.show()