function [sol, status] = OptAlg(x0, Obj, options)

% Function implementing your optimization algorithms
% The inputs are
% -- x0:  The starting point
% -- Obj: Structure containing functions to evaluate objective and its
%         derivatives
% -- options: Structure containing algorithmic options
%         method: steepest descent
%                 Newton 
%                 modified Newton
%         PLEASE DESCRIBE YOUR OWN OPTIONS HERE AS WELL


% use whatever quantities you need to implement the algorithm, e.g.,
iter_counter = 0;
max_iters = options.max_iters;
status = []

% Print headline
% This is one example how you can use the options
switch options.method
    case {'steepest_descent'}
        % Steepest Descent
        fprintf('\nRunning Steepest Descent Method\n\n');
    case {'Newton'}
        % Newton's Method
        fprintf('\nRunning Newton''s Method\n\n');
    case {'modified_Newton'}
        % Modified Newton's Method
        fprintf('\nRunning modified Newton''s Method\n\n');
    case {'Newton-CG'}
        % Newton - CG method
        fprintf('\nRunning Newton''s CG Method\n\n');
    case {'BFGS'}
        % BFGS Method
        fprintf('\nRunning BFGS Method\n\n');
    case {'L-BFGS'}
        % L-BFGS Method
        fprintf('\nRunning L-BFGS Method\n\n');
    otherwise
        error('Invalid choice of method');
end

% There are also algorithm parameters that you should get from the
% options structure:
rho = options.rho;
epsilon = options.epsilon;
m = min(length(x0),10);

% Iterative procedure till convergence criteria is met
fx = zeros(1,max_iters); grad = zeros(length(x0),max_iters);
normgrad = zeros(1, max_iters);
xs = zeros(length(x0), max_iters);
pks = zeros(length(x0),max_iters);
sks = [];
yks = [];
alphas = zeros(1,max_iters);
% Inside the loop 
xk = x0;
time_start = tic;
for k=1:1:max_iters
    % You compute your search directions for each method 
    % Example : Write a function that outputs 
    % Note how we call the Obj structure
    objk  = Obj.func(xk);
    gradk = Obj.grad(xk);
    grad(:,k) = gradk;
    normgrad(k) = norm(gradk);
    fx(k) = objk;
    xs(:,k) = xk;
    % Choose a steplength parameter using line search
    % This is an example how to print things nicely:
    if k == 1
       alpha_init = 0.99;
    else
       pkm1 = pks(:,k-1);
       alpha_init = ComputeAlpha(fx(k), fx(k-1), ...
                                   grad(:,k-1), pkm1);
    end
    if strcmp(options.method, 'BFGS')
       if k==1
           hessiank = eye(length(xk));
           pk = GetSearchDirection(xk, grad, hessiank, k, options); %with necessary inputs
       else
           pk = GetSearchDirection(xk, grad, hessiank, k, options); %with necessary inputs
       end
    elseif strcmp(options.method, 'L-BFGS')
        H0 = eye(length(xk));
        if k==1 
           gamma = options.gamma_init;
           pk = -H0*gradk;
        else
           if length(sks(1,:))==m
              gamma = (sks(:,end)'*yks(:,end))/...
                    (yks(:,end)'*yks(:,end));
           end
           H0 = gamma*H0;
           pk = -LBFGStwoLoopRecursion(H0, gradk, sks, ...
                                      yks);
        end
    else
       hessiank = Obj.hess(xk);
       pk = GetSearchDirection(xk, grad, hessiank, k, options); %with necessary inputs
    end
    
    pks(:,k) = pk;
    if isnan(pk)
        status = 'Optimal solution not found, pk is nan';
        break
    end
    alpha = WolfeBacktracking(xk, fx(k), gradk, @Obj.func, ... 
                              @Obj.grad, pk, options);
    alphas(k) = alpha;
    if gradk'*pk >= 0
        error("search direction pk is wrong (positive)")
    end
    iter_counter = k;
    fprintf('%6s %9s %9s %9s\n',...
        'iter', 'f', '||grad||', 'alpha');
    fprintf('%6i %9.2e %9.2e %9.2e\n',...
        iter_counter, fx(k), norm(gradk), alpha);
    % Update your iterates
    xkp1 = xk + alpha * pk;
    alphas(k) = alpha;
    sk = xkp1 - xk;
    yk = Obj.grad(xkp1) - gradk;
    if strcmp(options.method, 'BFGS')
        if yk'*sk > epsilon * norm(yk) * norm(sk)
           hessiank = BfgsUpdate(hessiank, yk, sk);
        end
    elseif strcmp(options.method, 'L-BFGS')
        if yk'*sk > epsilon * norm(yk) * norm(sk)
            if k >= m && length(sks(1,:)) == m
                sks = [sks(:,2:end) sk];
                yks = [yks(:,2:end) yk];
            else
                yks = [yks yk];
                sks = [sks sk];  
            end
        end
    end
    xk = xkp1;
    % Repeat till the convergence criteria is met.
    if norm(gradk) < rho
        status = 'optimal solution found';
        fprintf("CPU time: %s \n", toc(time_start));
        break
    elseif toc(time_start) > 5
        fprintf("CPU time: %s \n", toc(time_start));
        status = 'Cpu time exceeded';
        break
    end   
end

% Make sure you set the correct return values
sol = xk;

% status
if isempty(status)
    status = 'optimal solution found';  % or other messages, depending on the outcome! 
end
xs = linspace(0, k, k);
plotData(xs, alphas(1:k), options.method, "Iteration", "alpha", "-")
plotData(xs, log10(fx(1:k)), options.method, "Iteration", "log_{10}(fx)", "-")
plotData(xs, log10(normgrad(1:k)), options.method, "Iteration", "log_{10}||\nabla(fx)||", "-")
% maximum cpu time has reached, max iterations have reached
