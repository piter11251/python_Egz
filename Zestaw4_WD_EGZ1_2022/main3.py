import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("D:\\Users\piokoz\projekty\python\Zestaw4_WD_EGZ1_2022\kurs4.csv", delimiter=';')
dni = np.array(dane['Dzień'])
print(dane['Kurs CZK'].apply(lambda x: float(x)))
x = kurs.tolist().tofloat
dni_parzyste = []
np.reshape(x, (1, 2))
for i in dni:
    if i%2==0:
        dni_parzyste.append(i)



plt.plot(dni_parzyste, x)
