import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane = pd.read_excel('studenci15.xlsx')
labels = ['NST M', 'NST K', 'ST M', 'ST K']
dane.plot(x='Tryby nauczania', kind='barh')
plt.yticks(range(0,4), labels)
plt.xlabel('Liczba studentów')
plt.title('Wykres liczby studentów w przeciągu dwóch lat')
plt.tight_layout()
plt.grid()
plt.savefig('zad3.pdf')
plt.show()