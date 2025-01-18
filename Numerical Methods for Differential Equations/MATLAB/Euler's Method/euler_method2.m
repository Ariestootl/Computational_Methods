%% Name: Jose Aries E. De Los Santos
%% Math 171 Exercise 11
clear
clc
close all
a=0; b=5; N=100; t = linspace(a,b,N); f = @(t,y) y+t; 
ftrue = @(t) (-t-1)+exp(t); %Exact solution solved using an intergrating factor see pdf
h = (t(2)-t(1)) ; ff  = @(x) x-y-h*f(t,y);
%%Forward euler method
y1(:,1) = 0;
for i=1:N-1
    y1(:,i+1) = y1(:,i) + h*f(t(:,i),y1(:,i));
end
%% Backward euler method via Fixed Point Interation
y2(1) = 0;
for i=1:N-1
    y2(i+1) = (y2(i)+h*t(i+1))/(1-h); %% Explicit Solution is shown in the PDF
end

%% Backward euler method using fsolve
y6(1) = 0;
for i=1:N-1
    ff  = @(x) x-y6(i)-h*f(t(i+1),x);
    y6(i+1) = fsolve(ff,y6(i));
end

%%Use ODE45
% ODE45 solution
[t_ode45, y_ode45] = ode45(f, [a b], 0);

%%plotting
figure 
plot(t,ftrue(t),"color","#000033","LineWidth",2.0,"LineStyle","-"); %% True solution
hold on
plot(t,y1,"color","#7E2F8E","LineStyle","--","LineWidth",2.0); %% Forward Euler Method
plot(t,y2,"k--","LineWidth",2.0); %% Backward Euler (FPI) Method
plot(t,y6,"c*","LineWidth",1.0); %% Backward Euler (fsolve) Method
plot(t_ode45, y_ode45, "color", "#FF0000","LineStyle","-.","LineWidth",1.5);
legend("$True$ $Solution$","$Forward$ $Euler$","$Backward$ $Euler$ $(FPI)$ ","$Backward$ $Euler$ $(fsolve)$","ODE45","location","North","Interpreter","Latex","FontSize",13);
ylabel("$y$","Interpreter","Latex","FontSize",14);
xlabel("$x$","Interpreter","Latex","FontSize",14);
title("Math 171 Exercise 11 Ordinary Differential Equations","FontSize",10)
ylabel("$y$","Interpreter","Latex","FontSize",14);
xlabel("$x$","Interpreter","Latex","FontSize",14);
title("Euler's Method ","FontSize",10)