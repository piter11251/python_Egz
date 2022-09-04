import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
months = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
values1 = [-15, -20, -16, -13, -16, -18]
plt.bar(x, values1, color='brown', label='Y')
values2 = [35, 25, 26, 10, 30, 15]
plt.bar(x, values2, color='yellow', label='X')
plt.xticks(x, months, rotation=45)
plt.title("Wykres zmian X i Y")
plt.legend()
plt.savefig('zad1.png')
plt.show()