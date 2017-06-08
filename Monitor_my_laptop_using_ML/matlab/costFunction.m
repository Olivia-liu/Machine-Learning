function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%
%%% caculate J
neg_y = -y; 

h = sigmoid((theta'*X')');
log_h = log(h);

left_sum = neg_y'*log_h; %will be used later

one = ones(m, 1);
one_minus_y = one-y; 
log_one_minus_h = log(one-h); 

right_sum = one_minus_y'*log_one_minus_h;

sum = left_sum - right_sum;

J = sum./m;

%%% calculate grad
grad = ((h-y)'*X)./m;
grad = grad';
% =============================================================

end
