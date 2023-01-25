%% Steering Angle Identification:
% This file takes .mat objects (filtered data)
% Use Px, Py to fit a circle using Taubin Circle Fit
% Use Radius of circle to estimate steering angle
% Store it alongside delta_counts from ROS
% Plot delta VS encoder_value to obtain steering model
% extract equation of line

clc;
clear;

steering = zeros(40,2); % [calculated_steering_angle, ticks]
% For all the mat objects:
% for i = 1:40
%     
% Load the mat object
% matFileName = sprintf('data%d.mat',i);
% load(matFileName);
load('data1.mat');
% Fit the circle on the xy datapoints
params = TaubinCircleFit([Px(:,1),Py(:,1)]);

% Plot to verify
figure('name', 'Trajectory and Plotted Circles')
h = plot(Px,Py);
hold on
th = 0:pi/50:2*pi;
xunit = params(3) * cos(th) + params(1);
yunit = params(3) * sin(th) + params(2);
h = plot(xunit, yunit);

wheel_base = 0.325; % Measured Wheelbase in meters

% Calculate Steering Angle and Ticks matrix
% steering(i,:) = [wheel_base/params(3), ticks];
% end

