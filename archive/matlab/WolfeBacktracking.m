function [alpha] = WolfeBacktracking(xk, fk, gradk,func, gradfn, pk, options)
% This function computes the steplength parameter alpha 
% that satisfies the Armijo condition 

% This is just a reference file. 
% You need to give all the necessary input paramaters. 

% You can get the parameters used in the Armijobacktracking 
% linesearch
c1=options.c1; tau = options.tau; alpha = 1;
c2=options.c2;
%% lower bound
alpha_l = 0;
%% upper bound
alpha_u = inf;

%% Objective function
f = func;

%% Define phi for clarity
phi = @(alp) f(xk + alp*pk);
phi_prime = @(alp) gradfn(xk + alp * pk)'*pk;
%% should result in (gradk' * pk) CHECK!!

% You need to write your code here.  


k = 0;
while true 
    k = k +1;
    if phi(alpha) > phi(0) + c1 * alpha * phi_prime(0)
       alpha_u = alpha;
    else
        if phi_prime(alpha) < c2*phi_prime(0)
            alpha_l = alpha;
        else
            return
        end
    end
    if alpha_u < inf 
        alpha = (alpha_l + alpha_u)/2;
    else
        alpha = 2*alpha;
    end
    if k > 100000
        
        return
        %error('Wolfe conditions in infinite loop')
    end
    
end
