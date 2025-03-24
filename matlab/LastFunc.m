function fx = LastFunction(x)
a = x(1:end-1,1);
b = x(2:end,1);
twoai= linspace(1,9,9)*2;
c = a - b;
fx = 0;
for k=1:1:length(twoai)
   fx = fx + c(k).^twoai(k) ;
end
fx = fx + x(1)^2;
end