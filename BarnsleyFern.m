clear all;
clc;

%% the times of Iterated Function System(IFS)
ITERATIONNUM = 50000;

%% coordinate origin
coor = zeros(2,1);

%% transform style : Y=K*x+b
% first transform
ax1 = [0.0,0.0;0.0,0.6];
b1 = [0.0;0.0];

% second transform
ax2 = [0.85,0.04;-0.04,0.85];
b2 = [0.0;1.6];

% third transform
ax3 = [0.2,-0.26;0.23,0.2];
b3 = [0.0;1.6];

% fourth transform
ax4 = [-0.15,0.28;0.26,0.24];
b4 = [0.0;0.44];

%% each transform's possible
possible = [0.01,0.85,0.07,0.07];

% sum the possible for use the roulette wheel
for  i = 2:length(possible)
    possible(i) = possible(i) + possible(i-1);
end

%% initial the current coordinate origin
coorCur = coor;

%% Ittration
for i =1:ITERATIONNUM
    % random an uniformly-distributed data in (0,1)
    currSelect = rand();

    if currSelect < possible(1)
        coorCur = ax1 * coorCur + b1;
        coor = [coor coorCur];
    end

    if currSelect < possible(2)  && currSelect >= possible(1)
        coorCur = ax2 * coorCur + b2;
        coor = [coor coorCur];
    end

    if currSelect < possible(3)  && currSelect >= possible(2)
        coorCur = ax3 * coorCur + b3;
        coor = [coor coorCur];
    end

    if currSelect < possible(4)  && currSelect >= possible(3)
        coorCur = ax4 * coorCur + b4;
        coor = [coor coorCur];
    end
end

%% display
figure(1);
title('Barnsley Fern');
% x in the first row of coordinate origin
% y in the second row of coordinate origin
h=scatter(coor(1,:),coor(2,:));
% scatter size
h.SizeData = 3;
% scatter color = [r g b] and the range of rgb is (0,1)
h.CData = [1 0 0];
saveas(gca,'Barnsley Fern');