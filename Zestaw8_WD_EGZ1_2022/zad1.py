import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [11.3, 15.3, 15.5, 16.6, 19.2]
y = [0.44, 0.37, 0.51, 0.01, 0.06]
colors = ['green', 'pink', 'red', 'brown', 'gray']

z = np.arange(5)
plt.scatter(x,y, color=colors, s=150)
plt.title("Wykres punktowy - 5 punktów")
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.grid()
plt.savefig('zad1.png')
plt.show()