import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_excel('kina13.xlsx')
woj = dane['Nazwa']
wartosc = dane['Wartosc']
colors = ['tab:blue', 'tab:green', 'tab:olive', 'tab:orange', 'tab:purple', 'tab:pink']
plt.pie(wartosc, labels=woj, autopct="%.2f", colors=colors)
plt.tight_layout()
plt.title("Roznica w objętości między województwami w 2018 roku")
plt.annotate(text='2022-09-01', xy=(0.826, -1.076))
plt.show()

