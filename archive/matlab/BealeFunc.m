function fx = BealeFunc(x)
%% This function computes the Beale Function
%% Data
y = [1.5, 2.25, 2.625];
%%
n = 3;
fx = 0;
for k=1:1:n
    fx = fx + (y(k) - x(1)*(1-x(2)^k))^2;
end
