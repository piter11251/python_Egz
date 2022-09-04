import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane1 = [15.70, 25.58, 16.86, 21.51, 12.79, 7.56]
dane2 = [20.37, 17.59, 9.72, 19.91, 15.74, 16.67]

labels = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['brown', 'pink', 'yellow', 'green', 'brown', 'blue']
fig = plt.figure(figsize=(4,3), dpi=144)
ax1 = fig.add_subplot(221)
ax1.set_title('Lewo góra')
ax1.pie(dane1, explode=(0, 0.1, 0, 0, 0, 0), labels=labels, autopct='%.2f%%', textprops={'fontsize':6}, colors=colors)
ax2 = fig.add_subplot(212)
ax2.pie(dane2, labels=labels, explode=(0, 0.1, 0, 0, 0, 0), autopct='%.2f%%', textprops={'fontsize':6}, colors=colors)
ax2.set_title('Prawo dół')
plt.tight_layout()
plt.savefig('zad1.jpg')
plt.show()