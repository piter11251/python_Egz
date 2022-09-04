import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_excel("D:\\Users\\piokoz\\projekty\\python\\Zestaw5_WD_EGZ1_2022\\uczniowie5.xlsx")
rok = dane['Rok']
wartosc = dane['Wartość']
lata = [2015, 2016, 2017, 2018, 2019]
plt.plot(rok, wartosc, color='red', linestyle='--', label='Wartosc')
plt.annotate(text='2022-08-29', xy=[2018.5,600000])
plt.title('Wykres wartosci wzgledem lat')
plt.xlabel('Lata')
yt = [680000, 620000, 600000, 720000, 760000]
ytz = ['680 tys', '620 tys', '600 tys', '720 tys', '760 tys']
plt.yticks(yt, ytz)
plt.xticks(rok, lata)
plt.legend()
plt.savefig('zad2.jpg')
plt.show()