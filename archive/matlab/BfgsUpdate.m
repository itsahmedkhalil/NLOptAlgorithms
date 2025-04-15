function Hkp1 = BfgsUpdate(Hk, yk, sk)
%% Compute the BFGS update
I = eye(length(Hk));
pk = 1/(yk'*sk);
Hkp1 = (I - pk*sk*yk')*Hk*(I-pk*yk*sk') + pk*sk*sk';