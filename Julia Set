import numpy as np
import matplotlib.pyplot as plt

# My Implementation 

x, y = np.ogrid[-1.5:1.5:800j, -1.5:1.5:1000j]

c = x + 1j*y
z = 0

for g in range(216):

    if g == 0:
        z = z**2 + c
    else:
        z = z**2 + -0.8+0.156j

threshold = 2
mask = np.abs(z) < threshold

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.gca().set_aspect('equal')

plt.imshow(mask.T, extent=[-1.5, 1.5, -1.5, 1.5], cmap='twilight')

plt.show()

# source = "https://www.learnpythonwithrune.org/numpy-calculate-the-julia-set-with-vectorization/"
# Alternate implementation making use of code from above site.
c = -0.8+0.156j
n = 512

x = np.linspace(-1.5, 1.5, 1000).reshape((1, 1000))
y = np.linspace(-1.2, 1.2, 800).reshape((800, 1))
z = x + 1j*y

c = np.full(z.shape, c)

diverge = np.zeros(z.shape)

m = np.full(c.shape, True)

for i in range(n):
    z[m] = z[m]**2 + c[m]
    m[np.abs(z) > 2] = False
    diverge[m] = i

plt.imshow(diverge, cmap='magma')

plt.show()
