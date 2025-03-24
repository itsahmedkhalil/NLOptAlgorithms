% The gradient of the Rosenbrock function
function grad = rosenbrockgrad(x)
% x : n by 1 vector
n=length(x);
% You need to implement this! 

% Compute the analytical gradient and implement the formula.
grad=zeros(n,1);

n = length(x);
grad = zeros(size(x));
a = x(2:end-1,1);
b = x(1:end-2,1);
c = x(3:end,1);
grad(1) = -400*x(1)*(x(2)-x(1)^2) + 2*(x(1) - 1);
if n > 2
    grad(2:end-1) = 200*(a-b.^2)-400*a.*(c-a.^2)-2*(1-a);
end
grad(end) = 200*(x(end)-x(end-1)^2);

