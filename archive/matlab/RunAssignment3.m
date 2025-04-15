%% This is the main file to run the programming problem in the assignment

clc
clear
close all %1  2  3  4  5  6  7  8  9 10
problem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1];
%problem = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
% Methods implemented
methods_list = {'L-BFGS'}%, 'L-BFGS', 'Newton-CG'};
% Methods are: 'steepest_descent' 'Newton' 'modified_Newton' 'L-BFGS' 'Newton-CG'

%% Problem 1

if problem(1)
    % Starting point
    x0 = [-1.2;1];
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @rosenbrockfunc;
        Obj.grad = @rosenbrockgrad;
        Obj.hess = @rosenbrockhess;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
        for i = 1:size(sol)
            fprintf('x[%4d] = %15.8e\n', i,sol(i));
        end
    end
end
%% Problem 2 
if problem(2)
    
    % Starting point
    n = 10;
    x0 = -ones(n,1);
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @rosenbrockfunc;
        Obj.grad = @rosenbrockgrad;
        Obj.hess = @rosenbrockhess;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
        for i = 1:size(sol)
            fprintf('x[%4d] = %15.8e\n', i,sol(i));
        end
    end
end
%% Problem 3
if problem(3)
    
    % Starting point
    n = 10;
    x0 = 2*ones(n,1);
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @rosenbrockfunc;
        Obj.grad = @rosenbrockgrad;
        Obj.hess = @rosenbrockhess;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
        for i = 1:size(sol)
            fprintf('x[%4d] = %15.8e\n', i,sol(i));
        end
    end
end
%% Problem 4
if problem(4)
    
    % Starting point
    n = 100;
    x0 = -ones(n,1);
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @rosenbrockfunc;
        Obj.grad = @rosenbrockgrad;
        Obj.hess = @rosenbrockhess;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
        for i = 1:size(sol)
            fprintf('x[%4d] = %15.8e\n', i,sol(i));
        end
    end
end
%% Problem 5
if problem(5)
    
    % Starting point
    n = 100
    x0 = 2*ones(n,1);
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @rosenbrockfunc;
        Obj.grad = @rosenbrockgrad;
        Obj.hess = @rosenbrockhess;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
        for i = 1:size(sol)
            fprintf('x[%4d] = %15.8e\n', i,sol(i));
        end
    end
end
%% Problem 6
if problem(6)
    
    % Starting point
    n = 1000
    x0 = 2*ones(n,1);
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @rosenbrockfunc;
        Obj.grad = @rosenbrockgrad;
        Obj.hess = @rosenbrockhess;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
        for i = 1:size(sol)
            fprintf('x[%4d] = %15.8e\n', i,sol(i));
        end
    end
end
%% Problem 7
if problem(7)
    
    % Starting point
    n = 10000;
    x0 = 2*ones(n,1);
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @rosenbrockfunc;
        Obj.grad = @rosenbrockgrad;
        Obj.hess = @rosenbrockhess;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
%         for i = 1:size(sol)
%             fprintf('x[%4d] = %15.8e\n', i,sol(i));
%         end
    end
end
%% Problem 8
if problem(8)
    
    % Starting point
    n = 3;
    x0 = [1; 1];
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @BealeFunc;
        Obj.grad = @BealeGrad;
        Obj.hess = @BealeHessian;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
%         for i = 1:size(sol)
%             fprintf('x[%4d] = %15.8e\n', i,sol(i));
%         end
    end
end
%% Problem 9
if problem(9)
    
    % Starting point
    n = 3;
    x0 = [0; 0];
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @BealeFunc;
        Obj.grad = @BealeGrad;
        Obj.hess = @BealeHessian;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
%         for i = 1:size(sol)
%             fprintf('x[%4d] = %15.8e\n', i,sol(i));
%         end
    end
end
%% Problem 10
if problem(10)
    
    % Starting point
    n = 10;
    x0 = [1;2;3;4;5;6;7;8;9;10];
    % Print the starting point
    fprintf('Starting point:\n');
    for i = 1:size(x0)
        fprintf('x0[%4d] = %15.8e\n', i,x0(i));
    end


    % Loop through the different methods
    for j = 1:length(methods_list)

        % options
        options = Initialize(); % Initializes default values for some parameters
        % j = 1 for SteepestDescent
        % j = 2 for Newton
        % j = 3 for Modified Newton
        options.method = methods_list{j};

        % You need to define all necessary input parameetrs in this options
        % structure

        % Characterize the function we want to optimize. 
        % First create separate files for the objective, gradient and hessian
        % matrix. Then call these functions with function handle @.
        Obj.func = @LastFunc;
        Obj.grad = @LastGrad;
        Obj.hess = @LastHessian;
        % Optimize the function
        [sol, status] = OptAlg(x0, Obj, options);

        % Print the return status:
        fprintf('\nReturn status: %s\n\n', status);

        % Print the optimal solution
        fprintf('Optimal solution:\n');
%         for i = 1:size(sol)
%             fprintf('x[%4d] = %15.8e\n', i,sol(i));
%         end
    end
end

