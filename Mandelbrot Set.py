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

############################################################################

# Alternate approach (cooler result)

x = np.linspace(-1.2-0.15, -1.2+0.15, 2000).reshape((1, 2000))
y = np.linspace(0.35-0.15, 0.35+0.15, 2000).reshape((2000, 1))
c = x + 1j*y
z = x + 1j*y

n = 512

c = np.full(z.shape, c)

diverge = np.zeros(z.shape)

m = np.full(c.shape, True)

for i in range(n):
    z[m] = z[m]**2 + c[m]
    m[np.abs(z) > 2] = False
    diverge[m] = i
upper = 1.2
lower = 0.35
plt.imshow(diverge, cmap='magma', origin='lower')

plt.show()

# To save the image:
# plt.savefig("mandlebrot.png", dpi=1200, orientation='landscape')
