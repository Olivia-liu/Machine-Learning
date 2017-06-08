%% Initialization
clear ; close all; clc

%% Load Data
%  The first two columns contains the exam scores and the third column
%  contains the label.

data = load('percent_data.txt');
X = data(:, [1, 2]); y = data(:, 3);

%% ==================== Plotting ====================
fprintf(['Plotting data with + indicating (y = 1) examples and o ' ...
         'indicating (y = 0) examples.\n']);

plotData(X, y);

% Put some labels 
hold on;
% Labels and Legend
xlabel('CPU %')
ylabel('Memory %')

% Specified in plot order
legend('Abnormal', 'Normal')
hold off;

fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% ============ Compute Cost and Gradient ============
%  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X);

% Add intercept term to x and X_test
X = [ones(m, 1) X];

% Initialize fitting parameters
initial_theta = zeros(n + 1, 1);

% Compute and display initial cost and gradient
[cost, grad] = costFunction(initial_theta, X, y);

fprintf('Cost at initial theta (zeros): %f\n', cost);
fprintf('Gradient at initial theta (zeros): \n');
fprintf(' %f \n', grad);

pause;


%% =============  Optimizing using fminunc  =============
%  use a built-in function (fminunc) to find the optimal parameters theta.

%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

%  Run fminunc to obtain the optimal theta
%  This function will return theta and the cost 
[theta, cost] = ...
	fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);

% Print theta to screen
fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
fprintf(' %f \n', theta);

% Plot Boundary
plotDecisionBoundary(theta, X, y);

% Put some labels 
hold on;
% Labels and Legend
xlabel('CPU %')
ylabel('Memory %')

% Specified in plot order
legend('Abnormal', 'Normal')
hold off;

fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% ============== Predict and Accuracies ==============
%  Use the model to predict the outcomes on unseen data.
%
%  Compute the training and test set accuracies of the model.
%

prob = sigmoid([1 45 85] * theta);
fprintf(['For CPU percent with 45 and memory percent with 85, we predict abnormal ' ...
         'probability of %f\n'], prob);
     
prob = sigmoid([1 66 35] * theta);
fprintf(['For CPU percent with 66 and memory percent with 35, we predict abnormal ' ...
         'probability of %f\n'], prob);

% Load data
data = load('percent_data_new.txt');
X2 = data(:, [1, 2]); y2 = data(:, 3);
[m2, n2] = size(X2);
X2 = [ones(m2, 1) X2];

% Compute accuracy on the training set
p = predict(theta, X2);

fprintf('Train Accuracy: %f\n', mean(double(p == y2)) * 100);
fprintf('\n');


