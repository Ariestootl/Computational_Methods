% Script to solve the ODE using Euler's method and compare with the true solution

% Define the derivative function
function dy = ydot(t, y)
    dy = t * y + t^3;
end

% Define the Euler step function
function y = eulerstep(t, y, h)
    y = y + h * ydot(t, y);
end

% Define the Euler method function
function [t, y] = euler(inter, y0, n)
    t(1) = inter(1); 
    y(1) = y0;
    h = (inter(2) - inter(1)) / n;
    for i = 1:n
        t(i + 1) = t(i) + h;
        y(i + 1) = eulerstep(t(i), y(i), h);
    end
end

% Main script
% Clear the workspace and command window
clear; clc;

% Parameters for the problem
inter = [0, 1];  % Interval [0, 1]
y0 = 1;          % Initial condition y(0) = 1
n = 5;           % Number of steps

% Call the Euler function
[t, y] = euler(inter, y0, n);

% True solution
true_solution = @(t) 3 * exp(t.^2 / 2) - t.^2 - 2;
t_true = linspace(inter(1), inter(2), 100);
y_true = true_solution(t_true);

% Plot the numerical and true solutions
figure;
plot(t, y, 'o-', 'DisplayName', 'Euler Approximation');
hold on;
plot(t_true, y_true, '-', 'DisplayName', 'True Solution');
xlabel('t');
ylabel('y');
title('Comparison of Euler''s Method Approximation and True Solution');
legend show;
grid on;

% Display the results
disp('t values:');
disp(t);
disp('Euler method y values:');
disp(y);
disp('True solution y values at Euler points:');
disp(true_solution(t));