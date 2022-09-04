import matplotlib.pyplot as plt
import numpy as np

wykres1 = [19.7, 18.8, 7.5, 22.1, 15.5, 16.4]
wykres2 = [19.8, 17.2, 5.6, 21.1, 15.9, 20.3]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['green', 'royalblue', 'aqua', 'orange', 'yellow', 'gray']
fig = plt.figure(figsize=(4,3), dpi=144)
ax1 = fig.add_subplot(121)
ax1.pie(wykres1, labels=labels, explode=(0,0.1,0,0,0.1,0), autopct='%.1f%%', startangle=30, colors=colors)
ax1.set_title('Lewo')
ax2 = fig.add_subplot(122)
ax2.pie(wykres2, labels=labels, explode=(0,0.1,0,0,0.1,0), autopct='%.1f%%', startangle=60, colors=colors)
ax2.set_title('Prawo')
plt.tight_layout()
plt.savefig('zad1_z23.jpg')
plt.show()