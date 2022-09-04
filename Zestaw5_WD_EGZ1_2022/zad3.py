import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv('wyksz5.csv', delimiter=',')
wiek = dane['Wiek']
liczebnosc = dane['Liczebność']
wyksztalcenie = dane['Wykształcenie']
width = 0.4
index = np.arange(6)
brak = dane[dane['Wykształcenie']=='brak']
brak1liczebosc = brak['Liczebność']
brak1wiek = brak['Wiek']
podst = dane[dane['Wykształcenie']=='podstawowe']
podstliczebnosc = podst['Liczebność']
zasad = dane[dane['Wykształcenie']=='zasadnicze']
sred = dane[dane['Wykształcenie']=='średnie']
polic = dane[dane['Wykształcenie']=='policealne']
wyz = dane[dane['Wykształcenie']=='wyższe']

x=np.arange(3)
plt.figure(figsize=(15,15))
plt.barh(x, brak['Liczebność'], color='blue', height=0.25, label='brak')
plt.barh(x+0.25, podst['Liczebność'], color='red', height=0.25, label='podstawowe')
plt.barh(x+0.55, zasad['Liczebność'], color='green', height=0.25, label='zasadnicze')
plt.barh(x+0.80, sred['Liczebność'], color='yellow', height=0.25, label='średnie')
plt.barh(x+1.05, polic['Liczebność'], color='orange', height=0.25, label='policealne')
plt.barh(x+1.30, wyz['Liczebność'], color='black', height=0.25, label='wyższe')
plt.legend()
plt.title("Wykształcenie poszczególnych osób")
plt.xlabel("Liczba ludzi w mln")
plt.yticks(x, brak['Wiek'])
##plt.barh(x+1, podst['Liczebność'], color='green', label='podstawowe')
#plt.barh(x+2, zasad['Liczebność'], color='red', label='zasadnicze')
#plt.barh(x+3, sred['Liczebność'], color='pink', label='średnie')
#plt.barh(x+4, polic['Liczebność'], color='aqua', label='policealne')
#plt.barh(x+5, wyz['Liczebność'], color='black', label='wyższe')

plt.show()

