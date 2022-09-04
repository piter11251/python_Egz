import matplotlib.pyplot as plt
import numpy as np

A = np.array([31, 18, 22, 16, 20])
B = np.array([10, 18, 8, 14, 22])
C = np.array([13, 17, 10, 15, 25])
z = [2015, 2016, 2017, 2018, 2019]
fig,ax = plt.subplots()
x = np.arange(5)
w = 0.6
ax.bar(x, A, w, color='orange', label='A')
ax.bar(x, B, w, color='red', bottom=A, label='B')
ax.bar(x, C, w, color='blue', bottom=A+B, label='C')
ax.set_title('Słupki potrójne')
ax.legend(loc=2)
plt.yticks(color='blue')
plt.xticks(x, z, color='royalblue')
plt.show()