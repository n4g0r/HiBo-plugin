function i=homo (x1,x2)
% =========
% x1 =[144.90937499999993, 331.47281250000015, 322.81375000000014, 130.73999999999992;
%      288.1303125,        305.84203125,       341.26546875,       356.6156250000001 ;
%      1,                  1,                  1,                  1                  ]
%     
% x2 =[997117.4422382201, 1135642.7102414735,  1130022.3533057806, 984554.291440789;
%      7269441.552735677, 7258200.838864291,   7232413.318806406,  7218527.731082929;
%      1,                 1,                   1,                  1                 ]


i = homography2(x1, x2);     % Compute homography H



function H = homography2(x1, x2)  % Planar projective transformation
% ===================
T1 = condition2(x1); c1 = T1 * x1;     % Image point conditioning
T2 = condition2(x2); c2 = T2 * x2;
A = design_homo2(c1, c2);     % Build design matrix
h = solve_dlt(A);    % Linear least squares solution
H = inv(T2) * reshape(h, 3, 3)' * T1;   % Reshape row-wise and deconditioning

function T = condition2(x)  % Conditioning matrix for image points
% =============
tx = mean(x(1,:)); ty = mean(x(2,:));  % Translation tx, ty
sx = mean(abs(x(1,:) - tx)); sy = mean(abs(x(2,:) - ty));  % Scaling sx, sy
T = [1/sx 0   -tx/sx; 
0   1/sy -ty/sy; 
0   0   1];

function A = design_homo2(x1, x2)  % Design matrix for 2D homography
% ====================
A = [];
for i = 1 : size(x1, 2)
A = [ A; -x2(3, i)*x1(:, i)'  0  0  0  x2(1, i)*x1(:, i)' ;
0  0  0  -x2(3, i)*x1(:, i)'  x2(2, i)*x1(:, i)' ];
end

function x = solve_dlt(A)  % Direct linear transformation, solver for A*x = 0
% ============
[U, D, V] = svd(A);   % Singular value decomposition
x = V(:, end); % Last column is singular vector to the smallest singular value 