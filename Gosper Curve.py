import matplotlib.pyplot as plt
import numpy as np

axiom = "A"
rule1 = "A-B--B+A++AA+B-"
rule2 = "+A-BB--B-A++A+B"

iterations = 4
count = 0
coordinates = [(0, -1), (0, 0)]

for x in range(iterations):

    last = len(coordinates)-1

    coordinates = [(coordinates[last]), coordinates[last-1]]

    substr = ""
    for k in axiom:
        if k == "A":
            substr += rule1
        elif k == "B":
            substr += rule2
        else:
            substr += k

    stack = []

    for i in substr:

        if i == "+":
            stack.append(60)
        elif i == "-":
            stack.append(-60)
        else:
            if (i == "A" or i == "B") and count != 0:

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

plt.plot([i[0] for i in coordinates], [i[1] for i in coordinates])
plt.axis("equal")
plt.show()
