import random
import math
import numpy as np
import matplotlib.pyplot as plt

n = 64


def PascalTriangle(n):
    trow = [1]
    y = [0]
    final = [trow]
    for x in range(n):
        trow = [left+right for left, right in zip(trow+y, y+trow)]
        final.append(trow)
    return final


pascal = PascalTriangle(n-1)
pascaliter1 = n

plt.axes()

for i in range(n):

    cutoff = i/2
    pascaliter1 -= 1
    pascaliter2 = 0

    for j in range(i, n):
        cutoff += 1

        if pascal[pascaliter1][pascaliter2] % 2 == 0:
            plt.gca().add_patch(plt.Rectangle((cutoff, 0+i), 1, 1, fc='white', ec="black"))
        else:
            plt.gca().add_patch(plt.Rectangle((cutoff, 0+i), 1, 1, fc='black', ec="black"))

        pascaliter2 += 1

plt.axis('scaled')
plt.show()
