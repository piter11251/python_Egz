import numpy as np
import matplotlib.pyplot as plt

labels = ['PL', 'DE', 'FR', 'SK']
x = np.arange(4)
X = [56, 60, 58, 37]
Y = [45, 47, 19, 38]
Z = [8, 38, 37, 15]
width = 0.2
fig,ax1 = plt.subplots()
ax1.bar(x, Z, width, color='royalblue', label='Z')
ax1.bar(x+width, Y, width, color='tab:cyan', label='Y')
ax1.bar(x+2*width, X, width, color='cornflowerblue', label='X')
ax1.legend(loc='center right')
plt.savefig('zad1.jpg')
plt.show()