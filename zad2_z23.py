import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane = pd.read_excel("ceny23.xlsx")
dzem = dane[dane['Rodzaje towarów']=='dżem - za 360g']
rok = dzem['Rok']
dane_dzem = dzem['Wartosc']
cukier = dane[dane['Rodzaje towarów']=='cukier biały kryształ - za 1kg']
dane_cukier = cukier['Wartosc']
fig,ax1 = plt.subplots()
ax1.scatter(dane_cukier, rok, marker='^', label='cukier', color='royalblue')
ax1.scatter(dane_dzem, rok, marker='D', label='dżem', color='pink')
ax1.set_ylabel('Rok')
ax1.set_xlabel('Cena w zł')
ax1.set_title('Cena cukru i dżemu na przestrzeni lat')
ax1.legend(loc='best')
plt.show()