from random import random
import numpy as np
import matplotlib.pyplot as plt

# the times of Iterated Function System(IFS)
ITERATIONNUM = 10000

# coordinate origin
coor = np.array([[0],[0]])

# transform style : Y=K*x+b
# first transform
ax1 = np.array([[0.0,0.0],[0.0,0.6]])
b1 = np.array([[0.0],[0.0]])

# second transform
ax2 = np.array( [[0.85,0.04],[-0.04,0.85]])
b2 = np.array([[0.0],[1.6]])

# third transform
ax3 = np.array([[0.2,-0.26],[0.23,0.2]])
b3 = np.array([[0.0],[1.6]])

# fourth transform
ax4 = np.array([[-0.15,0.28],[0.26,0.24]])
b4 = np.array([[0.0],[0.44]])

# each transform's possible
possible = np.array([0.01,0.85,0.07,0.07])

# sum the possible for use the roulette wheel
for  i in range(1,len(possible)):
    possible[i] = possible[i] + possible[i-1]

# initial the current coordinate origin
coorCur = coor

for i in range(1,ITERATIONNUM):
    # random a data in (0,1)
    currSelect = random()

    if currSelect < possible[0] :
        coorCur = np.dot(ax1,coorCur) + b1
        coor = np.append(coor, coorCur, axis=1)

    if currSelect < possible[1]  and currSelect >= possible[0]:
        coorCur = np.dot(ax2, coorCur) + b2
        coor = np.append(coor,coorCur,axis=1)

    if currSelect < possible[2]  and currSelect >= possible[1]:
        coorCur = np.dot(ax3, coorCur) + b3
        coor = np.append(coor, coorCur, axis=1)

    if currSelect < possible[3]  and currSelect >= possible[2]:
        coorCur = np.dot(ax4, coorCur) + b4
        coor = np.append(coor,coorCur,axis=1)

plt.figure()
plt.title('Barnsley Fern')
# x in the first row of coordinate origin
# y in the second row of coordinate origin
plt.scatter(coor[0],coor[1],s=0.3,edgecolor='green')
plt.savefig('Barnsley Fern')
# if you want to show the figure ,uncomment  plt.show()
# plt.show()