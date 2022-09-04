import matplotlib.pyplot as plt
from matplotlib import figure
import pandas as pd
import numpy as np

dane = pd.read_excel('kina15.xlsx')
values = dane['Wartosc']
woj = dane['Nazwa']
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.pie(values, autopct='%.0f', labels=woj)
plt.tight_layout()
plt.legend(loc='upper right')
plt.annotate(text='2022-09-02', xy=(1.002, -0.928))
plt.savefig('zad2.png')
plt.show()