function pk = getSearchDirection(x, grad, hessiank, k, options)
type=options.method;
eta = options.eta;
if strcmp(type,"steepest_descent")
    pk = -grad(:,k);
elseif strcmp(type,"Newton")
    H = hessiank;
    v = rand(length(H),1);
    test = v' * H * v;
    if test > 0
        pk = - H \ grad(:,k);
        return
    else
        vector_x = x
        vector_v = v
        Hessian = H
        disp('Hessian is negative definite')
        pk = NaN;
    end
elseif strcmp(type,"modified_Newton")
    H = hessiank;
    n = length(x);
    delta = 0;
    min_diag = min(diag(H));
    if min_diag < 0
       delta = - min_diag + 10e-4;
    end
    for i=1:1:100
        try
            A = chol(H + delta * (eye(n)), "lower");
            Success = 0;
            break;
        catch
            delta = max(2 * delta, 10e-4); 
        end
    end
    H = H + delta *(eye(n));
    pk = - H \ grad(:,k);
elseif strcmp(type, "Newton-CG")
    n = length(grad(:,k))+ 10;
    d = zeros(n-10,n); z = zeros(n-10,n);
    r = zeros(n-10,n);
    z(:,1) = 0; r(:,1) = grad(:,k); d(:,1) = -r(:,1);
    for j=1:1:n
        
        if d(:,j)'*hessiank*d(:,j) <= 0
            if j==0
                pk = - grad(:,k);
                return
            else
                pk = z(:,j);
                return
            end
        else
            alpha = (r(:,j)'*r(:,j))/(d(:,j)'*hessiank*d(:,j));
            z(:,j+1) = z(:,j) + alpha*d(:,j);
            r(:,j+1) = r(:,j) + alpha*hessiank*d(:,j);
            if norm(r(:,j+1)) <= eta * norm(grad(:,k))
                pk = z(:,j+1);
                return
            end
            beta = r(:,j+1)'*r(:,j+1)/(r(:,j)'*r(:,j));
            d(:,j+1) = -r(:,j+1) + beta*d(:,j);
        end
    end
elseif strcmp(type, "BFGS")
    pk = -hessiank*grad(:,k);
else
    not_assigned = 1
    disp("No search direction specified")
end

end