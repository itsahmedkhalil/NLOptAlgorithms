% The Rosenbrock function
function f = rosenbrockfunc(x)
% x : n by 1 vector

%% This function computes the Rosenbrock Function
xkp1 = x(2:end,1); xk = x(1:end-1,1);

%% compute internal term
f = sum(100 * (xkp1-xk.^2).^2 + (1-xk).^2); %% broadcasting

