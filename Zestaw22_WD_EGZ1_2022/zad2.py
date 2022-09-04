import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane = pd.read_excel('ceny22.xlsx')
dane['Wartość'] = pd.Series(dane['Wartość'], dtype=float)
z = ['2009', '2010', '2011', '2012', '2013', '2014']
bulki = dane[dane['Rodzaje towarów'] == 'bułka pszenna - za 50g']
wartoscB = bulki['Wartość']
chleb = dane[dane['Rodzaje towarów'] == 'chleb pszenno-żytni - za 0,5kg']
wartoscC = chleb['Wartość']
colors = ['orange', 'red']
x = np.arange(6)
rok = dane['Rok']
fig,ax1 = plt.subplots()
ax1.scatter(y=wartoscB, x=x, label='bulki', color='red', marker='^')
ax1.scatter(y=wartoscC, x=x, label='chleb', color='green', marker='^')
ax1.set_xticks(x, z)
ax1.legend(loc=5)
plt.annotate(text='Piotr', xy=(0, 2.232))
plt.title('Wykres')
plt.xlabel('Lata')
plt.ylabel('Cena')
plt.savefig('zad2.png')
plt.show()