import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = pd.read_csv('D:\\Users\piokoz\projekty\python\Zestaw8_WD_EGZ1_2022\pekin8.csv', delimiter=';')
norwegia = dane[dane['Państwo']=='Norwegia']
medale_nor = norwegia.iloc[0, 1]
holandia = dane[dane['Państwo']=='Holandia']
medale_hol = holandia.iloc[0, 1]
austria = dane[dane['Państwo']=='Austria']
medale_aus = austria.iloc[0, 1]
medale = [medale_nor, medale_hol, medale_aus]
labels = ['Norwegia', 'Holandia', 'Austria']
x = np.arange(3)
colors = ['blue', 'green', 'orange']
plt.bar(x, medale, color=colors)
plt.xticks(x, labels)
plt.title('Złote medale')
plt.xlabel('Państwa')
plt.ylabel('Ilość medali')
plt.savefig('zad3.pdf')
plt.show()
