# Barnsley-Fern
Use IFS to produce Barnsley Fern

# the transform style of IFS is Y=K*x+b  
1.first transform:  
K1 = [0.0,0.0;0.0,0.6];  
b1 = [0.0;0.0];  

2.second transform:  
K2 = [0.85,0.04;-0.04,0.85];  
b2 = [0.0;1.6];  

3.third transform:  
K3 = [0.2,-0.26;0.23,0.2];  
b3 = [0.0;1.6];  

4.fourth transform:  
K4 = [-0.15,0.28;0.26,0.24];  
b4 = [0.0;0.44];

# each transform's possible
possible = [0.01,0.85,0.07,0.07];  

# note
the source of matlab in the ./matlab  
the source of matlab in the ./python  
