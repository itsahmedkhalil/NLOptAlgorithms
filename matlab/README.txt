***Main functions***

RunAssingment3: Runs all problems with all methods. There is an array in the beginning that can be used to select individual problems.

% Problem #1  2  3  4  5  6  7  8  9 10
problem = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]; % Just input 1 or 0 to activate/deactivate a problem 
 
**Rosenbrock**

rosenbrockfunc(x): Evaluates f(x) where f is the rosenbrock function.
rosenbrockgrad(x): Evaluates the gradient of f (rosenbrock).
rosenbrockhess(x): Evaluates the hessian of f(rosenbrock).

**Beale**

BealeFunc(x): Evaluates f(x) where f is the Beale function.
Bealegrad(x): Evaluates the gradient of f (Beale).
Bealehess(x): Evaluates the hessian of f (Beale).

*** Problem 10 function ***

LastFunc(x): Evaluates f(x) where f is the Last function.
LastGrad(x): Evaluates the gradient of f (Last function).
LastHess(x): Evaluates the hessian of f(Last function).

On all previous functions x is the objective variable.

*** step size functions ***

WolfeBacktracking(xk, fk, gradk,func, gradfn, pk, options) :
Performs Wolfe's backtracking line search

xk : objective variable at step k
fk : Objective function value at step k
gradk: gradient of f(xk)
func: functor for f(x) function
gradfn: functor for grad(x) function
pk: Search direction
options: Struct with the optimization parameters.

** Search direction Functions **

BfgsUpdate(hessiank, yk, sk): Computes the Bk matrix of the BFGS algorithm

hessiank : hessian of f(x) at time k
yk : gradient difference between steps k+1 and k
sk : direction of xk to xk+1

LBFGStwoLoopRecursion: Computes the term Hk*pk for the L-BFGS update.
 
*** Plotting function ***

plotData


