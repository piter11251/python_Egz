import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = pd.read_excel('D:\\Users\piokoz\projekty\python\Zestaw8_WD_EGZ1_2022\kolej8.xlsx')
rok = dane['Rok']
wartosc = dane['Wartosc']

plt.plot(rok, wartosc, color='red', linewidth=3, label='Kolej normalnotorowa w Polsce', linestyle=':')
plt.title('Wykres długości normalnotorowych linii kolei na przestrzeni lat')
plt.ylabel('Długość w km')
plt.xlabel('Lata')
plt.grid()
plt.legend()
plt.savefig('zad2.jpg')
plt.show()