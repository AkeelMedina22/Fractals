import numpy as np
import matplotlib.pyplot as plt

x, y = np.ogrid[-1.5:1.5:800j, -1.5:1.5:800j]

c = x + 1j*y
z = 0

for g in range(512):
    z = z**2 + c

threshold = 2
mask = np.abs(z) < threshold

plt.xlim(-1.5, 1)
plt.ylim(-1.5, 1.5)

plt.gca().set_aspect('equal')

plt.imshow(mask.T, extent=[-1.5, 1.5, -1.5, 1.5], cmap='magma')

plt.show()
