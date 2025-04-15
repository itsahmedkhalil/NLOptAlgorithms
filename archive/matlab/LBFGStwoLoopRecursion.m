function r = LBFGStwoLoopRecursion(H0_k, gradk, sks,...
                                    yks)

q = gradk;
m = length(sks(1,:));
p_l = zeros(1,m);
alpha = zeros(1,m);
for l=m:-1:1
    p_l(l) = 1/(yks(:,l)'*sks(:,l));
    alpha(l) = p_l(l) * sks(:,l)'*q;
    q = q - alpha(l) * yks(:,l);
end
r = H0_k*q;
for j = 1:1:m
    beta = p_l(j) * yks(:,j)'*r;
    r = r + sks(:,j).*(alpha(j)-beta);
end