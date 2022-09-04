import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y = [-15, -10, -14, -19, -18, -28]
x = [37, 39, 20, 23, 36, 35]
z = np.arange(6)
months = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']

plt.bar(z, x, color='green', label='X')
plt.bar(z, y, color='red', label='Y')
plt.xticks(z, months, rotation=45)
plt.title("Wykres zmian X i Y")
plt.legend()
plt.savefig('zad1.png')
plt.show()