%% Vector Field Plot
clear
clc
close all

a=0; b=5; N=100; t = linspace(a,b,N); f = @(t,y) y+t; 
ftrue = @(t) (-t-1)+exp(t); %Exact solution solved using an intergrating factor see pdf
h = (t(2)-t(1)) ; ff  = @(x) x-y-h*f(t,y);

% Define a grid for the vector field
[t_grid, y_grid] = meshgrid(linspace(-1, 6, 30), linspace(-20, 20, 20)); % Adjust y range as needed
u = ones(size(t_grid)); % The t component of vectors is always 1
v = f(t_grid, y_grid);  % The y component of vectors is f(t, y)

% Plotting the vector field
figure;
quiver(t_grid, y_grid, u, v, 'AutoScale', 'on', 'AutoScaleFactor', 0.5);
title('Vector Field of f(t, y) = y + t');
xlabel('t');
ylabel('y');
grid on;