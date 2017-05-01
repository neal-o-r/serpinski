import numpy as np
import random as rd
import matplotlib.pyplot as plt

np.random.seed(123)

a = [0, 0]
b = [1, 0]
c = [0.5, 1]

p = np.random.rand(2)

x, y = np.zeros(5000), np.zeros(5000)
for i in range(5000):

	s = rd.choice([a, b, c])

	p1 = [(p[0] + s[0]) / 2, (p[1] + s[1]) / 2]
		
	x[i] = p1[0]
	y[i] = p1[1]
	p = p1


plt.scatter([a[0]], [a[1]], c='k')
plt.scatter([b[0]], [b[1]], c='k')
plt.scatter([c[0]], [c[1]], c='k')

plt.scatter(x, y, s=1, alpha=0.7, marker='.', c='0.75')
plt.axis('off')
plt.show()

