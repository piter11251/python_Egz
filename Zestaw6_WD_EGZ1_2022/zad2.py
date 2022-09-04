import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_excel('D:\\Users\piokoz\projekty\python\Zestaw6_WD_EGZ1_2022\\uczniowie6.xlsx')
rok = dane['Rok']
wartosc = dane['Wartość']
yt = [660000, 620000, 600000, 720000, 760000]
ytz = ['660 tys', '620 tys', '600 tys', '720 tys', '760 tys']
lata = [2015, 2016, 2017, 2018, 2019]
plt.plot(rok, wartosc, color='purple', linewidth=2)
plt.xticks(rok, lata)
plt.yticks(yt, ytz)
plt.annotate(xy=(2015, 600000), text='2022-08-30')
plt.savefig('zad2.jpg')
plt.show()