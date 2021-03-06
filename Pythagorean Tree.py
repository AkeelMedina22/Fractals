import random
import math
import numpy as np
import matplotlib.pyplot as plt

n = 11

howbrown = 3

squares = [((0, 1), (0, 0), (1, 0), (1, 1), (0, 1)),
           ((0, 0), (0, -1), (1, -1), (1, 0), (0, 0))]
triangles = [((0.5, 1+(0.5)), (0, 1),
              (1, 1), (0.5, 1+(0.5)))]
x, y = zip(*squares[0])
plt.plot(x, y, color='#654321')
x, y = zip(*squares[1])
plt.plot(x, y, color='#654321')
x, y = zip(*triangles[0])
plt.plot(x, y, color='#654321')


def distance(pt1, pt2):
    return math.sqrt(((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2))


for i in range(n):

    squares = list()

    for j in triangles:

        dist1 = distance(j[1], j[3])

        vector1 = [j[3][0] - j[2][0], j[3][1] - j[2][1]]
        vector2 = [j[3][0] - j[1][0], j[3][1] - j[1][1]]

        x = [(j[1][0] + vector1[0]), j[1][0], j[3][0],
             (j[3][0] + vector1[0]), (j[1][0] + vector1[0])]
        y = [(j[1][1] + vector1[1]), j[1][1], j[3][1],
             (j[3][1] + vector1[1]),  (j[1][1] + vector1[1])]

        squares.append(
            (((j[1][0] + vector1[0], j[1][1] + vector1[1]), j[1], j[3], (j[3][0] + vector1[0], j[3][1] + vector1[1]), (j[1][0] + vector1[0], j[1][1] + vector1[1]))))

        if i > howbrown:
            plt.plot(x, y, color='green')
        else:
            plt.plot(x, y, color='#654321')

        x = [(j[2][0] + vector2[0]), j[2][0], j[3][0],
             (j[3][0] + vector2[0]), (j[2][0] + vector2[0])]
        y = [(j[2][1] + vector2[1]), j[2][1], j[3][1],
             (j[3][1] + vector2[1]),  (j[2][1] + vector2[1])]

        squares.append(
            (((j[2][0] + vector2[0], j[2][1] + vector2[1]), j[2], j[3], (j[3][0] + vector2[0], j[3][1] + vector2[1]), (j[2][0] + vector2[0], j[2][1] + vector2[1]))))

        if i > howbrown:
            plt.plot(x, y, color='green')
        else:
            plt.plot(x, y, color='#654321')

    triangles = list()

    for k in squares:

        dist2 = distance(k[3], k[4])/2

        vector1 = [(k[4][0] - k[1][0])/2, (k[4][1] - k[1][1])/2]
        vector2 = [vector1[0] + k[4][0],
                   vector1[1] + k[4][1]]
        vector3 = [vector2[0] + (k[2][0]-k[1][0])/2,
                   vector2[1] + (k[2][1]-k[1][1])/2]

        x = [vector3[0], k[3][0],
             k[4][0], vector3[0]]
        y = [vector3[1], k[3][1],
             k[4][1], vector3[1]]

        triangles.append(
            (vector3, k[3], k[4], vector3))
        if i > howbrown:
            plt.plot(x, y, color='green')
        else:
            plt.plot(x, y, color='#654321')


plt.gca().set_aspect('equal')
plt.show()


# Step 1: Draw a square.
# Step 2: Attach a right triangle to one of its sides along its hypotenuse (here
# with two equal sides).
# Step 3: Attach two squares along the free sides of the triangle.
# Step 4: Attach two right triangles.
# Step 5: Attach four squares.
# Step 6: Attach four right triangles.
# Step 7: Attach eight squares.
