% Plotting a Sine Wave

x = linspace(0, 2*pi, 100);  % Create 100 points between 0 and 2*pi
y = sin(x);                  % Compute the sine of each point

figure;                      % Create a new figure window
plot(x, y);                  % Plot y vs. x
title('Sine Wave');
xlabel('x');
ylabel('sin(x)');
grid on;                     % Turn the grid on
