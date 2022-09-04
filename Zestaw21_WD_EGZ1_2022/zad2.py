import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_excel('ceny21.xlsx')
rok = dane['Rok']
wartosc = dane['Wartość']
x1 = dane[dane['Rodzaje towarów']=='mąka pszenna - za 1kg']
x2 = dane[dane['Rodzaje towarów']=='kasza jęczmienna - za 0,5kg']

fig,ax1 = plt.subplots()
ax1.scatter(x1['Wartość'], x1['Rok'], label='mąka pszenna(1kg)', marker='^', color='green')
ax1.scatter(x2['Wartość'], x2['Rok'], label='kasza jęczmienna(0.5kg)', marker='^', color='blue')
ax1.legend(loc=2)
plt.xlabel('Cena za produkt w zł')
plt.annotate(text='Piotr', xy=(2.62, 2014))
plt.title("Wykres cen produktów na przestrzeni lat")
plt.savefig('zad2.png')
plt.show()
