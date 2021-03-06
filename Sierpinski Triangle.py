import random
import math
import numpy as np
import matplotlib.pyplot as plt

# This is the Chaos Game implementation of the Sierpinski Triangle. Method found on Wikipedia.

# Step 1: Take three points in a plane to form a triangle, you need not draw it.
# Step 2: Randomly select any point inside the triangle and consider that your current position.
# Step 3: Randomly select any one of the three vertex points.
# Step 4: Move half the distance from your current position to the selected vertex.
# Step 5: Plot the current position.
# Step 6: Repeat from step 3.

n = 100000

datax = []
datay = []

pt1 = (0, 0)
pt2 = (2, 3)
pt3 = (4, 0)

s, t = sorted([random.random()*0.9, random.random()*0.9])
current = [s * pt1[0] + (t-s)*pt2[0] + (1-t)*pt3[0],
           s * pt1[1] + (t-s)*pt2[1] + (1-t)*pt3[1]]

for i in range(n):

    moveto = ()
    prob = random.random()*0.9

    if prob <= 0.3:
        moveto = (0, 0)
    elif prob <= 0.6:
        moveto = (2, 3)
    else:
        moveto = (4, 0)

    distance = math.sqrt(
        ((moveto[0]-current[0])**2)+((moveto[1]-current[1])**2)) / 2

    current[0] += (moveto[0]-current[0])/2
    current[1] += (moveto[1]-current[1])/2

    datax.append(current[0])
    datay.append(current[1])

plt.xlim(0, 4)
plt.ylim(0, 3)

plt.gca().set_aspect('equal')

plt.scatter(x=datax, y=datay, color='crimson', s=0.01)
plt.show()
