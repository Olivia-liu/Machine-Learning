function J = computeCostMulti(X, y, theta)
%COMPUTECOSTMULTI Compute cost for linear regression with multiple variables
%   J = COMPUTECOSTMULTI(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.
% this is the same code as used in computeCost for only 1 feature dataset
h = theta'*X'; %calculate h(sub thetha)(x) = thetha^T*x = theta0 + thetha1*x1
diff = h - y'; %calculate h(sub thetha)(x) - y
sum = diff * diff'; %calculate sum i=1:m (h(sub thetha)(x(super 1)-y(super 1))^2)
J = sum/2/m;

% =========================================================================

end
