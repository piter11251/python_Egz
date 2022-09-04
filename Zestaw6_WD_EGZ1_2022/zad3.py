import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_excel('D:\\Users\piokoz\projekty\python\Zestaw6_WD_EGZ1_2022\\rod6.xlsx', header=None).T
dane2 = dane.iloc[1:, :]
dane2.columns = dane.iloc[0, :]
dane2['Rok'] = pd.Series(dane2['Rok'], dtype=int)
dane2['Wartosc'] = pd.Series(dane2['Wartosc'], dtype=int)
dzialki = dane2[dane2['Rodzaje terenu'] == 'działki']
dp = dzialki[dzialki['Ogrody'] == 'powierzchnia']

plt.barh(dp['Rok'], dp['Wartosc'])
plt.title('Dane o powierzchni działek')
plt.yticks(dp['Rok'])
plt.xlabel("Powierzchnia w hektarach")
plt.savefig('zad3.pdf')
plt.show()