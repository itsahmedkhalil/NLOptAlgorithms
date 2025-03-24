% The Hessian of the Rosenbrock function
function H = rosenbrockhess(x)
% x : n by 1 vector
n=length(x);
% You need to implement this!
% Compute the analytical Hessian and implement the formula.

H = zeros(n,n);  % This is wrong!
x1 = x(1);
x2 = x(2);
H(1,1) = 1200*x1^2 - 400*x2 + 2;
for k=1:1:n-1
        if n > 2
            H(k,k) = 1200*x(k)^2 - 400*x(k+1) + 202;
        end
        H(k, k+1) = -400*x(k);
        H(k+1, k) = H(k,k+1);
end
H(n,n) = 200;
    


       