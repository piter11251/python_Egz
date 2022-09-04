import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_excel('studenci14.xlsx')
colors = ['green', 'red', 'royalblue']
labels1 = ['St K', 'St M', 'Nst K', 'Nst M']
dane.plot(x='Tryby nauczania', kind='bar', stacked=False, rot=0, color=colors)
plt.xticks(range(0, 4),labels1)
plt.title("Ilość studentów w kolejnych latach")
plt.grid()
plt.tight_layout()
plt.savefig('zad3_14.pdf')
plt.show()