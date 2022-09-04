import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane1 = [20.4, 17.6, 9.7, 19.9, 15.7, 16.7]
dane2 = [15.7, 25.6, 16.9, 21.5, 12.8, 7.6]

labels = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['brown', 'pink', 'yellow', 'green', 'brown', 'blue']
fig = plt.figure(figsize=(4,3), dpi=144)
ax1 = fig.add_subplot(223)
ax1.set_title('Lewo dół')
ax1.pie(dane1, explode=(0, 0.1, 0, 0, 0, 0), labels=labels, autopct='%.2f%%', textprops={'fontsize':6}, colors=colors)
ax2 = fig.add_subplot(222)
ax2.pie(dane2, labels=labels, explode=(0, 0.1, 0, 0, 0, 0), autopct='%.2f%%', textprops={'fontsize':6}, colors=colors)
ax2.set_title('Prawo góra')
plt.tight_layout()
plt.savefig('zad1.jpg')
plt.show()