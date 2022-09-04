import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
values = np.array([-19, -15, -16, -20, -18, -19])
months = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
plt.bar(x, values, color='pink', label='A')
values2 = np.array([23, 29, 30, 19, 8, 15])
plt.bar(x, values2, color='aqua', label='B')
plt.xticks(x, months, rotation=45)
plt.title("Wykres zmian A i B")
plt.legend()
plt.savefig("zad1.jpg")
plt.show()
