function [f,Df]=rosenbrockMatlab(x)
% the 2D Rosenbrock function and its gradient
[m,n]=size(x);
if (m ~= 2 | n ~= 1)
	error('Bad data sent to 2D Rosenbrock function')
end
z    = [x(1)^2 - x(2), x(1)-1]';
f    = 100*z(1)^2 + z(2)^2;
Df   = [400*x(1)*z(1) + 2*z(2), -200*z(1)]';