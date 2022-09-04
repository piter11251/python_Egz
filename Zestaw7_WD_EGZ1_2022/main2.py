import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = pd.read_excel('D:\\Users\piokoz\projekty\python\Zestaw7_WD_EGZ1_2022\kolej7.xlsx')
rok = dane['Rok']
wartosc = dane['Wartosc']
plt.plot(rok, wartosc, linewidth=2, color='orange')
plt.title('Wykres z rozstawem normalnotorowym ogółem w Polsce')
plt.xlabel('Lata')
plt.ylabel('Ilosc km torów')
plt.savefig('zad2.jpg')
plt.show()
