import matplotlib.pyplot as plt
import numpy as np

labels = ['PL', 'DE', 'FR', 'SK']
Y = [13, 19, 50, 45]
X = [38, 35, 43, 28]
x = np.arange(4)
width = 0.3

plt.bar(x, Y, width, color='blue', label='Y')
plt.bar(x+width, X, width, color='orange', label='X')
plt.xticks(x, labels)
plt.grid()
plt.title('Wykres')
plt.xlabel('Kraje', color='green')
plt.ylabel('Sprzedaż', color='red')
plt.show()