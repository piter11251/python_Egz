import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_excel('D:\\Users\piokoz\projekty\python\Zestaw13_WD_EGZ1_2022\studenci13.xlsx')
x = np.arange(4)
width = 0.2
rok2016 = dane[(dane[2016]) & (dane['Płeć'] == 'mężczyźni')]
fig,ax = plt.subplots()
ax.bar(x, rok2016, width)
plt.show()
#fig,ax = plt.subplots()
#ax.bar(x, rok2016, width, label='blue')
#ax.bar(x*2, , width)

#ax.legend()
#plt.show()

