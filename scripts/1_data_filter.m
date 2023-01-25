%% Data Filtering and Cleaning
% This file takes csv files obtained from ROS.
% Extracts Position, Velocity and Acceleration from the recorded VICON Data
% Filters Used:
% 2 Passes of Hampel Filter to remove outliers
% Lowpass filter to reduce noise.

% This file saves relevant information in the form of .mat objects

clc;
clear;


for i = 1:29

matFileName1 = sprintf('data/data%d.csv',i);
matFileName2 = sprintf('data/data%d.mat',i);

% Read csv file
M = csvread(matFileName1,1,1);
    
size = length(M(:,1)); % Number of data points

str_in = [8050; 8300; 8550; 8800; 9050; 9300];

% Extract Positions from csvfile object
Px = M(:,1);
Py = M(:,2);
Pz = M(:,3);
Yaw = M(:,6);

% Create containers for velocities
Vx = zeros(size,1);
Vy = zeros(size,1);
Vz = zeros(size,1);

% Create containers for acceleration
Ax = zeros(size,1);
Ay = zeros(size,1);
Az = zeros(size,1);

% Create containers for Yawrates
Yaw_d = zeros(size,1);
Yaw_dd = zeros(size,1);

% Calculate Velocities, Acceleration and Yawrates 
for i = 1:(size-1)
    Vx(i,1) = (M(i+1,1) - M(i,1))/0.01;
    Vy(i,1) = (M(i+1,2) - M(i,2))/0.01;
    Vz(i,1) = (M(i+1,3) - M(i,3))/0.01;
    
    Ax(i,1) = (M(i+1,4) - M(i,4))/0.01;
    Ay(i,1) = (M(i+1,5) - M(i,5))/0.01;
    Az(i,1) = (M(i+1,6) - M(i,6))/0.01;
    
    Yaw_d(i,1) = (M(i+1,6) - M(i,6))/0.01;
    
end

for i = 1:(size-1)
    Yaw_dd(i,1) = (Yaw_d(i+1,1) - Yaw_d(i,1))/0.01;
end

% Use double hampel filters to filter outliers:
Vx_hmpl = hampel(hampel(Vx));
Vy_hmpl = hampel(hampel(Vy));
Vz_hmpl = hampel(hampel(Vz));

Ax_hmpl = hampel(hampel(Ax));
Ay_hmpl = hampel(hampel(Ay));
Az_hmpl = hampel(hampel(Az));

Yawd_hmpl = hampel(hampel(Yaw_d));
Yawdd_hmpl = hampel(hampel(Yaw_d));

% Clean variables 
clear Vx Vy Vz Ax Ay Az Yaw_d Yaw_dd

% Use Lowpass filter to filter out noise:
Vx = lowpass(Vx_hmpl, 0.01,100);
Vy = lowpass(Vy_hmpl, 0.01,100);
Vz = lowpass(Vz_hmpl, 0.01,100);

Ax = lowpass(Ax_hmpl, 0.01,100);
Ay = lowpass(Ay_hmpl, 0.01,100);
Az = lowpass(Az_hmpl, 0.01,100);

Yaw_d = lowpass(Yawd_hmpl, 0.01,100);
Yaw_dd = lowpass(Yawdd_hmpl,0.01,100);

% Clear unnecessary objects from workspace
clear Vx_hmpl Vy_hmpl Vz_hmpl Ax_hmpl Ay_hmpl Az_hmpl Yawd_hmpl Yawdd_hmpl i M

save(matFileName2);

end