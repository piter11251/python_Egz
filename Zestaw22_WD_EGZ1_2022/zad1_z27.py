import matplotlib.pyplot as plt
import numpy as np

A = [31, 18, 22, 16, 20]
B = [43, 35, 29, 28, 45]
C = [55, 53, 40, 43, 70]

fig,ax = plt.subplots()
x = np.arange(5)
w = 0.6
ax.bar(x, A, w, color='orange')
ax.bar(x, B, w, color='red', bottom=A)
ax.bar(x, C, w, color='blue', bottom=B)
plt.show()