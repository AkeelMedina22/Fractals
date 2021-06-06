import matplotlib.pyplot as plt
import numpy as np

iterations = 4

# This is a typical Koch Snowflake
# start = [(0, 0), (1, 0), (0.5, -(np.sqrt(3)/2)), (0, 0)]

# This is a square version
# start = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

# This looks like a cross
start = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0),
         (2, -1), (1, -1), (1, -3), (0, -3), (0, -1), (-1, -1), (-1, 0), (0, 0)]

# Rotation matrix to change angle (usually it is set to 60)
theta = np.radians(110)

R = np.array(((np.cos(theta), -np.sin(theta)),
              (np.sin(theta),  np.cos(theta))))

temp = []
final = []
newstart = []

for _ in range(iterations):

    newstart = []

    for i in range(len(start)-1):

        vector = [(start[i+1][0]-start[i][0])/3, (start[i+1][1]-start[i][1])/3]
        vector1 = [start[i][0]+vector[0], start[i][1]+vector[1]]
        vector2 = [start[i][0]+(2*vector[0]), start[i][1]+(2*vector[1])]

        vector3 = R.dot(np.array(
            [vector2[0]-vector1[0], vector2[1]-vector1[1]]))
        vector3 = [vector1[0]+vector3[0], vector1[1]+vector3[1]]

        newstart.append(start[i])
        newstart.append(vector1)
        newstart.append(vector3)
        newstart.append(vector2)
        newstart.append(start[i+1])

    start = newstart
    temp = []

x = [i[0] for i in newstart]
y = [i[1] for i in newstart]

plt.plot(x, y, c="#660000")
plt.axis('equal')
plt.show()
