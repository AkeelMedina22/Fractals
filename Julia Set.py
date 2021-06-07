import numpy as np
import matplotlib.pyplot as plt

# "https://www.learnpythonwithrune.org/numpy-calculate-the-julia-set-with-vectorization/"

c = -0.74543+0.11301j
n = 512

x = np.linspace(-1.5, 1.5, 2000).reshape((1, 2000))
y = np.linspace(-1.2, 1.2, 1600).reshape((1600, 1))
z = x + 1j*y

c = np.full(z.shape, c)

# keeps track of iteration# of divergence
diverge = np.zeros(z.shape)
# keeps track of convergence
m = np.full(z.shape, True)

for i in range(n):
    z[m] = z[m]**2 + c[m]
    # threshold for convergence of absolute is 2
    m[np.abs(z) > 2] = False
    diverge[m] = i

plt.imshow(diverge, cmap='magma')

plt.show()
