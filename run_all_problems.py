import os
import subprocess
import sys

# List of problem scripts to run
problem_scripts = [
    'problem1.py',
    'problem2.py',
    # 'problem3.py',
    # 'problem4.py',
    'problem5.py',
    'problem6.py',
    'problem7.py',
    'problem8.py',
    'problem9.py',
    'problem10.py',
    'problem11.py',
    'problem12.py'
]


# Run each problem script
for script in problem_scripts:
    print(f"Running {script}...")
    try:
        subprocess.run([sys.executable, script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script}: {e}")
    else:
        print(f"{script} completed successfully.")
    print("-" * 40)
    print()
