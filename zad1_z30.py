import matplotlib.pyplot as plt
import numpy as np

A = np.array([28, 17, 38, 18, 18])
B = np.array([14, 23, 7, 16, 17])
C = np.array([13, 25, 10, 17, 20])
z = [2015, 2016, 2017, 2018, 2019]
fig,ax = plt.subplots()
x = np.arange(5)
w = 0.6
ax.barh(x, A, w, color='blue', label='A')
ax.barh(x, B, w, color='green', left=A, label='B')
ax.barh(x, C, w, color='pink', left=A+B, label='C')
ax.set_title('Słupki poziome')
ax.legend(loc=1)
plt.yticks(x, z, color='royalblue')
plt.xticks(color='orange')
plt.savefig('zad1_z30.jpg')
plt.show()