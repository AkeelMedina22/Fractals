import matplotlib.pyplot as plt
import numpy as np

axiom = "F"
rule = "FF-[-F+F+F]+[+F-F-F]"
# max 4 iterations. 5 iterations is too slow, the length of the axiom explodes
iterations = 4
count = 0
coordinates = [(0, -1), (0, 0)]

for x in range(iterations):

    last = len(coordinates)-1

    coordinates = [(coordinates[last-1]), coordinates[last]]

    substr = ""

    for ch in axiom:

        if ch == "F":
            substr += rule
        else:
            substr += ch

    stack = []
    pos = []

    for i in substr:

        if i == "+":
            stack.append(22.5)
        elif i == "-":
            stack.append(-22.5)

        elif i == "[":
            plt.plot([i[0] for i in coordinates], [i[1]
                                                   for i in coordinates], c="green")
            plt.axis("equal")
            last = len(coordinates)-1
            pos.append(
                ([coordinates[last-1], coordinates[last]], stack.copy()))
        elif i == "]":
            temp = pos.pop()
            coordinates = temp[0]
            stack = temp[1]

        elif i == "F" and count != 0:
            angle = 0
            for j in stack:
                angle += j
            stack = []

            theta = np.radians(angle)

            R = np.array(((np.cos(theta), -np.sin(theta)),
                          (np.sin(theta),  np.cos(theta))))

            last = len(coordinates)-1

            line = np.array([coordinates[last][0]-coordinates[last-1]
                             [0], coordinates[last][1]-coordinates[last-1][1]])

            vector = list(R.dot(line))

            coordinates.append(
                (coordinates[last][0]+vector[0], coordinates[last][1]+vector[1]))
        count += 1
    axiom = substr
plt.show()
