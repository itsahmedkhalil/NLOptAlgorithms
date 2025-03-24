function [H] = LastFunctionHessian(x)
    n = length(x); 
    H = zeros(n, n);
    
    H(1,1) = 4;
    for i = 2:n-1
        H(i,i) = 2*i*(2*i-1)*(x(i) - x(i+1))^(2*i-2) ...
               + 2*(i-1)*(2*(i-1)-1)*(x(i-1) - x(i))^(2*(i-1)-2);
    end
    H(n,n) = 2*(n-1)*(2*(n-1)-1)*(x(n-1) - x(n))^(2*(n-1)-2);

    for i = 1:n-1
        H(i, i+1) = -2*i*(2*i-1)*(x(i) - x(i+1))^(2*i-2);
        H(i+1, i) = H(i, i+1);
    end
end