# Barnsley-Fern
Use IFS to produce Barnsley Fern

# note
the source of matlab in the ./matlab \n
the source of matlab in the ./python

# the transform style of IFS is Y=K*x+b
# first transform
ax1 = [0.0,0.0;0.0,0.6];
b1 = [0.0;0.0];

# second transform
ax2 = [0.85,0.04;-0.04,0.85];
b2 = [0.0;1.6];

# third transform
ax3 = [0.2,-0.26;0.23,0.2];
b3 = [0.0;1.6];

# fourth transform
ax4 = [-0.15,0.28;0.26,0.24];
b4 = [0.0;0.44];

# each transform's possible
possible = [0.01,0.85,0.07,0.07];
