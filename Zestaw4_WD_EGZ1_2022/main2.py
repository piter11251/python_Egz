import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_excel("D:\\Users\piokoz\projekty\python\Zestaw4_WD_EGZ1_2022\\uczniowie4.xlsx")
rok = dane['Rok']
wartosc = dane['Wartość']
x = np.arange(5)
plt.scatter(x, wartosc, marker='^', color='green', s=300)
plt.annotate(text='2022-08-29', xy=[2019,610000])
plt.title("Wykres wartosci wzgledem lat")
plt.xlabel("Lata")
yt = [600000, 620000, 640000, 660000, 760000]
ytz = ['600 tys', '620 tys', '640 tys', '660 tys', '760 tys']
plt.xticks(x, rok)
plt.yticks(yt, ytz)
plt.savefig('zad2.png')
plt.show()