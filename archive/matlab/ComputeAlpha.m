function alpha_init = compute_alpha(fk, fkm1, gradfkm1, pkm1)
%% Function for computing alpha_init every iteration
phi = gradfkm1'*pkm1;
alpha_init = 2*(fk - fkm1)/phi;
end
