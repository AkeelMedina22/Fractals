import matplotlib.pyplot as plt
import numpy as np

x, y = np.ogrid[-2:2:3000j, -2:2:3000j]

c = x + 1j*y
z = 0

def quadratic(z, c):
    return z**2 + c

for g in range(20):
    z = quadratic(np.abs(z.real) + 1j*np.abs(z.imag), c)

threshold = 2
mask = np.abs(z) < threshold

plt.xlim(-1.5, 1)
plt.ylim(-0.75, 1.5)

plt.gca().set_aspect('equal')

plt.imshow(mask.T, extent=[-1.5, 1.5, -1.5, 1.5], cmap='magma')

plt.show()
