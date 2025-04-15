function grad = BealeGrad(x)
%% This function computes the gradient of the Beale Function
%% Data
y = [1.5, 2.25, 2.625];
%%
n = 3;
fx = 0;
grad = zeros(size(x));
for k=1:1:n
    grad(1) = grad(1) + 2*(y(k)-x(1)*(1-x(2)^k))*(x(2)^k -1);
    grad(2) = grad(2) + 2*(y(k)-x(1)+x(1)*x(2)^k)*(k*x(1)*x(2)^(k-1));
end