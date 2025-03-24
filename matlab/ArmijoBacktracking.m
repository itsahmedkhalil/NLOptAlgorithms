function [alpha] = ArmijoBacktracking(xk,fk,gradk,pk,alpha_init,func,options)
% This function computes the steplength parameter alpha 
% that satisfies the Armijo condition 

% This is just a reference file. 
% You need to give all the necessary input paramaters. 

% You can get the parameters used in the Armijobacktracking 
% linesearch
c1=options.c1; tau = options.tau; alpha = alpha_init;
% You need to write your code here.  

% Objective function
f = func;

while f(xk + alpha * pk)> fk + c1 * alpha * (gradk' * pk)
    alpha = tau * alpha;
end

end

