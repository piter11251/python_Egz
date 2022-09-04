import matplotlib.pyplot as plt
import numpy as np

labels = ['PL', 'DE', 'FR', 'SK']
X = [25, 23, 21, 33]
Y = [18, 42, 49, 25]
Z = [36, 26, 15, 26]

x = np.arange(4)
width = 0.2
fig,ax = plt.subplots()
ax.barh(x, Z, width, color='gray', label='Z')
ax.barh(x+width, Y, width, color='orange', label='Y')
ax.barh(x+2*width, X, width, color='purple', label='X')
ax.set_ylabel('Sprzedaż', color='red')
ax.set_xlabel('Kraje', color='green')
ax.set(yticks=x+width, yticklabels=labels)
ax.set_title('Wykres')
ax.legend(loc='lower right')
plt.savefig('zad1.png')
plt.show()