function options = Initialize()
% This function sets some default values for parameters 
% used in the algorithm 
% 
% Armijo line search parameters
options.c1=10^-3;
options.c2=0.9;
options.tau = 0.5; 
options.max_iters= 10000;
options.rho = 10e-8;
options.epsilon = 10e-8;
options.gamma_init = 1;
options.eta = 0.01;

% etc.... You can initialeize the deafult values here. 

end

