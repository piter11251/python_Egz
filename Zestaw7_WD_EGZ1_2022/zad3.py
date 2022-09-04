import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = pd.read_csv('D:\\Users\piokoz\projekty\python\Zestaw7_WD_EGZ1_2022\pekin7.csv', delimiter=';')
#print(dane[dane['Państwo']=='Norwegia'])
labels = ['Norwegia', 'Niemcy', 'Szwecja']
norwegia = dane[dane['Państwo']=='Norwegia']
medale_nor = norwegia.iloc[0, 1]
niemcy = dane[dane['Państwo']=='Niemcy']
medale_niem = niemcy.iloc[0, 1]
szwecja = dane[dane['Państwo']=='Szwecja']
medale_szwe = szwecja.iloc[0, 1]
medale = [medale_nor, medale_niem, medale_szwe]
x = np.arange(3)
colors = ['blue', 'green', 'orange']
plt.bar(x, medale, color=colors)
plt.xticks(x, labels)
plt.title('Złote medale')
plt.xlabel('Państwa')
plt.ylabel('Ilość medali')
plt.savefig('zad3.pdf')
plt.show()

