function grad = LastFunctionGrad(x)
a = x(1:end-1,1);
b = x(2:end,1);
twoai= linspace(1,9,9)*2;
twoai = twoai(:);
c = a - b;
pow = twoai-1;
d = twoai.*(c).^pow;
grad = zeros(size(x));
grad(1,1) = 2*x(1) + d(1);
grad(2:end-1,1) = d(2:end) - d(1:end-1);
grad(end,1) = - d(end);
end