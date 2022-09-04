import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [0.05, 0.05, 0.48, 0.7, 0.85]
y = [0.05, 0.15, 0.85, 0.55, 0.32]
colors = ['brown', 'green', 'pink', 'gray', 'orange']
plt.scatter(x,y, color=colors)
plt.grid()
plt.title("Wykres punktowy - 5 punktów")
plt.ylabel("Oś Y")
plt.xlabel("Oś X")
plt.savefig('zad1.png')
plt.show()